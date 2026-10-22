---
name: assessing-thread-safety
description: Evaluates Python code, libraries, and interpreter-level constructs for thread-safety guarantees, especially under free-threaded (no-GIL) builds. Use when reviewing concurrent Python code, migrating to free-threaded Python 3.13+, diagnosing race conditions, or determining whether specific operations (dict/list mutation, refcounting, C extensions) are safe without external locks.
---

## Quick Start

When asked "is this thread-safe?", check three things in order:

1. **Which interpreter build?** GIL-enabled (default) vs free-threaded (`--disable-gil` / `t` suffix, PEP 703). Guarantees differ substantially.
2. **What's the operation category?** Atomic bytecode op, container mutation, C-API call, or third-party C extension?
3. **What does CPython actually guarantee vs what "seems safe"?** Many operations look atomic but aren't guaranteed across versions/builds.

```python
# Example triage
import sys
free_threaded = sys._is_gil_enabled is not None and not sys._is_gil_enabled()

# dict.setdefault, list.append: atomic under GIL, but under free-threaded
# builds only *individual* container ops are internally locked -
# compound operations (check-then-act) are NEVER safe in either mode.
counter = {}
counter[key] = counter.get(key, 0) + 1  # NOT thread-safe in any mode
```

## Workflow

Progress:
- [ ] Identify interpreter mode (GIL vs free-threaded) the code must support
- [ ] Classify each shared-state operation
- [ ] Check against known-atomic operation list
- [ ] Check C extensions for `Py_mod_gil` slot / explicit free-threading support
- [ ] Flag compound/check-then-act patterns regardless of atomicity
- [ ] Recommend explicit synchronization (`threading.Lock`, `queue.Queue`, immutable data) where guarantees are insufficient
- [ ] Note version-specific caveats (behavior can change between minor versions; nothing here is a language-level contract unless documented)

### 1. Interpreter mode matters
- **GIL-enabled build**: bytecode-level atomicity for single ops; the GIL serializes execution, giving many single opcode operations effective atomicity as a side effect (not a guarantee).
- **Free-threaded build (PEP 703, 3.13+)**: no GIL; CPython instead guarantees *specific* operations are safe via internal per-object locks (critical sections). Anything not explicitly documented as safe should be treated as unsafe.

### 2. Operation classification
- **Documented atomic**: e.g., single container item get/set/del on `dict`, `list`, `set` for built-in types — safe from corrupting interpreter state, but does **not** mean no race conditions in program logic.
- **Compound operations**: `x += 1`, `if k not in d: d[k] = v`, `list.sort()` interleaved with reads — never safe without a lock, in any mode.
- **Reference counting**: under free-threaded builds, refcounting uses biased/deferred reference counting; safe by design, not something users manage directly.
- **C extensions**: must opt in to free-threading support (`Py_MOD_GIL_NOT_USED`); otherwise CPython re-enables the GIL automatically when such a module is imported. Flag any extension without explicit multi-phase init support as unsafe to assume free-threaded-safe.

### 3. Never trust "looks atomic"
Even single bytecode instructions are an implementation detail unless explicitly documented in `threadsafety`-style guarantees. Recommend explicit locking for any correctness-critical shared mutable state.

## Examples

**Example 1:**
Input: `shared_list.append(x)` called from multiple threads, free-threaded build, no lock.
Output: Safe — `list.append` is a documented atomic operation protected by internal critical sections in free-threaded CPython. No external lock needed for this single call, but iterating and mutating from another thread concurrently still needs care (iteration is not itself atomic).

**Example 2:**
Input: 
```python
if key not in cache:
    cache[key] = expensive_compute(key)
```
Output: Not thread-safe in either GIL or free-threaded mode. This is a check-then-act compound operation — two threads can both pass the `not in` check before either writes. Recommend `cache.setdefault(key, expensive_compute(key))` (still recomputes redundantly but avoids corruption) or a lock/`functools.lru_cache` with internal locking, or `dict.setdefault` combined with a sentinel + lock if compute is expensive.

**Example 3:**
Input: A C extension module with no free-threading support, imported under `python3.13t`.
Output: CPython will implicitly re-enable the GIL for the whole process (with a `RuntimeWarning`) when it detects the extension lacks the `Py_mod_gil` slot declaring support. Flag this as: (a) safe from corruption, but (b) silently defeats the purpose of running free-threaded — surface this to the user as a performance/architecture issue, not just a safety one.

## Best Practices

- Default recommendation for shared mutable state: use `threading.Lock`/`RLock` or higher-level primitives (`queue.Queue`, `concurrent.futures`) rather than relying on interpreter internals.
- Prefer immutable data structures or message-passing (queues) over shared mutable state — sidesteps the entire question.
- When reviewing library code intended to support free-threaded Python, check for explicit test matrix entries (`3.13t`, `3.14t`) and CI runs with `PYTHON_GIL=0`.
- Cite the specific CPython version when giving atomicity guarantees — behavior is not a stable language guarantee, only what a given release documents/implements.
- For C extensions, check for `Py_mod_gil` module slot and `Py_MOD_GIL_NOT_USED` usage as the marker of intentional free-threading support.

## Common Pitfalls

- Assuming "the GIL makes everything thread-safe" — it only serializes bytecode execution, not multi-step logic.
- Assuming free-threaded builds require locks for *everything* — many single container operations remain internally safe by design.
- Treating undocumented "seems atomic" behavior as a guarantee across Python versions.
- Forgetting that iteration over a container while another thread mutates it is unsafe even when individual get/set ops are safe.
- Ignoring C extensions as a hidden source of GIL re-activation or actual data races when they lack free-threading support.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: assessing-python-thread-safety
description: Assesses thread safety of Python standard library modules and APIs using CPython's documented thread safety levels. Use when reviewing concurrent code, deciding whether locking is needed around stdlib calls, or auditing multi-threaded Python programs for data races.
---

# Assessing Python Thread Safety

## Quick Start

CPython documents thread safety per-module/per-API using four levels (as of docs.python.org/3.16/library/threadsafety.html):

1. **Thread-safe** — safe to call from multiple threads concurrently, no external locking needed.
2. **Conditionally thread-safe** — safe under specific conditions (e.g., each thread uses its own instance, or a documented restriction is followed).
3. **Not thread-safe** — requires external synchronization (locks) if shared across threads.
4. **GIL-only safe / undocumented** — safety, if any, is an accidental artifact of the GIL, not a documented guarantee; do not rely on it, especially under free-threaded (no-GIL) builds.

When reviewing code: identify every stdlib object shared across threads, look up its documented level, and add locking or redesign if it's not "Thread-safe."

## Workflow

Progress:
- [ ] Step 1: List all stdlib modules/objects touched by multiple threads in the code under review.
- [ ] Step 2: For each, check the official thread-safety classification (module docs or the threadsafety.html table).
- [ ] Step 3: Classify each usage into one of the four levels above.
- [ ] Step 4: For "Conditionally thread-safe," verify the stated condition actually holds in this codebase.
- [ ] Step 5: For "Not thread-safe" or "GIL-only," flag and prescribe a fix (lock, thread-local storage, immutable/copy-on-read pattern, or queue-based handoff).
- [ ] Step 6: Re-check under free-threaded CPython (PEP 703 builds) assumptions — GIL-only safety disappears there.
- [ ] Step 7: Document findings inline or in a review comment with the level and citation.

## Examples

**Example 1:**
Input: Multiple threads append to the same `list` and read from it without locks.
Output: `list.append`/`list.pop` on a single list are individually atomic under the GIL (documented as thread-safe for these ops), but compound operations (check-then-act, e.g., "if item in list: list.remove(item)") are **not thread-safe** as a sequence. Recommend a `threading.Lock` around the compound operation or switch to `queue.Queue`.

**Example 2:**
Input: A `dict` is read by many threads and occasionally written by one.
Output: Single `dict[key] = value` and `dict[key]` reads are atomic (thread-safe for individual ops) even under free-threading. But iteration (`for k in d`) concurrent with mutation is **not thread-safe** — can raise `RuntimeError: dictionary changed size during iteration`. Recommend snapshotting with `list(d.items())` before iterating, or a lock around the mutate+iterate region.

**Example 3:**
Input: Code relies on `sys.modules` caching behavior during concurrent imports.
Output: The import system is documented as thread-safe (uses an internal per-module lock since Python 3.3+), so concurrent `import` of the same module from multiple threads is safe without extra locking.

**Example 4:**
Input: Shared `collections.OrderedDict` mutated by two threads with no lock, code "seems fine" because tests pass under GIL.
Output: Flag as **GIL-only safe / undocumented** for compound patterns (e.g., move_to_end + iterate). Passing tests under the GIL is not a guarantee — under a free-threaded build this can race. Add explicit locking.

## Best Practices

- Never infer thread safety from "it works in testing" — the GIL historically masked races; free-threaded builds won't.
- Distinguish **atomicity of a single bytecode-level op** from **safety of a sequence of ops** — the former being safe doesn't make compound logic safe.
- Prefer higher-level concurrency primitives (`queue.Queue`, `concurrent.futures`, `threading.Lock`/`RLock`) over relying on implicit atomicity.
- When a module's docs don't explicitly state a thread-safety level, treat it as **not thread-safe** by default (conservative assumption).
- Re-audit any "GIL reliance" code before deploying on Python builds with `--disable-gil` / free-threading enabled.
- Cite the specific documented level and source when flagging an issue, so reviewers can verify.

## Common Pitfalls

- Assuming an entire class/module is thread-safe because one method is documented as such — check per-operation, not just per-object.
- Confusing "atomic" (won't corrupt memory) with "correct" (won't produce logically wrong results under interleaving).
- Treating GIL-era safe patterns as portable guarantees going forward — they are not, once free-threaded CPython is in play.
- Overlooking mutable default arguments or module-level globals shared implicitly across threads.
- Forgetting that C-extension modules may have their own (possibly undocumented) thread-safety characteristics independent of the GIL.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: analyzing-python-thread-safety
description: Analyzes Python code for thread-safety issues around built-in container operations (list, dict, set) and determines whether specific operations are atomic under CPython's GIL or free-threaded builds. Use when reviewing concurrent Python code, debugging race conditions, or deciding whether locks are needed around shared container access.
---

## Quick Start

When asked "is this list/dict operation thread-safe?", check:

1. Is it a single bytecode-level operation (e.g., `list.append`, `dict[key] = val`, `list.pop()`)? → Generally atomic under GIL.
2. Is it a compound read-modify-write expressed across multiple statements (e.g., `if key not in d: d[key] = v`)? → NOT atomic, needs a lock even under GIL.
3. Is the code targeting free-threaded CPython (3.13+ `--disable-gil` / 3.16 default free-threading)? → Re-verify: many single-method atomicity guarantees still hold (CPython uses internal per-object locks for these), but interleaving of *separate* method calls is never guaranteed.

```python
import threading

shared = []
lock = threading.Lock()

def worker():
    shared.append(1)          # atomic, no lock needed (single op)
    with lock:                # compound op, lock required
        if shared:
            shared.pop()
```

## Workflow

Progress:
- [ ] Identify the container type (list, dict, set, deque, etc.)
- [ ] Identify whether the operation is a single built-in method call or a multi-step sequence
- [ ] Check if it's a mutating op (append, extend, pop, insert, remove, sort) vs. just iteration
- [ ] Determine execution mode: GIL-enabled CPython vs free-threaded build
- [ ] Classify: atomic (safe standalone) / non-atomic (needs lock) / undefined (avoid pattern)
- [ ] If iterating while another thread mutates, flag as unsafe regardless of build
- [ ] Recommend fix: lock, `queue.Queue`, copy-before-iterate, or immutable snapshot

## Reference: list operation atomicity (CPython, both GIL and free-threaded)

**Atomic (safe from a single call, no torn state):**
- `list.append(x)`, `list.pop()`, `list.pop(i)`
- `list[i] = x`, `del list[i]`
- `list.extend(iterable)` — atomic as a whole op, but if `iterable` is itself being mutated concurrently, behavior is undefined
- `x in list`, `list[i]` (read)

**NOT atomic / unsafe to assume ordering:**
- `list.sort()` — atomic w.r.t. not corrupting internal state, but concurrent reads during sort may see partially-sorted data; concurrent mutation during sort raises `ValueError`/undefined in some cases
- Iterating a list (`for x in lst`) while another thread appends/removes — length/index changes mid-iteration can skip or repeat elements; free-threaded builds do NOT make this deterministic
- Any sequence like `lst[i] = lst[i] + 1` (read-modify-write) — race condition even though each half is atomic
- `len(lst)` followed by indexed access — TOCTOU race

**Free-threaded build specifics (3.13+):**
- Individual list/dict/set methods remain internally consistent (no memory corruption, no crashes) because CPython holds a per-object critical section lock during the call.
- This does **not** extend to multi-statement logic — same rules as GIL builds apply for compound operations.
- Do not assume `del`/resize during iteration is safe just because it's free-threaded; it can still raise `RuntimeError: list changed size during iteration` or skip elements.

## Examples

**Example 1:**
Input: `counts[word] = counts.get(word, 0) + 1` shared across threads without a lock.
Output: Unsafe — this is a read-modify-write compound operation. `.get()` and the assignment are two separate steps; a race can lose updates. Fix: wrap in `with lock:` or use `collections.Counter` with an external lock, or use `multiprocessing`/`concurrent.futures` with per-thread local counters merged at the end.

**Example 2:**
Input: Thread A does `my_list.append(item)`; Thread B does `len(my_list)` concurrently, no lock.
Output: Safe. Both are single atomic operations on the list; no corruption or crash. B may see the list before or after A's append, but never a torn/partial state.

**Example 3:**
Input: Thread A iterates `for x in shared_list:` while Thread B does `shared_list.remove(x)`.
Output: Unsafe regardless of build — mutating a list during iteration in another thread can cause skipped elements or `RuntimeError`. Fix: iterate over `list(shared_list)` (a snapshot copy) or use a lock around the whole iteration+mutation region.

## Best Practices

- Prefer high-level concurrency primitives (`queue.Queue`, `concurrent.futures`, `threading.Lock`) over relying on low-level atomicity guarantees.
- Treat "atomic" as meaning "won't corrupt memory," not "produces the logically correct result" — logical correctness still requires locks for compound operations.
- When reviewing code for the free-threaded build, don't assume behavior identical to GIL builds beyond single-call atomicity; re-audit any code that relied on the GIL as an implicit global lock across multiple statements.
- Snapshot before iterating if concurrent mutation is possible: `for x in list(shared): ...`.

## Common Pitfalls

- Assuming "the GIL makes everything thread-safe" — it only guarantees atomicity of individual bytecode-level operations, not sequences of them.
- Assuming free-threaded CPython removes the need for locks — it changes performance characteristics, not the need for correctness locking on compound logic.
- Using `if key not in d: d[key] = ...` without a lock ("check-then-act" race).
- Iterating and mutating the same container from different threads without a lock or a copy.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: assessing-python-dict-thread-safety
description: Evaluates whether Python dict operations are safe under concurrent access, particularly regarding the free-threaded build (PEP 703, no-GIL CPython 3.13+) and standard GIL-enabled builds. Use when reviewing code that shares dict objects across threads, debugging race conditions involving dicts, or deciding whether locks are needed around dict operations.
---

# Assessing Python Dict Thread Safety

## Quick Start

Rule of thumb:
- **GIL-enabled build**: single dict method calls (`d[k] = v`, `d.get(k)`, `d.pop(k)`, `len(d)`) are atomic and safe across threads. Multi-step sequences (check-then-act) are NOT safe.
- **Free-threaded build (no-GIL)**: single dict method calls are still atomic/thread-safe (CPython guarantees internal consistency), but multi-step sequences are still NOT safe without external locking.

```python
# UNSAFE on both builds — race between check and act
if key not in d:
    d[key] = compute()

# SAFE — use atomic single-call alternatives
d.setdefault(key, compute())  # note: compute() still runs even if key exists

# SAFE for actual atomicity guarantee — use a lock for compound logic
with lock:
    if key not in d:
        d[key] = compute()
```

## Workflow

1. **Identify the build target.** Determine if the code must run correctly under free-threaded CPython (3.13+, `Py_GIL_DISABLED`), standard GIL builds, or both. Thread-safety guarantees differ subtly.
2. **Classify each dict operation:**
   - Single atomic operation (`__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `get`, `pop`, `setdefault`, `update` with a single dict/iterable argument, `len`) → safe from corruption in both build types.
   - Compound/check-then-act sequences (read-modify-write across multiple statements, iterating while another thread mutates) → unsafe in both build types.
3. **Check iteration patterns.** Iterating over a dict (`for k in d`, `.keys()`, `.values()`, `.items()`) while another thread mutates it can raise `RuntimeError: dictionary changed size during iteration` on GIL builds, and can still be unsafe/undefined on free-threaded builds if not otherwise protected. Never assume safe iteration under concurrent mutation.
4. **Add explicit locking for compound operations.** Wrap multi-step logic (read-check-write, counters, "get or create" patterns needing side-effect-free guarantees) in a `threading.Lock`.
5. **Do not rely on the GIL for correctness in future-proof code.** Code that "works" only because the GIL serializes bytecode is fragile once run under free-threaded builds — always use explicit synchronization for compound logic.
6. **Verify with docs/version specifics.** Confirm behavior against the target CPython version's `threadsafety` documentation, since guarantees are an evolving part of the free-threaded build's specification.

## Examples

**Example 1:**
Input: `counts[word] = counts.get(word, 0) + 1` called concurrently from multiple threads.
Output: Unsafe on both build types — this is a read-modify-write sequence spanning two bytecode-level operations (`get` then `__setitem__`), so increments can be lost. Fix: wrap in a lock, or use `collections.Counter` with explicit locking, or restructure with `dict.setdefault` inside a lock.

**Example 2:**
Input: `value = my_dict.get("key")` executed from many threads while another thread does `my_dict["key"] = new_value`.
Output: Safe — both are single atomic dict operations. Each thread sees either the old or new value, never a corrupted/partial one, on both GIL and free-threaded builds.

**Example 3:**
Input: `for k, v in shared_dict.items(): process(k, v)` while another thread calls `shared_dict.pop(k)` concurrently.
Output: Unsafe — may raise `RuntimeError` (GIL build) or produce inconsistent iteration results (free-threaded build). Fix: iterate over `list(shared_dict.items())` snapshot taken under a lock, or hold a lock for the full iteration.

## Best Practices

- Prefer single built-in dict method calls over multi-statement patterns when possible.
- Use `threading.Lock` (or `RLock` if reentrancy is needed) around any compound dict logic shared across threads.
- Take a snapshot copy (`dict(d)` or `list(d.items())`) before iterating if concurrent mutation is possible, and take the snapshot while holding the same lock used for mutations.
- When targeting free-threaded builds specifically, re-verify assumptions against `docs.python.org` threadsafety docs for the exact CPython version — guarantees have been refined across 3.13/3.14+ releases.
- Prefer `queue.Queue`, `concurrent.futures`, or higher-level synchronization primitives over hand-rolled locking when the access pattern is producer/consumer.

## Common Pitfalls

- Assuming "atomic in CPython with the GIL" automatically means "safe under free-threaded CPython" — verify, don't assume equivalence.
- Using `setdefault(key, expensive_compute())` and forgetting `expensive_compute()` always executes eagerly, even when the key already exists — wasteful and can have unwanted side effects.
- Treating `dict.update()` as fully atomic when its argument is a lazily-evaluated generator/iterable that itself accesses shared mutable state — the *update* is atomic but the *evaluation of its argument* may not be.
- Believing that removing the GIL (free-threaded build) makes dict-heavy code automatically thread-safe without review — it only preserves internal dict consistency, not program-level correctness of compound logic.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```
---
name: assessing-python-thread-safety
description: Assesses thread-safety guarantees of Python built-in types and standard library operations, particularly for free-threaded (no-GIL) CPython builds. Use when reviewing concurrent Python code, deciding whether locks are needed around shared data structures, or debugging race conditions involving sets, dicts, lists, or other builtins accessed from multiple threads.
---

## Quick Start

When someone asks "is this thread-safe?" for a Python operation, check against these tiers:

1. **Single atomic bytecode operation on a builtin** (e.g., `d[k] = v`, `s.add(x)`, `list.append`) → thread-safe against corruption in both GIL and free-threaded builds, but **not** safe for compound logic (check-then-act).
2. **Iteration while another thread mutates the container** → NOT safe. Raises `RuntimeError: <container> changed size during iteration` or produces inconsistent results.
3. **Compound operations** (`if k not in d: d[k] = v`, `x = s.pop(); s.add(x)`, `+=` on shared mutable) → NOT safe. Needs explicit locking regardless of GIL.
4. **Free-threaded builds (3.13+ `--disable-gil`, 3.16 default consideration)** → some historically "safe by GIL accident" patterns are now explicitly documented as unsafe or require the object's internal lock.

## Workflow

Progress:
- [ ] Identify the exact operation(s) and container type in question
- [ ] Classify: single atomic op vs. compound/multi-step
- [ ] Check if code will run under free-threaded CPython (no-GIL) — this changes guarantees
- [ ] Consult the specific object's thread-safety documentation (set, dict, list, deque)
- [ ] Determine if iteration co-occurs with mutation from another thread
- [ ] Recommend lock/no-lock verdict with reasoning
- [ ] If unsafe, suggest fix: `threading.Lock`, `queue.Queue`, immutable snapshot, or atomic alternative

## Reference: Set Thread Safety (CPython 3.16)

- **Atomic, thread-safe** (no corruption, GIL or no-GIL):
  - `add()`, `discard()`, `remove()`, `pop()` — individually
  - Membership test `in` — individually
  - `len()` — individually
- **NOT thread-safe:**
  - Iterating a set (`for x in s`) concurrently with any mutation from another thread — may raise `RuntimeError` or skip/duplicate elements
  - Set comprehensions or `set()` copy-construction reading from a set being mutated elsewhere
  - Compound patterns: `if x in s: s.remove(x)` (TOCTOU race)
  - Set algebra operators (`|`, `&`, `-`, `^`) and their in-place forms (`|=`, etc.) when operands are mutated concurrently — these internally iterate
- **Free-threaded build specifics:** individual set methods use internal critical sections (per-object locks) to stay atomic, but this does not extend across multiple calls or to iteration — same rules as above, just now enforced without relying on GIL as an implicit lock.

Apply the same tiered reasoning to `dict`, `list`, and `deque` — each has its own doc page under `threadsafety.html` with per-method atomicity tables; check the specific one rather than assuming set semantics generalize.

## Examples

**Example 1:**
Input: "Is `my_set.add(item)` called from multiple threads safe without a lock?"
Output: Yes — `add()` is atomic on both GIL and free-threaded CPython. No corruption risk. If subsequent logic depends on set state after the add (e.g., checking size to trigger an action), that compound check needs a lock.

**Example 2:**
Input:
```python
for item in shared_set:
    process(item)
# meanwhile another thread does shared_set.discard(item)
```
Output: Unsafe. Iterating while another thread mutates raises `RuntimeError: Set changed size during iteration` or yields inconsistent traversal. Fix: `for item in list(shared_set): ...` to snapshot, or wrap both iteration and mutation in the same `threading.Lock`.

**Example 3:**
Input: `if x not in my_set: my_set.add(x)` from multiple threads — thread-safe?
Output: No. Classic TOCTOU race — two threads can both pass the `not in` check before either adds, but since `add()` is idempotent for sets this specific race is often harmless *unless* you're counting insertions or triggering side effects on "first add". Flag as unsafe for correctness of side effects even though it won't corrupt the set.

## Best Practices

- Never assume free-threaded CPython gives the same "GIL accidentally serializes everything" safety net — always check documented atomicity per method.
- Treat any multi-statement read-modify-write on a shared container as needing a lock, regardless of GIL status.
- Prefer immutable snapshots (`list(s)`, `dict(d)`) before iterating if concurrent mutation is possible and exact real-time accuracy isn't required.
- For producer/consumer patterns, prefer `queue.Queue` over manually locking a list/set/dict.
- When in doubt, cite the specific CPython docs page (`threadsafety.html`) for the container type rather than generalizing from another type's guarantees.

## Common Pitfalls

- Assuming "GIL means my code is thread-safe" — true only for single atomic bytecode-level ops, not for logic spanning multiple operations.
- Assuming set/dict/list share identical thread-safety tables — check each type individually.
- Forgetting that iteration itself is a multi-step operation vulnerable to concurrent mutation, even if each individual mutation call is atomic.
- Over-locking: wrapping every single atomic builtin call in a lock when unnecessary, hurting performance without correctness benefit.
- Under-locking: leaving compound check-then-act patterns unprotected because "the individual calls are atomic."

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: assessing-bytearray-thread-safety
description: Assesses whether bytearray operations are safe under free-threaded (no-GIL) Python execution and identifies where explicit locking is required. Use when reviewing concurrent code that mutates bytearray objects, porting code to free-threaded CPython 3.13+, or debugging data races involving bytearray buffers shared across threads.
---

## Quick Start

Under free-threaded CPython (PEP 703, no-GIL builds), individual `bytearray` method calls are atomic (thread-safe against corruption), but **sequences of operations are not atomic**. Any code that reads-then-writes, or relies on invariants holding across multiple statements, needs an explicit `threading.Lock`.

```python
import threading

buf = bytearray(1024)
lock = threading.Lock()

# UNSAFE under free-threading: check-then-act race
if len(buf) > 0:
    buf[0] = 42          # buf could have been resized/cleared by another thread

# SAFE: single atomic call
buf.append(1)             # atomic, no lock needed

# SAFE: compound operation needs a lock
with lock:
    if len(buf) > 0:
        buf[0] = 42
```

## Workflow

Progress:
- [ ] Identify every `bytearray` instance shared across threads
- [ ] Classify each access as single-operation vs. compound (multi-statement)
- [ ] For single operations (single method call, single subscript get/set, `append`, `extend`, slice assignment as one statement), no lock needed — CPython guarantees the operation itself won't corrupt internal state
- [ ] For compound operations (read-modify-write, length-check-then-index, iterate-while-mutating, buffer resize interacting with a `memoryview`), add a `threading.Lock` or `threading.RLock` around the whole sequence
- [ ] Pay special attention to `memoryview` objects backed by a `bytearray` — resizing the bytearray while a memoryview is exported is unsafe and can raise `BufferError` or, if not guarded, race
- [ ] Verify on the standard GIL build too — locks are correct there and add negligible overhead, so code should be written lock-safe regardless of build
- [ ] Test with `PYTHON_GIL=0` (or a free-threaded build) using stress loops (many threads hammering the same bytearray) to surface races that only appear without the GIL

## Examples

**Example 1:**
Input:
```python
counter_buf = bytearray(8)

def increment():
    val = int.from_bytes(counter_buf, "little")
    val += 1
    counter_buf[:] = val.to_bytes(8, "little")
```
Output: Unsafe — this is a classic read-modify-write race. Two threads can read the same `val` before either writes back, losing an increment. Fix:
```python
lock = threading.Lock()

def increment():
    with lock:
        val = int.from_bytes(counter_buf, "little")
        val += 1
        counter_buf[:] = val.to_bytes(8, "little")
```

**Example 2:**
Input:
```python
log_buf = bytearray()

def append_entry(data: bytes):
    log_buf.extend(data)
```
Output: Safe as-is. `extend` is a single atomic method call; free-threaded CPython guarantees the internal buffer state stays consistent even with concurrent callers. No lock required (though ordering of entries across threads is still nondeterministic — add a lock only if ordering matters, not for safety).

**Example 3:**
Input:
```python
data = bytearray(range(256))
mv = memoryview(data)

def resize():
    data.extend(b"\x00" * 100)   # thread A

def read():
    print(mv[0])                  # thread B
```
Output: Unsafe. Resizing a `bytearray` while a `memoryview` exports it is undefined/racy territory even beyond normal thread-safety — CPython may raise `BufferError` on the resize if the memoryview is still exported, and concurrent access patterns are unreliable. Guard both the resize and any memoryview-based access with the same lock, or avoid holding long-lived memoryviews over bytearrays that are concurrently resized.

## Best Practices

- Treat "thread-safe against corruption" and "correct under concurrency" as different things — an atomic op prevents crashes/corrupted memory, not logical races.
- Default to wrapping any multi-step interaction with a shared `bytearray` in a lock; only skip the lock when you're confident the operation is a single C-level call.
- Prefer `bytes` (immutable) over `bytearray` when the data doesn't need in-place mutation — it sidesteps thread-safety concerns entirely.
- When using `memoryview` on a `bytearray`, keep the memoryview's lifetime short and lock around any resize (`extend`, `+=`, `del buf[:]`, slice assignment that changes length) that happens concurrently with the memoryview's use.
- Write lock-based code even if you only target the GIL build today — it future-proofs against free-threaded builds and costs little.

## Common Pitfalls

- Assuming "the docs say bytearray operations are thread-safe" means the whole program logic is thread-safe — it only covers individual operations, not sequences.
- Forgetting that slice assignment with a size change (`buf[2:5] = b"longer_replacement"`) can trigger a resize, which interacts badly with concurrently held memoryviews.
- Using a plain `Lock` for read-heavy workloads when an `RLock` or a `threading.Condition`-based readers/writer pattern would avoid unnecessary serialization — pick the right primitive for the access pattern, not just "any lock."
- Testing only on the standard GIL-enabled interpreter and assuming that guarantees correctness on free-threaded builds — the GIL currently masks many races that free-threading exposes.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: ensuring-memoryview-thread-safety
description: Ensures safe concurrent access to memoryview objects and their underlying buffers in multithreaded Python code, accounting for free-threaded (no-GIL) builds. Use when writing or reviewing code that shares memoryview, bytearray, or buffer-protocol objects across threads, or when porting code to CPython 3.13+ free-threaded builds.
---

# Ensuring memoryview Thread Safety

## Quick Start

```python
import threading

# Underlying mutable buffer shared across threads
buf = bytearray(1024)
mv = memoryview(buf)

lock = threading.Lock()

def worker(start, end, value):
    with lock:
        mv[start:end] = bytes([value]) * (end - start)

threads = [threading.Thread(target=worker, args=(i*100, (i+1)*100, i)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

Key fact: on the standard GIL-enabled CPython build, individual memoryview operations (single-item get/set, slicing) are atomic at the bytecode level, but *compound* operations (read-modify-write, multi-step slice assignment) are **not** atomic and require explicit locking. On free-threaded builds (`--disable-gil` / PEP 703), even individual operations can race unless the memoryview's internal locking guarantees are understood — treat both builds the same way: assume nothing is atomic across multiple opcodes.

## Workflow

Progress:
- [ ] Step 1: Identify every memoryview/buffer-protocol object shared across threads
- [ ] Step 2: Classify each access pattern as read-only, single-write, or read-modify-write
- [ ] Step 3: Determine if the underlying object is mutable (bytearray, array.array, numpy array) or immutable (bytes)
- [ ] Step 4: Add synchronization (Lock/RLock) around any compound or read-modify-write access
- [ ] Step 5: Verify behavior under both the default GIL build and the free-threaded build if targeting 3.13+
- [ ] Step 6: Check for use-after-free hazards — releasing a buffer while a memoryview into it is still live on another thread

**Step 1 — Inventory shared objects**
Grep for `memoryview(`, `.cast(`, `buffer(`, and any object passed to `threading.Thread` args that supports the buffer protocol.

**Step 2 — Classify access**
- Read-only across threads → generally safe, no lock needed.
- Single atomic write (`mv[i] = x`) → safe under GIL builds for single-element assignment; still verify on free-threaded builds.
- Read-modify-write (`mv[i] += 1`, slice assignment computed from current contents) → always needs a lock.

**Step 3 — Mutability of backing store**
- `bytes` objects backing a memoryview are immutable — no data race possible, but the memoryview object itself (its state: shape, released flag) can still race.
- `bytearray`, `array.array`, mmap, numpy buffers — mutable, so concurrent writes need locks.

**Step 4 — Add synchronization**
Wrap compound operations in `threading.Lock`. Prefer one lock per logical buffer, not a global lock, to avoid contention.

**Step 5 — Verify across builds**
Free-threaded CPython removes the GIL, so operations that were "accidentally atomic" under GIL (e.g., single bytecode ops) may no longer be. Test with `python3.13t` or the `--disable-gil` build if supporting it.

**Step 6 — Lifetime hazards**
Calling `.release()` on a memoryview or letting the exporting object be garbage collected while another thread holds a view into it causes undefined behavior or crashes. Ensure the exporting object outlives all views, and don't release a shared memoryview from one thread while another is using it — protect release with the same lock.

## Examples

**Example 1:**
Input:
```python
counter_buf = bytearray(8)
mv = memoryview(counter_buf).cast('q')  # int64 view

def increment():
    mv[0] += 1  # read-modify-write, NOT atomic
```
Output (fixed):
```python
counter_buf = bytearray(8)
mv = memoryview(counter_buf).cast('q')
lock = threading.Lock()

def increment():
    with lock:
        mv[0] += 1
```
Reasoning: `mv[0] += 1` compiles to separate LOAD/ADD/STORE steps — a race condition on any build, GIL or not.

**Example 2:**
Input:
```python
data = bytearray(range(256))
mv = memoryview(data)

def reader():
    return bytes(mv)  # full read

def releaser():
    mv.release()
```
Output (fixed): Guard release with the same lock used for reads, and only release once no other thread holds a reference:
```python
lock = threading.Lock()

def reader():
    with lock:
        return bytes(mv)

def releaser():
    with lock:
        mv.release()
```
Reasoning: releasing a memoryview while another thread is mid-read causes a `BufferError` or crash; synchronize lifetime operations, not just data mutation.

## Best Practices

- Default to one `Lock` per shared buffer; avoid sharing a single global lock across unrelated buffers.
- Treat `+=`, slice-assignment-from-self, and any multi-step read-then-write as compound — always lock these.
- Never assume GIL-build atomicity guarantees carry over to free-threaded builds — write code as if no GIL exists.
- Keep the exporting object (the bytearray/array/mmap) alive at least as long as any memoryview into it across all threads.
- Prefer immutable snapshots (`bytes(mv)`) for cross-thread reads when the buffer is being concurrently mutated, rather than reading through the live view.
- When targeting both GIL and free-threaded builds, test explicitly on `python3.13t` (or later free-threaded builds) under thread-sanitizer-style stress tests (many iterations, `threading.Barrier` to maximize contention).

## Common Pitfalls

- Assuming a single memoryview element assignment is always safe just because "it's one line of Python" — check the actual bytecode/operation count.
- Forgetting that `.cast()` creates a new memoryview sharing the same underlying buffer — locks must cover all cast views, not just the original.
- Releasing or letting a buffer's exporter get garbage-collected while a background thread still holds a memoryview into it.
- Using a global interpreter-wide lock for unrelated buffers, creating unnecessary contention and negating the performance benefit of free-threading.
- Porting GIL-era code to free-threaded builds without re-auditing every "looked atomic" operation.
---
End Of Part
===========🔐™️®️©️🔐===========

---