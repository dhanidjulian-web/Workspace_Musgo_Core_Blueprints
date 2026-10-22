---
name: using-python-builtins
description: Provides guidance on Python's built-in functions, their correct usage, parameters, and idiomatic application. Use when writing Python code that involves built-in functions like open(), sorted(), enumerate(), zip(), map(), filter(), isinstance(), or when choosing the most Pythonic built-in for a task.
---

## Quick Start

When writing Python code, prefer built-in functions over manual implementations:

```python
# Instead of manual iteration with index tracking
i = 0
for item in items:
    print(i, item)
    i += 1

# Use enumerate()
for i, item in enumerate(items):
    print(i, item)
```

## Workflow

1. **Identify the task pattern** - iteration, transformation, filtering, type checking, I/O, etc.
2. **Check for a built-in match** before writing custom logic or importing a library.
3. **Verify signature and edge cases** - check argument order, default values, and return types.
4. **Prefer built-ins over `itertools`/manual code** when a direct built-in exists; reach for `itertools` only for more complex iterator composition.
5. **Combine built-ins idiomatically** (e.g., `sorted(data, key=..., reverse=True)`, `zip(*pairs)`).

## Common Built-ins by Category

**Iteration & Sequences**
- `enumerate(iterable, start=0)` — index/value pairs
- `zip(*iterables, strict=False)` — parallel iteration; use `strict=True` (3.10+) to catch length mismatches
- `map(func, *iterables)`, `filter(func, iterable)` — prefer comprehensions for readability unless chaining lazily
- `reversed(seq)`, `sorted(iterable, key=None, reverse=False)`
- `range(start, stop, step)`
- `all(iterable)`, `any(iterable)` — short-circuiting boolean checks
- `sum(iterable, start=0)`, `min()`, `max()` (support `key=` and `default=`)

**Type & Object Introspection**
- `isinstance(obj, cls_or_tuple)` — prefer over `type(obj) == cls`
- `issubclass(cls, classinfo)`
- `callable(obj)`, `hasattr(obj, name)`, `getattr(obj, name, default)`, `setattr()`
- `type(obj)` — for introspection; use `isinstance()` for checks

**Functional / Higher-order**
- `sorted(..., key=lambda x: ...)` over custom sort loops
- `functools` complements builtins for `reduce`, `partial`, `lru_cache` (not builtin, but commonly paired)

**I/O**
- `open(file, mode='r', encoding=None, ...)` — **always pass `encoding='utf-8'` explicitly** for text mode to avoid platform-dependent behavior
- `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
- `input(prompt=None)`

**Conversion & Construction**
- `list()`, `tuple()`, `dict()`, `set()`, `frozenset()`, `str()`, `int()`, `float()`, `bytes()`, `bytearray()`
- `int(x, base=10)` — supports parsing non-base-10 strings
- `chr()`/`ord()` for char-codepoint conversion
- `format(value, format_spec)` — underlies f-strings

**Object/Class utilities**
- `super()`, `property()`, `staticmethod()`, `classmethod()`
- `vars(obj)`, `dir(obj)`, `id(obj)`
- `iter(obj, sentinel=None)`, `next(iterator, default)`

**Evaluation (use cautiously)**
- `eval()`, `exec()`, `compile()` — avoid on untrusted input; prefer `ast.literal_eval()` for safe literal parsing

## Examples

**Example 1:**
Input: Need to check if all elements in a list are positive.
Output:
```python
all(x > 0 for x in numbers)
```

**Example 2:**
Input: Need to iterate two lists together and stop safely on mismatched lengths.
Output:
```python
for a, b in zip(list1, list2, strict=True):
    ...
```

**Example 3:**
Input: Need to safely parse a string that might represent a Python literal (list, dict, number).
Output:
```python
from ast import literal_eval
value = literal_eval(user_input)  # NOT eval(user_input)
```

**Example 4:**
Input: Need to open a config file for reading text.
Output:
```python
with open("config.yaml", "r", encoding="utf-8") as f:
    contents = f.read()
```

## Best Practices

- Always use `with open(...)` for file handling — never leave files unclosed.
- Explicitly set `encoding="utf-8"` when opening text files; don't rely on system default.
- Prefer `isinstance(x, (int, float))` over chained `type()` checks; tuple form checks multiple types.
- Use `sorted(..., key=...)` instead of `sorted(..., cmp=...)` (cmp removed since Python 3).
- Use `next(iterator, default)` to avoid `StopIteration` boilerplate.
- Use `zip(..., strict=True)` (3.10+) whenever lengths must match, to fail loudly on bugs.
- Use `min()/max()` with `default=` when the iterable might be empty, to avoid `ValueError`.

## Common Pitfalls

- **Never use bare `eval()`/`exec()` on user input** — arbitrary code execution risk. Use `ast.literal_eval` instead.
- **Don't compare types with `==`** (`type(x) == list`) — use `isinstance()` to respect subclassing.
- **Don't forget `zip()` truncates silently** to the shortest iterable unless `strict=True` is passed.
- **Don't use mutable default arguments** in functions that wrap builtins (e.g., `def f(x, opts=[])`) — classic Python bug, unrelated to builtins directly but often surfaces when combining with `map`/`filter`.
- **Avoid `open()` without `encoding`** on cross-platform code — Windows vs. Linux default encodings differ.
- **Don't use `map()`/`filter()` chained deeply** where a generator expression or comprehension would be clearer.