---
name: processing-text-with-python
description: Applies Python's built-in text processing libraries (string, re, difflib, textwrap, unicodedata, stringprep, rlcompleter) to manipulate, match, compare, and format text. Use when writing Python code that parses strings, performs regex matching, wraps/fills text, computes diffs, normalizes Unicode, or needs common string constants and templates.
---

## Quick Start

```python
import re
import textwrap
from difflib import unified_diff
from string import Template

# Regex matching
match = re.search(r'(\d+)-(\d+)', "range: 10-20")
if match:
    start, end = match.groups()

# Text wrapping
print(textwrap.fill("A very long line of text that needs wrapping", width=20))

# String templating
t = Template("Hello, $name!")
print(t.substitute(name="World"))

# Diffing
diff = unified_diff("line1\nline2\n".splitlines(),
                     "line1\nline3\n".splitlines(), lineterm="")
print("\n".join(diff))
```

## Workflow

Progress:
- [ ] Step 1: Identify the text task category (matching, formatting, comparing, normalizing, constants)
- [ ] Step 2: Select the right module (see mapping below)
- [ ] Step 3: Write minimal, correct code using the module's idiomatic API
- [ ] Step 4: Handle edge cases (empty strings, Unicode, unmatched patterns)
- [ ] Step 5: Test with representative inputs

### Module Selection Map

| Task | Module | Key API |
|---|---|---|
| Pattern matching/extraction | `re` | `re.match`, `re.search`, `re.findall`, `re.sub`, `re.compile` |
| String constants (ascii letters, digits, punctuation) | `string` | `string.ascii_letters`, `string.digits`, `string.punctuation` |
| Template-based substitution | `string.Template` | `.substitute()`, `.safe_substitute()` |
| Wrapping/indenting paragraphs | `textwrap` | `textwrap.wrap`, `textwrap.fill`, `textwrap.dedent`, `textwrap.indent` |
| Comparing sequences/text | `difflib` | `SequenceMatcher`, `unified_diff`, `get_close_matches` |
| Unicode normalization | `unicodedata` | `unicodedata.normalize`, `unicodedata.category` |
| Internationalized string prep (rare, legacy) | `stringprep` | used internally by `encodings.idna` |
| Interactive completion (REPL only) | `rlcompleter` | rarely used directly in scripts |

## Examples

**Example 1: Extract and validate structured data with `re`**
Input: Extract all email addresses from a block of text.
```python
import re
text = "Contact: alice@example.com or bob@test.org"
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
```
Output: `['alice@example.com', 'bob@test.org']`

**Example 2: Wrap CLI help text with `textwrap`**
Input: A long description string that must fit an 80-column terminal, indented as a bullet.
```python
import textwrap
desc = "This tool processes large datasets efficiently using streaming."
wrapped = textwrap.fill(desc, width=40, initial_indent="- ", subsequent_indent="  ")
```
Output:
```
- This tool processes large datasets
  efficiently using streaming.
```

**Example 3: Fuzzy-match user input against known commands with `difflib`**
Input: User types "stauts", available commands are `["status", "start", "stop"]`.
```python
from difflib import get_close_matches
suggestion = get_close_matches("stauts", ["status", "start", "stop"], n=1)
```
Output: `['status']`

**Example 4: Safe templating with missing keys**
Input: Template with a placeholder not present in the substitution dict.
```python
from string import Template
t = Template("$greeting, $name!")
result = t.safe_substitute(name="Sam")
```
Output: `'$greeting, Sam!'` (no `KeyError`, unlike `.substitute()`)

**Example 5: Normalize Unicode for comparison**
Input: Compare `"café"` (composed) vs `"café"` (decomposed, e + combining accent).
```python
import unicodedata
a = unicodedata.normalize('NFC', "café")
b = unicodedata.normalize('NFC', "cafe\u0301")
a == b
```
Output: `True`

## Best Practices

- **Compile regex once** with `re.compile()` when reused in loops; use raw strings (`r"..."`) always.
- **Prefer `re.fullmatch`** over `re.match` when validating an entire string against a pattern.
- **Use `Template.safe_substitute`** over `.substitute()` when input keys aren't guaranteed complete — avoids exceptions in user-facing tools.
- **Use `textwrap.shorten`** instead of manual truncation for building "..." previews with word-boundary awareness.
- **Normalize Unicode (`NFC` typically)** before any string equality check or hashing involving user-supplied international text.
- **Use `difflib.SequenceMatcher.ratio()`** for similarity scoring, not just `get_close_matches`, when you need a numeric score.
- **Avoid greedy `.*` in regex** — use `.*?` or explicit character classes to prevent catastrophic backtracking on large inputs.

## Common Pitfalls

- Don't use `re` for full HTML/XML parsing — use a real parser (`html.parser`, `xml.etree`, or `BeautifulSoup`); regex breaks on nested/irregular structures.
- Don't forget `re.MULTILINE` when using `^`/`$` on multi-line text — default only matches start/end of the whole string.
- Don't compare Unicode strings without normalizing first — visually identical strings can differ byte-wise and fail `==`.
- Don't use `string.Template` for HTML/code generation with untrusted input without escaping — it does plain substitution, no escaping.
- Don't call `textwrap.wrap` expecting it to preserve existing line breaks — it collapses whitespace by default (use `replace_whitespace=False` to preserve).
- Don't rely on `rlcompleter` or `stringprep` directly in application code — they're low-level building blocks for other stdlib features (readline, IDNA encoding).
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```
---
name: formatting-strings-with-python
description: Applies Python's string module and format-string mini-language to build templates, custom formatters, and safe string substitution. Use when working with str.format(), f-strings, string.Template, Formatter subclasses, or string constants like ascii_letters/digits/punctuation.
---

# Formatting Strings with Python

## Quick Start

```python
# Format spec mini-language
f"{value:>10.2f}"          # right-align, 2 decimals
f"{value:,}"                # thousands separator
f"{value:.1%}"               # percentage

# string.Template for user-facing substitution (safer than % or .format for untrusted input)
from string import Template
t = Template("Hello, $name! You have $count new messages.")
t.substitute(name="Ana", count=3)
t.safe_substitute(name="Ana")   # missing keys left as-is instead of raising

# Useful constants
import string
string.ascii_letters   # 'abcdefghij...XYZ'
string.digits          # '0123456789'
string.punctuation     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

## Workflow

Progress:
- [ ] Step 1: Decide the right tool — f-string (static, dev-controlled), `str.format()` (reusable template, dev-controlled), or `string.Template` (untrusted/user-supplied templates)
- [ ] Step 2: Choose format spec (`{:spec}`) for numeric/alignment/width needs
- [ ] Step 3: For repeated custom formatting logic, subclass `string.Formatter` and override `format_field`/`get_value`
- [ ] Step 4: For generating random strings/tokens, combine `string.ascii_letters`, `digits`, `punctuation` with `random`/`secrets`
- [ ] Step 5: Test edge cases — missing keys, special characters, locale-sensitive numbers

### Format Spec Mini-Language Reference

```
[[fill]align][sign][#][0][width][,|_][.precision][type]

align: < > ^ =        (left, right, center, pad-after-sign)
sign:  + - ' '         (always show, only negative, space for positive)
type:  d f e g % x o b n s
```

Common patterns:
```python
f"{n:04d}"        # zero-padded int, width 4      -> "0007"
f"{n:+d}"         # force sign                     -> "+7"
f"{pi:.3f}"       # 3 decimal places                -> "3.142"
f"{big:,}"        # comma thousands separator       -> "1,234,567"
f"{ratio:.2%}"    # percentage with 2 decimals      -> "45.67%"
f"{text:^20}"     # center in width 20
f"{n:#x}"         # hex with 0x prefix
```

## Examples

**Example 1: Safe template for user-editable messages**
Input: App lets users customize a notification template like `"Hi $user, your order $order_id shipped."`
Output:
```python
from string import Template

template = Template(user_supplied_template)
message = template.safe_substitute(user="Ana", order_id="A1023")
# safe_substitute avoids KeyError crashes if a $variable is missing/mistyped
```

**Example 2: Custom Formatter for domain objects**
Input: Need `{obj:currency}` to format a `Decimal` as `$1,234.50`.
Output:
```python
from string import Formatter
from decimal import Decimal

class MyFormatter(Formatter):
    def format_field(self, value, spec):
        if spec == "currency":
            return f"${value:,.2f}"
        return super().format_field(value, spec)

fmt = MyFormatter()
fmt.format("Total: {0:currency}", Decimal("1234.5"))
# -> "Total: $1,234.50"
```

**Example 3: Generating a random alphanumeric token**
Input: Need an 8-char token from letters+digits.
Output:
```python
import secrets, string

alphabet = string.ascii_letters + string.digits
token = "".join(secrets.choice(alphabet) for _ in range(8))
```

## Best Practices

- Prefer f-strings for internal/static formatting — fastest, clearest, evaluated at write time.
- Use `string.Template` (not `.format()` or f-strings) when the template string comes from users, config files, or translators — it only substitutes `$identifier`/`${identifier}`, avoiding arbitrary attribute/method access.
- Use `random.choice`/`random.sample` with `string` constants only for non-security purposes (test data, IDs); use `secrets` module for tokens, passwords, or anything security-sensitive.
- Reuse `Formatter` subclassing when the same custom format types (`currency`, `duration`, etc.) are needed across many call sites — beats scattering manual string logic.
- For number formatting with locale (comma vs. period), consider `locale` module or `Babel` library rather than hardcoding `,`.

## Common Pitfalls

- Using `str.format()` or f-strings on untrusted/user-provided template strings — allows access to object internals (e.g. `"{0.__class__.__init__.__globals__}".format(x)`), a real security risk. Use `string.Template` instead.
- Forgetting `safe_substitute` vs `substitute` — `substitute` raises `KeyError` on missing placeholders; `safe_substitute` silently leaves them unresolved (choose deliberately, don't default blindly).
- Confusing `string.punctuation`/`whitespace` platform assumptions — these are ASCII-only, not full Unicode punctuation sets.
- Misusing `%` old-style formatting mixed with new-style specs — stick to one style per codebase.
- Forgetting `{{` and `}}` to escape literal braces in `.format()`/f-strings.

---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: processing-template-strings
description: Processes PEP 750 t-string (Template) objects from Python's string.templatelib module, handling Interpolation objects, format specs, conversions, and safe rendering (e.g., HTML/SQL escaping). Use when working with t-strings (t"..."), Template/Interpolation objects, or building custom string-processing DSLs that need access to interpolated values before they become strings.
---

# Processing Template Strings

## Quick Start

```python
# t-strings (t"...") produce Template objects, NOT strings.
# Unlike f-strings, interpolated values stay as live objects until you process them.

name = "World"
template = t"Hello, {name}!"

print(type(template))  # <class 'string.templatelib.Template'>

# Iterate over strings and interpolations in order
for item in template:
    print(repr(item))
# 'Hello, '
# Interpolation(value='World', expression='name', conversion=None, format_spec='')
# '!'

# Convert to a plain string manually (no auto-escaping happens for you)
result = "".join(
    str(item.value) if hasattr(item, "value") else item
    for item in template
)
print(result)  # "Hello, World!"
```

## Core Concepts

- **`Template`** — the object produced by `t"..."`. Iterable, yielding a mix of `str` literal segments and `Interpolation` objects in source order.
  - `.strings` — tuple of the literal string parts (length = interpolations + 1).
  - `.interpolations` — tuple of `Interpolation` objects.
  - `.values()` — shortcut generator of just the interpolation values.
  - Supports `+` concatenation with other `Template` or `str` objects (returns a `Template`).
- **`Interpolation`** — represents one `{expr}` slot. Fields:
  - `.value` — the evaluated Python object (already evaluated, not lazy).
  - `.expression` — source text of the expression, e.g. `"name"` or `"x + 1"`.
  - `.conversion` — `"s"`, `"r"`, `"a"`, or `None` (from `!s`/`!r`/`!a`).
  - `.format_spec` — string from `:spec`, `""` if absent (raw, not pre-applied).
- Key distinction from f-strings: **nothing is stringified automatically**. You own the conversion/format/escaping logic — this is the entire point of t-strings (safe templating DSLs).

## Workflow

Progress:
- [ ] Identify whether you need a `Template` (t-string, deferred) or an f-string (immediate string)
- [ ] Write a renderer that walks `template.strings` / `template.interpolations` or iterates the `Template` directly
- [ ] Apply `conversion` (`!s`/`!r`/`!a`) manually if present
- [ ] Apply `format_spec` manually (typically via `format(value, spec)`)
- [ ] Apply domain-specific escaping (HTML, SQL, shell) to interpolated values only — never to literal segments
- [ ] Join everything into the final output

### Step-by-step renderer pattern

```python
from string.templatelib import Template, Interpolation

def render(template: Template, escape=str) -> str:
    parts = []
    for item in template:
        if isinstance(item, Interpolation):
            value = item.value
            if item.conversion == "s":
                value = str(value)
            elif item.conversion == "r":
                value = repr(value)
            elif item.conversion == "a":
                value = ascii(value)
            if item.format_spec:
                value = format(value, item.format_spec)
            parts.append(escape(str(value)))
        else:
            parts.append(item)  # literal text: NOT escaped
    return "".join(parts)
```

## Examples

**Example 1: HTML auto-escaping (the canonical t-string use case)**
Input:
```python
import html

def html_escape(template):
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            parts.append(html.escape(str(item.value)))
    return "".join(parts)

user_input = "<script>alert(1)</script>"
page = t"<p>Comment: {user_input}</p>"
print(html_escape(page))
```
Output:
```
<p>Comment: &lt;script&gt;alert(1)&lt;/script&gt;</p>
```

**Example 2: Safe SQL parameterization**
Input:
```python
def to_sql(template):
    sql_parts = []
    params = []
    for item in template:
        if isinstance(item, str):
            sql_parts.append(item)
        else:
            sql_parts.append("?")
            params.append(item.value)
    return "".join(sql_parts), tuple(params)

name = "Robert'); DROP TABLE students;--"
query = t"SELECT * FROM users WHERE name = {name}"
sql, params = to_sql(query)
print(sql, params)
```
Output:
```
SELECT * FROM users WHERE name = ? ("Robert'); DROP TABLE students;--",)
```

**Example 3: Inspecting format spec and conversion**
Input:
```python
value = 3.14159
t_obj = t"{value!r:.2f}"
interp = t_obj.interpolations[0]
print(interp.value, interp.conversion, interp.format_spec)
```
Output:
```
3.14159 r .2f
```
(Note: conversion and format_spec are metadata only — applying both is your responsibility, e.g. `format(repr(value), ".2f")` would error since repr returns a str; typically you choose one or handle order deliberately.)

## Best Practices

- Treat `Template` as an AST-like object, not a string — never call `str(template)` expecting sensible output (it does not exist as a stringification API; iterate instead).
- Centralize escaping in one `render`/`escape` function per output context (HTML, SQL, shell, logging) rather than escaping ad hoc.
- Preserve literal `.strings` segments verbatim — only transform `Interpolation.value`.
- When building a DSL, validate `.expression` only for debugging/error messages, not as executable logic — `.value` is already evaluated.
- Use `.values()` when you only need the raw interpolated objects and don't care about surrounding literals or metadata.
- Combine `Template` objects with `+` to compose reusable partial templates before final rendering.

## Common Pitfalls

- **Assuming auto-conversion**: unlike f-strings, `t"{x}"` does not stringify `x` — `interpolation.value` keeps its original type (int, list, custom object, etc.).
- **Escaping literal segments**: only escape `Interpolation` values; escaping the plain `str` segments from `.strings` will double-escape or corrupt intended markup.
- **Ignoring `format_spec`/`conversion`**: these are captured as metadata strings, not auto-applied — forgetting to apply them silently drops formatting like `.2f` or `!r`.
- **Using t-strings where f-strings suffice**: if no deferred processing/escaping is needed, an f-string is simpler and produces a `str` directly.
- **Mutating and reusing `Interpolation` objects**: they're immutable value carriers; build new `Template`/output rather than trying to patch fields in place.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-regex
description: Applies Python's re module for pattern matching, searching, splitting, and substitution in strings. Use when writing or debugging regular expressions in Python, validating text formats, extracting substrings, or performing find-and-replace operations with pattern logic.
---

# Using Python Regex (re module)

## Quick Start

```python
import re

# Compile once, reuse often
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

text = "Contact: alice@example.com or bob@test.org"
matches = pattern.findall(text)
# ['alice@example.com', 'bob@test.org']

# Single search
m = re.search(r'\d+', "Order #4521")
if m:
    print(m.group())  # '4521'
```

## Workflow

Progress:
- [ ] Step 1: Define the exact string shape you need to match (be explicit about anchors, boundaries, optional parts)
- [ ] Step 2: Choose the right function (`match`, `search`, `findall`, `finditer`, `sub`, `split`)
- [ ] Step 3: Write the pattern using raw strings (`r"..."`) to avoid escape confusion
- [ ] Step 4: Use named groups `(?P<name>...)` for clarity when extracting multiple fields
- [ ] Step 5: Compile the pattern with `re.compile()` if reused in a loop or called repeatedly
- [ ] Step 6: Test against edge cases (empty string, multiline, unicode, overlapping matches)
- [ ] Step 7: Apply flags (`re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`, `re.VERBOSE`) as needed
- [ ] Step 8: Verify no catastrophic backtracking on large/adversarial inputs

## Core Function Reference

| Function | Purpose | Returns |
|---|---|---|
| `re.match(p, s)` | Match at start of string only | Match object or `None` |
| `re.fullmatch(p, s)` | Entire string must match | Match object or `None` |
| `re.search(p, s)` | Find first match anywhere | Match object or `None` |
| `re.findall(p, s)` | Find all non-overlapping matches | List of strings/tuples |
| `re.finditer(p, s)` | Find all matches, lazily | Iterator of Match objects |
| `re.sub(p, repl, s)` | Replace matches | New string |
| `re.subn(p, repl, s)` | Replace + count | Tuple (string, count) |
| `re.split(p, s)` | Split string by pattern | List of strings |

## Examples

**Example 1: Extracting structured data with named groups**
Input:
```python
log = "2024-01-15 ERROR: Connection failed"
pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<level>\w+):\s+(?P<msg>.+)')
m = pattern.match(log)
```
Output:
```python
m.group('date')   # '2024-01-15'
m.group('level')  # 'ERROR'
m.group('msg')    # 'Connection failed'
m.groupdict()     # {'date': '2024-01-15', 'level': 'ERROR', 'msg': 'Connection failed'}
```

**Example 2: Substitution with a function**
Input:
```python
text = "price: 100, discount: 20"
result = re.sub(r'\d+', lambda m: str(int(m.group()) * 2), text)
```
Output:
```python
"price: 200, discount: 40"
```

**Example 3: Splitting on multiple delimiters**
Input:
```python
re.split(r'[,;]\s*', "apple, banana;cherry,  date")
```
Output:
```python
['apple', 'banana', 'cherry', 'date']
```

**Example 4: Verbose mode for readable complex patterns**
Input:
```python
pattern = re.compile(r"""
    (?P<area>\d{3})   # area code
    -
    (?P<num>\d{4})    # number
""", re.VERBOSE)
pattern.match("555-1234").groupdict()
```
Output:
```python
{'area': '555', 'num': '1234'}
```

## Best Practices

- Always use raw strings (`r"..."`) for patterns to avoid double-escaping backslashes.
- Use `re.compile()` when the same pattern runs many times (loops, per-request validation).
- Prefer non-capturing groups `(?:...)` when you don't need to extract that group, for performance and clarity.
- Use `\b` word boundaries to avoid partial-word matches (e.g., matching "cat" inside "category").
- Use `re.VERBOSE` with inline comments for patterns longer than ~40 characters.
- Anchor patterns (`^`, `$`, `\A`, `\Z`) when the entire string must conform to a format — use `fullmatch()` instead of `match()` when validating full strings.
- For known-safe literal text, use `re.escape()` before inserting user input into a pattern.
- Use `finditer()` instead of `findall()` when you need match positions (`.start()`, `.end()`) or when working with large text (lazy iteration).

## Common Pitfalls

- **Greedy quantifiers by default** — `.*` grabs as much as possible; use `.*?` for lazy/minimal matching when needed.
- **Forgetting `re.DOTALL`** — `.` does not match newlines by default; multiline text needs `re.DOTALL` if you want `.` to span lines.
- **Confusing `match()` vs `search()`** — `match()` only anchors at the start of the string, not the whole string; unexpected `None` results often come from this.
- **Unescaped special characters** — literal `.`, `*`, `+`, `(`, `)`, `[`, `]`, `{`, `}`, `|`, `^`, `$`, `\` must be escaped or passed through `re.escape()`.
- **Catastrophic backtracking** — nested quantifiers like `(a+)+` on adversarial input can hang; prefer possessive-like restructuring or bound repetition counts.
- **Ignoring compiled flags scope** — flags set inside `(?i)` apply differently across Python versions/positions; prefer passing flags explicitly to `re.compile()`.
- **Using regex for deeply nested/structured data** — HTML, JSON, or nested parentheses are not reliably parseable with regex; use a proper parser instead.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: computing-sequence-diffs
description: Computes and presents differences between sequences (text lines, strings, lists) using Python's difflib module. Use when comparing files, generating diffs, finding close string matches, computing similarity ratios, or building patch/merge-like output.
---

## Quick Start

```python
import difflib

a = ["line1\n", "line2\n", "line3\n"]
b = ["line1\n", "line2 modified\n", "line3\n"]

diff = difflib.unified_diff(a, b, fromfile="a.txt", tofile="b.txt", lineterm="")
print("\n".join(diff))
```

Output:
```
--- a.txt
+++ b.txt
@@ -1,3 +1,3 @@
 line1
-line2
+line2 modified
 line3
```

## Workflow

Progress:
- [ ] Identify the comparison need: line-by-line diff, similarity score, or closest-match lookup
- [ ] Pick the right tool (see decision table below)
- [ ] Prepare inputs as sequences (lists of lines/strings), not raw multi-line strings
- [ ] Run the comparison
- [ ] Format/present output (unified, context, or HTML)

**Decision table:**

| Need | Tool |
|---|---|
| Git-style unified diff | `difflib.unified_diff(a, b)` |
| Context diff (before/after blocks) | `difflib.context_diff(a, b)` |
| Human-readable inline diff (ndiff style, `+`/`-`/`?`) | `difflib.ndiff(a, b)` |
| Side-by-side HTML diff | `difflib.HtmlDiff().make_file(a, b)` |
| Similarity ratio between two strings (0.0–1.0) | `difflib.SequenceMatcher(None, a, b).ratio()` |
| Fuzzy match closest strings from a list | `difflib.get_close_matches(word, possibilities)` |
| Detailed opcodes (replace/insert/delete/equal ranges) | `SequenceMatcher.get_opcodes()` |

Steps:
1. Read files with `.readlines()` (keepends=True) so diffs preserve line structure — don't use `.split("\n")` unless you strip newlines consistently.
2. Choose the tool from the table.
3. For `SequenceMatcher`, pass `autojunk=False` if comparing short/technical strings (default autojunk can skew results on repetitive text >200 chars).
4. Join generator output with `"\n".join(...)` or iterate directly — these functions return generators/iterators, not lists.

## Examples

**Example 1: Similarity ratio**
Input:
```python
difflib.SequenceMatcher(None, "python", "pytohn").ratio()
```
Output: `0.8333333333333334`

**Example 2: Closest match lookup**
Input:
```python
difflib.get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
```
Output: `['apple', 'ape']`

**Example 3: Opcodes for custom diff rendering**
Input:
```python
s = difflib.SequenceMatcher(None, "qabxcd", "abycdf")
s.get_opcodes()
```
Output:
```python
[('delete', 0, 1, 0, 0),
 ('equal', 1, 3, 0, 2),
 ('replace', 3, 4, 2, 3),
 ('equal', 4, 6, 3, 5),
 ('insert', 6, 6, 5, 6)]
```

**Example 4: File diff (CLI-style)**
Input: two files `old.py`, `new.py`
```python
with open("old.py") as f1, open("new.py") as f2:
    diff = difflib.unified_diff(f1.readlines(), f2.readlines(),
                                 fromfile="old.py", tofile="new.py")
    print("".join(diff))
```
Output: standard unified diff text block with `@@` hunk headers.

## Best Practices

- Use `readlines()` (keeps `\n`) for file diffs so `unified_diff`/`context_diff` output looks correct; use `lineterm=""` when lines already lack newlines.
- Use `get_close_matches(word, possibilities, n=3, cutoff=0.6)` — tune `n` and `cutoff` for stricter/looser fuzzy matching.
- For large files, prefer `unified_diff` over `context_diff` (more compact, standard for patches).
- Cache a `SequenceMatcher` instance with `set_seq2()` when comparing one string against many candidates repeatedly — avoids reprocessing the second sequence each time.
- Use `Differ().compare()` when you need inline `+`/`-`/`?` markers showing exact character-level changes within modified lines.

## Common Pitfalls

- Don't pass raw strings with embedded `\n` directly to `unified_diff`/`context_diff` — split into a list of lines first.
- Don't forget diffs are generators — printing the object directly shows a generator repr, not the diff.
- Don't rely on default `autojunk=True` for short or highly repetitive strings; it can silently produce misleading ratios/matches.
- `ratio()` is not symmetric-cost-free — it's O(n×m) in the worst case; avoid calling it in tight loops over large datasets without pre-filtering.
- `get_close_matches` returns `[]` silently if nothing meets `cutoff` — always handle the empty-result case.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
```yaml
---
name: wrapping-and-formatting-text
description: Wraps, fills, shortens, and dedents plain text using Python's textwrap module. Use when formatting long strings into readable paragraphs, wrapping CLI output, truncating text with ellipsis, removing common leading whitespace from multi-line strings, or indenting text blocks.
---
```

# Wrapping and Formatting Text

Uses Python's built-in `textwrap` module to programmatically wrap, fill, indent, dedent, and shorten text.

## Quick Start

```python
import textwrap

text = "The quick brown fox jumps over the lazy dog. " * 3

# Wrap into a list of lines (width in characters)
lines = textwrap.wrap(text, width=40)

# Wrap and rejoin into a single string with newlines
wrapped = textwrap.fill(text, width=40)

print(wrapped)
```

## Workflow

Progress:
- [ ] Identify the goal: list of lines (`wrap`), single string (`fill`), truncation (`shorten`), whitespace normalization (`dedent`), or adding prefixes (`indent`)
- [ ] Choose the right function for that goal
- [ ] Configure relevant keyword arguments (width, prefixes, break behavior)
- [ ] Apply to input text
- [ ] Verify output formatting (line lengths, indentation, no unwanted whitespace)

### Function selection guide

| Need | Function |
|---|---|
| List of wrapped lines | `textwrap.wrap(text, width=70)` |
| Single wrapped string | `textwrap.fill(text, width=70)` |
| Truncate to fit width + add `[...]` | `textwrap.shorten(text, width=50)` |
| Remove common leading whitespace | `textwrap.dedent(text)` |
| Add prefix to each line | `textwrap.indent(text, prefix)` |
| Reusable wrapper with custom settings | `textwrap.TextWrapper(**options)` |

### Key options (for `wrap`/`fill`/`TextWrapper`)

- `width` (default 70) — max line length
- `initial_indent` / `subsequent_indent` — string prepended to first/later lines
- `break_long_words` (default `True`) — split words longer than width
- `break_on_hyphens` (default `True`) — allow breaking at hyphens
- `replace_whitespace` (default `True`) — collapse all whitespace to single spaces
- `drop_whitespace` (default `True`) — strip leading/trailing whitespace per line
- `max_lines` — truncate output, adding a placeholder (default `' [...]'`) on the last line
- `tabsize` — expand tabs to this many spaces before processing (default 8)

## Examples

**Example 1: Wrapping paragraph for terminal output**
Input:
```python
textwrap.fill("This is a very long line of text that needs wrapping for a narrow terminal.", width=30)
```
Output:
```
This is a very long line of
text that needs wrapping for
a narrow terminal.
```

**Example 2: Dedenting a triple-quoted string**
Input:
```python
text = """
    def foo():
        return 1
    """
print(textwrap.dedent(text))
```
Output:
```

def foo():
    return 1

```

**Example 3: Indenting with a prefix (e.g., for quoting/logging)**
Input:
```python
textwrap.indent("line one\nline two", "> ")
```
Output:
```
> line one
> line two
```

**Example 4: Shortening text with placeholder**
Input:
```python
textwrap.shorten("The quick brown fox jumps over the lazy dog", width=25)
```
Output:
```
The quick brown fox [...]
```

**Example 5: Reusable wrapper for hanging indent**
Input:
```python
wrapper = textwrap.TextWrapper(width=40, initial_indent="- ", subsequent_indent="  ")
print(wrapper.fill("This is a bullet point that wraps onto multiple lines nicely."))
```
Output:
```
- This is a bullet point that wraps
  onto multiple lines nicely.
```

## Best Practices

- Use `dedent()` **before** `fill()`/`wrap()` when processing triple-quoted strings defined inside indented code — combine as `textwrap.fill(textwrap.dedent(text))`.
- Prefer `TextWrapper` over repeated `wrap()`/`fill()` calls when applying the same settings many times — it avoids re-parsing options.
- Use `initial_indent`/`subsequent_indent` for bullet points, blockquotes, or comment-style prefixes instead of manual string concatenation.
- Set `break_long_words=False` and `break_on_hyphens=False` when wrapping text containing URLs, file paths, or code identifiers that shouldn't be split.
- Use `shorten()` for generating previews/summaries (e.g., truncated log lines, table cells) since it collapses whitespace and adds a clean placeholder automatically.

## Common Pitfalls

- Don't use `dedent()` on text with mixed tabs/spaces without normalizing first — it only strips leading whitespace common to *all* lines, so inconsistent indentation results in no-op.
- Don't forget `dedent()` operates on the *whole* text as a block; it won't help per-line indentation removal for irregularly indented lines.
- Don't assume `wrap()` preserves original line breaks — `replace_whitespace=True` (the default) collapses newlines/tabs into spaces before wrapping.
- Don't use `fill()` when you need the individual lines for further processing (e.g., adding line numbers) — use `wrap()` and join manually instead.
- Remember `indent()` by default adds the prefix to lines consisting solely of whitespace too; pass a `predicate` function to control which lines get prefixed.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: querying-unicode-character-data
description: Looks up Unicode character properties (category, combining class, bidirectional class, numeric/decimal values, decomposition, normalization) using Python's unicodedata module. Use when handling text normalization, validating characters, comparing strings across encodings, or debugging encoding/rendering issues involving Unicode.
---

## Quick Start

```python
import unicodedata

# Basic lookups
unicodedata.name('€')          # 'EURO SIGN'
unicodedata.category('A')      # 'Lu' (Letter, uppercase)
unicodedata.decimal('9')       # 9
unicodedata.numeric('½')       # 0.5

# Normalization (most common real-world use)
s1 = unicodedata.normalize('NFC', 'café')   # composed form
s2 = unicodedata.normalize('NFD', 'café')   # decomposed form
s1 == s2  # False — same visual string, different byte representation!

# Safe comparison of visually-equivalent strings
def unicode_equal(a, b):
    return unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b)
```

## Workflow

Progress:
- [ ] Identify the problem type: comparison, validation, stripping, or inspection
- [ ] Choose the right normalization form (NFC/NFD/NFKC/NFKD)
- [ ] Apply the appropriate function(s)
- [ ] Handle `ValueError` for unassigned/invalid codepoints
- [ ] Test with edge cases (combining marks, surrogate pairs, CJK, emoji)

**1. Diagnose what's actually needed**

| Symptom | Likely fix |
|---|---|
| Two "identical-looking" strings compare unequal | Normalize both with `NFC` before comparing |
| Need to strip accents/diacritics | Decompose with `NFD`, then filter out combining marks |
| Need to compare full-width vs half-width, or ligatures | Use `NFKC`/`NFKD` (compatibility forms) |
| Validating that input is a digit/letter/etc. | Use `category()`, `decimal()`, `numeric()` |
| Debugging garbled text or mojibake | Use `name()` and `category()` to inspect codepoints one by one |

**2. Pick the right normalization form**

- `NFC` — canonical composition. Default choice for storage/comparison/general use.
- `NFD` — canonical decomposition. Use before stripping accents or doing per-character analysis.
- `NFKC` / `NFKD` — compatibility forms. Use when visually/semantically equivalent but differently-encoded characters (full-width "Ａ" vs "A", ligature "ﬁ" vs "fi") should be treated as the same. **Lossy** — don't use for round-tripping.

**3. Apply functions**

```python
unicodedata.lookup('LATIN SMALL LETTER A')   # 'a' — name to char
unicodedata.name(chr(0x1F600))               # char to name
unicodedata.category(c)                      # 'Lu','Ll','Nd','Zs','Cc', etc.
unicodedata.bidirectional(c)                 # 'L','R','AL','EN', etc.
unicodedata.combining(c)                     # canonical combining class (0 = not combining)
unicodedata.mirrored(c)                      # 1 if char is mirrored in bidi text
unicodedata.east_asian_width(c)              # 'W','Na','A','H','F','N'
unicodedata.decomposition(c)                 # raw decomposition mapping string
unicodedata.is_normalized('NFC', s)          # fast check without allocating result
```

## Examples

**Example 1: Strip accents/diacritics from text**
Input: `"café naïve"`
```python
def strip_accents(s):
    nfd = unicodedata.normalize('NFD', s)
    return ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')

strip_accents("café naïve")
```
Output: `"cafe naive"`

**Example 2: Compare user input for equality regardless of composition**
Input: `"e\u0301"` (e + combining acute accent) vs `"\u00e9"` (é precomposed)
```python
a, b = "e\u0301", "\u00e9"
a == b                                          # False
unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b)  # True
```
Output: `False` then `True`

**Example 3: Validate that a string is all decimal digits (including non-ASCII)**
Input: `"٣٤٥"` (Arabic-Indic digits)
```python
def all_decimal(s):
    try:
        return all(unicodedata.decimal(c) is not None for c in s)
    except ValueError:
        return False

[unicodedata.decimal(c) for c in "٣٤٥"]
```
Output: `[3, 4, 5]`

**Example 4: Inspect a mystery character for debugging**
Input: `'\u200b'` (appeared unexpectedly in scraped text)
```python
c = '\u200b'
unicodedata.name(c), unicodedata.category(c)
```
Output: `('ZERO WIDTH SPACE', 'Cf')` — reveals it's a formatting control char, explains invisible-but-present-length bugs.

## Best Practices

- **Normalize at input boundaries** (when reading files, receiving API/form data) rather than scattering normalization calls throughout code.
- **Use NFC for storage and comparison** by default; it's the most compact and widely expected form.
- **Use NFKC for search/matching** where visual equivalence matters more than exact representation (e.g., full-width Japanese input).
- **Category `Mn`** = "Mark, nonspacing" — the standard way to identify combining accent marks for stripping.
- **Always provide a default to `decimal()`/`digit()`/`numeric()`** (e.g., `unicodedata.decimal(c, None)`) instead of catching `ValueError` everywhere.
- **Use `is_normalized()`** to skip unnecessary work when checking already-normalized strings at scale.
- Remember `unicodedata` reflects a specific **Unicode version** (check `unicodedata.unidata_version`); behavior can shift slightly across Python versions as the database updates.

## Common Pitfalls

- **Comparing strings without normalizing first** — visually identical strings from different sources (macOS filesystem NFD vs. web input NFC) will silently fail `==`.
- **Using NFKC/NFKD for data you need to round-trip** — these are lossy; a full-width "Ａ" becomes ASCII "A" and you can't get it back.
- **Assuming `len(s)` equals visual character count** — combining marks, ZWJ emoji sequences, and surrogate-adjacent codepoints break this assumption; `unicodedata` alone won't group grapheme clusters (that needs a grapheme-segmentation library).
- **Forgetting `category()` returns a 2-letter code**, not a human-readable label — e.g. `'Zs'` is "Separator, space", not obvious without a lookup table.
- **Not handling unassigned codepoints** — `name()` raises `ValueError` for characters without an assigned name; always catch or provide a default.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: applying-stringprep
description: Applies the deprecated stringprep protocol (RFC 3454) for preparing Unicode strings before comparison, using character tables to map, prohibit, or check bidirectional text. Use when working with legacy protocols requiring stringprep (e.g., old SASL, XMPP, or Nameprep/IDNA implementations) or when maintaining code that imports Python's `stringprep` module.
---

## Quick Start

```python
import stringprep
import unicodedata

def prepare_string(s, mapping_table=stringprep.b1_set):
    """Apply basic stringprep steps: map, then check prohibited chars."""
    # Step 1: Mapping - remove characters mapped to nothing (B.1)
    chars = [c for c in s if c not in mapping_table]

    # Step 2: Normalize (KC form, per RFC 3454 profiles like Nameprep)
    normalized = unicodedata.normalize('NFKC', ''.join(chars))

    # Step 3: Prohibit check
    for c in normalized:
        if stringprep.in_table_c12(c):  # Non-ASCII space
            raise ValueError(f"Prohibited character: {c!r}")

    return normalized

print(prepare_string("Hello\u00ad World"))  # soft hyphen (B.1) is stripped
```

**Note:** `stringprep` is deprecated (removal planned per PEP 594-style cleanup for legacy protocol modules). Only use it for interoperability with existing systems; do not build new protocols on it. Prefer modern Unicode normalization (`unicodedata`, IDNA via `encodings.idna` or the third-party `idna` package) for anything new.

## Workflow

Stringprep implements RFC 3454's generic framework. A concrete profile (e.g., Nameprep, SASLprep) picks specific tables/operations from this toolkit. To implement or verify a profile:

Progress:
- [ ] Step 1: Identify the profile spec (Nameprep RFC 3491, SASLprep RFC 4013, etc.) and which tables it references
- [ ] Step 2: Apply the **mapping** step using the relevant `in_table_*` functions that indicate "map to nothing" or "map to space"
- [ ] Step 3: Apply **normalization** (usually NFKC) if the profile requires it
- [ ] Step 4: Run the **prohibited output** check — reject strings containing characters in prohibited tables
- [ ] Step 5: Run the **bidirectional (BiDi) check** — enforce RFC 3454 Section 6 rules on RandALCat/LCat mixing
- [ ] Step 6: Return the prepared string, or raise/report the specific violation

### Key table functions

| Function | Meaning |
|---|---|
| `in_table_a1(c)` | Unassigned code points |
| `in_table_b1(c)` | Commonly mapped to nothing (soft hyphen, zero-width chars) |
| `in_table_b2/b3` | Case-folding mapping tables |
| `in_table_c11`–`c22` | Prohibited character categories (spaces, control chars, private use, surrogates, tagging chars) |
| `in_table_c6`–`c9` | Prohibited: unassigned, inappropriate for canonical rep, tagging, change display/deprecated |
| `in_table_d1(c)` | RandALCat (right-to-left) characters |
| `in_table_d2(c)` | LCat (left-to-right) characters |

## Examples

**Example 1: Nameprep-style prohibited check**
Input: `"us\u200der"` (contains zero-width non-joiner, table B.1)
Output: After mapping step strips B.1 chars → `"user"`. Passes prohibited-check (no C.1–C.9 chars remain).

**Example 2: BiDi violation**
Input: `"abc\u05D0"` (Latin followed by Hebrew aleph, a RandALCat char)
Output: Raises — RFC 3454 Section 6 requires a string containing RandALCat chars to *only* contain RandALCat/LCat consistently (a string can't mix L and R categories per the BiDi rule); implementation must call `in_table_d1`/`in_table_d2` and reject mixed-directionality strings that violate the rule.

**Example 3: Full SASLprep-like pipeline**
Input: `"I\u00adX"` (contains soft hyphen)
Output: Map step removes `\u00ad` (in `b1_set`) → `"IX"` → NFKC normalize (no change) → prohibited/BiDi checks pass → final: `"IX"`

## Best Practices

- Always apply mapping **before** normalization **before** prohibition/BiDi checks — order matters per RFC 3454.
- Use `unicodedata.normalize('NFKC', s)` for the normalization step unless the profile specifies otherwise.
- Implement the BiDi rule explicitly — it's easy to skip: if any character satisfies `in_table_d1` (RandALCat), the string must not contain `in_table_d2` (LCat) at all, and must start and end with a RandALCat character.
- Cache/memoize `in_table_*` checks in hot paths — they're pure functions over Unicode data and safe to precompute per-input-string.
- When implementing SASLprep specifically, remember it forbids unassigned code points outright (table A.1) rather than allowing them.

## Common Pitfalls

- **Don't use `stringprep` for new protocol design.** It's deprecated; modern designs use `PRECIS` (RFC 8264) instead.
- **Don't skip the BiDi check** — many implementations only do mapping + prohibition and silently produce RFC-non-compliant results.
- **Don't apply NFC when the profile calls for NFKC** (or vice versa) — Nameprep/SASLprep specifically require NFKC for compatibility folding.
- **Don't assume `in_table_b1` characters are prohibited** — they're mapped to nothing (deleted), not rejected.
- **Don't forget** `stringprep` operates per-character; you must loop over code points, not bytes — always work on properly decoded `str` objects, never raw bytes.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: implementing-readline-features
description: Implements interactive line-editing, history, and tab-completion for Python CLI tools using the readline module. Use when building REPLs, interactive shells, or CLI prompts that need command history, tab completion, or emacs/vi-style line editing.
---

# Implementing Readline Features

## Quick Start

```python
import readline
import atexit
import os

histfile = os.path.join(os.path.expanduser("~"), ".myapp_history")

try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

def completer(text, state):
    options = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    return options[state] if state < len(options) else None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while True:
    line = input("myapp> ")
    if line == "quit":
        break
```

Note: `readline` is POSIX-only (Unix/macOS). On Windows, use `pyreadline3` as a drop-in substitute, guarded by a try/except import.

## Workflow

Progress:
- [ ] Determine platform support (wrap import in try/except for Windows)
- [ ] Set up history persistence (load on start, save on exit)
- [ ] Implement a completer function if tab-completion is needed
- [ ] Bind completer with `parse_and_bind`
- [ ] Configure delimiters if completing paths/dotted names
- [ ] Test interactively — history navigation (up/down), tab completion, Ctrl-R search

### 1. Cross-platform import guard

```python
try:
    import readline
except ImportError:
    readline = None  # Windows fallback; input() still works, just without history/completion
```

### 2. History management

```python
histfile = os.path.expanduser("~/.myapp_history")
try:
    readline.read_history_file(histfile)
except (FileNotFoundError, PermissionError):
    pass
readline.set_history_length(1000)
atexit.register(readline.write_history_file, histfile)
```

Use `readline.append_history_file(nlines, filename)` for multi-session apps that shouldn't overwrite others' entries.

### 3. Writing a completer

A completer is called repeatedly with increasing `state` (0, 1, 2, ...) until it returns `None`.

```python
def make_completer(options):
    def completer(text, state):
        matches = [o for o in options if o.startswith(text)]
        try:
            return matches[state]
        except IndexError:
            return None
    return completer

readline.set_completer(make_completer(["get", "set", "list", "quit"]))
readline.parse_and_bind("tab: complete")
```

For hierarchical completion (subcommands, file paths), inspect `readline.get_line_buffer()` inside the completer to determine context.

### 4. Delimiters for completion

```python
# Default includes many punctuation chars; narrow it for path-like completion
readline.set_completer_delims(' \t\n')
```

### 5. Key bindings

```python
readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")   # or "emacs" (default)
readline.parse_and_bind('"\e[A": history-search-backward')
```

## Examples

**Example 1: Filename completion**
Input: User types `open ./sr<TAB>` in a custom shell.
Output:
```python
import glob

def path_completer(text, state):
    matches = glob.glob(text + '*')
    return matches[state] if state < len(matches) else None

readline.set_completer_delims(' \t\n/')
readline.set_completer(path_completer)
readline.parse_and_bind("tab: complete")
```

**Example 2: Persistent history across sessions**
Input: App needs history preserved between runs, capped at 500 entries.
Output:
```python
histfile = os.path.expanduser("~/.app_history")
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    open(histfile, 'wb').close()
readline.set_history_length(500)
atexit.register(readline.write_history_file, histfile)
```

## Best Practices

- Always guard history file I/O with try/except (`FileNotFoundError`, `PermissionError`).
- Keep completer functions pure and fast — they're called on every keystroke-tab.
- Cache expensive completion candidate lists (e.g., don't re-scan the filesystem on every `state=0` call if avoidable).
- Use `readline.set_pre_input_hook()` sparingly — it's rarely needed and can cause subtle bugs.
- Prefer `parse_and_bind` strings over deprecated individual binding functions for portability with inputrc-style config.
- On libedit-based systems (macOS default Python builds historically), check `readline.backend` (3.13+) or `"libedit" in readline.__doc__` to adjust binding syntax, since libedit uses a different config format than GNU readline.

## Common Pitfalls

- **Assuming readline is available everywhere**: it's absent on stock Windows Python; always import-guard it.
- **Forgetting `state` semantics**: a completer must return `None` once exhausted, not raise or loop forever.
- **Not deduplicating completions**: if multiple sources match the same string, users see duplicate tab-cycling entries — dedupe before returning.
- **Overwriting shared history files**: use `append_history_file` instead of `write_history_file` when multiple concurrent sessions write to the same file.
- **Ignoring the libedit/GNU readline binding syntax difference** on macOS, leading to bindings silently not working.
- **Blocking in the completer**: network calls or slow I/O inside a completer freezes the prompt on every tab press.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: implementing-tab-completion
description: Implements Python readline tab-completion for interactive interpreters using the rlcompleter module. Use when building REPLs, custom interactive shells, or adding attribute/identifier completion to Python's interactive console.
---

## Quick Start

```python
import readline
import rlcompleter

readline.parse_and_bind("tab: complete")
```

That's it for the standard interactive interpreter case—`rlcompleter.Completer` binds against the `__main__` namespace by default when used this way (as `python -m` startup does via `site.py` / `PYTHONSTARTUP`).

## Workflow

Progress:
- [ ] Step 1: Decide the namespace to complete against (global `__main__` vs. a custom dict/namespace)
- [ ] Step 2: Instantiate `rlcompleter.Completer` (optionally with a namespace)
- [ ] Step 3: Register the completer with `readline.set_completer`
- [ ] Step 4: Bind the Tab key via `readline.parse_and_bind`
- [ ] Step 5: Test simple identifier completion and dotted attribute completion

### Step 1–4: Custom namespace example

```python
import readline
import rlcompleter

namespace = {"foo": 42, "bar": "hello"}
completer = rlcompleter.Completer(namespace)

readline.set_completer(completer.complete)
readline.parse_and_bind("tab: complete")
```

### Step 5: How completion resolves

- `complete(text, state)` is called repeatedly by readline with increasing `state` (0, 1, 2...) until it returns `None`.
- No dot in `text` → matches keywords, builtins, and names in the namespace.
- Dot in `text` (e.g. `"foo.up"`) → evaluates the expression before the last dot using `eval()` in the namespace, then completes attributes via `dir()`. **This means completion can execute arbitrary code** (property getters, `__getattr__`, etc.).

## Examples

**Example 1: Default interactive interpreter setup**
Input: Add tab completion to a script meant to be run with `python -i myscript.py`
Output:
```python
try:
    import readline
except ImportError:
    pass
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
```

**Example 2: Completion inside a sandboxed REPL**
Input: Build a mini-REPL that only completes names from a restricted namespace, not `__main__`
Output:
```python
import readline, rlcompleter

sandbox_ns = {"__builtins__": {}, "x": [1, 2, 3]}
completer = rlcompleter.Completer(sandbox_ns)
readline.set_completer(completer.complete)
readline.parse_and_bind("tab: complete")

while True:
    line = input(">>> ")
    exec(line, sandbox_ns)
```

**Example 3: Inspecting raw completion matches (non-interactive/testing)**
Input: Programmatically get completions for `"li"` and `"str.up"`
Output:
```python
c = rlcompleter.Completer({"list": list})
i = 0
matches = []
while True:
    m = c.complete("li", i)
    if m is None:
        break
    matches.append(m)
    i += 1
# matches -> ['list(', 'list.']  (exact strings vary by Python version)

i, attr_matches = 0, []
while True:
    m = c.complete("str.up", i)
    if m is None:
        break
    attr_matches.append(m)
    i += 1
# attr_matches -> ['str.upper(']
```

## Best Practices

- Guard `import readline` in `try/except ImportError` — it's not available on Windows without `pyreadline3` or similar.
- Prefer letting `rlcompleter` default to `__main__.__dict__` for general-purpose interactive tools; only pass a custom namespace when you need isolation.
- Combine with `atexit` + `readline.write_history_file` for a complete REPL experience (history + completion).
- Use `readline.set_completer_delims()` if you need to tweak which characters break "words" for completion (defaults exclude `.` handling specially inside `rlcompleter` itself).
- Remember completion for dotted names calls `eval()` — only wire this up against namespaces where arbitrary attribute access/property evaluation is acceptable.

## Common Pitfalls

- **Forgetting `parse_and_bind`**: instantiating `Completer` and calling `set_completer` alone does nothing until Tab is bound.
- **Assuming safety**: `rlcompleter` evaluates expressions to resolve attributes on tab-press, which can trigger side effects (e.g., `@property` methods with side effects, `__getattr__` doing I/O). Never expose this against untrusted/attacker-controlled namespaces.
- **Platform assumption**: assuming `readline` is always importable; it's absent by default on Windows.
- **Confusing module scope**: passing a *copy* of a namespace expecting live updates — `Completer` holds a reference to the dict, so mutating the original dict is fine, but replacing it wholesale is not reflected unless you re-instantiate or use a `Completer` with no namespace and rely on `__main__`.
- **State parameter misuse**: manually calling `complete(text, state)`, forgetting that `state` must increment from 0 and stop at the first `None`, not stop at empty string.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---