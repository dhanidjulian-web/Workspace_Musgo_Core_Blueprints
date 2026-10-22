---
name: writing-python-code
description: Guides writing, debugging, and reviewing Python code following standard library conventions and idioms from Python 3.16 documentation. Use when writing Python scripts, choosing appropriate standard library modules, debugging Python code, or reviewing Python code for correctness and idiomatic style.
---

# Writing Python Code

## Quick Start

Given a task, first identify the right standard library tool before writing custom code:

```python
# Task: read a CSV, dedupe rows, write JSON output
import csv
import json
from pathlib import Path

def dedupe_csv_to_json(src: str, dst: str) -> None:
    seen = set()
    rows = []
    with Path(src).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = tuple(row.items())
            if key not in seen:
                seen.add(key)
                rows.append(row)
    Path(dst).write_text(json.dumps(rows, indent=2), encoding="utf-8")

if __name__ == "__main__":
    dedupe_csv_to_json("in.csv", "out.json")
```

Note: use `pathlib` over `os.path`, `f-strings` over `%` or `.format()`, and always specify `encoding` for file I/O.

## Workflow

Progress checklist for any non-trivial Python task:

```
- [ ] Clarify input/output shape and constraints
- [ ] Search stdlib for an existing module before writing custom logic
- [ ] Write a minimal working version
- [ ] Add type hints
- [ ] Add error handling for expected failure modes
- [ ] Write/verify with a quick test (doctest or assert)
- [ ] Review for idiomatic style (PEP 8, EAFP over LBYL)
```

**Step 1 — Map the task to a stdlib domain.** Common mappings:

| Need | Module |
|---|---|
| File paths | `pathlib` |
| CLI args | `argparse` |
| Structured data serialization | `json`, `csv`, `pickle` (trusted data only) |
| Config files | `configparser`, `tomllib` (read-only TOML) |
| Dates/times | `datetime`, `zoneinfo` |
| Regex | `re` |
| Concurrency (I/O-bound) | `asyncio`, `concurrent.futures.ThreadPoolExecutor` |
| Concurrency (CPU-bound) | `concurrent.futures.ProcessPoolExecutor`, `multiprocessing` |
| Data structures | `collections` (`deque`, `Counter`, `defaultdict`, `namedtuple`) |
| Iteration helpers | `itertools`, `functools` |
| Testing | `unittest`, `doctest` |
| Logging | `logging` (never `print` in libraries) |
| HTTP client | `urllib.request` for stdlib-only; note third-party `requests`/`httpx` preferred in practice |
| Type hints | `typing`, `dataclasses` |
| Enums/constants | `enum` |
| Context managers | `contextlib` |
| Temp files | `tempfile` |
| Hashing | `hashlib` |
| Randomness (non-crypto) | `random`; crypto-secure use `secrets` |

**Step 2 — Write minimal code, then harden.** Start with the happy path, then add:
- Type hints (`def f(x: int) -> str:`)
- Exception handling scoped to specific exceptions, not bare `except:`
- Resource cleanup via `with` statements

**Step 3 — Validate.** Add at least one runnable check (doctest, assert-based smoke test, or `unittest` case).

## Examples

**Example 1: CLI tool with argparse**

Input: "Build a CLI that counts word frequency in a text file, prints top N."

Output:
```python
#!/usr/bin/env python3
import argparse
from collections import Counter
from pathlib import Path


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    words = text.lower().split()
    return Counter(words).most_common(n)


def main() -> None:
    parser = argparse.ArgumentParser(description="Word frequency counter")
    parser.add_argument("file", type=Path)
    parser.add_argument("-n", type=int, default=10, help="top N words")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    for word, count in top_words(text, args.n):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
```

**Example 2: Concurrent I/O-bound fetches**

Input: "Fetch 50 URLs concurrently and return status codes."

Output:
```python
import asyncio
from urllib.request import urlopen

async def fetch_status(url: str) -> tuple[str, int]:
    loop = asyncio.get_running_loop()
    def _blocking_get():
        with urlopen(url, timeout=10) as resp:
            return resp.status
    status = await loop.run_in_executor(None, _blocking_get)
    return url, status

async def main(urls: list[str]) -> dict[str, int]:
    results = await asyncio.gather(*(fetch_status(u) for u in urls))
    return dict(results)
```
Note: for real HTTP workloads, `asyncio` + third-party async HTTP client is preferred over blocking `urlopen` in executor, but this shows the stdlib-only pattern.

**Example 3: Choosing the right container**

Input: "Track counts of items streaming in, need O(1) increment and easy sorting by frequency."

Output: `collections.Counter` — `Counter(stream).most_common()` gives sorted-by-frequency directly; avoid manual `dict` + manual sort.

## Best Practices

- **Prefer stdlib over hand-rolled logic.** If a task looks common (grouping, caching, path handling), a module likely already solves it (`itertools.groupby`, `functools.lru_cache`, `pathlib`).
- **EAFP over LBYL**: use `try/except` for control flow (e.g., dict access) rather than pre-checking with `if key in d`, when failure is uncommon.
- **Use `dataclasses`** for plain data containers instead of hand-written `__init__`/`__repr__`.
- **Use `enum.Enum`** for fixed sets of related constants instead of bare strings/ints.
- **Always set `encoding="utf-8"`** explicitly when opening text files — platform defaults vary.
- **Use `logging` module**, not `print`, for anything beyond a throwaway script.
- **Use `contextlib.contextmanager`** for custom resource-management logic instead of manual try/finally when possible.
- **Type hints on public functions** improve reviewability even without static enforcement.
- **Use `pathlib.Path`** universally instead of string path manipulation.

## Common Pitfalls

- **Mutable default arguments**: `def f(x, items=[])` shares state across calls — use `None` sentinel and initialize inside the function.
- **Bare `except:`**: swallows `KeyboardInterrupt`/`SystemExit`. Catch specific exceptions.
- **Using `pickle` on untrusted data**: arbitrary code execution risk — use `json` for untrusted/interop data.
- **Ignoring `with` statements**: manual `open()`/`close()` leaks file descriptors on exceptions.
- **`random` for security-sensitive values**: not cryptographically secure — use `secrets` for tokens/passwords.
- **Blocking calls inside `asyncio` coroutines**: freezes the event loop — offload via `run_in_executor` or use async-native libraries.
- **String concatenation in loops**: use `"".join(parts)` instead of repeated `+=` for building large strings.
- **Comparing floats with `==`**: use `math.isclose()` for floating-point comparisons.
- **Overusing `multiprocessing` for I/O-bound work**: process overhead wastes resources; use threads or `asyncio` instead for I/O, reserve `multiprocessing`/`ProcessPoolExecutor` for CPU-bound work.

---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-python-builtin-functions
description: Explains and demonstrates Python's built-in functions (print, len, map, filter, zip, enumerate, isinstance, etc.) with correct usage patterns and idioms. Use when writing Python code that needs built-in functions, debugging misuse of built-ins, or choosing the right built-in for a task instead of writing custom code.
---

## Quick Start

```python
# Common built-ins in one glance
numbers = [5, 3, 8, 1]

len(numbers)                     # 4
sorted(numbers)                  # [1, 3, 5, 8]
sum(numbers)                     # 17
max(numbers, default=0)          # 8
list(enumerate(numbers))         # [(0, 5), (1, 3), (2, 8), (3, 1)]
list(map(str, numbers))          # ['5', '3', '8', '1']
list(filter(lambda x: x > 3, numbers))  # [5, 8]
list(zip(numbers, "abcd"))       # [(5,'a'), (3,'b'), (8,'c'), (1,'d')]
```

## Workflow

When a task needs a "helper function," check if a built-in already solves it before writing custom code.

Progress:
- [ ] Step 1: Identify the operation category (iteration, conversion, inspection, I/O, math)
- [ ] Step 2: Match to the right built-in (see reference table below)
- [ ] Step 3: Check signature/edge cases (default args, generator vs list return)
- [ ] Step 4: Verify with a quick REPL test before embedding in code

### Reference by Category

**Type conversion / construction**
`int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `dict()`, `set()`, `frozenset()`, `bytes()`, `bytearray()`, `complex()`

**Iteration & sequence ops**
`enumerate()`, `zip()`, `map()`, `filter()`, `range()`, `reversed()`, `sorted()`, `iter()`, `next()`, `all()`, `any()`

**Inspection / introspection**
`type()`, `isinstance()`, `issubclass()`, `id()`, `hasattr()`, `getattr()`, `setattr()`, `delattr()`, `dir()`, `vars()`, `callable()`

**Math / numeric**
`abs()`, `round()`, `sum()`, `min()`, `max()`, `pow()`, `divmod()`

**Functional programming**
`map()`, `filter()`, `zip()`, `sorted(key=...)`, `functools.reduce` (not built-in, note it separately)

**I/O**
`print()`, `input()`, `open()`

**Object protocol**
`len()`, `repr()`, `format()`, `hash()`, `iter()`, `next()`

**Scope / execution (use sparingly)**
`globals()`, `locals()`, `eval()`, `exec()`, `compile()`

## Examples

**Example 1: Filtering + transforming without a loop**
Input:
```python
words = ["apple", "Banana", "cherry", "Date"]
# Need: lowercase words only, capitalized
```
Output:
```python
result = [w.capitalize() for w in filter(str.islower, map(str.lower, words))]
# or simply:
result = [w.capitalize() for w in words if w[0].islower()]
```

**Example 2: Checking type safely**
Input:
```python
def process(value):
    if type(value) == list:   # fragile
        ...
```
Output:
```python
def process(value):
    if isinstance(value, list):   # handles subclasses correctly
        ...
```

**Example 3: Getting index + value together**
Input:
```python
for i in range(len(items)):
    print(i, items[i])
```
Output:
```python
for i, item in enumerate(items):
    print(i, item)
```

**Example 4: Combining two lists into pairs**
Input:
```python
names = ["Alice", "Bob"]
ages = [30, 25]
```
Output:
```python
paired = dict(zip(names, ages))
# {'Alice': 30, 'Bob': 25}
```

## Best Practices

- Prefer `isinstance()` over `type() ==` for type checks (respects inheritance).
- Use `enumerate()` instead of manual index counters.
- Use `sorted(iterable, key=..., reverse=...)` instead of manual sort logic — never write bubble sort by hand.
- `zip()` stops at the shortest iterable; use `itertools.zip_longest` if lengths may differ.
- `map()`/`filter()` return iterators (lazy) in Python 3 — wrap in `list()` to materialize.
- Use `any()`/`all()` for short-circuit boolean checks instead of manual loops with flags.
- Give `min()`/`max()` a `default=` value when the iterable might be empty, to avoid `ValueError`.
- Avoid `eval()`/`exec()` on untrusted input — they execute arbitrary code.
- Use `open()` with a context manager (`with open(...) as f:`) to ensure files close properly.

## Common Pitfalls

- **Comparing types with `==` instead of `isinstance()`** — breaks for subclasses.
- **Forgetting `map`/`filter`/`zip`/`range` are iterators** — printing them shows a generator object, not values; wrap with `list()`.
- **Using `eval()` for parsing data** — use `ast.literal_eval()` or `json.loads()` instead.
- **Calling `max()`/`min()` on an empty sequence** without `default=` — raises `ValueError`.
- **Shadowing built-ins** by naming variables `list`, `dict`, `str`, `len`, `type`, etc. — silently breaks later code using the real built-in.
- **Using `input()` return value as a number directly** — it's always a string; cast with `int()`/`float()`.
- **Assuming `sorted()` mutates in place** — it returns a new list; use `.sort()` on the list itself for in-place mutation.

---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-python-builtin-constants
description: Explains and applies Python's built-in constants (True, False, None, NotImplemented, Ellipsis, __debug__) correctly in code, including their semantics, identity checks, and common usage patterns. Use when writing Python code that involves boolean logic, singleton sentinel values, operator overloading fallbacks, type stubs/slicing, or assertions/debug-guarded code.
---

## Quick Start

```python
# Boolean constants — subclass of int, True == 1, False == 0
is_active = True
count = int(True) + int(False)  # 1

# None — the singleton "no value" sentinel
def find_user(id):
    return None  # use `is None` / `is not None`, never `== None`

result = find_user(1)
if result is None:
    print("not found")

# NotImplemented — return from rich comparison / arithmetic dunder methods
class Vector:
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

# Ellipsis (...) — placeholder in slices, stubs, unfinished code
def stub_function() -> int: ...

matrix[..., 0]  # advanced slicing

# __debug__ — True unless Python run with -O
if __debug__:
    assert isinstance(count, int)
```

## Workflow

Progress:
- [ ] Identify which built-in constant fits the situation (boolean, sentinel, fallback, placeholder, debug flag)
- [ ] Apply correct comparison/usage idiom (`is`, not `==`, for singletons)
- [ ] Verify no accidental reassignment or shadowing of constant names
- [ ] Test behavior under normal and optimized (`-O`) execution if `__debug__` is involved
- [ ] Apply the pattern into your target AI model/agent prompts or codebase

### Detail per constant

1. **`True` / `False`**
   - Instances of `int` (subclass `bool`); `True == 1`, `False == 0`.
   - Never reassign — reserved keywords since Python 3.

2. **`None`**
   - The sole instance of `NoneType`. Represents absence of value.
   - Always compare with `is None` / `is not None`.
   - Default return value of functions with no explicit `return`.

3. **`NotImplemented`**
   - Returned (not raised) from binary special methods (`__eq__`, `__lt__`, `__add__`, etc.) when the operation is unsupported for given operand types, letting Python try the reflected method or raise `TypeError`.
   - Do NOT use in a boolean context (`if x == NotImplemented` is wrong — deprecated/warns); use `x is NotImplemented`.
   - Distinct from `NotImplementedError` (an exception, used in abstract methods).

4. **`Ellipsis` (`...`)**
   - Singleton, usable as literal `...`.
   - Common uses: NumPy/array slicing, type hint stubs (`.pyi` files), placeholder body for unimplemented functions, `typing.Callable[..., ReturnType]`.

5. **`__debug__`**
   - `True` under normal execution, `False` when Python started with `-O`/`-OO`.
   - Read-only; assigning to it is a `SyntaxError`.
   - `assert` statements are compiled out entirely when `__debug__` is `False` — don't rely on `assert` for required runtime validation (e.g., input sanitization).

## Examples

**Example 1:**
Input: "Bagaimana cara mengecek apakah variabel kosong di Python?"
Output:
```python
value = None
if value is None:
    print("Variabel kosong")
```
Explanation: gunakan `is None`, bukan `== None`, karena `None` adalah singleton.

**Example 2:**
Input: "Buat class custom yang bisa dibandingkan dengan `==` tapi aman terhadap tipe lain."
Output:
```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount
```

**Example 3:**
Input: "Tulis stub function untuk API yang belum diimplementasi."
Output:
```python
def process_payment(order_id: str) -> bool: ...
```

**Example 4:**
Input: "Kapan assert tidak akan jalan?"
Output: Ketika script dijalankan dengan `python -O script.py`, karena `__debug__` menjadi `False` dan semua statement `assert` dihilangkan saat compile.

## Best Practices

- Gunakan `is`/`is not` untuk `None`, `NotImplemented`, `Ellipsis` — ini adalah singleton by identity, bukan value.
- Jangan gunakan `assert` untuk validasi input produksi (bisa hilang dengan `-O`); gunakan `raise ValueError(...)` eksplisit.
- Saat overload operator, selalu `return NotImplemented` (bukan `raise`) agar Python bisa fallback ke reflected method operand lain.
- Simpan hasil riset dokumentasi resmi (docs.python.org) sebagai referensi utama sebelum menerapkan ke prompt AI Agent — pastikan versi Python yang ditarget sesuai (di sini 3.16, masih pre-release/dev docs, cek ulang saat versi stabil rilis).
- Saat menerapkan skill ke berbagai platform AI (multi-platform workflow), uji konsistensi output pada tiap platform sebelum finalisasi.

## Common Pitfalls

- Menulis `if x == None` atau `if x == NotImplemented` — gunakan `is`.
- Meng-*raise* `NotImplemented` seolah exception — itu bukan exception, gunakan `NotImplementedError` untuk abstract method yang belum diimplementasikan.
- Bergantung pada `assert` untuk logic penting yang harus selalu jalan di production.
- Mencoba assign ke `__debug__`, `True`, `False`, atau `None` — akan menghasilkan `SyntaxError`.
- Lupa memverifikasi bahwa dokumentasi versi 3.16 masih development/unstable — selalu cross-check dengan changelog resmi sebelum mengunci skill ke versi tersebut.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-builtin-constants
description: Explains and applies Python's built-in constants (True, False, None, NotImplemented, Ellipsis, __debug__, and site-module-added constants like quit, exit, copyright, credits, license) correctly in code. Use when writing code that involves boolean logic, null checks, singleton comparisons, operator overloading with NotImplemented, ellipsis slicing, debug-conditional code, or when explaining differences between these constants.
---

## Quick Start

```python
# Correct usage patterns for Python built-in constants

# None: absence of a value, always compare with `is`
def find_user(id):
    result = None
    return result

if result is None:
    print("not found")

# True/False: instances of bool, subclass of int
assert True == 1 and False == 0
assert isinstance(True, int)

# NotImplemented: returned from special methods, not raised
class Vector:
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x

# Ellipsis (...): placeholder in slicing, stubs, type hints
def stub_function() -> int:
    ...

matrix[..., 0]  # slice shorthand for multi-dim arrays

# __debug__: True unless run with -O flag
if __debug__:
    print("debug mode checks run")
assert some_condition  # skipped entirely when -O is used

# Site-module constants (interactive shell only, not for scripts)
# quit, exit, copyright, credits, license
```

## Workflow

Progress:
- [ ] Identify which constant fits the semantic need (null vs boolean vs unimplemented vs placeholder)
- [ ] Use correct comparison idiom (`is`/`is not` for None, NotImplemented)
- [ ] Never use site-module constants (`quit`, `exit`, `copyright`, etc.) in production code
- [ ] Use `__debug__` for development-only assertions, not for security or business logic
- [ ] Return `NotImplemented` (don't raise it) inside dunder methods when operation isn't supported

### Step 1: Distinguish the six core constants

| Constant | Type | Purpose | Comparison |
|---|---|---|---|
| `True`/`False` | `bool` | Boolean truth values | `==`, `is` both work (singletons) |
| `None` | `NoneType` | "No value" / null | Always `is None` / `is not None` |
| `NotImplemented` | `NotImplementedType` | Signal unsupported operation in rich comparisons/arithmetic dunders | Return it, don't raise; don't use in boolean context |
| `Ellipsis` (`...`) | `EllipsisType` | Placeholder — slicing, stub bodies, type hints | Rarely compared; used as syntax `...` |
| `__debug__` | `bool` | True normally, False with `-O`/`-OO` | Use in `if __debug__:` guards |

### Step 2: Apply idiomatic patterns

**None checks:**
```python
if value is None:      # correct
if value == None:      # avoid — triggers __eq__, can misbehave
```

**NotImplemented in operator overloading:**
```python
def __lt__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented   # let Python try other.__gt__ or raise TypeError
    return self.value < other.value
```
Never do `if x == NotImplemented` or use it as a boolean — treat it strictly as a return sentinel.

**Ellipsis for stubs and slicing:**
```python
def not_yet_implemented(): ...

# numpy-style slicing
arr[..., 0]   # equivalent to arr[:, :, 0] for 3D array
```

**__debug__ for assert-guarded code:**
```python
if __debug__:
    _validate_invariants()  # stripped out entirely under python -O
```
Never rely on `__debug__`/`assert` for security checks — they vanish under `-O`.

### Step 3: Handle site-module constants correctly

`quit`, `exit`, `copyright`, `credits`, `license` are added by the `site` module **only in interactive interpreter sessions**. They:
- Are NOT guaranteed to exist in scripts, embedded interpreters, or when run with `-S`
- Should never be used programmatically (e.g., `exit()` in a script) — use `sys.exit()` instead
- Exist purely for human convenience at the REPL

```python
# Bad: script relying on interactive-only builtins
exit()  # may not exist if site module wasn't imported

# Good:
import sys
sys.exit(0)
```

## Examples

**Example 1:**
Input: Function should return `None` when no match is found, and caller needs to check.
Output:
```python
def find(items, target):
    for item in items:
        if item == target:
            return item
    return None

result = find([1, 2, 3], 5)
if result is None:
    print("Not found")
```

**Example 2:**
Input: Implement `__eq__` for a custom class that should support comparison only with same type.
Output:
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
```

**Example 3:**
Input: Write a type stub file (`.pyi`) function signature with no body.
Output:
```python
def process(data: list[int]) -> dict[str, int]: ...
```

**Example 4:**
Input: Code has `assert isinstance(x, int)` used to validate untrusted user input for a security check.
Output: Flag as pitfall — replace with explicit runtime check:
```python
if not isinstance(x, int):
    raise TypeError("x must be int")
```
Reason: `assert` and reliance on `__debug__` are removed with `-O`, so security-critical validation must never depend on them.

## Best Practices

- Always use `is`/`is not` for `None` and `NotImplemented` — they are singletons; identity comparison is faster and avoids operator overload surprises.
- Return `NotImplemented`, never raise it — raising breaks Python's reflected-operation fallback mechanism (`__radd__`, `__req__`, etc.).
- Use `Ellipsis`/`...` for stub bodies instead of `pass` when signaling "unimplemented but intentional" (helps distinguish from placeholder `pass`).
- Gate expensive diagnostic code with `if __debug__:` to let `-O` optimize it away in production.
- Prefer `sys.exit()` over the site-added `exit()`/`quit()` in any script or module.
- Remember `bool` is a subclass of `int`: `True + True == 2` is valid but should be avoided for readability — don't rely on this arithmetic behavior in serious code.

## Common Pitfalls

- **Comparing with `==` instead of `is`** for `None`/`NotImplemented` — can trigger unexpected `__eq__` behavior or return ambiguous truthy/falsy results.
- **Using `NotImplemented` in a boolean context** (e.g., `if not_implemented_value:`) — it's truthy, so `if x:` doesn't tell you whether an operation failed; always check `is NotImplemented` explicitly if needed.
- **Confusing `NotImplemented` with `NotImplementedError`** — the former is a value returned from dunder methods; the latter is an exception raised in abstract methods. They are not interchangeable.
- **Relying on `assert`/`__debug__` for input validation or security** — stripped under `python -O`, creating silent security holes.
- **Using `quit()`, `exit()`, `copyright`, `credits`, `license` in production scripts** — only guaranteed in interactive sessions; absent when `site` isn't imported (e.g., `-S` flag, embedded interpreters, some frozen apps).
- **Overusing `Ellipsis` outside stubs/slicing** — using `...` as a generic "TODO" placeholder in real logic paths can silently pass type checks while doing nothing at runtime.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: evaluating-python-truthiness
description: Determines the truth value of Python objects according to CPython's truth-value testing rules for use in conditionals, boolean contexts, and while/if statements. Use when reasoning about how Python evaluates objects as True or False, writing conditionals that rely on implicit truthiness, or debugging unexpected boolean behavior of custom objects.
---

## Quick Start

Python evaluates any object's truth value using `bool(obj)`. By default, everything is truthy except a specific set of built-in falsy values:

```python
# Falsy values
False, None, 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
'', (), [], {}, set(), frozenset(), range(0)

# Everything else is truthy
if []:      # False - empty list
if [0]:     # True  - non-empty list (even containing 0)
if "0":     # True  - non-empty string
```

## Workflow

1. **Identify the object's type category:**
   - Numeric type → falsy if equal to zero
   - Container/sequence → falsy if `len(obj) == 0`
   - Custom class → check for `__bool__`, then `__len__`, then default `True`

2. **Determine which dunder method controls truthiness:**
   ```
   Progress:
   - [ ] Does the class define __bool__? → its return value (must be bool) wins
   - [ ] No __bool__, but defines __len__? → truthy iff len(obj) != 0
   - [ ] Neither defined? → object is always truthy
   ```

3. **Validate `__bool__` implementation** — it must return an actual `bool`; returning something else raises `TypeError`.

## Examples

**Example 1:**
Input: `bool(0.0)`
Output: `False` — numeric zero of any numeric type is falsy.

**Example 2:**
Input:
```python
class Bucket:
    def __len__(self):
        return 0
bool(Bucket())
```
Output: `False` — no `__bool__` defined, falls back to `__len__`, which returns 0.

**Example 3:**
Input:
```python
class AlwaysTrue:
    pass
bool(AlwaysTrue())
```
Output: `True` — no `__bool__` or `__len__`, default object truthiness applies.

**Example 4:**
Input:
```python
class Weird:
    def __bool__(self):
        return "yes"
bool(Weird())
```
Output: `TypeError: __bool__ should return bool, returned str`

## Best Practices

- Prefer implicit truthiness checks (`if items:`) over explicit comparisons (`if len(items) > 0:`) for containers — it's idiomatic and handles all falsy cases uniformly.
- When designing custom classes meant to be used in boolean contexts, implement `__bool__` explicitly rather than relying on `__len__` inference if the semantics aren't literally "does it have length."
- Use `is None` / `is not None` instead of truthiness when you specifically care about `None` vs. other falsy values (e.g., `0` or `""` are valid but falsy).

## Common Pitfalls

- **Confusing `0`, `""`, `[]`, and `None` in conditionals** — `if x:` treats all of these as `False`; use explicit checks (`if x is None`, `if x == 0`) when the distinction matters.
- **Forgetting that non-empty containers with falsy contents are still truthy** — `if [0]:` is `True` because the list has one element, regardless of that element's own truthiness.
- **Returning non-bool from `__bool__`** — this raises `TypeError`, unlike `__len__`, which just needs to return a non-negative integer.
- **Assuming NaN is falsy** — `bool(float('nan'))` is `True`; only actual zero values are falsy for numerics.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: applying-boolean-operations
description: Applies Python's short-circuit boolean operations (and, or, not) correctly, including their evaluation rules, return values, and truthiness semantics. Use when writing conditional logic, default-value expressions, guard clauses, or reviewing code that relies on and/or for control flow instead of pure booleans.
---

# Applying Boolean Operations

## Quick Start

```python
# and/or return operands, not True/False
x = None
y = x or "default"        # "default"
z = x and x.upper()       # None (short-circuits, avoids AttributeError)

# not always returns True/False
flag = not []              # True
```

Key facts (Python `and`, `or`, `not`):
- `not x` → `True` if `x` is false, else `False`. Always boolean.
- `x and y` → evaluates `x`; if `x` is false, returns `x` (unevaluated `y`); else returns `y`.
- `x or y` → evaluates `x`; if `x` is true, returns `x` (unevaluated `y`); else returns `y`.
- Both `and`/`or` **short-circuit**: the second operand is only evaluated if needed.
- `not` has lower priority than non-Boolean operators, so `not a == b` is `not (a == b)`.

## Workflow

1. Identify whether you need a strict boolean (`True`/`False`) or an operand value.
   - Strict boolean → wrap with `bool(...)` or use `not not x`, or prefer explicit comparisons.
   - Operand value (e.g., default fallback) → use `or`/`and` directly.
2. Order operands so the cheap/safe check comes first — it determines whether the expensive/unsafe one runs.
3. Use `and` as a guard: `obj and obj.method()` avoids calling on `None`/falsy objects.
4. Use `or` for defaults: `value = user_input or fallback` — but beware falsy-but-valid values (`0`, `""`, `[]`).
5. Chain carefully: `a and b or c` is **not** a ternary; if `b` is falsy, `c` wins even when `a` is true. Use `b if a else c` instead.

## Examples

**Example 1 — safe attribute access:**
Input:
```python
config = None
timeout = config and config.get("timeout")
```
Output: `timeout = None` (short-circuits before calling `.get`)

**Example 2 — default value pitfall:**
Input:
```python
count = 0
display = count or "N/A"
```
Output: `display = "N/A"` — `0` is falsy, so this may be a bug if `0` is a valid count. Fix: `display = count if count is not None else "N/A"`.

**Example 3 — fake ternary trap:**
Input:
```python
result = True and 0 or "fallback"
```
Output: `"fallback"` — even though the condition (`True`) suggests `0` should win, `0` is falsy so `or` moves to the next operand. Use `0 if True else "fallback"` to get `0`.

**Example 4 — not precedence:**
Input:
```python
x = 5
print(not x == 5)
```
Output: `False`, because it parses as `not (x == 5)`.

## Best Practices

- Prefer `if/else` or conditional expressions (`a if cond else b`) over `and/or` chains when you need real ternary behavior.
- Use `and`/`or` for their natural short-circuit purpose: guards and defaults, not general branching.
- When you need a real boolean (e.g., for JSON serialization or strict typing), coerce explicitly with `bool(...)`.
- Remember truthiness: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, and `False` are all falsy.
- Combine with `is None` checks when falsy-but-valid values (`0`, `""`) must be distinguished from "missing."

## Common Pitfalls

- Assuming `and`/`or` return `True`/`False` — they return one of the operands.
- Using `a and b or c` as a ternary — fails silently when `b` is falsy.
- Forgetting `not`'s low precedence, leading to unintended groupings like `not a == b`.
- Relying on `or` for defaults when `0`, `""`, or `[]` are legitimate values.
- Evaluating expensive/side-effecting code in the second operand without realizing short-circuiting may skip it entirely (or unexpectedly not skip it).

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: comparing-python-objects
description: Explains Python's comparison operators and semantics, including rich comparisons, chained comparisons, and default equality/ordering behavior. Use when writing __eq__/__lt__/__gt__ methods, debugging comparison-related bugs, implementing sortable/comparable classes, or reasoning about how Python compares built-in types like numbers, sequences, and mixed types.

---

## Quick Start

Python has 8 comparison operators, all with the same priority and left-to-right chaining:

```python
<   <=   >   >=   ==   !=   is   is not
```

Default behavior:
- `==` / `!=` fall back to identity (`is`/`is not`) if no `__eq__` is defined.
- `<`, `<=`, `>`, `>=` raise `TypeError` unless the type defines them (no default ordering).
- Objects are compared using **rich comparison methods**, not a single `__cmp__`.

To make a class fully comparable, implement `__eq__` and one ordering method, then use `functools.total_ordering`:

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)
```

## Workflow

When implementing or debugging comparisons on a class:

- [ ] Decide if identity-based default (`is`) is sufficient — if so, skip overrides.
- [ ] Implement `__eq__` returning `NotImplemented` for incompatible types (not `False`).
- [ ] Implement `__lt__` (and optionally `__le__`, `__gt__`, `__ge__`) — or just `__lt__`/`__eq__` + `@total_ordering`.
- [ ] Ensure consistency: if `a == b`, then `hash(a) == hash(b)` (define `__hash__` alongside `__eq__`, or set `__hash__ = None` for unhashable/mutable types).
- [ ] Test reflected operations: `a < b` calls `b.__gt__(a)` if `a.__lt__(b)` returns `NotImplemented`.
- [ ] Check chained comparisons behave correctly (`a < b < c` is `a < b and b < c`, each side evaluated once).

## Comparison Rules Reference

**Rich comparison methods** (in order Python tries them):
| Operator | Method |
|---|---|
| `<` | `__lt__` |
| `<=` | `__le__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |
| `==` | `__eq__` |
| `!=` | `__ne__` (defaults to inverting `__eq__`) |

**Reflection rule:** For `a OP b`, if `a`'s method returns `NotImplemented`, Python tries `b`'s reflected method (`<` ↔ `>`, `<=` ↔ `>=`, `==`/`!=` reflect to themselves). If both return `NotImplemented`, `==`/`!=` fall back to identity; ordering operators raise `TypeError`.

**Built-in type comparison behavior:**
- **Numbers** (`int`, `float`, `complex`, `Decimal`, `Fraction`): compared by mathematical value across types (`1 == 1.0` is `True`); `complex` only supports `==`/`!=`, not ordering.
- **Sequences** (same type, e.g. two `list`s or two `tuple`s): compared lexicographically — element-by-element, first mismatch decides, shorter-is-less if one is a prefix of the other.
- **Mixed sequence types** (e.g. `list` vs `tuple`): `==`/`!=` work structurally only for same type; ordering between different sequence types raises `TypeError`.
- **str, bytes, bytearray**: lexicographic by underlying code points/byte values. `str` and `bytes` are never equal or orderable to each other.
- **dict**: `==`/`!=` compare keys and values regardless of order; no ordering operators.
- **set/frozenset**: `==` is set equality; `<`, `<=`, `>`, `>=` mean subset/superset (partial order, not total — some sets are simply "not comparable" and both `<` and `>` return `False`).
- **NaN**: `float('nan') != float('nan')` and all ordering comparisons with NaN are `False`.

## Examples

**Example 1: Chained comparison pitfall**
Input:
```python
1 < 2 < 3
```
Output: `True` — equivalent to `(1 < 2) and (2 < 3)`, `2` evaluated once, not `(1 < 2) < 3` (`True < 3`).

**Example 2: Mixed sequence ordering**
Input:
```python
[1, 2] < (1, 2)
```
Output: `TypeError: '<' not supported between instances of 'list' and 'tuple'` — ordering requires same/compatible types even though `==` between them (structurally) would just be `False`, not an error.

**Example 3: Set partial order**
Input:
```python
{1, 2} < {2, 3}
```
Output: `False` (not a subset) — and `{1, 2} > {2, 3}` is also `False`. Sets are a partial order, so "not `<`" does not imply "`>=`".

**Example 4: NotImplemented vs False**
Input: A custom `__eq__` compares against an unrelated type and returns `False` instead of `NotImplemented`.
Output: Breaks reflection — if the other object's `__eq__` would have returned `True`, Python never gets the chance to try it, since `False` short-circuits the comparison as "handled."

## Best Practices

- Always return `NotImplemented` (not `False`/`True`) from comparison methods when the other operand's type is unsupported — this lets Python try the reflected method.
- Use `functools.total_ordering` instead of hand-writing all six comparison methods.
- If you define `__eq__`, explicitly decide on `__hash__`: inherit/reuse it if the object is still hashable, or set `__hash__ = None` if mutable/unhashable.
- Prefer `==` over `is` for value comparisons; reserve `is` for singleton checks (`None`, `True`, `False`, enum members).
- Remember sequence/number comparisons are element-wise/value-wise, not identity-wise — don't assume `==` implies `is`.

## Common Pitfalls

- Comparing `NaN` and expecting equality/reflexivity — `nan == nan` is `False` by IEEE 754 design.
- Assuming all types support ordering — many (complex numbers, dicts, mixed sequence types) only support `==`/`!=`.
- Returning `False` instead of `NotImplemented` in custom `__eq__`/`__lt__`, silently breaking comparisons with subclasses or duck-typed objects.
- Forgetting that `!=` doesn't automatically invert a custom `__eq__` in old-style implementations — in modern Python it does by default, but overriding `__eq__` without checking `__ne__` behavior in edge cases (e.g., returning `NotImplemented`) can cause inconsistencies.
- Treating set `<`/`>` as a total order — two sets can be simultaneously "not less than" and "not greater than" each other.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: working-with-python-numeric-types
description: Explains and applies Python's numeric types (int, float, complex), their operators, conversions, and built-in methods. Use when writing code that performs arithmetic, handles number formatting, needs precise type conversions, or debugges numeric type errors in Python.
---

## Quick Start

```python
# Three numeric types: int, float, complex
a = 5          # int
b = 3.14       # float
c = 2 + 3j     # complex

# Mixed arithmetic promotes to the "wider" type: int -> float -> complex
result = a + b        # 8.14 (float)
result2 = a + c        # (7+3j) (complex)

# True division always returns float
print(7 / 2)    # 3.5
print(7 // 2)   # 3   (floor division)
print(7 % 2)    # 1   (modulo)
print(divmod(7, 2))  # (3, 1)
```

## Workflow

When writing or debugging numeric code, work through this checklist:

Progress:
- [ ] Identify which numeric type each value should be (int/float/complex)
- [ ] Choose the correct operator for the intended semantics (`/` vs `//`, `**` vs `pow()`)
- [ ] Handle type promotion/conversion explicitly where precision matters
- [ ] Guard against division-by-zero and float precision pitfalls
- [ ] Use appropriate formatting/rounding for output

### 1. Identify the right type
- Use `int` for counts, indices, exact values.
- Use `float` for measurements, results of division, scientific computation.
- Use `complex` only when working with imaginary components (signal processing, engineering math).

### 2. Choose operators deliberately

| Operator | Meaning | Example |
|---|---|---|
| `+ - *` | standard arithmetic | `3 * 4 -> 12` |
| `/` | true division (always float) | `5 / 2 -> 2.5` |
| `//` | floor division | `5 // 2 -> 2`, `-5 // 2 -> -3` |
| `%` | modulo (sign follows divisor) | `-5 % 2 -> 1` |
| `**` | exponentiation | `2 ** 10 -> 1024` |
| `divmod(a, b)` | `(a//b, a%b)` in one call | `divmod(5,2) -> (2,1)` |

### 3. Convert explicitly
```python
int(3.9)      # 3  (truncates toward zero, NOT rounds)
int("42")     # 42
float(3)      # 3.0
complex(1, 2) # (1+2j)
round(3.567, 2)  # 3.57 (banker's rounding on .5 boundaries)
```

### 4. Know int-specific tools
```python
(10).bit_length()      # 4
(255).to_bytes(2, 'big')       # b'\x00\xff'
int.from_bytes(b'\xff', 'big') # 255
(-7).__abs__()          # 7, or just abs(-7)
```

### 5. Know float-specific tools
```python
(3.75).as_integer_ratio()   # (15, 4)
(3.75).is_integer()         # False
float('inf'), float('nan')  # special values
import math
math.isclose(0.1 + 0.2, 0.3)  # True (handles float precision)
```

### 6. Know complex-specific tools
```python
z = 3 + 4j
z.real       # 3.0
z.imag       # 4.0
z.conjugate()  # (3-4j)
abs(z)       # 5.0 (magnitude)
```

## Examples

**Example 1:**
Input: Compute average of a list of ints and format to 2 decimal places.
Output:
```python
nums = [1, 2, 3, 4]
avg = sum(nums) / len(nums)   # 2.5 (float, true division)
print(f"{avg:.2f}")           # "2.50"
```

**Example 2:**
Input: Check whether 0.1 + 0.2 == 0.3 fails and fix it.
Output:
```python
0.1 + 0.2 == 0.3          # False, due to float precision
import math
math.isclose(0.1 + 0.2, 0.3)  # True — correct check
```

**Example 3:**
Input: Convert a negative float to int and explain the result.
Output:
```python
int(-3.9)   # -3, truncates toward zero (not floor)
import math
math.floor(-3.9)  # -4, use this if flooring is intended
```

## Best Practices

- Prefer `/` for math that should return float; use `//` only when floor semantics are intended.
- Use `math.isclose()` instead of `==` for float comparisons.
- Use `decimal.Decimal` or `fractions.Fraction` instead of float when exact precision matters (money, ratios).
- Use f-strings with format specs (`:.2f`, `:,`, `:e`) for numeric display instead of manual string building.
- Remember `bool` is a subclass of `int` (`True == 1`), which affects arithmetic and can cause subtle bugs.

## Common Pitfalls

- Assuming `int()` rounds — it truncates toward zero, not floors or rounds.
- Assuming `//` always floors — it does, but for negative numbers this differs from truncation (`-5 // 2 == -3`, not `-2`).
- Using `==` to compare floats after arithmetic.
- Forgetting that `%` result sign follows the divisor's sign in Python (differs from some other languages).
- Mixing `complex` into ordering comparisons (`<`, `>`) — complex numbers are unorderable and will raise `TypeError`.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: explaining-python-stdlib
description: Explains Python standard library types, functions, and modules with accurate technical details drawn from official documentation conventions. Use when a user asks about Python built-in types (bool, int, str, list, dict), stdlib modules (collections, itertools, datetime, re, functools), their methods, behaviors, edge cases, or version-specific changes.
---

# Explaining Python Standard Library

## Quick Start

When asked about any stdlib entity, first classify it, then answer with structure:
1. **Category**: builtin type / stdlib module / function / method / protocol
2. **Signature or construction**
3. **Key behaviors**, especially non-obvious ones
4. **Minimal runnable example**
5. **Related entities** worth knowing

Example for a builtin type (`bool`):

```python
>>> issubclass(bool, int)      # bool is an int subclass, only 2 instances
True
>>> True + True
2
>>> bool([0])                  # non-empty list -> truthy, even though element is falsy
True
```

Example for a stdlib module function (`itertools.groupby`):

```python
from itertools import groupby
# groupby only groups CONSECUTIVE equal keys — a frequent gotcha
data = [1, 1, 2, 1]
print([(k, list(g)) for k, g in groupby(data)])
# [(1, [1, 1]), (2, [2]), (1, [1])]  -- NOT grouped by value across the list
# fix: sort first if you want all equal keys grouped together
```

## Workflow

Progress:
- [ ] Determine scope: single function/method, a type, or an entire module?
- [ ] If scope is a whole module (e.g., "explain `collections`"), give a one-line summary of each major member first, then drill into the one most relevant to the user's actual goal — don't dump the full API.
- [ ] If scope is a single type/function, go directly to signature + behavior + example.
- [ ] If the question spans multiple stdlib areas (e.g., "how do I dedupe while preserving order" touches `dict`, `set`, and `itertools`), briefly compare 2-3 approaches with trade-offs instead of picking one silently.
- [ ] Identify surprising/edge-case behavior specific to that entity (mutability, ordering, laziness, locale/timezone sensitivity, etc.)
- [ ] Give a short, correct, copy-pasteable example demonstrating the surprising behavior, not just the happy path.
- [ ] Note version-specific changes if relevant ("changed in 3.7", "added in 3.9") — flag uncertainty rather than guessing.
- [ ] Cross-reference related types/functions/modules when it clarifies behavior or offers a better tool for the job.

## Examples

**Example 1: Single builtin type**
Input: "Why does `bool([0]) == True` but `bool(0) == False`?"
Output:
> Truth-value testing treats as false: `None`, `False`, numeric zero (`0`, `0.0`), and empty containers (`''`, `[]`, `{}`, `()`, `set()`) — or objects whose `__bool__`/`__len__` say so. `[0]` is a list of length 1 (truthy container), even though its only element is falsy. `0` is itself a falsy number. Container truthiness depends on length, not on the truthiness of contents.

**Example 2: Module-level ambiguous query**
Input: "Tell me about the `collections` module."
Output:
> `collections` provides specialized container types beyond the builtins:
> - `Counter` — multiset/frequency counting (`Counter("aab")` → `Counter({'a': 2, 'b': 1})`)
> - `defaultdict` — dict with a factory for missing keys, avoids `KeyError` boilerplate
> - `deque` — O(1) appends/pops from both ends, unlike `list`'s O(n) `pop(0)`
> - `namedtuple` — lightweight immutable record type with named fields
> - `OrderedDict` — mostly redundant since dicts preserve insertion order (3.7+), but still useful for `move_to_end()` and equality that considers order
>
> Which one matches what you're building? If it's "count occurrences," `Counter` is the direct answer — e.g. `Counter(words).most_common(3)`.

**Example 3: Cross-module comparison**
Input: "How do I remove duplicates from a list but keep order?"
Output:
> Three options, trade-offs differ:
> ```python
> list(dict.fromkeys(items))          # simplest, O(n), Python 3.7+ dict order guarantee
> 
> seen = set()
> [x for x in items if not (x in seen or seen.add(x))]  # explicit, works pre-3.7 too
> 
> from more_itertools import unique_everseen  # not stdlib — only if already a dependency
> ```
> Default recommendation: `list(dict.fromkeys(items))` — concise and relies on documented dict behavior, not an implementation detail.

**Example 4: Datetime quirk**
Input: "Why did subtracting two `datetime` objects give unexpected results?"
Output:
> `datetime` subtraction returns a `timedelta`, which stores only `days`, `seconds`, and `microseconds` — accessing `.seconds` alone on a multi-day delta gives just the *remainder* seconds, not the total:
> ```python
> from datetime import datetime
> d = datetime(2024, 1, 3) - datetime(2024, 1, 1, 23, 0, 0)
> print(d.days, d.seconds)      # 0 1200 (1 hour left after the days)
> print(d.total_seconds())      # 3600.0 total elapsed seconds — the one you usually want
> ```
> Also: naive vs. aware datetimes can't be subtracted/compared (`TypeError`) — check `d.tzinfo is None` when debugging.

## Best Practices

- Show behavior via runnable snippets, not prose-only claims.
- For containers/types: state mutability, hashability, ordering guarantees explicitly (e.g., "tuples are hashable if all elements are hashable; lists never are").
- For modules: summarize breadth first if the question is broad, then go deep on the part matching the user's actual need.
- When multiple stdlib tools solve the same problem, name 2-3 and give the default recommendation rather than an exhaustive survey.
- Always state Python version when behavior is version-dependent instead of assuming the latest release.

## Common Pitfalls

- Don't answer a whole-module question with a single deep-dive on one function — scan the module's main members first.
- Don't treat `==` equality as identity; call out `is` only when singleton/identity actually matters (e.g., `True`/`False`/`None`, small int caching).
- Don't assume container truthiness or equality without checking length/type rules (e.g., `bool("0")` is `True`).
- Don't state stdlib behavior from memory without flagging version sensitivity when unsure — signatures and defaults do change across releases (e.g., `dict` ordering became guaranteed in 3.7).

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: implementing-python-iterator-protocol
description: Implements and reasons about Python's iterator protocol, including iterator/iterable distinctions, generator-based iterators, and common iteration patterns. Use when writing custom iterators, debugging "object is not an iterator" errors, implementing __iter__/__next__, or explaining how for-loops, comprehensions, and unpacking use iteration under the hood.
---

## Quick Start

```python
class Countdown:
    """An iterable that returns a fresh iterator each time."""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)

class CountdownIterator:
    """The actual iterator: stateful, implements __next__."""
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self  # iterators must be iterable too

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(3):
    print(n)  # 3 2 1
```

Simpler version using a generator function (preferred in almost all real code):

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1
```

## Workflow

Progress:
- [ ] Determine if you need a reusable **iterable** (supports multiple independent iterations) or a one-shot **iterator**
- [ ] Choose implementation style: generator function, generator expression, or explicit class
- [ ] Implement `__iter__` (and `__next__` if a class-based iterator)
- [ ] Ensure `StopIteration` is raised correctly (or let generator return naturally)
- [ ] Verify with `iter()`, `next()`, and a `for` loop
- [ ] If stateful resource cleanup is needed, consider a context manager instead/alongside

### Core distinction

- **Iterable**: has `__iter__()` returning an iterator. Can be iterated over repeatedly, each time producing a new iterator.
- **Iterator**: has both `__iter__()` (returning itself) and `__next__()` (returning next value or raising `StopIteration`). Exhausted after one full pass — cannot restart.

Rule of thumb: **containers are iterables, not iterators**. If `__iter__` returns `self`, the object is single-use.

### Choosing an implementation

1. **Generator function** (`yield`) — default choice. Automatically implements the full protocol; state is managed by the interpreter via the frame.
2. **Generator expression** — for simple one-liner transformations of an existing iterable: `(x*x for x in range(10))`.
3. **Explicit class** — only when you need:
   - A reusable iterable (separate `__iter__` returning fresh iterator state each call)
   - Extra methods/attributes on the iterator itself
   - Fine control not expressible with `yield` (rare)

## Examples

**Example 1: Iterable vs iterator bug**

Input:
```python
class Numbers:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        v = self.data[self.i]
        self.i += 1
        return v

nums = Numbers([1, 2, 3])
print(list(nums))
print(list(nums))  # second call — what happens?
```
Output:
```
[1, 2, 3]
[]
```
Explanation: `Numbers` is its own iterator (`__iter__` returns `self`), so it's exhausted after the first pass. Fix by separating iterable state (`data`) from iterator state (`i`) into two classes, or by making `__iter__` return a fresh generator: `def __iter__(self): return iter(self.data)`.

**Example 2: Infinite iterator with manual protocol**

Input:
```python
def take(iterable, n):
    it = iter(iterable)
    result = []
    for _ in range(n):
        result.append(next(it))
    return result

def naturals():
    n = 1
    while True:
        yield n
        n += 1

take(naturals(), 5)
```
Output: `[1, 2, 3, 4, 5]`

**Example 3: Using `next()` with a default to avoid StopIteration**

Input:
```python
it = iter([])
value = next(it, "empty")
```
Output: `"empty"` (no exception raised)

## Best Practices

- Prefer generator functions over hand-written `__next__` classes — less state to manage manually.
- If a class represents a *collection*, give it `__iter__` that returns a new generator/iterator each call, so it can be iterated multiple times (e.g., in nested loops, `zip`, list comprehensions used twice).
- Use `iter(obj, sentinel)` two-arg form to turn callables into iterators that stop at a sentinel value (e.g., reading until EOF): `iter(file.readline, '')`.
- Combine with `itertools` (`islice`, `chain`, `takewhile`) instead of reimplementing common iterator patterns.
- Let `StopIteration` propagate naturally from a generator by simply `return`ing — don't raise it manually inside a generator body (deprecated behavior, was silently swallowed pre-3.7, now `RuntimeError`).
- Document whether a returned object is a one-shot iterator or a re-iterable, since callers can't tell just from a `for` loop working once.

## Common Pitfalls

- **Exhaustion confusion**: reusing an iterator (not iterable) across multiple loops silently yields nothing the second time — no error, just empty results.
- **Raising `StopIteration` manually inside a generator**: causes `RuntimeError: generator raised StopIteration` (PEP 479). Use `return` instead.
- **Forgetting `__iter__` returns `self` in a class-based iterator** — without it, `for` loops fail with `TypeError: iter() returned non-iterator`.
- **Assuming `len()` works on iterators** — iterators don't know their remaining length in general; don't rely on `len(it)`.
- **Mutating a collection while iterating over it directly** — causes skipped elements or `RuntimeError` (for dicts/sets). Iterate over a copy (`list(d.items())`) if mutation is needed.
- **Mixing up `iterable` and `iterator` in type hints/docs** — e.g., typing a parameter as `Iterator[int]` when callers should be able to pass a list (which is `Iterable[int]`, not `Iterator[int]`) forces unnecessary `iter()` calls on callers.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-string-methods
description: Guides selection and correct usage of Python's built-in text and binary sequence methods (str, bytes, bytearray). Use when writing code that parses, formats, searches, splits, joins, or transforms text/binary data in Python.
---

## Quick Start

```python
# Common patterns at a glance
"  hello world  ".strip()                    # 'hello world'
"hello,world,foo".split(",")                 # ['hello', 'world', 'foo']
",".join(["a", "b", "c"])                    # 'a,b,c'
"Hello {}!".format("World")                  # 'Hello World!'
f"Hello {name}!"                             # preferred over .format() for literals
"HELLO".lower()                              # 'hello'
"hello".startswith("he")                     # True
"hello".replace("l", "L")                    # 'heLLo'
b"data".decode("utf-8")                      # str
"data".encode("utf-8")                       # bytes
```

## Workflow

1. **Identify the data type**: `str` (text), `bytes`/`bytearray` (binary/encoded). Never mix `str` and `bytes` in one operation — decide which you have and convert explicitly with `.encode()`/`.decode()`.
2. **Pick the narrowest method for the task** — don't hand-roll logic that a stdlib method already does (see table below).
3. **Prefer immutable-safe patterns**: `str` and `bytes` are immutable; every "modifying" method returns a new object. Use `bytearray` only when in-place mutation is actually needed.
4. **Format output with f-strings** unless building a template string dynamically at runtime (then use `.format()`) or doing legacy `%`-formatting (avoid in new code).

### Method Selection Cheat Sheet

| Task | Method |
|---|---|
| Remove whitespace/chars from ends | `.strip()`, `.lstrip()`, `.rstrip()` |
| Split on delimiter | `.split(sep)`, `.rsplit(sep, maxsplit)` |
| Split on any whitespace, drop empties | `.split()` (no args) |
| Split into exactly 2 parts at first/last match | `.partition(sep)`, `.rpartition(sep)` |
| Split preserving line breaks | `.splitlines(keepends=False)` |
| Join iterable of strings | `sep.join(iterable)` |
| Case-insensitive-ish comparison | `.casefold()` (not `.lower()`, for Unicode correctness) |
| Check prefix/suffix | `.startswith(x)`, `.endswith(x)` — accepts tuples |
| Find substring index (or -1) | `.find()`, `.rfind()` |
| Find substring index (raises if missing) | `.index()`, `.rindex()` |
| Count occurrences | `.count(sub)` |
| Replace substring | `.replace(old, new, count=-1)` |
| Pad string | `.ljust()`, `.rjust()`, `.zfill()`, `.center()` |
| Test content type | `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`, `.isupper()`, etc. |
| Translate chars via mapping | `str.maketrans()` + `.translate()` |
| Template substitution | `.format()`, f-strings, or `string.Template` for user-supplied templates |
| bytes ↔ str | `.encode(encoding)`, `.decode(encoding)` |

## Examples

**Example 1: Parsing a CSV-like line**
Input: `line = "  Alice, 30 , Engineer  "`
Output:
```python
fields = [f.strip() for f in line.split(",")]
# ['Alice', '30', 'Engineer']
```

**Example 2: Safe substring check with multiple options**
Input: filename validation for `.jpg`/`.png`/`.gif`
Output:
```python
if filename.lower().endswith((".jpg", ".png", ".gif")):
    process(filename)
```

**Example 3: Splitting exactly once**
Input: `"key=value=extra"`, need only first split
Output:
```python
key, _, value = "key=value=extra".partition("=")
# key='key', value='value=extra'
```

**Example 4: bytes/str boundary**
Input: reading raw socket data `data = sock.recv(1024)`
Output:
```python
text = data.decode("utf-8", errors="replace")
```

## Best Practices

- Use `.casefold()` over `.lower()` for case-insensitive comparisons (handles Unicode edge cases like German ß).
- Use `.partition()`/`.rpartition()` instead of `.split(sep, 1)` when you need clean unpacking and no IndexError risk — partition always returns exactly 3 items.
- Use `in` operator (`"sub" in s`) for existence checks instead of `.find(sub) != -1` or `.count(sub) > 0`.
- Use `"".join(list_of_strs)` for concatenating many strings — never build strings with `+=` in a loop (O(n²)).
- Always pass explicit `encoding` to `.encode()`/`.decode()` (default is `'utf-8'` but being explicit avoids platform surprises and documents intent).
- Use `str.maketrans()` + `.translate()` for fast multi-character replacement instead of chained `.replace()` calls.
- For `.split()`, calling with no arguments (splits on any whitespace, collapses consecutive whitespace, strips empties) differs from `.split(" ")` (splits on literal single space, keeps empty strings) — pick deliberately.

## Common Pitfalls

- **Confusing `.strip(chars)` semantics**: `.strip("xy")` strips any combination of characters `x` and `y` from ends, not the literal substring `"xy"`.
- **Using `.split(sep, 1)[1]` for parsing**: raises `IndexError` if `sep` is absent. Prefer `.partition()` which never raises.
- **Mixing str/bytes**: `TypeError: can't concat str to bytes`. Always decode/encode at I/O boundaries, work in `str` internally.
- **Using `.index()`/`.rindex()` without a try/except or existence check** when the substring might be absent — they raise `ValueError`; use `.find()` if -1 is an acceptable sentinel.
- **Locale/Unicode-unaware case comparisons** with `.lower()` for security-sensitive checks (e.g., filename comparisons) — use `.casefold()`.
- **Forgetting `str.format()`/f-strings don't validate types** — `"{}".format(obj)` calls `__format__`/`__str__`, which may hide bugs if `obj` isn't what you expect.
- **Using `%`-style formatting in new code** — legacy, error-prone with tuples; prefer f-strings.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: manipulating-binary-sequences
description: Explains and applies Python's binary sequence types (bytes, bytearray, memoryview), including construction, conversion, slicing, and buffer-protocol operations. Use when working with binary data, byte strings, buffer protocol objects, or converting between binary and text representations in Python.
---

# Manipulating Binary Sequences

## Quick Start

```python
# Three binary sequence types
b = b"hello"                    # bytes: immutable
ba = bytearray(b"hello")        # bytearray: mutable
mv = memoryview(ba)              # memoryview: zero-copy view over a buffer

# Common conversions
bytes([104, 105])                # b'hi'  (from ints 0-255)
bytes("hi", "utf-8")              # b'hi' (from str, encoding required)
"hi".encode("utf-8")              # b'hi' (preferred str->bytes)
b"hi".decode("utf-8")             # 'hi' (preferred bytes->str)
bytearray(5)                      # bytearray(b'\x00\x00\x00\x00\x00')
```

## Workflow

Progress:
- [ ] Identify which type is needed: immutable data (`bytes`), mutable buffer (`bytearray`), or zero-copy view (`memoryview`)
- [ ] Construct from the right source (int, iterable of ints, str+encoding, or existing buffer)
- [ ] Perform required operations (slicing, concatenation, searching, formatting)
- [ ] Convert back to str/list if needed, being explicit about encoding
- [ ] Use `memoryview` when avoiding copies matters (large buffers, C extensions, file/socket I/O)

### Choosing a type

- **`bytes`**: fixed binary data, dictionary keys, hashable payloads, protocol constants.
- **`bytearray`**: building up binary data incrementally (e.g., parsing, buffering socket reads).
- **`memoryview`**: slicing/reading large buffers without copying; interop with `array`, `numpy`, C buffer protocol.

### Construction

```python
bytes(10)                 # 10 zero bytes
bytes(range(65, 70))      # b'ABCDE'
bytearray(b"abc")         # mutable copy
bytes.fromhex("48656c6c6f")   # b'Hello'
b"Hello".hex()                 # '48656c6c6f'
```

### Mutating bytearray

```python
ba = bytearray(b"hello")
ba[0] = ord('H')           # bytearray(b'Hello')
ba.extend(b" world")
ba += b"!"
del ba[0]
```

### memoryview essentials

```python
data = bytearray(b"0123456789")
mv = memoryview(data)
mv[2:5]                    # <memory> slice, no copy
bytes(mv[2:5])              # b'234' materialize when needed
mv[0:3] = b"abc"            # write-through to underlying buffer
mv.tobytes()
mv.cast('I')                 # reinterpret format (e.g., as unsigned ints)
```

### Common operations (shared by bytes/bytearray)

```python
b"hello world".split(b" ")        # [b'hello', b'world']
b"hello".startswith(b"he")        # True
b"a,b,c".split(b",")
b"%s is %d" % (b"x", 5)            # printf-style formatting (bytes % since 3.5)
b" hi ".strip()
b"abc".find(b"b")                   # 1
b"".join([b"a", b"b"])              # b'ab'
```

## Examples

**Example 1:**
Input: Convert a list of integers `[72, 101, 108, 108, 111]` to a bytes object and back.
Output:
```python
data = bytes([72, 101, 108, 108, 111])   # b'Hello'
list(data)                                # [72, 101, 108, 108, 111]
data.decode("ascii")                      # 'Hello'
```

**Example 2:**
Input: Read a large file in chunks and process without copying.
Output:
```python
with open("big.bin", "rb") as f:
    buf = bytearray(f.read())
mv = memoryview(buf)
chunk = mv[1024:2048]        # no copy, view into buf
process(chunk)                 # functions accepting buffer protocol work directly
```

**Example 3:**
Input: Build a binary message incrementally then freeze it.
Output:
```python
msg = bytearray()
msg += b"\x01"                 # header byte
msg += len(payload).to_bytes(2, "big")
msg += payload
frozen = bytes(msg)             # immutable for sending/hashing
```

## Best Practices

- Always specify encoding explicitly (`"utf-8"`) — never rely on defaults across platforms.
- Use `bytes.fromhex`/`.hex()` for human-readable binary debugging.
- Prefer `int.to_bytes(length, byteorder)` and `int.from_bytes(...)` for fixed-width integer packing instead of manual bit math.
- Use `memoryview` to avoid copies when slicing large binary buffers repeatedly.
- Use `bytearray` as an accumulator instead of repeated `bytes` concatenation (which is O(n²)).
- Compare binary data with `==`/`in`, not by decoding to str first.

## Common Pitfalls

- Don't mix `str` and `bytes` in operations (`b"a" + "b"` raises `TypeError`) — always encode/decode explicitly.
- Don't forget `bytes` is immutable; `+=` on `bytes` creates a new object each time (use `bytearray` for loops).
- Don't assume `memoryview` slices are independent copies — mutating the original buffer affects the view and vice versa.
- Don't call `.decode()` without handling potential `UnicodeDecodeError` on untrusted input.
- Remember `bytes(int)` creates a zero-filled buffer of that length, not a bytes representation of the number — use `.to_bytes()` for that.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-sets
description: Explains and applies Python's set and frozenset types, including construction, operators, methods, and performance characteristics. Use when working with unique collections, membership testing, deduplication, or set algebra (union, intersection, difference, symmetric difference) in Python code.
---

## Quick Start

```python
# Sets: mutable, unordered, unique elements, must be hashable
s = {1, 2, 3}
fs = frozenset([1, 2, 3])   # immutable, hashable variant

# Common operations
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # union -> {1, 2, 3, 4}
a & b   # intersection -> {2, 3}
a - b   # difference -> {1}
a ^ b   # symmetric difference -> {1, 4}

# Membership test — O(1) average
3 in a  # True
```

## Workflow

1. **Choose the right type**
   - `set` — need to add/remove elements later.
   - `frozenset` — need immutability (e.g., as dict key, set element, or for safety).

2. **Construct**
   - Literal: `{1, 2, 3}` (note: `{}` is an empty **dict**, use `set()` for empty set).
   - From iterable: `set(iterable)`, `frozenset(iterable)`.
   - Set comprehension: `{x*2 for x in range(5)}`.

3. **Pick operators vs methods**
   - Operators (`|`, `&`, `-`, `^`) require both operands to be sets.
   - Methods (`union()`, `intersection()`, `difference()`, `symmetric_difference()`) accept any iterable.
   - Use methods when combining a set with a list/generator; use operators between two sets for readability.

4. **Mutating vs non-mutating**
   - Non-mutating: `union`, `intersection`, `difference`, `symmetric_difference`, `copy`.
   - Mutating (set only): `update`, `intersection_update`, `difference_update`, `symmetric_difference_update`, `add`, `remove`, `discard`, `pop`, `clear`.
   - `remove(x)` raises `KeyError` if absent; `discard(x)` does not.

5. **Comparisons**
   - `<=` / `issubset()`, `>=` / `issuperset()`, `<` (proper subset), `>` (proper superset).
   - `isdisjoint()` checks for no common elements without building the intersection.

6. **Verify elements are hashable**
   - Set elements must be hashable (immutable types: `int`, `str`, `tuple` of hashables, `frozenset`). Lists/dicts/sets cannot be elements — use `frozenset` or `tuple` instead.

## Examples

**Example 1: Deduplicate while preserving a fast lookup**
Input:
```python
names = ["alice", "bob", "alice", "carol"]
unique = set(names)
```
Output:
```python
{"alice", "bob", "carol"}   # order not guaranteed
```

**Example 2: Combine a set with a list using a method (operator would fail)**
Input:
```python
a = {1, 2, 3}
b = [3, 4, 5]
a.union(b)
```
Output:
```python
{1, 2, 3, 4, 5}
```
Note: `a | b` raises `TypeError` since `b` is a list, not a set.

**Example 3: Frozenset as a dict key**
Input:
```python
groups = {}
groups[frozenset({1, 2})] = "pair"
```
Output:
```python
{frozenset({1, 2}): 'pair'}
```

**Example 4: Symmetric difference for "changed" detection**
Input:
```python
before = {"a", "b", "c"}
after = {"b", "c", "d"}
before ^ after
```
Output:
```python
{"a", "d"}
```

## Best Practices

- Use `set()` for empty sets — `{}` creates a dict.
- Prefer set/frozenset for membership testing over lists when the collection is large or checked repeatedly.
- Use `frozenset` for hashable, immutable groupings (dict keys, elements of other sets).
- Use `issubset`/`issuperset`/`isdisjoint` instead of manually computing intersections when you only need a boolean.
- When updating in a loop, use in-place methods (`update`, `add`) to avoid creating new set objects repeatedly.
- Use set comprehensions (`{expr for x in iterable}`) instead of `set(map(...))` for clarity.

## Common Pitfalls

- Assuming set order is stable or meaningful — sets are unordered; don't rely on iteration order.
- Using `{}` expecting an empty set — it's an empty dict.
- Putting mutable objects (lists, dicts, other sets) directly into a set — raises `TypeError: unhashable type`.
- Using `remove()` when the element might not exist — prefer `discard()` to avoid `KeyError`, or catch the exception explicitly.
- Applying operators (`|`, `&`, `-`, `^`) between a set and a non-set iterable — use the equivalent method instead.
- Forgetting that set operations return **new** sets unless using the `*_update` in-place variants — assigning the result is required for non-mutating methods.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: working-with-python-dict-frozendict
description: Explains and applies Python's mapping types dict and frozendict, including creation, methods, iteration, view objects, and immutability semantics. Use when writing or reviewing Python code that manipulates dictionaries, needs immutable mapping types, or requires guidance on dict/frozendict APIs and best practices.
---

## Quick Start

```python
# Mutable mapping
d = {"a": 1, "b": 2}
d["c"] = 3
d.update(x=10)

# Immutable mapping (frozendict, added as a builtin in newer Python)
fd = frozendict({"a": 1, "b": 2})
# fd["a"] = 99  # raises TypeError: object does not support item assignment

# Convert between them
d2 = dict(fd)
fd2 = frozendict(d2)
```

## Workflow

Progress:
- [ ] Determine if the mapping needs to be mutable (`dict`) or immutable/hashable (`frozendict`)
- [ ] Choose construction method (literal, `dict()`/`frozendict()` constructor, comprehension, `fromkeys`)
- [ ] Use appropriate access patterns (`[]`, `.get()`, `.setdefault()` for dict only)
- [ ] Iterate via `.keys()`, `.values()`, `.items()` view objects
- [ ] Apply merge/update via `|` and `|=` (dict) or `|` (frozendict, returns new frozendict)
- [ ] Use `frozendict` when a mapping must be a dict key, set member, or passed as an immutable default/config

### 1. Construction

```python
d = dict(a=1, b=2)
d = {k: v for k, v in pairs}
d = dict.fromkeys(["a", "b"], 0)

fd = frozendict(a=1, b=2)
fd = frozendict({"a": 1})
fd = frozendict(zip(keys, values))
```

### 2. Access and mutation

- Both support `d[key]`, `d.get(key, default)`, `key in d`, `len(d)`.
- Only `dict` supports `d[key] = value`, `del d[key]`, `.pop()`, `.popitem()`, `.clear()`, `.update()`, `.setdefault()`.
- `frozendict` raises `TypeError` on any mutation attempt — treat it like `tuple` vs `list`.

### 3. Views and iteration

```python
for k, v in d.items():
    ...
keys_view = d.keys()      # dynamic view, reflects later dict changes
values_view = d.values()
items_view = d.items()    # set-like if values are hashable
```

`frozendict` also exposes `.keys()`, `.values()`, `.items()`, but views are effectively static since the underlying mapping can't change.

### 4. Merging

```python
merged = d1 | d2          # new dict
d1 |= d2                  # in-place update, dict only

merged_fd = fd1 | fd2     # new frozendict, no in-place |= (would require mutation)
```

### 5. Hashability

```python
config = frozendict(timeout=30, retries=3)
cache = {config: "result"}   # valid: frozendict is hashable if all values are hashable
# {d: "result"}               # invalid: dict is unhashable, raises TypeError
```

## Examples

**Example 1:**
Input: Need a default function argument that's a mapping and must avoid the mutable-default-argument bug.
Output:
```python
def process(options: frozendict = frozendict()):
    ...
```
Using `frozendict()` as a default is safe because it can never be mutated, unlike `{}`.

**Example 2:**
Input: Need to use a set of key-value options as a dictionary key for memoization.
Output:
```python
from functools import lru_cache

@lru_cache
def compute(params: frozendict):
    ...

compute(frozendict(x=1, y=2))
```

**Example 3:**
Input: Convert a JSON-decoded dict into an immutable config object.
Output:
```python
import json
raw = json.loads(payload)
config = frozendict(raw)
```

## Best Practices

- Default to `dict` for general-purpose, mutable mappings; reach for `frozendict` only when immutability or hashability is required.
- Use dict/frozendict comprehensions instead of building via loops.
- Prefer `.get()` over `try/except KeyError` for optional lookups with defaults.
- Use `|` for merging in Python 3.9+ instead of `{**d1, **d2}` for readability.
- Nest `frozendict` inside `frozendict` (not `dict`) if you need deep immutability — a `frozendict` containing a `dict` value is still mutable through that inner value.
- Document API boundaries (e.g., public function signatures) with `frozendict` to signal "read-only" intent to callers.

## Common Pitfalls

- Assuming `frozendict` deep-freezes nested structures — it only prevents top-level key/value reassignment.
- Trying to use `frozendict` as a drop-in for `dict` in code that calls mutating methods (`update`, `pop`, etc.) — this raises `TypeError` at runtime, not at type-check time unless annotated.
- Using a plain `dict` as a cache key or set element — raises `TypeError: unhashable type: 'dict'`.
- Forgetting that dict view objects (`.keys()`, `.items()`) are live views over a mutable `dict`; mutating the dict during iteration raises `RuntimeError: dictionary changed size during iteration`.
- Assuming `frozendict | dict` mutates the frozendict — it always returns a new object.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: implementing-context-managers
description: Guides the design and implementation of Python context manager types using __enter__/__exit__ protocols, contextlib utilities, and async variants. Use when writing resource management code, implementing the `with`/`async with` statement support, or reviewing context manager correctness (exception suppression, cleanup guarantees, reentrancy).
---

## Quick Start

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    resource = acquire(name)
    try:
        yield resource
    finally:
        release(resource)

with managed_resource("db") as r:
    use(r)
```

For simple cases, prefer `@contextmanager` over hand-written `__enter__`/`__exit__` classes. Reach for a class-based implementation only when you need state across multiple `with` uses, reentrancy, or subclassing.

## Workflow

Progress:
- [ ] Determine sync vs async (`with` vs `async with`)
- [ ] Choose implementation style: generator-based (`@contextmanager`) vs class-based (`__enter__`/`__exit__`)
- [ ] Implement setup logic in `__enter__` (or before `yield`)
- [ ] Implement teardown logic in `__exit__` (or after `yield`, in `finally`)
- [ ] Decide exception handling: propagate (return falsy) or suppress (return truthy)
- [ ] Handle reentrancy/reusability requirements if any
- [ ] Test normal exit, exceptional exit, and (if relevant) suppressed-exception paths

### Class-based protocol

```python
class Resource:
    def __enter__(self):
        # setup; return value bound to `as` target
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup; return True to suppress exception
        return False
```

- `__exit__` receives `(None, None, None)` on normal exit.
- Returning a truthy value from `__exit__` **suppresses** the exception — do this deliberately, never by accident (e.g., don't let a bare `except:` inside `__exit__` swallow the return value implicitly).
- If cleanup itself raises, that new exception replaces the original unless you explicitly chain/reraise the original.

### Generator-based protocol (`contextlib.contextmanager`)

```python
@contextmanager
def cm():
    setup()
    try:
        yield value
    except SomeError:
        handle_and_suppress()   # swallowing: don't re-raise
    finally:
        teardown()
```

- Code before `yield` = `__enter__`; code after (in `finally`) = `__exit__`.
- To suppress an exception, catch it and **do not re-raise**.
- To propagate, either don't catch it, or catch/log/`raise`.

### Async variant

```python
class AsyncResource:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.disconnect()
        return False
```

Or with `contextlib.asynccontextmanager`:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def acm():
    await setup()
    try:
        yield
    finally:
        await teardown()
```

## Examples

**Example 1:**
Input: Need a context manager that times a code block and prints duration, never suppressing exceptions.
Output:
```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")
```

**Example 2:**
Input: Need a reusable, reentrant lock-like context manager as a class.
Output:
```python
class ReentrantFlag:
    def __init__(self):
        self._depth = 0

    def __enter__(self):
        self._depth += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._depth -= 1
        return False
```

**Example 3:**
Input: Suppress a specific exception type using stdlib instead of custom code.
Output:
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")
```

## Best Practices

- Prefer `contextlib.suppress`, `contextlib.closing`, `contextlib.contextmanager`, and `contextlib.ExitStack` over reinventing them.
- Use `ExitStack` when managing a dynamic/variable number of context managers.
- Always release resources in `finally` (generator style) or unconditionally in `__exit__` (class style) — cleanup must run even if setup partially failed after acquisition.
- Make `__enter__`/`__exit__` (or the generator) side-effect-minimal and fast; put expensive logic in explicit methods called from them if reuse outside `with` is needed.
- Document explicitly whether your context manager suppresses exceptions — this is a common source of silent bugs.
- For one-shot generator-based context managers, note they're **not reentrant** and **not reusable** by default (calling `with cm:` twice on the same generator-based instance raises `RuntimeError`). Use `contextlib.contextmanager`'s single-use semantics knowingly, or implement a class if reuse is required.
- For async code, don't mix `__enter__`/`__aexit__` or sync/async inconsistently — pick one protocol per class.

## Common Pitfalls

- **Accidentally suppressing exceptions**: returning `True` from `__exit__` (or not re-raising in a caught `except` before `yield`) silently swallows errors. Only do this intentionally.
- **Cleanup masking the original exception**: if teardown code itself throws, the original exception is lost. Wrap cleanup in `try/except` and chain (`raise ... from original`) or log if you must swallow secondary errors.
- **Reusing a generator-based context manager instance** across multiple `with` blocks — raises `RuntimeError: generator didn't stop`. Create a fresh instance each time, or use a class for reusable managers.
- **Forgetting `finally`** in generator-based managers — an exception before `yield` skips teardown if not guarded.
- **Not checking `exc_type` before acting** in `__exit__` — always inspect all three args if behavior depends on whether an exception occurred.
- **Blocking calls in `__aenter__`/`__aexit__`** — use `await` for I/O; don't call synchronous blocking code in async context managers.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: writing-generic-type-annotations
description: Applies Python type annotation patterns using generic aliases and union types per PEP 585/604 standards. Use when adding type hints to Python code, choosing between typing module constructs and built-in generics, or reviewing/refactoring type annotations for modern Python (3.9+/3.10+) idioms.
---

# Writing Generic Type Annotations

## Quick Start

```python
# Modern (Python 3.9+): use built-in collection types directly
def process(items: list[int]) -> dict[str, int]:
    ...

# Modern (Python 3.10+): use | for unions instead of typing.Union/Optional
def find(key: str) -> int | None:
    ...

# Avoid legacy forms unless supporting Python < 3.9 / < 3.10
from typing import List, Dict, Union, Optional  # legacy, avoid in new code
```

## Workflow

Progress:
- [ ] Step 1: Determine minimum supported Python version for the codebase
- [ ] Step 2: Choose generic alias style (built-in vs `typing` module) based on version
- [ ] Step 3: Choose union style (`|` vs `typing.Union`/`Optional`) based on version
- [ ] Step 4: Apply consistently across the file/module
- [ ] Step 5: Verify with a type checker (mypy/pyright) since these are compile-time-only checks

**Step 1 — Version check:**
- Python >= 3.9: built-in generics (`list[int]`, `dict[str, int]`, `tuple[int, ...]`, `set[str]`) work at runtime.
- Python >= 3.10: `X | Y` union syntax works at runtime (`isinstance` checks, `int | None`).
- Python < 3.9: must use `typing.List`, `typing.Dict`, etc.
- Python < 3.10 but >= 3.7 with `from __future__ import annotations`: can use both new syntaxes in annotations (they're stored as strings, not evaluated), but not in runtime contexts like `isinstance(x, int | str)`.

**Step 2 — Generic alias mapping:**

| Legacy (`typing`) | Modern (built-in) |
|---|---|
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Tuple[int, str]` | `tuple[int, str]` |
| `Set[int]` | `set[int]` |
| `FrozenSet[int]` | `frozenset[int]` |
| `Type[C]` | `type[C]` |

**Step 3 — Union mapping:**

| Legacy | Modern |
|---|---|
| `Union[int, str]` | `int \| str` |
| `Optional[int]` | `int \| None` |
| `Union[int, str, None]` | `int \| str \| None` |

**Step 4 — Apply consistently.** Don't mix `List[int]` and `dict[str, int]` in the same file — pick one style per codebase, driven by the minimum supported version.

**Step 5 — Verify.** Built-in generics and `|` unions are purely typing-time constructs; run `mypy` or `pyright` to catch mistakes, since Python itself won't validate annotation contents at runtime beyond syntax.

## Examples

**Example 1:**
Input: `def get_user(id: int) -> Optional[User]:` in a Python 3.11 codebase
Output: `def get_user(id: int) -> User | None:`

**Example 2:**
Input: `def merge(a: Dict[str, List[int]], b: Dict[str, List[int]]) -> Dict[str, List[int]]:` targeting Python 3.9+
Output: `def merge(a: dict[str, list[int]], b: dict[str, list[int]]) -> dict[str, list[int]]:`

**Example 3:**
Input: A library must support Python 3.8 as minimum
Output: Keep `from typing import List, Dict, Optional, Union` and legacy syntax throughout; do not introduce `list[int]` or `X | Y` since they'll raise `TypeError` at runtime on 3.8.

**Example 4:**
Input: `isinstance(value, Union[int, float])` — runtime isinstance check
Output: `isinstance(value, (int, float))` — note that `Union`/`|` are not valid as the second argument to `isinstance`; use a tuple instead. `X | Y` unions in `types.UnionType` form (Python 3.10+) *do* work with `isinstance(x, int | float)`, but `typing.Union[...]` never does.

## Best Practices

- Prefer built-in generic aliases (`list`, `dict`, `tuple`, `set`, `type`) over `typing` equivalents when the minimum Python version allows it — they're simpler and require no import.
- Prefer `X | Y` over `Optional[X]`/`Union[X, Y]` on Python 3.10+.
- Use `from __future__ import annotations` to unlock modern syntax in annotations on older interpreters (3.7+), remembering this only affects annotations, not runtime type objects.
- For generic classes you define, subscript with built-ins too, e.g. `class Stack(list[T]): ...`.
- Use `X | Y` for `isinstance`/`issubclass` checks only when targeting 3.10+; otherwise use a tuple `(X, Y)`.
- Keep annotation style consistent within a project; document the chosen minimum version and style in contribution guidelines.

## Common Pitfalls

- Using `list[int]` or `X | Y` at runtime (not just in annotations) on Python < 3.9/3.10 — causes `TypeError`.
- Mixing legacy and modern styles inconsistently within the same module.
- Passing `typing.Union[...]` to `isinstance`/`issubclass` — it's not supported; use a tuple or a 3.10+ `X | Y` union instead.
- Forgetting that `from __future__ import annotations` makes all annotations strings (not evaluated), which can break tools that need real runtime type objects (e.g., some uses of `typing.get_type_hints`, dataclasses relying on runtime introspection without resolution).
- Assuming built-in generics support all `typing` features — some constructs (`Callable`, `TypeVar` bounds, `Protocol`, `Literal`, `TypedDict`) still require importing from `typing`.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: navigating-python-stdtypes
description: Explains and applies Python's built-in type system (numeric, sequence, mapping, set, text, binary types, and other built-in types like modules, classes, functions, and generic alias types) per CPython documentation. Use when writing code that relies on precise built-in type semantics, debugging type-related behavior, or explaining how Python's built-in types work under the hood.
---

## Quick Start

When a question touches Python's built-in type behavior, identify which category it falls into first, then apply the specific semantics for that category:

```python
# Category check example
type([])          # <class 'list'>       -> sequence type (mutable)
type(())          # <class 'tuple'>      -> sequence type (immutable)
type({})          # <class 'dict'>       -> mapping type
type(set())       # <class 'set'>        -> set type (mutable)
type(frozenset()) # <class 'frozenset'>  -> set type (immutable)
type(1).__mro__   # int -> object        -> numeric type
type(lambda:0)    # <class 'function'>   -> "other built-in type"
type(int)         # <class 'type'>       -> "other built-in type" (class)
type(list[int])   # <class 'types.GenericAlias'>  -> generic alias type
```

## Workflow

Progress:
- [ ] Identify the object's category (numeric, sequence, text, binary, set, mapping, or "other")
- [ ] For "other built-in types," determine the specific subtype (module, class, function, method, code, type, generic alias, ellipsis, notimplemented)
- [ ] Recall the defining attributes/protocol for that type (dunder methods, mutability, hashability)
- [ ] Apply or explain the relevant behavior with a minimal code example
- [ ] Note version-specific caveats (e.g., features added/changed in 3.9+, 3.12+)

### Other Built-in Types Reference

These don't fit neatly into numeric/sequence/mapping/set but appear constantly in real code:

- **Modules**: `type(module) -> types.ModuleType`. Attribute access via `__dict__`; `import` creates these.
- **Classes and instances**: Classes are created by `type` or a metaclass; instances via `__call__`. Key dunders: `__init__`, `__new__`, `__class__`.
- **Functions**: `def` and `lambda` produce `types.FunctionType`. Have `__code__`, `__defaults__`, `__closure__`, `__globals__`.
- **Methods**: Bound methods (`types.MethodType`) wrap a function + instance (`__self__`, `__func__`).
- **Code objects**: `func.__code__`, produced by compilation; immutable, introspectable (`co_varnames`, `co_consts`).
- **Type objects**: `type` itself; `isinstance(x, type)` checks if `x` is a class.
- **The `NotImplemented` singleton**: Returned by rich comparison / arithmetic dunders when an operation isn't supported for given operand types — **never test truthiness of `NotImplemented`**, always `return NotImplemented` and let Python retry with reflected method or raise `TypeError`.
- **The `Ellipsis` singleton (`...`)**: Used as a placeholder (type stubs, NumPy slicing, unimplemented function bodies).
- **`types.GenericAlias`**: Produced by subscripting builtin containers (`list[int]`, `dict[str, int]`) — supports `__origin__` and `__args__`, used heavily for typing since PEP 585.

## Examples

**Example 1:**
Input: "Why does `list.__eq__(other)` sometimes return `NotImplemented` instead of `False`?"
Output:
```python
class Point:
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented  # let Python try other.__eq__(self)
        return self.x == other.x and self.y == other.y
```
`NotImplemented` signals "I don't know how to compare with this type" — distinct from `False`, which asserts inequality. Returning `False` outright breaks symmetric comparison with subclasses/other types; Python falls back to `other.__eq__(self)` or identity-based default only when `NotImplemented` is returned.

**Example 2:**
Input: "What's the type of `dict[str, int]` and why does it matter?"
Output: `type(dict[str, int])` is `types.GenericAlias`. It matters because `dict[str, int]` is not itself a class you can subclass reliably pre-3.9 semantics without `__class_getitem__`, but it *does* support `isinstance`-adjacent introspection via `__origin__` (`dict`) and `__args__` (`(str, int)`) — used by type checkers and `typing.get_origin()`/`get_args()`.

**Example 3:**
Input: "How do I introspect a function's default arguments and closure variables?"
Output:
```python
def make_adder(n):
    def adder(x, y=1):
        return x + y + n
    return adder

f = make_adder(10)
f.__defaults__      # (1,)
f.__closure__       # (<cell: contents=10>,)
f.__code__.co_varnames  # ('x', 'y')
```

## Best Practices

- Distinguish **mutable vs immutable** built-ins early — it drives hashability (`tuple` hashable if elements are; `list` never) and safe use as dict keys/set members.
- When comparing against `NotImplemented`, use `is`, never `==` or truthiness (`if result is NotImplemented`).
- Prefer `types.GenericAlias` introspection (`get_origin`, `get_args` from `typing`) over manually parsing `__args__`/`__origin__` for forward compatibility.
- For module/class/function introspection, prefer the `inspect` module over raw dunder access when writing production tooling — it handles edge cases (bound vs unbound, wrapped functions via `functools.wraps`).
- Check the Python version when relying on newer built-in type features (e.g., PEP 585 generic alias subscripting requires 3.9+; some `types` module additions are version-gated).

## Common Pitfalls

- Treating `NotImplemented` as a boolean sentinel (`if not result:`) — it's truthy and this is a common source of silent bugs.
- Assuming `type(x) == int` instead of `isinstance(x, int)` — breaks with `bool` (subclass of `int`) and other subclassing scenarios.
- Confusing `Ellipsis` (`...`, a real singleton object) with "not yet implemented" — it's valid runtime data, not just a stub marker.
- Forgetting that bound methods (`instance.method`) create a **new** `MethodType` object on each attribute access — `instance.method is instance.method` is `False`.
- Mutating `__defaults__` or assuming default arguments are re-evaluated per call — they're evaluated once at function definition time (the classic mutable-default-argument trap).
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: introspecting-python-objects
description: Explains and utilizes Python's special attributes (__dict__, __class__, __name__, __qualname__, __mro__, etc.) to inspect and reason about objects, classes, modules, and functions. Use when investigating an object's type hierarchy, module origin, defined attributes, or when writing introspection/reflection code, debugging tools, or serialization logic that depends on special attributes.
---

## Quick Start

```python
class Animal:
    """Base class for animals."""
    pass

class Dog(Animal):
    """A dog."""
    pass

d = Dog()

d.__class__          # <class '__main__.Dog'>
d.__dict__           # {} (instance attribute dict)
Dog.__name__         # 'Dog'
Dog.__qualname__     # 'Dog'
Dog.__mro__          # (Dog, Animal, object)
Dog.__bases__        # (Animal,)
Dog.__doc__          # 'A dog.'
Dog.__module__       # '__main__'
```

## Workflow

Progress:
- [ ] Identify what kind of introspection is needed (identity, hierarchy, namespace, or metadata)
- [ ] Pick the correct special attribute(s) for that object type
- [ ] Handle attributes that may not exist (use `getattr` with defaults or `hasattr`)
- [ ] Distinguish instance-level vs class-level attribute access
- [ ] Validate results against edge cases (built-ins, slots, dynamic classes)

**Step 1: Identify the introspection goal**

| Goal | Attribute(s) |
|---|---|
| Get the class of an instance | `obj.__class__` |
| Get a class/function/module's bare name | `__name__` |
| Get the dotted path to where it was defined | `__qualname__` |
| Get inheritance chain (method resolution order) | `__mro__` (classes only, not instances) |
| Get direct parent classes | `__bases__` |
| Get instance/class namespace dict | `__dict__` |
| Get docstring | `__doc__` |
| Get defining module's name | `__module__` |
| Get allowed instance attribute names (memory-optimized classes) | `__slots__` |

**Step 2: Choose instance vs. class access**

- `type(obj).__mro__` works; `obj.__mro__` does not (MRO is a class-only attribute).
- `obj.__dict__` gives per-instance attributes; `type(obj).__dict__` gives the class namespace (a `mappingproxy`, read-only).
- Objects using `__slots__` have no `__dict__` unless `__dict__` is explicitly included in slots.

**Step 3: Guard against missing attributes**

Not all objects define every special attribute (e.g., built-in types, `__slots__` classes lack `__dict__`; lambdas have `__qualname__` like `<locals>.<lambda>`). Always prefer `getattr(obj, '__dict__', None)` or `hasattr` in generic tooling.

## Examples

**Example 1: Inspecting instance vs class dict**
Input:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
```
Output:
```python
p.__dict__          # {'x': 1, 'y': 2}
Point.__dict__       # mappingproxy({'__init__': <function...>, '__dict__': <attribute...>, '__weakref__': <attribute...>, '__doc__': None})
```

**Example 2: Walking the MRO for a diamond hierarchy**
Input:
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

D.__mro__
```
Output:
```python
(<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

**Example 3: Qualname vs name for nested definitions**
Input:
```python
class Outer:
    class Inner:
        def method(self): pass

Outer.Inner.method.__name__
Outer.Inner.method.__qualname__
```
Output:
```python
'method'
'Outer.Inner.method'
```

**Example 4: Slots preventing __dict__**
Input:
```python
class Slotted:
    __slots__ = ('x',)

s = Slotted()
s.x = 5
s.__dict__
```
Output:
```python
AttributeError: 'Slotted' object has no attribute '__dict__'
```

## Best Practices

- Use `type(obj)` rather than `obj.__class__` when correctness matters, since `__class__` can be overridden (e.g., proxy objects) — but `__class__` is fine for typical introspection/debugging.
- Use `__qualname__` over `__name__` in logs/tracebacks when nested classes or closures are involved — it disambiguates identically named functions/classes.
- For serialization or debugging tools, iterate `vars(obj)` (equivalent to `obj.__dict__`) rather than accessing `__dict__` directly — `vars()` raises a clearer `TypeError` when unsupported.
- When building generic MRO/hierarchy tools, call `.__mro__` on the *type*, not the instance: `type(obj).__mro__`.
- Check `__module__` alongside `__qualname__` to fully disambiguate identically named classes from different modules.

## Common Pitfalls

- Calling `obj.__mro__` directly on an instance — it's only defined on classes (via `type`). Use `type(obj).__mro__`.
- Assuming every object has `__dict__` — built-ins (`int`, `str`) and `__slots__`-based classes often don't.
- Mutating `type(obj).__dict__` directly — it's a read-only `mappingproxy`; use `setattr(cls, name, value)` instead.
- Confusing `__name__` with `__qualname__` for nested or locally-defined functions/classes, leading to ambiguous logs.
- Relying on `__module__` for dynamically created classes (e.g., via `type()` in a factory) — it may default to the factory's module, not the intended logical one.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```markdown
---
name: managing-integer-string-conversion-limits
description: Explains and resolves Python's integer-string conversion length limitation (int/str conversion digit cap introduced for DoS protection). Use when encountering ValueError about "Exceeds the limit for integer string conversion", converting very large integers to/from strings, or configuring sys.set_int_max_str_digits.
---

## Quick Start

If you hit this error:

```
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5000 digits
```

Fix it by raising or disabling the limit before the conversion happens:

```python
import sys
sys.set_int_max_str_digits(20000)   # raise limit
# or
sys.set_int_max_str_digits(0)       # disable limit entirely (0 = no limit)

print(str(10**10000))  # now works
```

## Background

Python limits `int` <-> `str` conversions to prevent quadratic-time DoS attacks when converting huge integers (conversion is O(n²) in digit count). This applies to:

- `str(int)`, `repr(int)`, `f"{n}"`, `"%d" % n`
- `int(str)`, `int(s, base=10)`
- Any implicit conversion going through these paths

Default limit: **4300 digits** (roughly a number with ~14000 bits). This is intentionally set above what most legitimate programs need but low enough to block abuse.

**Not affected:** non-decimal bases (`hex()`, `oct()`, `bin()`, `int(s, 16)`, etc.) — the limit only applies to base-10 conversions since those are the ones with quadratic blowup risk.

## Workflow

Progress:
- [ ] Identify whether the error comes from legitimate large-number use or a bug producing runaway integers
- [ ] Decide: raise the limit, disable it, or fix the underlying issue
- [ ] Apply the fix at the right scope (interpreter, module, or command line)
- [ ] Verify no security regression if disabling in a public-facing service

### Option 1: Command line
```
python -X int_max_str_digits=0 script.py
```

### Option 2: Environment variable
```
PYTHONINTMAXSTRDIGITS=0 python script.py
```

### Option 3: Programmatic (must run before any large conversion)
```python
import sys
sys.set_int_max_str_digits(0)  # or specific integer >= 640
```

### Check current limit
```python
sys.get_int_max_str_digits()
```

Setting must be `0` (no limit) or an integer `>= 640`. Lower values raise `ValueError`.

## Examples

**Example 1 — legitimate math (factorials, big computations):**
Input:
```python
import math
str(math.factorial(3000))
```
Output: Raises `ValueError` (factorial(3000) has >4300 digits). Fix:
```python
import sys, math
sys.set_int_max_str_digits(0)
str(math.factorial(3000))  # works
```

**Example 2 — parsing untrusted input (should keep the limit):**
Input:
```python
int(user_supplied_string)  # user_supplied_string is 1,000,000 chars of digits
```
Output: Raises `ValueError` by default — this is the *intended* protection. Do not disable the limit here; instead validate/reject oversized input before parsing.

**Example 3 — library needs a higher limit only temporarily:**
```python
import sys
old = sys.get_int_max_str_digits()
sys.set_int_max_str_digits(0)
try:
    result = str(big_int)
finally:
    sys.set_int_max_str_digits(old)
```

## Best Practices

- Set the limit as early as possible (top of `main`, or via `-X`/env var) — changing it mid-conversion doesn't help retroactively.
- Prefer the command-line/env-var approach for whole-program policy; use `sys.set_int_max_str_digits()` for library-level, scoped adjustments.
- If writing a library that legitimately needs big-int string conversion, don't silently call `set_int_max_str_digits(0)` globally — this weakens protection for the whole process, including unrelated code. Save/restore the previous value.
- For services parsing untrusted input, **keep the default limit** (or set something explicit and low) — the whole point is DoS protection against attacker-supplied huge numeric strings.
- Non-decimal conversions (`hex`, `bin`, `oct`) are unaffected — use them if you don't actually need decimal representation.

## Common Pitfalls

- Setting the limit *after* the conversion call already executed (order matters — it's a global interpreter setting checked at call time).
- Disabling the limit globally in server/web code that parses user-provided numeric strings — reintroduces the DoS vector this feature exists to prevent.
- Assuming the limit affects `int(s, 16)` or similar — it only applies to base-10 conversions.
- Forgetting that `f"{n}"` and `%`-formatting also go through the same limited conversion path, not just `str()`/`int()`.
```