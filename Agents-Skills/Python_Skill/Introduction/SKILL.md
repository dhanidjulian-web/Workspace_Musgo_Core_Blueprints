---
name: navigating-python-stdlib-docs
description: Guides retrieval and interpretation of Python standard library documentation, including module conventions, availability notes, and platform-specific caveats. Use when looking up standard library modules, explaining what a module does, checking version/platform availability, or writing code that depends on stdlib behavior described in the official docs.
---

## Quick Start

When asked about a Python standard library module, follow this lookup pattern:

```
1. Identify module name (e.g., `os`, `asyncio`, `re`)
2. Check docs.python.org/3/library/<module>.html
3. Note: "Availability" boxes, "Deprecated since", "Changed in version" markers
4. Summarize: purpose, key functions/classes, platform caveats
```

Example query: "What does `os.path` do and is it cross-platform?"
Answer: `os.path` manipulates pathnames; behavior depends on OS (splits into `posixpath`/`ntpath` under the hood). Always check the **Availability** note if present.

## Workflow

Progress:
- [ ] Identify the exact module/function being asked about
- [ ] Locate the relevant doc conventions (see below)
- [ ] Check version compatibility markers
- [ ] Check platform-specific availability notes
- [ ] Note deprecation status
- [ ] Extract minimal working example if present
- [ ] Summarize in plain language with a code snippet

### Documentation Conventions to Recognize

The Python stdlib docs use standardized markers — always surface these to the user:

- **Availability: Unix** / **Availability: Windows** — feature only works on that platform
- **Changed in version X.Y** — behavior changed; flag if user's Python version predates this
- **Deprecated since version X.Y** — recommend the replacement instead
- **New in version X.Y** — don't suggest for code targeting older Python
- **Source code** links — point to CPython Lib/ source for implementation detail
- Module synopsis line at the top of each page — use as the one-line summary

### Structure of a Typical Module Page

1. Synopsis (one-line description, right after title)
2. Deprecation/availability banner (if applicable)
3. Overview / description
4. Classes / functions / constants, alphabetically or logically grouped
5. Examples section (not all modules have one)
6. "See also" cross-references to related modules

## Examples

**Example 1:**
Input: "Is `os.fork()` available on Windows?"
Output: "No. `os.fork()` has an **Availability: Unix** note in the docs — it raises `OSError` on Windows. Use `multiprocessing` for a cross-platform alternative."

**Example 2:**
Input: "What's the difference between `asyncio.get_event_loop()` behavior in 3.16 vs older versions?"
Output: "Check the 'Changed in version' and 'Deprecated since' annotations on that function's doc entry — `get_event_loop()` has had deprecation warnings evolve across 3.10–3.12 for creating loops implicitly. Always quote the exact version note rather than assuming behavior is unchanged."

**Example 3:**
Input: "Summarize the `pathlib` module."
Output: "`pathlib` — Object-oriented filesystem paths. Synopsis: 'Object-oriented filesystem paths.' Provides `Path` (and `PurePath`) classes representing filesystem paths with methods like `.exists()`, `.glob()`, `.read_text()`. Cross-platform: `PosixPath`/`WindowsPath` subclasses chosen automatically via `Path()`. Preferred over `os.path` in modern code."

## Best Practices

- Always quote the **synopsis line** verbatim when introducing a module — it's the canonical one-sentence description.
- Surface availability/version caveats proactively, don't wait to be asked.
- When multiple modules solve the same problem (e.g., `os.path` vs `pathlib`, `urllib` vs `requests`), state the docs' recommended modern choice.
- Link conceptually to "See also" sections to help users find adjacent tools.
- For version-numbered docs (e.g., "3.16"), treat it as the target reference — don't silently assume the user's runtime matches; ask or infer from context if a mismatch could matter.

## Common Pitfalls

- Don't state a module is deprecated without checking — verify against the "Deprecated since" marker, not memory.
- Don't ignore platform-specific **Availability** notes when giving code examples that must run cross-platform.
- Don't confuse *module deprecation* with *function/parameter deprecation* — they're marked separately.
- Don't assume behavior is identical across Python versions when a "Changed in version" note exists between the user's version and the doc version.
- Don't fabricate function signatures — if uncertain, say so rather than guessing parameter names.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```markdown
---
name: checking-platform-availability
description: Determines and documents platform availability constraints for Python standard library modules and features, following the conventions used in CPython documentation. Use when writing or reviewing "Availability" notes for docs, deciding whether code relying on platform-specific APIs is portable, or auditing modules for Unix/Windows/macOS/mobile/WASI/free-threading support.
---

## Quick Start

When documenting or evaluating a module/function that depends on OS or build-specific features, produce an availability note in this form:

```
Availability: Unix, Windows.
```

or with detail:

```
Availability: Unix, not Emscripten, not WASI.

This function is not available on Emscripten or WASI, see
:ref:`wasm-availability` for more information.
```

Rule of thumb: state the **positive** set of supported platforms first; if exceptions exist within a broad platform (e.g. "Unix but not this specific flavor"), add explicit `not X` clauses.

## Workflow

Progress:
- [ ] Identify what platform-gated behavior is involved (syscall, header, library, hardware, build option)
- [ ] Classify against the standard availability categories (see below)
- [ ] Check for known exceptions within a category (specific Unix variants, mobile restrictions, WASI/Emscripten sandboxing)
- [ ] Check build-time gating (e.g., free-threaded builds, optional modules)
- [ ] Write the note using standard phrasing
- [ ] Add a explanatory sentence + cross-reference if the restriction is non-obvious
- [ ] Verify against CPython source (`Doc/library/`, `configure.ac`, `#ifdef` guards) if precision matters

### Standard availability categories

- **Unix** — general POSIX-like systems. If only some Unixes support it, name them or say "most Unix systems, see specific platform note."
- **Windows**
- **macOS** — sometimes distinct from generic Unix due to Darwin-specific behavior.
- **Linux** — used when a feature is genuinely Linux-only (e.g. `/proc`, epoll, `sendfile` flags).
- **Emscripten**, **WASI** — WebAssembly targets; frequently *excluded* rather than included, since these sandboxes lack process/thread/networking primitives. Reference `wasm-availability` for details.
- **iOS**, **Android** — mobile platforms; often excluded from filesystem, subprocess, or multiprocessing features due to OS sandboxing.
- **GNU/kFreeBSD**, **NetBSD**, etc. — named explicitly only when behavior diverges from generic Unix.
- **free-threaded build** — call out when a feature behaves differently or is unavailable under `Py-GIL-disabled` builds.

### Phrasing template

```
Availability: <supported list>[, not <excluded list>].

<Optional: one-sentence reason>, see :ref:`<cross-ref>` for more information.
```

## Examples

**Example 1:**
Input: `os.fork()` behavior note needed.
Output:
```
Availability: Unix, not Emscripten, not WASI, not iOS.

See :ref:`wasm-availability` for more information on WASM platforms.
```

**Example 2:**
Input: `winreg` module.
Output:
```
Availability: Windows.
```

**Example 3:**
Input: `socket.SO_REUSEPORT` constant.
Output:
```
Availability: Unix. Not available on all Unix platforms; check with
``hasattr(socket, "SO_REUSEPORT")``.
```

**Example 4:**
Input: A feature that works everywhere except under free-threaded builds where it silently degrades.
Output:
```
Availability: all platforms.

On the free-threaded build, this function acquires an internal lock,
which may affect performance under high contention.
```

## Best Practices

- Prefer the exact platform names used in CPython docs (`Unix`, `Windows`, `macOS`, `Linux`, `Emscripten`, `WASI`, `iOS`, `Android`) rather than inventing new labels.
- Always check `hasattr`/`sys.platform` guidance if runtime detection is more reliable than static docs (many POSIX features vary by libc).
- When multiple exclusions exist, list them together after the main clause, each prefixed with `not`.
- Link to `wasm-availability` whenever Emscripten/WASI are excluded — don't just state the exclusion without explanation, since sandboxing reasons aren't obvious to readers.
- For mobile (iOS/Android), note *why* — usually sandboxing, lack of subprocess spawning, or restricted filesystem access.
- Distinguish "not implemented" from "not applicable": some features are meaningless on a platform (e.g., `os.setuid` on Windows) rather than merely unported.
- When auditing existing code for portability, search for `#ifdef` guards and `sys.platform ==` checks as ground truth, not just docstrings.

## Common Pitfalls

- Don't write "Availability: most platforms" without enumerating exceptions — always be explicit.
- Don't conflate "Unix" with "Linux" — a feature using `/proc` or `epoll` is Linux-specific, not general Unix.
- Don't omit WASI/Emscripten exclusions for anything touching threads, processes, sockets, or file locking — these are almost always unsupported there.
- Don't assume macOS behaves like generic Unix for filesystem case-sensitivity, sandboxing, or fork safety — call it out separately when relevant.
- Don't forget free-threaded build caveats for modules dealing with the GIL, C extension state, or module-level singletons.
- Don't state availability without verifying against current source; availability changes across versions (e.g., features later ported to Windows or gaining WASI support).
```