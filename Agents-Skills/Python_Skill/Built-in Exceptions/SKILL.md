---
name: handling-python-exceptions
description: Provides guidance on Python's built-in exception hierarchy, when to use each exception type, and best practices for raising and handling exceptions. Use when writing error handling code, choosing appropriate exception types, creating custom exceptions, or debugging exception-related issues in Python.
---

## Quick Start

```python
# Raise the most specific built-in exception that fits
def get_item(items, index):
    if not isinstance(index, int):
        raise TypeError(f"index must be int, got {type(index).__name__}")
    if index < 0 or index >= len(items):
        raise IndexError(f"index {index} out of range for length {len(items)}")
    return items[index]

# Catch specific exceptions, not bare except
try:
    value = get_item(my_list, user_input)
except (TypeError, IndexError) as e:
    logger.error(f"Invalid access: {e}")
    raise
```

## Workflow

Progress:
- [ ] Identify what error condition needs signaling
- [ ] Check if a built-in exception fits exactly
- [ ] If not, create a custom exception subclassing the closest built-in or `Exception`
- [ ] Raise with a clear, actionable message
- [ ] Catch at the appropriate level of specificity
- [ ] Use `finally`/context managers for cleanup, not exception handling for control flow

### Step 1: Choose the right built-in exception

Core hierarchy (all inherit from `BaseException`):

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration / StopAsyncIteration
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── FileExistsError
      │    ├── PermissionError
      │    ├── TimeoutError
      │    ├── InterruptedError
      │    ├── IsADirectoryError / NotADirectoryError
      │    └── ConnectionError (BrokenPipe/ConnectionReset/Refused/Aborted)
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── RecursionError
      │    └── PythonFinalizationError
      ├── SyntaxError
      │    └── IndentationError → TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError (UnicodeDecodeError/EncodeError/TranslateError)
      └── Warning (DeprecationWarning, UserWarning, etc.)
```

**Selection guide:**
- Wrong type passed → `TypeError`
- Right type, invalid value → `ValueError`
- Missing key/index → `KeyError` / `IndexError`
- Missing attribute/name → `AttributeError` / `NameError`
- Abstract method not implemented → `NotImplementedError`
- Invalid state/logic error not covered elsewhere → `RuntimeError`
- File/OS-level failure → appropriate `OSError` subclass

### Step 2: Only catch `Exception`, never `BaseException`

`BaseException` includes `SystemExit` and `KeyboardInterrupt` — catching it breaks Ctrl-C and `sys.exit()`. Bare `except:` is equivalent to `except BaseException:` — avoid it.

### Step 3: Use exception chaining for context

```python
try:
    parse_config(path)
except FileNotFoundError as e:
    raise ConfigError(f"Cannot load config from {path}") from e

# Suppress chaining when the original is irrelevant noise
raise ConfigError("bad config") from None
```

### Step 4: Custom exceptions — subclass meaningfully

```python
class AppError(Exception):
    """Base class for this application's exceptions."""

class ValidationError(AppError, ValueError):
    """Raised when input fails validation. Also catchable as ValueError."""
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")
```

Define one base exception per package/library so callers can catch broadly (`except AppError`) or narrowly.

### Step 5: Use exception groups for multiple concurrent errors (3.11+)

```python
try:
    results = run_concurrent_tasks()
except* ValueError as eg:
    for err in eg.exceptions:
        log_validation_error(err)
except* ConnectionError as eg:
    for err in eg.exceptions:
        log_network_error(err)
```

Raise multiple related errors together with `ExceptionGroup("summary", [err1, err2])`.

## Examples

**Example 1:**
Input: Function receives a negative value where only non-negative is valid.
Output:
```python
def set_quantity(n):
    if not isinstance(n, int):
        raise TypeError(f"quantity must be int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"quantity must be non-negative, got {n}")
```

**Example 2:**
Input: Catching a file read error and re-raising with context.
Output:
```python
try:
    with open(path) as f:
        data = f.read()
except FileNotFoundError as e:
    raise RuntimeError(f"Required file missing: {path}") from e
```

**Example 3:**
Input: Abstract base class method that subclasses must implement.
Output:
```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
```

## Best Practices

- Raise the most specific exception available; only fall back to `Exception`/`RuntimeError` when nothing else fits.
- Always include a descriptive message with relevant values (`f"expected X, got {actual}"`).
- Use `except SpecificError:` blocks in order from most to least specific.
- Prefer `try`/`except`/`else`/`finally` fully: `else` for code that only runs on success, `finally` for cleanup.
- Use context managers (`with`) instead of manual `try/finally` for resource cleanup.
- Chain exceptions with `from` to preserve the original traceback/cause.
- Check `e.args`, `str(e)`, and exception attributes for structured error data rather than parsing message strings.
- Use `warnings.warn()` with the `Warning` hierarchy for deprecations, not exceptions.

## Common Pitfalls

- **Bare `except:`** — catches `SystemExit`/`KeyboardInterrupt`, hides bugs. Use `except Exception:` minimum.
- **Catching too broadly then swallowing errors** — `except Exception: pass` hides real bugs; at least log them.
- **Using exceptions for normal control flow** — e.g., using `KeyError` catch instead of `dict.get()` for expected-missing keys.
- **Re-raising with `raise e`** — destroys the original traceback; use bare `raise` inside an `except` block to preserve it.
- **Mutable default state in custom exception `__init__`** — avoid mutable defaults as args.
- **Forgetting `ModuleNotFoundError` is a subclass of `ImportError`** — catching `ImportError` also catches missing-module errors; be specific if you need to distinguish.
- **Overusing custom exceptions** — don't create a new exception class when a built-in with a good message suffices.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-exception-context
description: Explains and applies Python's exception chaining and context mechanisms (__context__, __cause__, raise...from, and __suppress_context__). Use when writing exception handlers, re-raising errors, translating exceptions, or debugging confusing traceback chains involving "During handling of the above exception, another exception occurred."
---

## Quick Start

```python
# Implicit chaining (__context__): happens automatically when an exception
# is raised inside an except/finally/with block.
try:
    1 / 0
except ZeroDivisionError:
    raise RuntimeError("computation failed")
# Traceback shows both exceptions, joined by:
# "During handling of the above exception, another exception occurred."

# Explicit chaining (__cause__): use `raise ... from ...` to state the cause
# deliberately, e.g. when translating a low-level error into a domain error.
try:
    connect()
except ConnectionError as e:
    raise ServiceUnavailable("cannot reach backend") from e
# Traceback says: "The above exception was the direct cause of the
# following exception."

# Suppress chaining entirely with `from None`.
try:
    parse(data)
except ValueError:
    raise ValueError("bad input") from None
```

## Workflow

Progress checklist for reasoning about or writing chained-exception code:

- [ ] Identify whether the new exception is raised *while handling* another (implicit context) or is *caused by* another (explicit cause you want documented)
- [ ] Decide if the original exception is genuinely relevant to the caller — if not, suppress it
- [ ] Choose the right mechanism: implicit (`__context__`), explicit (`raise X from Y`, sets `__cause__` and implies `__suppress_context__ = True`), or suppressed (`raise X from None`)
- [ ] Verify traceback output matches intent (correct linking message, or no extra context)
- [ ] For libraries: prefer explicit `from e` when translating exceptions across abstraction boundaries so users can inspect the root cause via `e.__cause__`

## Key Concepts

- **`__context__`**: Set automatically whenever an exception is raised inside the handling of another exception (`except`, `except*`, `finally`, or `with` block). Represents "this happened while dealing with that."
- **`__cause__`**: Set only via `raise NewExc from original_exc`. Represents an explicit, intentional causal link. Setting `__cause__` also sets `__suppress_context__ = True` so the implicit context isn't printed redundantly.
- **`__suppress_context__`**: When `True`, the traceback printer skips showing `__context__`. Set implicitly by `raise ... from ...`, or explicitly by `raise ... from None`.
- **Traceback messages**:
  - Implicit: `"During handling of the above exception, another exception occurred:"`
  - Explicit cause: `"The above exception was the direct cause of the following exception:"`
- **`from None`**: Fully suppresses display of the previous exception (sets `__cause__ = None` and `__suppress_context__ = True`).
- All three attributes are inspectable on exception instances at runtime, not just in tracebacks (`err.__cause__`, `err.__context__`, `err.__suppress_context__`).

## Examples

**Example 1 — Implicit context (accidental double failure):**
Input:
```python
try:
    open("missing.txt")
except FileNotFoundError:
    log.write("error")  # log is undefined -> NameError
```
Output: Traceback shows `FileNotFoundError` first, then `"During handling of the above exception, another exception occurred:"`, then `NameError`. Both are genuinely useful for debugging, so leave as-is.

**Example 2 — Explicit cause (intentional translation):**
Input:
```python
try:
    json.loads(payload)
except json.JSONDecodeError as e:
    raise ConfigError("invalid config file") from e
```
Output: Traceback shows the original `JSONDecodeError`, then `"The above exception was the direct cause of the following exception:"`, then `ConfigError`. `config_error.__cause__` is the `JSONDecodeError` instance.

**Example 3 — Suppressed context (irrelevant internal detail):**
Input:
```python
try:
    cache[key]
except KeyError:
    raise LookupError(f"{key} not found") from None
```
Output: Traceback shows only `LookupError`; the internal `KeyError` is hidden because it's an implementation detail irrelevant to the caller.

## Best Practices

- Use `from e` in library/API boundary code so callers can programmatically inspect `err.__cause__` for root-causing.
- Use `from None` when the intermediate exception is purely an implementation detail (e.g., dict lookups, internal parsing) that would confuse end users.
- Don't silently swallow context you might need later — prefer suppressing display (`from None`) over losing information (e.g., logging the original before raising).
- When re-raising the *same* exception type for retry logic, plain `raise` (no argument) preserves the original traceback without adding a new context frame.

## Common Pitfalls

- Don't assume `except Exception: raise NewError()` loses the original — it's still attached via `__context__` and will print unless suppressed.
- Don't use `from None` reflexively; it destroys debugging information for legitimate infrastructure/logic errors.
- Don't confuse `__cause__` (explicit, from `raise...from`) with `__context__` (implicit, automatic) — only one drives the "direct cause" message, the other drives "during handling."
- Remember `raise X from Y` sets `__suppress_context__ = True` automatically — the implicit context still exists on the object but won't print in the default traceback.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: inheriting-builtin-exceptions
description: Guides safe subclassing of built-in Python exceptions like OSError, ImportError, StopIteration, and others whose __new__ or __init__ override instance attributes. Use when creating custom exception hierarchies, subclassing built-in exceptions, or debugging cases where custom exception attributes mysteriously disappear or get overwritten.
---

## Quick Start

Some built-in exceptions (notably `OSError` subclasses) use `__new__` to select a subclass based on `errno`, and override `__init__`/`__new__` to set attributes like `errno`, `strerror`, `filename`. If you subclass these and add your own attributes without careful handling, they can be silently dropped or overwritten.

```python
class MyError(OSError):
    def __init__(self, message, foo):
        super().__init__(message)
        self.foo = foo

    def __str__(self):
        return f"{super().__str__()} (foo={self.foo!r})"

try:
    raise MyError("bad thing", foo=42)
except MyError as e:
    print(e.foo)  # 42
    print(str(e))  # bad thing (foo=42)
```

## Workflow

Progress:
- [ ] Step 1: Identify if the base exception has custom `__new__` (e.g., `OSError` picks subclasses like `FileNotFoundError` based on `errno`).
- [ ] Step 2: Check whether base `__init__`/`__new__` accepts and stores extra positional args — subclass args beyond what the base expects are stored in `args` but not as separate attributes.
- [ ] Step 3: Always call `super().__init__(...)` explicitly with the args the base class expects, then set additional custom attributes afterward in your own `__init__`.
- [ ] Step 4: If overriding `__new__` (rare, only needed for immutable-like customization), pass through `*args, **kwargs` to `super().__new__` and avoid overwriting base attributes.
- [ ] Step 5: Override `__str__`/`__repr__` if you want custom attributes reflected in the printed message — the base `__str__` won't know about them.
- [ ] Step 6: Test pickling/copying if relevant — exceptions with custom `__init__` signatures may fail to unpickle unless `__reduce__` is implemented, since default pickling replays `args` through `__init__` or `__new__`.

## Examples

**Example 1: Adding an attribute to OSError subclass**
Input:
```python
class ValidationError(OSError):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field
```
Output: `ValidationError("bad", field="x").field == "x"`; `str(exc) == "bad"`; pickling works if `args == (message,)` matches what `__init__` expects — but `field` is lost on unpickle unless `__reduce__` is added:
```python
    def __reduce__(self):
        return (self.__class__, (self.args[0], self.field))
```

**Example 2: OSError subclass hijacked by errno-based dispatch**
Input:
```python
class MyOSError(OSError):
    pass

err = MyOSError(2, "No such file")
type(err)
```
Output: `FileNotFoundError` — because `OSError.__new__` inspects the errno argument (2 == ENOENT) and returns an instance of the more specific built-in subclass instead of `MyOSError`, unless `MyOSError` itself overrides `__new__` to prevent this dispatch.

**Example 3: StopIteration with custom value**
Input:
```python
class MyStop(StopIteration):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra

e = MyStop("done", extra="meta")
e.value, e.extra
```
Output: `("done", "meta")` — `StopIteration.__init__` already sets `self.value` from the first arg, so no need to set it manually.

## Best Practices

- Always call `super().__init__()` with exactly the arguments the built-in expects; don't assume it forwards `**kwargs`.
- Keep custom attributes as plain instance attributes set *after* `super().__init__()`, not passed through it.
- Override `__str__`/`__repr__` when custom attributes should appear in tracebacks/logs.
- If subclassing `OSError`, be aware of implicit subclass dispatch via `__new__`; override `__new__` in your subclass if you need to force your exact type to be preserved.
- Implement `__reduce__` for exceptions with non-standard `__init__` signatures to keep pickling/multiprocessing working.

## Common Pitfalls

- Forgetting that `OSError(errno, strerror[, filename])` auto-selects a more specific subclass (`FileNotFoundError`, `PermissionError`, etc.), silently changing your exception's type.
- Overriding `__init__` without calling `super().__init__()`, leaving `args`, `strerror`, `errno`, etc. unset.
- Assuming default pickling works — it calls `cls(*exc.args)`, which breaks if `__init__` has a different signature (extra required args like `field` above).
- Not overriding `__str__`, resulting in custom attributes being invisible in printed tracebacks.
- Adding attributes via `__new__` instead of `__init__` when `__new__` doesn't need customizing — unnecessary complexity for most cases.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-python-exceptions
description: Explains and applies Python's exception class hierarchy, built-in exception types, and exception handling patterns. Use when writing try/except blocks, choosing which exception to raise or catch, creating custom exceptions, or debugging exception-related behavior.
---

## Quick Start

```python
# Catch specific exceptions, not bare Exception
try:
    value = int(user_input)
except ValueError as e:
    print(f"Invalid input: {e}")
except (TypeError, KeyError) as e:
    print(f"Unexpected type/key issue: {e}")

# Raise with context
try:
    process()
except OSError as e:
    raise RuntimeError("processing failed") from e

# Custom exception
class ConfigError(Exception):
    """Raised when configuration is invalid."""
```

## Workflow

Progress:
- [ ] Identify what can go wrong and which built-in exception naturally fits
- [ ] Choose the narrowest exception class(es) to catch
- [ ] Decide whether to handle, re-raise, or wrap the exception
- [ ] Add custom exception classes only when built-ins don't convey domain meaning
- [ ] Use `raise ... from ...` when re-raising in an except block
- [ ] Clean up resources with `finally` or context managers, not duplicated code

## Exception Hierarchy (base classes)

```
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ExceptionGroup(BaseExceptionGroup, Exception)
      ├── ArithmeticError (ZeroDivisionError, OverflowError, FloatingPointError)
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError (ModuleNotFoundError)
      ├── LookupError (IndexError, KeyError)
      ├── MemoryError
      ├── NameError (UnboundLocalError)
      ├── OSError (FileNotFoundError, PermissionError, TimeoutError, ...)
      ├── ReferenceError
      ├── RuntimeError (NotImplementedError, RecursionError)
      ├── StopIteration / StopAsyncIteration
      ├── SyntaxError (IndentationError → TabError)
      ├── SystemError
      ├── TypeError
      ├── ValueError (UnicodeError → UnicodeDecodeError/EncodeError/TranslateError)
      └── Warning (DeprecationWarning, UserWarning, ...)
```

Key base-class facts:

- **`BaseException`** is the root of *all* exceptions. Almost never catch this directly.
- **`Exception`** is what nearly all user code should subclass and catch. It excludes `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`, so catching `Exception` doesn't accidentally swallow program-termination signals.
- **`ArithmeticError`, `LookupError`, `OSError`** are "umbrella" bases — catch them when you want to handle a family of related errors generically (e.g., `except LookupError` catches both `IndexError` and `KeyError`).
- **`OSError`** subsumes what used to be separate `IOError`/`WindowsError`/`socket.error` — they're now aliases.
- Every exception has `.args`, and supports `__cause__` (explicit `raise ... from`) and `__context__` (implicit chaining during handling).
- `BaseExceptionGroup`/`ExceptionGroup` wrap multiple unrelated exceptions raised together (used with `except*` syntax).

## Examples

**Example 1: Choosing the right catch**
Input: Code that parses a JSON config file and looks up a key.
Output:
```python
import json

try:
    with open(path) as f:
        config = json.load(f)
    value = config["timeout"]
except FileNotFoundError:
    raise ConfigError(f"config file not found: {path}")
except json.JSONDecodeError as e:
    raise ConfigError(f"invalid JSON: {e}") from e
except KeyError:
    raise ConfigError("missing required key 'timeout'")
```

**Example 2: Custom exception hierarchy**
Input: A library needs its own errors that users can catch broadly or specifically.
Output:
```python
class LibraryError(Exception):
    """Base class for all errors raised by this library."""

class ValidationError(LibraryError):
    """Raised when input validation fails."""

class ConnectionFailedError(LibraryError):
    """Raised when a network connection cannot be established."""

# Users can do:
try:
    do_thing()
except LibraryError:      # catches both subclasses
    ...
```

**Example 3: `except*` for exception groups**
Input: A task runner collects failures from multiple concurrent subtasks.
Output:
```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fetch(a))
        tg.create_task(fetch(b))
except* ValueError as eg:
    for e in eg.exceptions:
        log.error("bad value: %s", e)
except* TimeoutError as eg:
    for e in eg.exceptions:
        log.error("timed out: %s", e)
```

## Best Practices

- Catch the most specific exception type that makes sense; fall back to umbrella bases (`LookupError`, `OSError`) only when handling truly applies to the whole family.
- Never bare `except:` — it also catches `KeyboardInterrupt` and `SystemExit`. Use `except Exception:` at minimum if you must catch broadly.
- Use `raise NewError(...) from original` to preserve the causal chain instead of losing context.
- Define custom exceptions as subclasses of `Exception` (not `BaseException`), and give a library a single root exception class so users can catch everything from it with one `except`.
- Prefer context managers (`with`) over manual `try/finally` for resource cleanup.
- Use `exc.args` or `str(exc)` for messages rather than parsing `repr(exc)`.

## Common Pitfalls

- Catching `Exception` (or worse, bare `except:`) to silence errors — hides bugs and swallows Ctrl-C.
- Subclassing `BaseException` directly for custom errors — breaks user expectations that `except Exception` catches everything reasonable.
- Re-raising with `raise NewError(str(e))` instead of `raise NewError(...) from e` — destroys the traceback/context chain.
- Confusing `IndexError`/`KeyError` (subclasses of `LookupError`) with `AttributeError`/`TypeError`, which are unrelated bases.
- Forgetting that `ModuleNotFoundError` is a subclass of `ImportError`, so catching `ImportError` alone is usually sufficient.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-python-exceptions
description: Guides selection, raising, and handling of Python's built-in concrete exception types according to their intended semantics. Use when writing error handling code, choosing which exception to raise, designing custom exception hierarchies, or reviewing code for incorrect exception usage.
---

# Handling Python Exceptions

## Quick Start

```python
def get_item(container, key, index):
    if not isinstance(key, str):
        raise TypeError(f"key must be str, got {type(key).__name__}")
    if index < 0 or index >= len(container):
        raise IndexError(f"index {index} out of range")
    try:
        return container[key][index]
    except KeyError as e:
        raise LookupError(f"key {key!r} not found") from e
```

Pick the exception based on the *nature of the error*, not convenience. Always raise the most specific applicable built-in before inventing a custom one.

## Workflow

Progress:
- [ ] Identify the failure category (bad value, bad type, missing resource, bad state, environment/system failure)
- [ ] Match to the most specific built-in exception
- [ ] Add a clear, actionable message with relevant values
- [ ] Chain exceptions with `from` when translating one error into another
- [ ] Only subclass a built-in when the built-ins genuinely don't fit
- [ ] Catch narrowly; never bare `except:` unless re-raising or at a top-level boundary

### Step 1: Classify the failure

| Situation | Exception |
|---|---|
| Wrong type passed | `TypeError` |
| Right type, invalid value | `ValueError` |
| Numeric value out of representable range | `OverflowError` |
| Sequence/mapping index or key doesn't exist | `IndexError` / `KeyError` (both subclass `LookupError`) |
| Attribute doesn't exist | `AttributeError` |
| Name not defined/bound | `NameError` (`UnboundLocalError` for locals) |
| Division/modulo by zero | `ZeroDivisionError` (subclass of `ArithmeticError`) |
| Object used in wrong state (e.g. closed file, exhausted generator) | `RuntimeError` or `StopIteration`/`StopAsyncIteration` as applicable |
| Method not implemented in subclass | `NotImplementedError` |
| Recursion too deep | `RecursionError` |
| File/resource missing or inaccessible | `OSError` and subclasses: `FileNotFoundError`, `FileExistsError`, `PermissionError`, `IsADirectoryError`, `NotADirectoryError`, `InterruptedError`, `TimeoutError`, `ConnectionError` (+ `BrokenPipeError`, `ConnectionResetError`, `ConnectionAbortedError`, `ConnectionRefusedError`) |
| Import fails | `ImportError` / `ModuleNotFoundError` |
| String/bytes can't be parsed as expected format | `SyntaxError`, `UnicodeError` (`UnicodeDecodeError`/`UnicodeEncodeError`/`UnicodeTranslateError`) |
| Assertion failed | `AssertionError` |
| Iterator exhausted | `StopIteration` |
| Multiple unrelated errors from concurrent/grouped operations | `ExceptionGroup` / `BaseExceptionGroup` |

### Step 2: Write the raise site

- Include the offending value(s) in the message: `f"expected positive int, got {n}"`.
- Never raise a bare string or non-exception object.
- Use `raise X(...) from original` when converting one exception into another to preserve the causal chain; use `from None` to deliberately suppress chaining noise.

### Step 3: Catch precisely

- Catch the narrowest exception(s) that a caller can meaningfully recover from.
- Catch tuples explicitly rather than broad supertypes: `except (KeyError, IndexError):`
- Never swallow `KeyboardInterrupt` or `SystemExit` (they subclass `BaseException`, not `Exception`) — don't use bare `except:` for that reason.
- Use `except* SomeError:` (3.11+) when handling `ExceptionGroup`s from concurrent tasks.

### Step 4: Custom exceptions only when needed

Subclass the closest matching built-in (e.g. `class ConfigError(ValueError):`) rather than `Exception` directly, so existing `except ValueError` handlers still work.

## Examples

**Example 1:**
Input: Function receives a negative value for a "count" parameter that must be non-negative.
Output:
```python
if count < 0:
    raise ValueError(f"count must be non-negative, got {count}")
```

**Example 2:**
Input: A dict lookup fails inside a function that's translating a public-facing API error.
Output:
```python
try:
    config = registry[name]
except KeyError as e:
    raise LookupError(f"no config registered under {name!r}") from e
```

**Example 3:**
Input: Opening a file that may not exist.
Output:
```python
try:
    with open(path) as f:
        data = f.read()
except FileNotFoundError:
    data = default_data
except PermissionError as e:
    raise RuntimeError(f"cannot read {path}: insufficient permissions") from e
```

**Example 4:**
Input: An abstract base class method that subclasses must override.
Output:
```python
class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")
```

## Best Practices

- Prefer `LookupError`'s subclasses (`KeyError`, `IndexError`) over generic exceptions for missing data access.
- Use `OSError` subclasses instead of checking `errno` manually — Python maps errno values automatically since 3.3.
- Reserve `RuntimeError` for genuinely unclassifiable state errors; don't use it as a catch-all default.
- Use exception chaining (`raise ... from ...`) whenever translating exceptions across abstraction layers — it preserves debuggability.
- When catching to log-and-reraise, use bare `raise` (no argument) to preserve the original traceback.
- Group related concurrent failures with `ExceptionGroup` rather than picking just one to propagate.

## Common Pitfalls

- Using `Exception` or bare `except:` to catch everything — hides bugs and can swallow `KeyboardInterrupt`/`SystemExit` if written as bare `except:`.
- Raising `ValueError` for wrong *type* — that's `TypeError`'s job.
- Re-raising with `raise NewError(str(e))` instead of `raise NewError(...) from e`, losing the traceback chain.
- Defining custom exceptions as direct `Exception` subclasses when a built-in subclass would let existing handlers catch them.
- Using `assert` for input validation in production code — asserts are stripped under `-O` and are for invariants, not user input checks.
- Catching `StopIteration` broadly inside a generator body (raises `RuntimeError` per PEP 479) instead of letting it propagate naturally or handling it explicitly.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-python-exceptions-and-warnings
description: Guides selection, raising, and catching of Python built-in exceptions and warnings according to the standard library semantics. Use when writing error handling code, choosing which exception/warning class to raise, designing custom exception hierarchies, or filtering warnings.
---

# Handling Python Exceptions and Warnings

## Quick Start

```python
# Raise the most specific built-in exception that fits
def get_item(d, key):
    if key not in d:
        raise KeyError(f"{key!r} not found")
    return d[key]

# Chain exceptions to preserve context
try:
    get_item({}, "x")
except KeyError as e:
    raise RuntimeError("lookup failed") from e

# Emit a warning instead of failing hard
import warnings
def old_api():
    warnings.warn("old_api() is deprecated, use new_api()", DeprecationWarning, stacklevel=2)
```

## Workflow

Progress checklist for designing error handling:

- [ ] Identify the failure mode: programmer error, runtime/environment error, or a non-fatal condition
- [ ] Pick the narrowest matching built-in exception/warning class (see table below)
- [ ] If no built-in fits, define a custom exception inheriting from the closest built-in base
- [ ] Decide whether to chain (`raise X from Y`) or suppress (`raise X from None`) the causing exception
- [ ] Use `try/except/else/finally` correctly: `else` for success-only code, `finally` for cleanup
- [ ] For warnings, choose the right category and set `stacklevel` so the reported location is the caller's
- [ ] Configure warning filters only at the application entry point, not inside library code

### Exception class selection

| Situation | Use |
|---|---|
| Wrong type passed | `TypeError` |
| Value of correct type but invalid | `ValueError` |
| Key missing from mapping | `KeyError` |
| Index out of range | `IndexError` |
| Attribute doesn't exist | `AttributeError` |
| Name not found | `NameError` (usually not raised manually) |
| Operation not supported / not yet implemented | `NotImplementedError` |
| Feature unsupported on this platform/config | `NotImplementedError` or custom |
| Invalid internal state / logic bug | `AssertionError` (via `assert`) or `RuntimeError` |
| File/OS-level errors | `OSError` (and subclasses: `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, `TimeoutError`) |
| Arithmetic problems | `ArithmeticError` subclasses: `ZeroDivisionError`, `OverflowError` |
| Iteration exhausted | `StopIteration` (don't catch manually in generators) |
| User interrupted program | `KeyboardInterrupt` (never catch broadly) |
| Recursion too deep | `RecursionError` |
| Custom domain error | Subclass `Exception` directly (never subclass `BaseException` unless it must escape normal handling like `SystemExit`) |

### Warning category selection

| Situation | Use |
|---|---|
| API scheduled for removal, visible to end users | `DeprecationWarning` |
| Deprecation only relevant to other library authors | `PendingDeprecationWarning` |
| Code likely has a bug | `RuntimeWarning` |
| Syntax is deprecated/questionable | `SyntaxWarning` |
| Use of obsolete feature that still works | `FutureWarning` (user-facing, unlike `DeprecationWarning`) |
| Import-related issue | `ImportWarning` |
| Unicode-related issue | `UnicodeWarning` |
| Bytes/bytearray related issue | `BytesWarning` |
| Resource not cleaned up (e.g., unclosed file) | `ResourceWarning` |
| Custom category | Subclass `Warning` |

## Examples

**Example 1: Wrapping a low-level error with context**
Input:
```python
def load_config(path):
    with open(path) as f:
        return parse(f.read())
```
Output:
```python
def load_config(path):
    try:
        with open(path) as f:
            return parse(f.read())
    except OSError as e:
        raise RuntimeError(f"could not load config from {path}") from e
    except ValueError as e:
        raise RuntimeError(f"config at {path} is malformed") from e
```

**Example 2: Deprecating a function**
Input: `def send(msg): ...` needs to be replaced by `send_message(msg)`.
Output:
```python
import warnings

def send(msg):
    warnings.warn(
        "send() is deprecated since v2.0; use send_message() instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return send_message(msg)
```

**Example 3: Custom exception hierarchy**
Input: A library needs its own errors for a parsing module.
Output:
```python
class ParserError(Exception):
    """Base class for all parser errors."""

class SyntaxParseError(ParserError):
    """Raised when input violates grammar rules."""

class EncodingParseError(ParserError, ValueError):
    """Raised when input encoding is invalid."""
```

**Example 4: Suppressing exception chaining**
Input: Re-raising a domain error without leaking internal details.
Output:
```python
try:
    _internal_lookup(key)
except _InternalKeyMiss:
    raise KeyError(key) from None
```

## Best Practices

- Prefer the most specific built-in exception; only create a custom one when none fits.
- Always inherit custom exceptions from `Exception`, not `BaseException`.
- Use `raise ... from err` to preserve the traceback chain; use `from None` to intentionally hide internal implementation exceptions.
- Use `stacklevel=2` (or higher) in `warnings.warn` so the warning points to the caller, not the library internals.
- Catch narrow exception types; avoid bare `except:` or broad `except Exception:` unless re-raising or logging at a top-level boundary.
- Use `else` clause in `try` blocks for code that should only run when no exception occurred.
- Use `finally` for cleanup that must run regardless of success/failure (or prefer context managers).
- Group related exceptions with `except (TypeError, ValueError):` rather than duplicating handler bodies.
- For libraries, never call `warnings.simplefilter` or change global filter state — that's the application's decision.

## Common Pitfalls

- Don't catch `BaseException`, `KeyboardInterrupt`, or `SystemExit` unintentionally with a bare `except:`.
- Don't swallow exceptions silently (`except Exception: pass`) — at minimum log them.
- Don't raise a bare `Exception()` or `RuntimeError()` for everything — it loses semantic meaning for callers.
- Don't forget `stacklevel` in `warnings.warn`; default (`1`) makes the warning appear to originate inside your own function.
- Don't use warnings for conditions that should actually stop execution — that's what exceptions are for.
- Don't mutate `__traceback__` or re-raise without `from` when context is genuinely useful for debugging.
- Don't subclass multiple unrelated exception bases without checking MRO consistency (e.g., mixing `ValueError` and `TypeError` bases can create confusing catches).
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-exception-groups
description: Guides construction and handling of Python ExceptionGroups and except* syntax for managing multiple concurrent exceptions. Use when dealing with tasks that can raise multiple errors simultaneously (asyncio.TaskGroup, concurrent.futures, structured concurrency), or when refactoring code that needs to handle heterogeneous error collections.
---

Quick Start

```python
# Raising multiple exceptions at once
try:
    raise ExceptionGroup("multiple failures", [
        ValueError("bad value"),
        TypeError("bad type"),
    ])
except* ValueError as eg:
    print(f"Caught ValueErrors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Caught TypeErrors: {eg.exceptions}")
```

`except*` matches by exception type against each leaf exception in the group, splits the group into "matched" and "unmatched" subgroups, and re-raises any unmatched portion after all clauses run.

## Workflow

Progress:
- [ ] Step 1: Identify whether errors arise from concurrent/parallel operations (asyncio tasks, thread pools, batch validation) — these are prime candidates for ExceptionGroup
- [ ] Step 2: Decide grouping strategy — one flat group, or nested groups preserving sub-task boundaries
- [ ] Step 3: Construct the group with `ExceptionGroup(msg, [exc1, exc2, ...])` or `BaseExceptionGroup` if any exception is a `BaseException` (e.g., `KeyboardInterrupt`, `SystemExit`)
- [ ] Step 4: Handle with `except*` clauses ordered from most specific to most general type
- [ ] Step 5: Verify unmatched exceptions propagate correctly (don't swallow silently)
- [ ] Step 6: Test with `.split()` / `.subgroup()` if you need programmatic filtering instead of `except*`

## Examples

**Example 1: Basic construction and type selection**

Input:
```python
excs = [ValueError("v1"), ValueError("v2")]
KeyboardInterrupt  # one of the exceptions is a BaseException, not Exception
```
Output:
```python
# Because KeyboardInterrupt is not an Exception, must use BaseExceptionGroup
eg = BaseExceptionGroup("mixed", [ValueError("v1"), KeyboardInterrupt()])
# ExceptionGroup() would raise TypeError here since it requires all Exception subclasses
```

**Example 2: Nested groups from concurrent tasks**

Input:
```python
import asyncio

async def worker(n):
    if n % 2 == 0:
        raise ValueError(f"even fail {n}")
    raise TypeError(f"odd fail {n}")

async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(4):
            tg.create_task(worker(i))
```
Output:
```python
try:
    asyncio.run(main())
except* ValueError as eg:
    print("ValueErrors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("TypeErrors:", [str(e) for e in eg.exceptions])
# TaskGroup automatically collects all task failures into one ExceptionGroup
```

**Example 3: Programmatic filtering without except\***

Input:
```python
eg = ExceptionGroup("errors", [ValueError("a"), TypeError("b"), ValueError("c")])
```
Output:
```python
value_errors, rest = eg.split(ValueError)
# value_errors: ExceptionGroup("errors", [ValueError("a"), ValueError("c")])
# rest: ExceptionGroup("errors", [TypeError("b")])
```

## Best Practices

- Use `except*` (not `except`) whenever you're catching from a block that may raise `ExceptionGroup`/`BaseExceptionGroup` — mixing them raises `SyntaxError`.
- Choose `BaseExceptionGroup` only when necessary (contains a `BaseException`); prefer `ExceptionGroup` for normal error handling since it's a subclass and satisfies both.
- Order `except*` clauses from specific to general — like regular `except`, but each clause can still match if the group contains a mix of types.
- Preserve nesting from source tasks/operations rather than flattening, so `.exceptions` retains context (e.g., which task failed).
- Use `traceback.print_exception(eg)` for readable nested tracebacks — the standard traceback module has explicit support for exception groups.
- Attach `__notes__` via `add_note()` for extra context on individual exceptions before grouping, rather than stuffing details into the group message.

## Common Pitfalls

- Don't mix bare `except` and `except*` in the same `try` statement — it's a `SyntaxError`.
- Don't assume `except*` clause runs once per matching exception type only — it collects *all* matching leaf exceptions from the (possibly nested) group into one subgroup and runs the handler once.
- Don't forget that unhandled/unmatched exceptions inside the group still propagate — an `except*` block that doesn't cover all types will re-raise a new group with the leftovers.
- Don't call `ExceptionGroup(msg, [])` — an empty exceptions list raises `ValueError`; a group must always contain at least one exception.
- Don't use `isinstance(e, ExceptionGroup)` checks inside a plain `except` and manually iterate `.exceptions` when `except*` already does this correctly, including nested groups.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: navigating-python-exception-hierarchy
description: Explains Python's built-in exception class hierarchy, inheritance relationships, and which exceptions to catch or raise in given scenarios. Use when writing exception handling code, deciding which exception class to catch or raise, debugging unexpected exception behavior, or creating custom exception classes.
---

## Quick Start

```python
# Catch the most specific applicable exception, not a broad parent
try:
    value = int(user_input)
except ValueError:          # specific: str couldn't convert to int
    print("Invalid number")

# Never catch BaseException or bare except unless re-raising
try:
    risky_operation()
except Exception:            # catches app errors, NOT SystemExit/KeyboardInterrupt
    log_and_continue()
```

## Workflow

1. **Identify the failure mode** — what actually goes wrong (bad type, bad value, missing key, missing attribute, IO failure)?
2. **Locate it in the hierarchy** — pick the narrowest built-in exception that matches semantically.
3. **Decide catch scope** — catch only what you can meaningfully handle; let everything else propagate.
4. **Consider custom exceptions** — if this is domain logic, subclass `Exception` (never `BaseException` directly).
5. **Verify ordering** — in multi-except blocks, list more specific exceptions before more general ones.

## The Hierarchy (Python 3.16)

```
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

**Key structural facts:**
- `Exception` is the base for essentially all program-level errors; `except Exception` will not catch `SystemExit`, `KeyboardInterrupt`, or `GeneratorExit`, since these inherit directly from `BaseException`.
- `OSError` unifies what used to be `IOError`, `EnvironmentError`, `WindowsError`, and socket errors — these are now aliases.
- `ImportError` → `ModuleNotFoundError` is raised when a module isn't found at all (subclass); plain `ImportError` covers other import failures (e.g., name not found in module).
- `LookupError` is the parent of `IndexError` and `KeyError` — catch `LookupError` when handling "container access failed" generically.
- `NameError` → `UnboundLocalError` specifically means a local variable was referenced before assignment.
- `ArithmeticError` groups `ZeroDivisionError`, `OverflowError`, `FloatingPointError`.
- `ExceptionGroup`/`BaseExceptionGroup` wrap multiple exceptions raised together (used with `except*` syntax).
- `Warning` is a subclass of `Exception` but conceptually separate — warnings are typically shown, not raised, via the `warnings` module.

## Examples

**Example 1:**
Input: Code does `d["missing_key"]` and needs to handle missing keys.
Output: `except KeyError:` — not the broader `LookupError` unless also handling list index errors in the same block.

**Example 2:**
Input: Need one handler for both `list[idx]` out-of-range and `dict[key]` missing.
Output: `except LookupError:` since it's the common parent of `IndexError` and `KeyError`.

**Example 3:**
Input: Writing a top-level handler that should log unexpected errors but let the user Ctrl-C out and let `sys.exit()` work.
Output: `except Exception:` (not `except BaseException:`), so `KeyboardInterrupt` and `SystemExit` propagate normally.

**Example 4:**
Input: Custom domain error for "insufficient funds" in a banking module.
Output:
```python
class InsufficientFundsError(Exception):
    """Raised when an account lacks funds for a transaction."""
```
Subclass `Exception`, not `BaseException` or `RuntimeError`, unless there's a stronger semantic fit.

## Best Practices

- Catch the narrowest exception that lets you handle the error meaningfully.
- Order `except` clauses from most specific to least specific — Python checks them top to bottom.
- Use `except (TypeError, ValueError):` for tuples of unrelated but co-handled exceptions instead of catching a shared broad ancestor.
- When re-raising with added context, use `raise NewError(...) from original_exc` to preserve the chain.
- Define custom exceptions per module/package, subclassing `Exception`, and build a small hierarchy of your own if the domain has multiple related error types.
- Use `except*` and `ExceptionGroup` when concurrent tasks (e.g., `asyncio.TaskGroup`) may raise multiple independent exceptions.

## Common Pitfalls

- Using bare `except:` — catches `BaseException`, swallowing `KeyboardInterrupt`/`SystemExit`, making programs unkillable via Ctrl-C in bad cases.
- Catching `Exception` broadly "just in case" and silently passing — hides real bugs.
- Confusing `ImportError` and `ModuleNotFoundError` — only the latter is guaranteed when a module doesn't exist; catch `ImportError` if also handling partial/attribute import failures.
- Assuming `IOError`/`EnvironmentError` still exist as distinct types — they're aliases of `OSError` now.
- Placing a general exception (e.g., `Exception`) before a specific one (e.g., `ValueError`) in the same `try` block — the specific branch becomes unreachable.
- Treating `Warning` subclasses as things to `except` in normal control flow — they're meant for the `warnings` filter system, not typical error handling.
- 