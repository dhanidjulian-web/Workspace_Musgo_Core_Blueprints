---
name: explaining-python-builtin-constants
description: Explains Python's built-in constants (True, False, None, NotImplemented, Ellipsis, __debug__) and their correct usage patterns. Use when writing code involving boolean logic, singleton comparisons, type stub placeholders, operator overloading fallbacks, or debug-conditional code.
---

## Quick Start

```python
# Correct singleton comparisons: use `is`, not `==`
if value is None:
    ...

# NotImplemented: return from special methods when operation unsupported
class Vector:
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

# Ellipsis: placeholder in stubs/slices
def stub_function() -> int: ...
matrix[..., 0]

# __debug__: guards code stripped in optimized mode (-O)
if __debug__:
    assert expensive_check(), "This block vanishes under python -O"
```

## Workflow

1. **Identify which constant applies** to the situation:
   - `True`/`False` — boolean values (instances of `int` subclass `bool`)
   - `None` — absence of a value (the sole instance of `NoneType`)
   - `NotImplemented` — signal to Python that a binary operator/comparison isn't supported for these types
   - `Ellipsis` (`...`) — placeholder (slices, stubs, unimplemented bodies)
   - `__debug__` — `True` unless run with `-O`/`-OO`; controls `assert` execution

2. **Use identity checks (`is`/`is not`) for singletons** — never `==` for `None`, `True`, `False`, `NotImplemented`, `Ellipsis`. These are guaranteed singletons; identity comparison is faster and semantically correct.

3. **For operator overloading**, return `NotImplemented` (not raise an exception, not return `False`) when your type can't handle the other operand. Python then tries the reflected method or raises `TypeError` itself.

4. **Never evaluate `NotImplemented` in a boolean context directly** — it's truthy and doing `if x == y:` where `__eq__` might return `NotImplemented` can silently produce wrong results if not handled by Python's dispatch. Only return it from special methods; don't manually branch on it in general code.

5. **For `__debug__`-guarded code**, remember it's a compile-time constant — the `if __debug__:` block is literally removed from bytecode under `-O`. Don't put code with side effects required for correctness inside it (same rule as `assert`).

## Examples

**Example 1:**
Input: Reviewing code with `if x == None:`
Output: Flag and rewrite as `if x is None:` — `==` can be overridden by `__eq__` and is semantically wrong for singleton identity checks; `is` is also faster.

**Example 2:**
Input: Implementing `__lt__` for a custom class comparing against arbitrary types
Output:
```python
def __lt__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented
    return self.value < other.value
```

**Example 3:**
Input: Writing a `.pyi` stub file for a function body
Output:
```python
def connect(host: str, port: int) -> Connection: ...
```
`...` (Ellipsis) is the idiomatic stub body placeholder, distinct from `pass`.

**Example 4:**
Input: `assert user.is_authenticated(), "must be logged in"` used to enforce security
Output: Flag as a bug — under `python -O`, `__debug__` is `False` and all `assert` statements are compiled out, so this check silently disappears. Use an explicit `if not ...: raise PermissionError(...)` instead.

## Best Practices

- Treat `True`/`False` as `int` subtypes when relevant (`True == 1`, `isinstance(True, int)` is `True`) but don't rely on this for readability — prefer explicit booleans in conditionals.
- Use `None` as the default sentinel for "no value provided" in function signatures, but if `None` is a valid meaningful argument, use a dedicated sentinel object instead.
- Document custom classes' `__eq__`/`__lt__`/etc. as returning `NotImplemented` for unsupported types so subclasses and reflected operations behave correctly.
- Use `Ellipsis` in NumPy-style slicing (`arr[..., 0]`) and in type-stub/interface bodies; avoid using it as a generic "TODO" placeholder in production logic (use `raise NotImplementedError` instead — different from `NotImplemented`).

## Common Pitfalls

- **Confusing `NotImplemented` with `NotImplementedError`.** `NotImplemented` is a constant returned from special methods; `NotImplementedError` is an exception raised in abstract method bodies. They are not interchangeable.
- **Using `==` instead of `is` for `None`/singletons** — fragile if `__eq__` is overridden.
- **Putting required side effects inside `if __debug__:` or `assert`** — vanishes under `-O`.
- **Returning `False` instead of `NotImplemented`** from comparison dunders when the type doesn't match — this incorrectly asserts inequality/falsity rather than deferring to the other operand's reflected method.
- **Using `Ellipsis` as an empty function body placeholder in real (non-stub) code** where `pass` or a real implementation is expected — reserve `...` for stubs/interfaces.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```markdown
---
name: explaining-python-builtin-constants
description: Explains Python's built-in constants (True, False, None, NotImplemented, Ellipsis, __debug__) and site-module-added constants (quit, exit, copyright, credits, license). Use when clarifying constant behavior, differences between them, or interactive-shell-only availability.
---

## Quick Start

```python
>>> None is None
True
>>> NotImplemented  # used by rich comparison/binary ops, not general code
NotImplemented
>>> ... is Ellipsis  # `...` literal is Ellipsis
True
>>> __debug__  # False when run with -O
True
>>> exit()  # only in interactive interpreter / site module enabled
```

## Workflow

1. **Identify which category the constant belongs to:**
   - Core language constants (always available, part of `builtins`): `True`, `False`, `None`, `NotImplemented`, `Ellipsis`/`...`, `__debug__`
   - Site-module constants (added by `site.py`, interactive convenience only): `quit`, `exit`, `copyright`, `credits`, `license`

2. **Explain semantics accurately:**
   - `True`/`False`: instances of `bool`, subclass of `int` (`True == 1`, `False == 0`)
   - `None`: sole instance of `NoneType`, represents absence of a value
   - `NotImplemented`: return value from rich comparison/arithmetic special methods signaling "try the other operand's method"; **not** the same as raising `NotImplementedError`
   - `Ellipsis`: singleton, written as `...`, used in slicing, type stubs, stub bodies
   - `__debug__`: `True` unless Python started with `-O`/`-OO`; guards `assert` statements
   - `quit`/`exit`: callables (instances of `_sitebuiltins.Quitter`) that raise `SystemExit`; **only guaranteed in interactive mode** — absent if `site` module is disabled (`-S` flag) or in some embedded contexts
   - `copyright`/`credits`/`license`: callables that print interpreter info when called (e.g. `license()`), added by `site` module

3. **Flag common confusions:**
   - `NotImplemented` vs `NotImplementedError` (data value vs exception class)
   - `exit()`/`quit()` are **not** meant for use in production scripts — use `sys.exit()` instead
   - These site-module constants may not exist if `site.py` wasn't imported (`python -S`)

## Examples

**Example 1:**
Input: "What's the difference between `NotImplemented` and `NotImplementedError`?"
Output:
`NotImplemented` is a singleton **value** returned from methods like `__eq__`, `__lt__`, `__add__` to tell Python "I don't know how to handle this operand type, try the reflected method or fall back." Python then either calls the other object's method or raises `TypeError` itself.
`NotImplementedError` is an **exception class**, typically raised in abstract base methods to signal a subclass must override them.
Returning `NotImplementedError()` instead of `NotImplemented` from `__eq__` is a common bug — it won't trigger Python's fallback protocol.

**Example 2:**
Input: "Why does `exit()` work in my REPL but fail in my script run with `python -S script.py`?"
Output:
`exit` and `quit` aren't language builtins — they're injected into the `builtins` namespace by the `site` module specifically for interactive convenience. The `-S` flag skips `site` initialization, so those names are never defined. For scripts, always use `sys.exit([code])` from the `sys` module, which is guaranteed available.

**Example 3:**
Input: "Does `assert` cost anything in production?"
Output:
`assert expr, msg` compiles to a check guarded by `__debug__`. Running Python with `-O` sets `__debug__` to `False` and the compiler **strips assert statements entirely** — no runtime cost. Don't rely on assert for input validation that must run in production; use explicit `if`/`raise` instead.

## Best Practices

- Point users to `sys.exit()` over `exit()`/`quit()` in any non-interactive code
- Clarify that `True`/`False`/`None` are keywords (cannot be reassigned) as of Python 3, unlike `NotImplemented`/`Ellipsis` which are ordinary names bound to singletons
- Mention `...` as a valid no-op placeholder in function bodies and type stubs, equivalent to `pass` but semantically "not implemented yet"
- When discussing `__debug__`, tie it to the `-O`/`-OO` flags and `PYTHONOPTIMIZE` env var

## Common Pitfalls

- Don't claim `quit`/`exit`/`copyright`/`credits`/`license` are guaranteed builtins — they depend on the `site` module being loaded
- Don't confuse `NotImplemented` (value) with raising `NotImplementedError` (exception)
- Don't say `assert` is "always safe to use for validation" — it disappears under `-O`
- Don't treat `Ellipsis` as Python-2-only trivia — it's actively used in NumPy slicing and type stub (`.pyi`) syntax
```