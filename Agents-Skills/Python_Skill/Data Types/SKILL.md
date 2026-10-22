---
name: working-with-python-datatypes
description: Provides guidance on Python's built-in and standard library data types including datetime, calendar, collections, array, enum, and related modules. Use when choosing or working with Python data structures, handling dates/times, working with enumerations, or manipulating specialized collections.
---

## Quick Start

```python
from datetime import datetime, date, timedelta
from collections import defaultdict, Counter, namedtuple
from enum import Enum, auto

# Common patterns
now = datetime.now()
tomorrow = date.today() + timedelta(days=1)

counts = Counter(["a", "b", "a"])  # Counter({'a': 2, 'b': 1})

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

class Color(Enum):
    RED = auto()
    GREEN = auto()
```

## Workflow

1. **Identify the need**: dates/times, structured records, counting/grouping, fixed sets of constants, or memory-efficient sequences.
2. **Pick the right module/type** (see decision table below).
3. **Check mutability requirements** — use `namedtuple`/`dataclass` for immutable records, plain classes or dicts for mutable state.
4. **Consider performance** — `array` for homogeneous numeric data, `deque` for queue-like operations, `set`/`frozenset` for membership tests.
5. **Verify timezone handling** for datetime — always prefer timezone-aware objects (`datetime.now(timezone.utc)`) over naive ones in production code.

Progress checklist for a data-modeling task:
- [ ] Determine if data is temporal, categorical, or collection-based
- [ ] Choose the specific type/module
- [ ] Handle edge cases (timezones, empty collections, enum uniqueness)
- [ ] Add type hints referencing the chosen types

## Decision Table

| Need | Use |
|---|---|
| Calendar dates only | `datetime.date` |
| Date + time | `datetime.datetime` |
| Time deltas/arithmetic | `datetime.timedelta` |
| Timezone-aware time | `datetime.timezone`, `zoneinfo.ZoneInfo` |
| Month/year calendar utilities | `calendar` module |
| Fixed set of named constants | `enum.Enum` / `enum.IntEnum` / `enum.Flag` |
| Bitwise combinable flags | `enum.Flag` or `enum.IntFlag` |
| Fast counting | `collections.Counter` |
| Default values on missing keys | `collections.defaultdict` |
| Ordered key-value with move-to-end | `collections.OrderedDict` |
| Lightweight immutable record | `collections.namedtuple` or `typing.NamedTuple` |
| Double-ended queue | `collections.deque` |
| Compact numeric arrays | `array.array` |
| Fast membership/uniqueness | `set` / `frozenset` |
| Weak references to avoid leaks | `weakref` |
| Sortable priority structures | `heapq` with lists |
| Copy semantics (shallow/deep) | `copy.copy` / `copy.deepcopy` |

## Examples

**Example 1:**
Input: Need to count word frequency in a list of strings.
Output:
```python
from collections import Counter
freq = Counter(words)
freq.most_common(3)  # top 3 words
```

**Example 2:**
Input: Need an immutable, lightweight coordinate object with named fields.
Output:
```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(1.0, 2.0)
```

**Example 3:**
Input: Need a set of mutually exclusive status constants with string values for logging.
Output:
```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    DONE = "done"

print(Status.ACTIVE.value)  # "active"
```

**Example 4:**
Input: Need to compute the date 90 days from now, timezone-aware.
Output:
```python
from datetime import datetime, timedelta, timezone

future = datetime.now(timezone.utc) + timedelta(days=90)
```

## Best Practices

- Always use timezone-aware `datetime` objects (`timezone.utc` or `zoneinfo.ZoneInfo`) rather than naive datetimes to avoid ambiguity across systems.
- Prefer `enum.Enum` over plain string/int constants for closed sets of values — it gives type safety and IDE support.
- Use `collections.namedtuple`/`NamedTuple` or `dataclasses.dataclass(frozen=True)` instead of raw tuples/dicts for structured, self-documenting data.
- Use `defaultdict` instead of manually checking `if key not in dict`.
- Prefer `deque` over `list` for queue/stack operations requiring O(1) appends/pops from both ends.
- Use `array.array` only when memory efficiency for large homogeneous numeric data matters; otherwise a `list` is simpler.

## Common Pitfalls

- Don't use naive `datetime` objects when comparing across timezones — this silently produces wrong results.
- Don't mutate a `namedtuple` — it's immutable by design; use `._replace()` to create a modified copy.
- Don't use `list` for frequent front-insertion/removal — it's O(n); use `deque`.
- Don't compare `Enum` members by value equality when identity (`is`) comparisons are expected — use `is` for enum members.
- Don't forget that `IntEnum`/`IntFlag` members compare equal to plain ints, which can hide bugs if strict typing is desired — prefer plain `Enum` unless int compatibility is required.
- Don't deep-copy objects containing unpicklable resources (file handles, sockets) — implement `__deepcopy__` explicitly if needed.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: working-with-datetime
description: Provides guidance on Python's datetime module for creating, manipulating, formatting, and comparing dates, times, and timedeltas. Use when writing code that handles dates, times, timezones, or durations in Python.
---

## Quick Start

```python
from datetime import datetime, date, time, timedelta, timezone

# Current date/time
now = datetime.now()
today = date.today()

# Create specific date/time
dt = datetime(2024, 3, 15, 14, 30, 0)

# Timezone-aware datetime (preferred over naive)
utc_now = datetime.now(timezone.utc)

# Parse a string into datetime
dt = datetime.strptime("2024-03-15", "%Y-%m-%d")

# Format a datetime into a string
dt.strftime("%Y-%m-%d %H:%M:%S")  # "2024-03-15 14:30:00"

# ISO format (preferred for parsing/serialization)
dt.isoformat()                       # "2024-03-15T14:30:00"
datetime.fromisoformat("2024-03-15T14:30:00")

# Arithmetic with timedelta
tomorrow = today + timedelta(days=1)
diff = dt2 - dt1  # returns timedelta
```

## Workflow

Progress checklist for date/time handling tasks:

- [ ] Decide if you need `date`, `time`, `datetime`, or `timedelta`
- [ ] Decide naive vs. timezone-aware (default to aware for anything crossing systems)
- [ ] Choose parsing method (`strptime`, `fromisoformat`, or third-party if formats vary)
- [ ] Perform arithmetic/comparisons using `timedelta`
- [ ] Format output with `strftime` or `isoformat`
- [ ] Test edge cases: DST transitions, leap years, month/year boundaries

### 1. Choose the right type
- `date`: calendar date only (year, month, day)
- `time`: time of day only (hour, minute, second, microsecond, tzinfo)
- `datetime`: combination of both — use this for almost everything
- `timedelta`: duration/difference between two dates or times

### 2. Naive vs. aware
Naive objects have no `tzinfo` — never compare naive and aware datetimes (raises `TypeError`). Always attach a timezone when the value will be stored, transmitted, or compared across systems:

```python
from datetime import timezone, timedelta

# UTC
dt = datetime.now(timezone.utc)

# Fixed offset
tz = timezone(timedelta(hours=-5))
dt = datetime.now(tz)

# Full IANA timezone support (Python 3.9+)
from zoneinfo import ZoneInfo
dt = datetime.now(ZoneInfo("America/New_York"))
```

### 3. Parsing input
- Known fixed format → `strptime(s, fmt)`
- ISO 8601 string → `datetime.fromisoformat(s)` (handles most ISO variants natively in modern Python)
- Unix timestamp → `datetime.fromtimestamp(ts, tz=timezone.utc)`

### 4. Arithmetic and comparison
```python
delta = timedelta(weeks=1, days=2, hours=3)
future = now + delta
diff = future - now          # timedelta
diff.total_seconds()         # float seconds

# Comparisons work directly
if dt1 < dt2:
    ...
```

### 5. Formatting output
```python
dt.strftime("%A, %B %d, %Y")   # "Friday, March 15, 2024"
dt.isoformat(timespec="seconds")
```

## Examples

**Example 1: Parse and reformat a date string**
Input: `"2024-03-15"` needs to become `"March 15, 2024"`
Output:
```python
dt = datetime.strptime("2024-03-15", "%Y-%m-%d")
dt.strftime("%B %d, %Y")  # "March 15, 2024"
```

**Example 2: Compute age in days between two dates**
Input: `date(1990, 5, 20)` and `date.today()`
Output:
```python
delta = date.today() - date(1990, 5, 20)
delta.days  # integer number of days
```

**Example 3: Convert a UTC timestamp to a local timezone**
Input: Unix timestamp `1710512400`, target zone `"Europe/Berlin"`
Output:
```python
from zoneinfo import ZoneInfo
dt_utc = datetime.fromtimestamp(1710512400, tz=timezone.utc)
dt_local = dt_utc.astimezone(ZoneInfo("Europe/Berlin"))
```

**Example 4: Add 30 business-agnostic days to a deadline**
Input: `datetime(2024, 1, 1)`, add 30 days
Output:
```python
deadline = datetime(2024, 1, 1) + timedelta(days=30)  # datetime(2024, 1, 31)
```

## Best Practices

- Default to timezone-aware datetimes (`timezone.utc` or `zoneinfo.ZoneInfo`) for anything persisted or shared.
- Use `datetime.fromisoformat`/`.isoformat()` for serialization instead of custom string formats — it round-trips cleanly.
- Store datetimes in UTC; convert to local timezone only for display.
- Use `timedelta` for durations rather than manually computing seconds/days.
- Prefer `zoneinfo` (stdlib, Python 3.9+) over `pytz` for timezone handling in new code.
- Use `total_seconds()` when you need a numeric duration from a `timedelta`, not `.seconds` (which discards days).

## Common Pitfalls

- Comparing or subtracting a naive and an aware datetime — raises `TypeError`.
- Using `datetime.utcnow()` — deprecated; it returns a naive datetime despite the name. Use `datetime.now(timezone.utc)` instead.
- Assuming `timedelta.seconds` gives total duration — it only gives the seconds component; use `total_seconds()`.
- Manually applying fixed UTC offsets for timezones that observe DST — use `zoneinfo` instead of hardcoded offsets.
- Forgetting that `%z`/`%Z` in `strptime` require the input string to actually contain offset/timezone info.
- Mutating date/time objects — they are immutable; arithmetic always returns new objects.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: handling-timezone-aware-datetimes
description: Applies IANA timezone data correctly using Python's zoneinfo module, including DST transitions, ambiguous/imaginary times, and cross-platform tzdata handling. Use when working with timezone-aware datetimes, converting between timezones, scheduling recurring events across DST boundaries, or debugging off-by-one-hour bugs.
---

# Handling Timezone-Aware Datetimes

## Quick Start

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Always construct timezone-aware datetimes with ZoneInfo
dt = datetime(2024, 11, 3, 1, 30, tzinfo=ZoneInfo("America/New_York"))
print(dt)  # 2024-11-03 01:30:00-04:00 (or -05:00 depending on fold)

# Convert between timezones
utc_dt = dt.astimezone(ZoneInfo("UTC"))

# Get current time in a zone
now = datetime.now(ZoneInfo("Europe/London"))
```

Never use `pytz`-style `localize()` patterns or naive `datetime.replace(tzinfo=...)` for arithmetic-sensitive code — `zoneinfo` uses PEP 495 `fold` instead.

## Workflow

Progress:
- [ ] Identify whether the datetime is a fixed instant (use UTC/`ZoneInfo("UTC")`) or a "wall clock" time in a location (use IANA zone key)
- [ ] Construct with `ZoneInfo(key)` passed directly to `tzinfo=`, never via `.replace()` after the fact for DST-sensitive calculations
- [ ] Check for ambiguous/imaginary times if the datetime falls near a DST transition
- [ ] Convert with `.astimezone()`, not manual offset math
- [ ] Verify tzdata source (system tz database vs `tzdata` pip package) for deployment consistency
- [ ] Cache `ZoneInfo` instances if creating many (they're already cached internally per-process, but be aware of `zoneinfo.reset_tzpath()` invalidation)

## Key Concepts

**Zone keys** are IANA names like `"America/New_York"`, `"Asia/Kolkata"`, `"Etc/UTC"` — never use fixed abbreviations like `"EST"` (ambiguous and not DST-aware).

**Ambiguous times**: when clocks fall back, a wall-clock time occurs twice.
```python
from zoneinfo import ZoneInfo
from datetime import datetime

# 1:30 AM on Nov 3, 2024 occurs twice in America/New_York
dt1 = datetime(2024, 11, 3, 1, 30, tzinfo=ZoneInfo("America/New_York"), fold=0)  # first occurrence (EDT, -04:00)
dt2 = datetime(2024, 11, 3, 1, 30, tzinfo=ZoneInfo("America/New_York"), fold=1)  # second occurrence (EST, -05:00)
```

**Imaginary times**: when clocks spring forward, some wall-clock times never occur.
```python
# 2:30 AM on Mar 10, 2024 doesn't exist in America/New_York (clocks jump 2:00 -> 3:00)
dt = datetime(2024, 3, 10, 2, 30, tzinfo=ZoneInfo("America/New_York"))
# zoneinfo will still produce a result, silently treating it per the `fold` rule —
# never assume such a datetime is "real"; validate against transition boundaries
# if imaginary times must be rejected
```

**Arithmetic pitfall**: adding a `timedelta` to a timezone-aware datetime does *wall-clock* arithmetic, not absolute-time arithmetic. To do correct elapsed-time math across a DST boundary, convert to UTC first.
```python
start = datetime(2024, 3, 9, 12, 0, tzinfo=ZoneInfo("America/New_York"))
end = start + timedelta(days=1)  # naive: assumes 24 real hours passed — WRONG across DST
correct_end = (start.astimezone(ZoneInfo("UTC")) + timedelta(days=1)).astimezone(ZoneInfo("America/New_York"))
```

## Examples

**Example 1:**
Input: Schedule a recurring 9 AM meeting in `Europe/Berlin` for the next 5 days, storing as UTC for a database.
Output:
```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

berlin = ZoneInfo("Europe/Berlin")
utc = ZoneInfo("UTC")

meetings_utc = []
base_date = datetime(2024, 3, 29, 9, 0, tzinfo=berlin)
for i in range(5):
    local_dt = base_date.replace(day=base_date.day + i) if False else \
        datetime(2024, 3, 29 + i, 9, 0, tzinfo=berlin)
    meetings_utc.append(local_dt.astimezone(utc))
# Result correctly reflects the DST jump on Mar 31 (Berlin springs forward)
```

**Example 2:**
Input: A user reports their app shows the wrong time exactly during DST changeover in `America/Sao_Paulo`.
Output: Check if the datetime is ambiguous or imaginary by comparing UTC offsets before/after:
```python
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

tz = ZoneInfo("America/Sao_Paulo")
dt = datetime(2019, 2, 16, 23, 30, tzinfo=tz)
offset_before = dt.utcoffset()
offset_after = (dt + timedelta(hours=1)).utcoffset()
if offset_before != offset_after:
    # near a transition — use fold to disambiguate, or reject if imaginary
    pass
```

**Example 3:**
Input: Deploying to a minimal Docker container that lacks `/usr/share/zoneinfo`.
Output: Add the `tzdata` package (`pip install tzdata`) as a dependency — `zoneinfo` falls back to it automatically when the system tz database is unavailable. Don't hardcode paths; let `zoneinfo` handle source resolution.

## Best Practices

- Store instants in UTC; store local wall-clock intent (e.g., "9 AM every day") with the IANA key separately, and compute UTC at read time — this correctly handles future DST rule changes.
- Always pass `ZoneInfo` via `tzinfo=` at construction time; avoid `.replace(tzinfo=...)` for anything that will do date arithmetic.
- Use `.astimezone()` for conversions, never manual UTC-offset math.
- Depend on the `tzdata` PyPI package explicitly for portability (Windows has no system tz database at all).
- Use `zoneinfo.available_timezones()` to validate user-supplied zone keys before construction.

## Common Pitfalls

- Using deprecated 3-letter abbreviations (`"EST"`, `"PST"`) — not supported as zone keys and inherently ambiguous.
- Assuming `timedelta` arithmetic on aware datetimes is DST-safe — it's wall-clock arithmetic, not elapsed real-time.
- Forgetting `fold` when a wall-clock time is ambiguous — default `fold=0` picks the first (earlier UTC offset in a fall-back) occurrence, which may not be what's intended.
- Mixing `pytz` and `zoneinfo` in the same codebase — `pytz` requires `localize()`/`normalize()` idioms incompatible with `zoneinfo`'s PEP 495 model.
- Not bundling `tzdata` for environments without a system timezone database (bare containers, Windows) — leads to `ZoneInfoNotFoundError` in production only.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: working-with-calendar-module
description: Provides guidance on using Python's calendar module to generate, format, and manipulate calendar data programmatically. Use when working with month/year calendars, calculating weekdays, handling leap years, generating HTML/text calendar output, or building date-related utilities in Python.
---

# Working with Python's calendar Module

## Quick Start

```python
import calendar

# Print a text calendar for a month
print(calendar.month(2024, 3))

# Print a full year calendar
print(calendar.calendar(2024))

# Check leap year
calendar.isleap(2024)  # True

# Get weekday of a specific date (0=Monday)
calendar.weekday(2024, 3, 15)  # Friday -> 4

# Get (first_weekday, number_of_days) for a month
calendar.monthrange(2024, 2)  # (3, 29) -> Feb 2024 starts Thu, has 29 days
```

## Workflow

Progress:
- [ ] Step 1: Decide output format needed (text, HTML, or raw data structures)
- [ ] Step 2: Choose the right class/function (`Calendar`, `TextCalendar`, `HTMLCalendar`, or module-level convenience functions)
- [ ] Step 3: Set locale/first-weekday if non-default behavior required
- [ ] Step 4: Generate data (iterators for weeks/months/years, or formatted strings)
- [ ] Step 5: Post-process output (e.g., strip empty days marked `0`, style HTML)

### Choosing the right tool

- **Quick print/debug** → `calendar.month(year, month)`, `calendar.calendar(year)`
- **Iterate raw day numbers** (0 = day outside month) → `Calendar.itermonthdays()`
- **Iterate `(day, weekday)` tuples** → `Calendar.itermonthdays2()`
- **Iterate actual `datetime.date` objects** → `Calendar.itermonthdates()` (note: can spill into adjacent years at Dec/Jan boundaries)
- **Group days into weeks** → `Calendar.monthdayscalendar()` / `monthdatescalendar()`
- **HTML output** → `HTMLCalendar` class, `formatmonth()`/`formatyear()`
- **Locale-specific names** → `LocaleTextCalendar` / `LocaleHTMLCalendar`

### Setting the first day of the week

```python
c = calendar.Calendar(firstweekday=6)  # Sunday-first
calendar.setfirstweekday(calendar.SUNDAY)  # affects module-level functions globally
```

Default is Monday (`0`). Constants: `MONDAY`=0 ... `SUNDAY`=6.

## Examples

**Example 1: Get weeks of a month as date objects**

Input:
```python
import calendar
cal = calendar.Calendar()
list(cal.monthdatescalendar(2024, 2))
```
Output:
```python
[[datetime.date(2024, 1, 29), ..., datetime.date(2024, 2, 4)],
 [datetime.date(2024, 2, 5), ..., datetime.date(2024, 2, 11)],
 ...
 [datetime.date(2024, 2, 26), ..., datetime.date(2024, 3, 3)]]
```
Each inner list has exactly 7 dates; padding days come from adjacent months.

**Example 2: Generate an HTML calendar for a month**

Input:
```python
import calendar
hc = calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)
html = hc.formatmonth(2024, 12)
```
Output: A string of `<table class="month">...</table>` HTML with `<td class="mon">`, `<td class="noday">` for padding cells, etc. — ready to embed in a page or style with CSS classes (`month`, `year`, `noday`, `mon`, `tue`, ... , `sun`).

**Example 3: Count weekday occurrences in a month**

Input:
```python
calendar.monthrange(2024, 2)
```
Output:
```python
(3, 29)  # Feb 2024 starts on a Thursday (index 3), has 29 days
```
Use this to compute how many Mondays/Fridays/etc. occur in a month without iterating.

## Best Practices

- Prefer `Calendar` iterator methods over string parsing of `calendar.month()`/`calendar.calendar()` output when you need structured data — the text output is for display only.
- Use `itermonthdates()` cautiously: it can raise `OverflowError` near `datetime.MAXYEAR`/`MINYEAR` boundaries since it includes adjacent-month dates. Use `itermonthdays()` (plain ints, `0` = padding) if you need to avoid date-range edge cases.
- Use `calendar.isleap(year)` and `calendar.leapdays(y1, y2)` rather than reimplementing leap-year math.
- For locale-aware month/day names, use `LocaleTextCalendar`/`LocaleHTMLCalendar` with a `(locale, encoding)` tuple, or the module-level `calendar.month_name`/`calendar.day_name` arrays (locale-independent, English by default).
- Remember `month_name` and `day_name` are 1-indexed for months (`month_name[0]` is `''`) but `day_name` is 0-indexed starting Monday.
- For CLI-style output, `python -m calendar 2024` works directly from the command line — useful for quick checks without writing a script.

## Common Pitfalls

- **Assuming week lists always belong to the queried month** — `monthdatescalendar`/`monthdayscalendar` pad with adjacent-month days (represented as `0` in the days variant); filter these out if you only want the target month.
- **Confusing `weekday()` (needs date) with `firstweekday()` (calendar setting)** — `calendar.weekday(y, m, d)` returns which day of week a specific date falls on; `Calendar.getfirstweekday()` returns the configured start-of-week for layout purposes.
- **Forgetting `setfirstweekday()` is global/stateful** for module-level functions — prefer instantiating your own `Calendar`/`TextCalendar`/`HTMLCalendar` object with `firstweekday` set explicitly to avoid side effects across code that shares the module.
- **Mixing up month indices** — `calendar` months are 1–12 (no month 0), unlike some other date libraries.
- **Using `calendar.calendar()`/`month()` for programmatic parsing** — these produce human-formatted strings with locale-dependent spacing; use the iterator/data methods instead.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-collections-module
description: Provides guidance on Python's collections module for specialized container datatypes (namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict/List/String). Use when working with counting/frequency tasks, need efficient queue/stack operations, want named field access on tuples, need multi-dict lookups, or require dict/list subclassing.
---

## Quick Start

```python
from collections import namedtuple, deque, ChainMap, Counter, defaultdict, OrderedDict

# Named fields instead of index access
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)  # p.x == 1

# Fast appends/pops from both ends (O(1) vs list's O(n))
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()

# Frequency counting
c = Counter("abracadabra")
c.most_common(2)  # [('a', 5), ('b', 2)]

# Auto-initializing dict
d = defaultdict(list)
d['key'].append(1)  # no KeyError, no manual init
```

## Workflow

1. **Identify the access pattern** driving container choice:
   - Counting/tallying → `Counter`
   - Queue/stack/sliding window → `deque`
   - Tuple with named fields, immutable record → `namedtuple`
   - Layered/fallback lookups across multiple dicts → `ChainMap`
   - Need dict but with default values on missing key → `defaultdict`
   - Need insertion-order guarantees pre-3.7 or `move_to_end` → `OrderedDict` (note: plain `dict` is ordered since 3.7; use `OrderedDict` mainly for equality-by-order semantics or `move_to_end`)
   - Need to subclass dict/list/str behavior → `UserDict`/`UserList`/`UserString`

2. **Pick the right constructor/factory:**
   - `namedtuple(typename, field_names)` — supports `_asdict()`, `_replace()`, `_fields`, defaults via `defaults=` param
   - `deque(iterable, maxlen=N)` — `maxlen` gives a fixed-size rolling buffer
   - `Counter(iterable_or_mapping)` — supports `+`, `-`, `&`, `|` set-like operations
   - `defaultdict(default_factory)` — factory called with no args (e.g. `list`, `int`, `set`, or a `lambda`)
   - `ChainMap(*maps)` — writes go to first map only; use `new_child()` for scoped updates

3. **Use built-in methods over manual logic:**
   - `Counter.most_common(n)` instead of sorting manually
   - `deque.rotate(n)` instead of slicing tricks
   - `namedtuple._replace(**kwargs)` instead of rebuilding tuples
   - `ChainMap.maps` to inspect/reorder the underlying list of mappings

4. **Verify performance assumptions** — deque is O(1) at both ends but O(n) for random access (`dq[i]` is slow); use `list` if you need indexing-heavy access.

## Examples

**Example 1:**
Input: Track word frequency in a large text and get the top 5 words.
Output:
```python
from collections import Counter
words = text.lower().split()
Counter(words).most_common(5)
```

**Example 2:**
Input: Implement a sliding window of the last N items seen in a stream.
Output:
```python
from collections import deque
window = deque(maxlen=N)
for item in stream:
    window.append(item)  # oldest auto-evicted
```

**Example 3:**
Input: Build a config system where user settings override defaults override built-ins.
Output:
```python
from collections import ChainMap
config = ChainMap(user_settings, defaults, builtins)
config['theme']  # checks user_settings first, falls through
```

**Example 4:**
Input: Group a list of (key, value) pairs into a dict of lists without checking for key existence.
Output:
```python
from collections import defaultdict
grouped = defaultdict(list)
for k, v in pairs:
    grouped[k].append(v)
```

## Best Practices

- Prefer `Counter` arithmetic (`c1 - c2`, `c1 & c2`) over manual dict merging loops.
- Use `namedtuple(..., defaults=(...))` to avoid repetitive constructor calls when some fields are usually constant.
- For `defaultdict`, pick the factory to match desired zero-value: `int` → 0, `list` → [], `set` → set().
- Convert `OrderedDict` comparisons only when order matters for equality — plain dicts compare by content regardless of order.
- Use `ChainMap.new_child(m)` to push a temporary scope (e.g., for nested function contexts) rather than copying/merging dicts.
- When subclassing built-in types with extra invariants, prefer `UserDict`/`UserList`/`UserString` over subclassing `dict`/`list`/`str` directly — they avoid subtle bugs where built-in methods bypass overridden methods.

## Common Pitfalls

- Don't index into a `deque` in a hot loop — it's O(n); convert to `list` first if random access is needed repeatedly.
- Don't forget `Counter[missing_key]` returns 0 instead of raising `KeyError` — this can mask bugs when you actually wanted to detect missing keys.
- Don't mutate a `defaultdict`'s structure through membership checks (`if key in d`) after accidentally accessing `d[key]` — the access itself inserts the default value.
- Don't assume `ChainMap` writes propagate to all layers — `chainmap[key] = value` only ever modifies `chainmap.maps[0]`.
- Don't use mutable default factories carelessly, e.g. `defaultdict(lambda: [])` is fine, but sharing a single mutable object across keys (`defaultdict(lambda: shared_list)`) causes cross-key mutation bugs.
- Don't rely on `OrderedDict`-specific behavior when a plain `dict` suffices — added complexity without benefit in Python 3.7+.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: choosing-abstract-base-classes
description: Selects and applies appropriate collections.abc abstract base classes for type checking, custom container design, and duck-typing validation in Python. Use when designing custom collection classes, writing isinstance() checks against protocols like Iterable or Mapping, or deciding which abstract methods to implement for a container type.
---

## Quick Start

```python
from collections.abc import Mapping, Sequence, Iterable

# Duck-typing check: does obj behave like a mapping?
if isinstance(obj, Mapping):
    for key in obj:
        print(key, obj[key])

# Custom container: implement minimum methods, get the rest free
class FrozenDict(Mapping):
    def __init__(self, data):
        self._data = dict(data)
    def __getitem__(self, key):
        return self._data[key]
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    # __contains__, keys, items, values, get, __eq__, __ne__ come for free
```

## Workflow

Progress:
- [ ] Step 1: Identify what behavior is needed (iteration? indexing? mutation? hashing?)
- [ ] Step 2: Pick the narrowest ABC that matches (don't over-implement)
- [ ] Step 3: Check the ABC's "Abstract Methods" — implement only those
- [ ] Step 4: Check "Mixin Methods" — these come free from the abstract ones
- [ ] Step 5: Use `isinstance()`/`issubclass()` for duck-typing checks instead of concrete types
- [ ] Step 6: Register unrelated classes with `.register()` if virtual subclassing is needed

### Reference table (most-used ABCs)

| ABC | Abstract Methods | Inherits From | Use for |
|---|---|---|---|
| `Iterable` | `__iter__` | — | anything you can loop over |
| `Iterator` | `__next__` | `Iterable` | stateful iteration objects |
| `Container` | `__contains__` | — | `in` operator support |
| `Sized` | `__len__` | — | `len()` support |
| `Hashable` | `__hash__` | — | usable as dict key / set member |
| `Collection` | `__contains__`, `__iter__`, `__len__` | `Sized`, `Iterable`, `Container` | general-purpose container check |
| `Sequence` | `__getitem__`, `__len__` | `Reversible`, `Collection` | ordered, indexable (list-like) |
| `MutableSequence` | + `__setitem__`, `__delitem__`, `insert` | `Sequence` | mutable list-like |
| `Mapping` | `__getitem__`, `__iter__`, `__len__` | `Collection` | dict-like read access |
| `MutableMapping` | + `__setitem__`, `__delitem__` | `Mapping` | dict-like read/write |
| `Set` | `__contains__`, `__iter__`, `__len__` | `Collection` | set-like, supports `&`, `\|`, `-`, `^` |
| `MutableSet` | + `add`, `discard` | `Set` | mutable set-like |
| `Callable` | `__call__` | — | function-like objects |

## Examples

**Example 1:**
Input: "I need a class that supports `len()`, `in`, and iteration, but I don't need indexing or mutation."
Output: Inherit from `Collection` and implement `__contains__`, `__iter__`, `__len__`. Don't reach for `Sequence` — it forces `__getitem__` and implies order/indexing you don't need.

**Example 2:**
Input: "How do I check if a function argument is 'list-like' without requiring it to actually be a `list`?"
Output:
```python
from collections.abc import Sequence

def process(items):
    if not isinstance(items, Sequence):
        raise TypeError("items must be a Sequence")
    return items[0], len(items)
```
This accepts `tuple`, custom `Sequence` subclasses, etc., while rejecting `str` only if that's explicitly desired (note `str` *is* a `Sequence` — guard separately if needed).

**Example 3:**
Input: "Building a custom read-only set-like collection backed by a database query."
Output: Inherit from `Set`, implement `__contains__`, `__iter__`, `__len__`. Get `__le__`, `__lt__`, `__gt__`, `__ge__`, `__eq__`, `__and__`, `__or__`, `__sub__`, `__xor__`, `isdisjoint` for free.

## Best Practices

- **Implement the minimum abstract set; let mixins provide the rest.** Overriding a mixin method is fine if you have a faster implementation (e.g., custom `__contains__` for O(1) lookup backed by a hash index).
- **Prefer ABC checks over concrete type checks** (`isinstance(x, Mapping)` over `isinstance(x, dict)`) to support duck-typing and third-party implementations.
- **Use `Iterable`/`Iterator` distinction correctly**: an `Iterable` produces an `Iterator` via `__iter__`; don't conflate the two when type-checking.
- **Register virtual subclasses** when a class already satisfies the interface but can't/shouldn't inherit: `Sequence.register(MyExternalType)`.
- **Remember `str`, `bytes`, `range` are `Sequence`** — guard against accidentally treating strings as sequences of characters when you meant "list-like".
- For generic type hints, prefer `collections.abc` classes over `typing` equivalents (e.g., `collections.abc.Sequence[int]`) — `typing` aliases are deprecated in favor of these.

## Common Pitfalls

- **Don't implement `Mapping`/`Sequence` from scratch** — subclass the ABC and only fill abstract methods; reimplementing `keys()`, `items()`, `get()`, etc. manually is redundant and error-prone.
- **Don't use `Sequence` when you just need `Iterable`** — forcing `__getitem__`/`__len__` unnecessarily overconstrains simple generators/streams.
- **Don't forget `Hashable` immutability contract** — if you implement `__hash__`, ensure the object's hash-relevant state never changes after creation.
- **Don't check `isinstance(x, list)` for "list-like" duck typing** — this excludes valid alternative implementations; use `MutableSequence` or `Sequence`.
- **Don't assume `Set` mixins imply sorted order** — `Set` operations don't guarantee ordering; that's a `Sequence` concern.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-heapq-for-priority-queues
description: Implements heap-based priority queues and heap operations using Python's heapq module. Use when needing efficient smallest/largest element retrieval, priority queues, k-largest/k-smallest problems, merging sorted inputs, or scheduling algorithms.
---

## Quick Start

```python
import heapq

# Build a min-heap in place from a list
data = [5, 7, 9, 1, 3]
heapq.heapify(data)          # data is now heap-ordered, data[0] is smallest

heapq.heappush(data, 4)      # push new item, maintain heap invariant
smallest = heapq.heappop(data)  # pop and return smallest item

# Get n largest/smallest without fully sorting
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))   # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]
```

## Workflow

Progress:
- [ ] Step 1: Decide if you need a full priority queue, a one-off top-k query, or a merge operation
- [ ] Step 2: Choose the right heapq function(s) for the task
- [ ] Step 3: For priority queues with ties/mutability, wrap items as tuples `(priority, counter, item)`
- [ ] Step 4: For max-heap behavior, negate priorities (heapq only implements min-heap)
- [ ] Step 5: Test edge cases — empty heap, equal priorities, updating/removing entries

**Core functions:**

| Function | Purpose |
|---|---|
| `heapify(x)` | Transform list into a heap, in-place, O(n) |
| `heappush(heap, item)` | Push item, maintain invariant, O(log n) |
| `heappop(heap)` | Pop smallest item, O(log n) |
| `heappushpop(heap, item)` | Push then pop, more efficient than separate calls |
| `heapreplace(heap, item)` | Pop then push, faster but pop happens before push (heap never empty briefly) |
| `merge(*iterables, key=None, reverse=False)` | Merge sorted inputs into single sorted generator |
| `nlargest(n, iterable, key=None)` | n largest elements, use when n is small relative to iterable |
| `nsmallest(n, iterable, key=None)` | n smallest elements |

**Choosing between approaches:**
- `n == 1`: use `min()`/`max()` — faster
- `n small`, iterable large: use `nlargest`/`nsmallest`
- `n ≈ len(iterable)`: use `sorted(iterable)[:n]` — faster than heap approach
- Repeated push/pop over time: use `heappush`/`heappop` directly on a heap list

## Examples

**Example 1: Priority queue with stable ordering and tie-breaking**

Input: Tasks with priorities, need FIFO order for equal priorities
```python
import heapq
import itertools

counter = itertools.count()
pq = []

def add_task(task, priority=0):
    entry = (priority, next(counter), task)
    heapq.heappush(pq, entry)

def pop_task():
    priority, count, task = heapq.heappop(pq)
    return task

add_task('write code', priority=2)
add_task('write spec', priority=1)
add_task('create tests', priority=1)
```
Output: `pop_task()` calls return `'write spec'`, `'create tests'`, `'write code'` — priority order, FIFO within same priority.

**Example 2: K largest elements from a stream**

Input: `stream = [3, 1, 4, 1, 5, 9, 2, 6]`, need top 3
```python
import heapq
print(heapq.nlargest(3, stream))
```
Output: `[9, 6, 5]`

**Example 3: Merging multiple sorted logs by timestamp**

Input: Several already-sorted iterables of log entries
```python
import heapq
log1 = [1, 4, 7]
log2 = [2, 5, 8]
log3 = [3, 6, 9]
merged = list(heapq.merge(log1, log2, log3))
```
Output: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

**Example 4: Max-heap via negation**

Input: Need largest-first pop behavior
```python
import heapq
nums = [3, 1, 4, 1, 5, 9]
heap = [-n for n in nums]
heapq.heapify(heap)
largest = -heapq.heappop(heap)  # 9
```
Output: `largest == 9`

## Best Practices

- Use tuples `(priority, item)` for ordered heap entries; ensure items are comparable or add a tiebreaker (e.g., a counter) to avoid comparing non-orderable items when priorities tie.
- For max-heaps, negate numeric priorities rather than writing a custom comparator (heapq has no `key`/`reverse` param for push/pop).
- `heapify()` is O(n) — always prefer it over repeated `heappush` calls when building from an existing list.
- Use `heapreplace` instead of `heappop` + `heappush` when you always want to maintain a fixed heap size (e.g., sliding window top-k).
- For mutable/updatable priority queues (need to change priority of existing item), mark old entries as invalid and push new one instead of trying to remove mid-heap — heaps don't support efficient arbitrary removal.
- `heapq.merge()` is lazy (returns iterator) — good for merging large sorted files/streams without loading everything into memory.

## Common Pitfalls

- Don't assume the heap list is fully sorted — only `heap[0]` is guaranteed to be the smallest; use `heapq.heapify` + repeated `heappop`, or just `sorted()`, if you need a fully sorted result.
- Don't use `heapq` for max-heap directly — there's no built-in max-heap; negate values or wrap in a class with reversed `__lt__`.
- Don't call `heappush`/`heappop` on a list that wasn't heapified first — behavior is undefined on non-heap-ordered lists.
- Don't try to update priority of an existing item in place — mutating a heap element doesn't re-sort the heap; use the "lazy deletion" pattern (push new entry, mark old as removed, skip removed entries on pop).
- Avoid `nlargest`/`nsmallest` when `n` is close to the full length of the iterable — plain `sorted()` is more efficient in that case.
- Remember comparisons happen on full tuples — if priorities tie and items aren't comparable (e.g., dicts), you'll get a `TypeError`; always include a unique tiebreaker.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-bisect-module
description: Provides array bisection algorithms for maintaining sorted lists and performing efficient binary search insertions. Use when inserting into sorted lists while preserving order, finding insertion points in sorted sequences, or avoiding manual binary search implementation.
---

## Quick Start

```python
from bisect import bisect_left, bisect_right, insort_left, insort_right

sorted_list = [1, 3, 4, 4, 6, 8]

# Find insertion point (no mutation)
idx = bisect_right(sorted_list, 4)  # 4 -> insert after existing 4s

# Insert while keeping list sorted
insort_right(sorted_list, 5)  # sorted_list -> [1, 3, 4, 4, 5, 6, 8]
```

## Workflow

1. **Decide left vs right** semantics for duplicate handling:
   - `bisect_left` / `insort_left`: insertion point before existing equal entries
   - `bisect_right` / `insort_right` (aka `bisect`/`insort`): insertion point after existing equal entries
2. **Use `bisect_*` when you only need the index** (e.g., for grading/lookup tables, avoiding a full insert).
3. **Use `insort_*` when you need to mutate the list** to keep it sorted after adding a value.
4. **For custom sort keys** (Python 3.10+), pass `key=` instead of pre-transforming the list:
   ```python
   bisect_left(data, target, key=lambda x: x.value)
   ```
5. **For narrowing search range**, use `lo` and `hi` parameters to limit the search to a slice `[lo, hi)`.
6. **Never call these on an unsorted list** — behavior is undefined/incorrect.

## Examples

**Example 1: Grade lookup table**
Input:
```python
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    from bisect import bisect
    i = bisect(breakpoints, score)
    return grades[i]

[grade(s) for s in [55, 60, 61, 89, 90, 100]]
```
Output: `['F', 'D', 'D', 'C', 'A', 'A']`

**Example 2: Insert maintaining order with objects**
Input:
```python
from bisect import insort_right
from dataclasses import dataclass

@dataclass
class Event:
    time: int

events = [Event(1), Event(5), Event(10)]
insort_right(events, Event(7), key=lambda e: e.time)
[e.time for e in events]
```
Output: `[1, 5, 7, 10]`

**Example 3: Finding index without inserting**
Input:
```python
from bisect import bisect_left
data = [10, 20, 30, 40]
bisect_left(data, 25)
```
Output: `2`

## Best Practices

- Prefer `bisect_left`/`bisect_right` over writing manual binary search loops.
- Use `key=` parameter (3.10+) instead of maintaining a parallel list of keys.
- For repeated insertions building a sorted list from scratch, `insort` in a loop is O(n²) total — consider sorting once at the end if inserting many items at once.
- Use `bisect_left(a, x)` to check membership: `i = bisect_left(a, x); found = i < len(a) and a[i] == x`.

## Common Pitfalls

- Calling `bisect`/`insort` functions on unsorted data — results are meaningless.
- Confusing `bisect_left` and `bisect_right` when duplicates matter (affects where equal values land).
- Using `insort` repeatedly in a hot loop for large datasets — O(n) shifting cost per insert dominates; batch and sort instead when possible.
- Forgetting that `bisect`/`insort` are aliases for `bisect_right`/`insort_right`, not `bisect_left`/`insort_left`.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-array-module
description: Provides guidance on using Python's array module for space-efficient storage of homogeneous numeric data. Use when working with large sequences of primitive numeric types (ints, floats) where memory efficiency matters more than list flexibility, or when interfacing with C code, struct, or binary data.
---

## Quick Start

```python
from array import array

# Create an array of signed integers ('i' typecode)
a = array('i', [1, 2, 3, 4, 5])
print(a)          # array('i', [1, 2, 3, 4, 5])
print(a[2])       # 3
print(a.tolist()) # [1, 2, 3, 4, 5]
```

Choose `array` over `list` when storing millions of numbers of the same type and memory footprint matters, or when you need to pass raw numeric buffers to C libraries, files, or sockets.

## Workflow

Progress:
- [ ] Step 1: Pick the correct typecode for the data's type and range
- [ ] Step 2: Construct the array with an iterable or bytes
- [ ] Step 3: Use list-like operations (append, extend, slicing, indexing)
- [ ] Step 4: Convert to/from bytes, lists, or files as needed
- [ ] Step 5: Validate itemsize and overflow behavior on the target platform

### Step 1: Typecodes

| Code | Type | Min bytes |
|---|---|---|
| `'b'` / `'B'` | signed/unsigned char | 1 |
| `'u'` | wchar_t (deprecated since 3.3, removed in later versions — prefer `str`) | 2/4 |
| `'h'` / `'H'` | signed/unsigned short | 2 |
| `'i'` / `'I'` | signed/unsigned int | 2 |
| `'l'` / `'L'` | signed/unsigned long | 4 |
| `'q'` / `'Q'` | signed/unsigned long long | 8 |
| `'f'` | float | 4 |
| `'d'` | double | 8 |

Use `array.itemsize` to check actual byte size on the running platform — it is not guaranteed identical across platforms.

### Step 2: Construction

```python
array(typecode)                 # empty array
array(typecode, iterable)       # from list/tuple/generator of numbers
array(typecode, bytes_obj)      # from raw bytes (interpreted per typecode)
```

### Step 3: Common operations

```python
a.append(6)
a.extend([7, 8])
a.insert(0, -1)
a.pop()
a.remove(3)
a.reverse()
a[1:3] = array('i', [10, 20])   # slice assignment must use same typecode
len(a)
a.count(10)
a.index(10)
```

### Step 4: Conversion

```python
a.tobytes()          # -> bytes
array('i').frombytes(b)   # populate from bytes
a.tolist()            # -> list
a.tofile(f)            # write to a binary file object
a.fromfile(f, n)       # read n items from a binary file object
```

### Step 5: Buffer / memoryview interop

```python
mv = memoryview(a)
mv[0] = 99            # mutates the array in place
```

## Examples

**Example 1: Efficient storage of sensor readings**
Input:
```python
from array import array
readings = array('f', [23.5, 24.1, 22.9, 25.0])
```
Output: A compact float array using 4 bytes per element (16 bytes total) instead of Python `list`'s per-object overhead (~28+ bytes per float object plus pointer).

**Example 2: Reading binary data from a file**
Input:
```python
from array import array
a = array('i')
with open('data.bin', 'rb') as f:
    a.frombytes(f.read())
```
Output: `a` contains the file's contents parsed as a sequence of signed ints, respecting native byte order.

**Example 3: Round-tripping through bytes**
Input:
```python
a = array('h', [1, -2, 3])
b = a.tobytes()
c = array('h')
c.frombytes(b)
```
Output: `c == a` → `True`

## Best Practices

- Always specify typecode explicitly; don't rely on inference.
- Use `array.itemsize` and `array.buffer_info()` when interfacing with C or low-level I/O to confirm memory layout.
- Prefer `bytearray` or `memoryview` if working with raw bytes rather than typed numeric sequences.
- For large numeric datasets needing math operations (not just storage), prefer `numpy.ndarray` — `array` module has no vectorized math.
- Use slice assignment with an `array` of matching typecode, not a plain list, to avoid `TypeError`.

## Common Pitfalls

- **Mixing typecodes in slice assignment**: `a[0:2] = [1, 2]` raises `TypeError`; must assign another `array` object.
- **Assuming fixed itemsize across platforms**: `'l'` and `'i'` sizes can vary; always check `itemsize` if byte-exact compatibility matters.
- **Using `'u'` typecode**: deprecated/removed in modern Python — use `str` or dedicated Unicode handling instead.
- **Overflow on append**: appending a value outside the typecode's range raises `OverflowError`, not silent truncation.
- **Expecting math methods**: `array` has no `sum()`, `mean()`, elementwise ops built in — use `sum(a)` (Python builtin) or convert to NumPy for numeric operations.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-weakref
description: Provides guidance on using Python's weakref module to create weak references to objects without preventing garbage collection. Use when caching objects, building observer patterns, avoiding reference cycles, implementing memoization, or managing parent-child object relationships without memory leaks.
---

## Quick Start

```python
import weakref

class Node:
    pass

obj = Node()
r = weakref.ref(obj)   # weak reference, doesn't keep obj alive
print(r())             # -> <Node object> (call it to get the referent)

del obj
print(r())              # -> None, object was garbage collected
```

## Workflow

1. **Identify the memory issue**: reference cycles, caches growing unbounded, or child objects keeping parents alive.
2. **Choose the right weakref tool** (see decision table below).
3. **Use `.callback` for cleanup notification** if you need to know when the referent dies.
4. **Test garbage collection behavior** explicitly (`del obj; gc.collect()`) to confirm no leaks.

Progress:
- [ ] Identify objects that should NOT be kept alive by references
- [ ] Pick appropriate weakref primitive (ref, proxy, WeakValueDictionary, WeakKeyDictionary, WeakSet)
- [ ] Handle the case where the referent has been collected (check for `None` or `ReferenceError`)
- [ ] Add callbacks if cleanup/logging is needed
- [ ] Verify with `gc` module or memory profiling

## Decision Table

| Need | Use |
|---|---|
| Single weak reference, explicit call to dereference | `weakref.ref(obj, callback=None)` |
| Weak reference that behaves like the object itself | `weakref.proxy(obj, callback=None)` |
| Dict mapping keys -> weakly-referenced values (cache pattern) | `weakref.WeakValueDictionary()` |
| Dict mapping weakly-referenced keys -> values (annotate objects w/o owning them) | `weakref.WeakKeyDictionary()` |
| Set of objects without keeping them alive | `weakref.WeakSet()` |
| Weak reference to a bound method (doesn't keep instance alive) | `weakref.WeakMethod()` |
| Finalization/cleanup callback tied to object lifetime, safer than `__del__` | `weakref.finalize(obj, func, *args, **kwargs)` |

## Examples

**Example 1: Caching expensive objects without leaking memory**

Input: Cache computed objects by key, but let them be garbage collected when nothing else references them.

Output:
```python
import weakref

class ExpensiveObject:
    def __init__(self, value):
        self.value = value

cache = weakref.WeakValueDictionary()

def get_object(key):
    obj = cache.get(key)
    if obj is None:
        obj = ExpensiveObject(key)
        cache[key] = obj
    return obj

a = get_object("x")
print(len(cache))  # 1
del a
import gc; gc.collect()
print(len(cache))  # 0, auto-removed
```

**Example 2: Observer pattern without preventing listener cleanup**

Input: A subject notifies observers, but shouldn't keep dead observers alive.

Output:
```python
import weakref

class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()

    def register(self, observer):
        self._observers.add(observer)

    def notify(self, *args):
        for obs in self._observers:
            obs.update(*args)
```

**Example 3: Using finalize for cleanup instead of `__del__`**

Input: Run cleanup code when an object is garbage collected, safely (no `__del__` pitfalls).

Output:
```python
import weakref

class Resource:
    def __init__(self, name):
        self.name = name
        self._finalizer = weakref.finalize(self, print, f"Cleaning up {name}")

    def close(self):
        self._finalizer()

r = Resource("db-connection")
del r  # prints "Cleaning up db-connection"
```

**Example 4: Weak reference to a bound method (avoid keeping instance alive via callback)**

Input: Register a callback that is a bound method without preventing the instance from being collected.

Output:
```python
import weakref

class Handler:
    def on_event(self):
        print("event handled")

h = Handler()
weak_method = weakref.WeakMethod(h.on_event)

callback = weak_method()
if callback is not None:
    callback()

del h
print(weak_method())  # None
```

## Best Practices

- Not all objects support weak references: built-ins like `int`, `list`, `dict`, `tuple` (without `__slots__` workaround) can't be weakly referenced directly. Custom classes support it by default unless `__slots__` excludes `__weakref__`.
- Always check if `ref()` or `proxy()` returned `None`/raised `ReferenceError` before using the result — the referent may already be gone.
- Prefer `weakref.finalize` over `__del__` for cleanup logic — it's more predictable, supports multiple finalizers, and doesn't resurrect objects.
- Use `WeakValueDictionary`/`WeakKeyDictionary` for caches and registries where entries should disappear automatically once no other strong references exist.
- Use `proxy()` when you want transparent attribute access instead of calling `ref()()`.
- Keep callbacks passed to `ref()`/`proxy()` simple; they run after the object is already gone (during GC), so the callback receives the dead weakref, not the object.

## Common Pitfalls

- **Storing the weakref in a way that outlives its usefulness**: iterating over a `WeakValueDictionary`/`WeakSet` while objects are being collected can raise `RuntimeError: dictionary changed size during iteration`. Take a snapshot (`list(...)`) before iterating if mutation during iteration is possible.
- **Assuming a weakref keeps working forever**: always re-check dereferenced weakrefs before use, especially across function boundaries or after `await`/context switches.
- **Trying to weakly reference an object without `__weakref__` slot**: define `__slots__ = ('__weakref__', ...)` explicitly if using `__slots__` and weakref support is needed.
- **Using `__del__` for cleanup instead of `finalize`**: `__del__` can resurrect objects, interacts badly with reference cycles and exceptions during interpreter shutdown.
- **Forgetting that a callback fires with the dead reference, not the object**: don't expect `obj` state inside the callback; the object's state is already unreachable.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-python-types-module
description: Provides guidance on using Python's types module for dynamic type creation, runtime type checking, and working with internal CPython types. Use when needing to create new types dynamically, check for generic aliases, work with function/module/method types, or inspect standard interpreter types not exposed as builtins.
---

## Quick Start

```python
import types

# Create a simple namespace object (lightweight alternative to a class)
ns = types.SimpleNamespace(x=1, y=2)
print(ns.x, ns.y)  # 1 2

# Get the type of a function for isinstance checks
def f(): pass
print(isinstance(f, types.FunctionType))  # True

# Dynamically create a new class
NewClass = types.new_class("NewClass", (object,))
```

## Workflow

1. **Identify the need**: dynamic class creation, type-checking against interpreter internals, or lightweight data containers.
2. **Pick the right type/function** from `types` (see reference table below).
3. **Use `isinstance`/`issubclass`** with `types` constants instead of guessing types via `type(x).__name__`.
4. **For dynamic classes**, prefer `types.new_class()` / `types.prepare_class()` over `type()` when metaclasses or `__init_subclass__`/`__set_name__` semantics matter.
5. **For generics**, use `types.GenericAlias` and `types.UnionType` checks when introspecting typing constructs at runtime.

## Reference: Common Members

**Dynamic type creation**
- `types.new_class(name, bases=(), kwds=None, exec_body=None)` — PEP 3115-compliant dynamic class creation.
- `types.prepare_class(name, bases=(), kwds=None)` — resolves metaclass and namespace before class body execution.
- `types.resolve_bases(bases)` — resolves `__mro_entries__` for dynamic bases.

**Simple containers**
- `types.SimpleNamespace` — mutable attribute-holding object, `repr()`-friendly. Good for quick objects without defining a class.
- `types.MappingProxyType` — read-only view over a dict, used to expose immutable-looking mappings (e.g., `cls.__dict__`).

**Callable / function-related types** (for `isinstance` checks)
- `types.FunctionType` / `types.LambdaType` — user-defined functions and lambdas.
- `types.MethodType` — bound methods.
- `types.BuiltinFunctionType` / `types.BuiltinMethodType` — C-implemented functions/methods.
- `types.CoroutineType`, `types.AsyncGeneratorType`, `types.GeneratorType` — for `async def`, async generators, and generator functions.

**Code & module internals**
- `types.CodeType` — compiled code objects (`func.__code__`).
- `types.CellType` — closure cell objects.
- `types.ModuleType` — used to create modules dynamically: `mod = types.ModuleType("mymod")`.
- `types.TracebackType`, `types.FrameType` — for introspecting exceptions/stack frames.

**Typing-adjacent runtime types**
- `types.GenericAlias` — the runtime type of `list[int]`, `dict[str, int]`, etc.
- `types.UnionType` — the runtime type of `int | str`.
- `types.NoneType` — canonical way to reference `type(None)` since Python 3.10.
- `types.EllipsisType`, `types.NotImplementedType` — canonical types for `...` and `NotImplemented`.

**Descriptors**
- `types.DynamicClassAttribute` — like `property()` but only triggers on instance access, not class access (used internally by `Enum`).
- `types.MemberDescriptorType`, `types.GetSetDescriptorType` — descriptor types found on slot-based classes.

## Examples

**Example 1: Dynamic module creation**
Input: Need to create a module object at runtime and populate it.
Output:
```python
import types
mod = types.ModuleType("config", "Dynamic config module")
mod.DEBUG = True
mod.VERSION = "1.0"
import sys
sys.modules["config"] = mod
```

**Example 2: Checking for None type explicitly**
Input: Want `isinstance` check equivalent to `x is None` but usable in a type tuple.
Output:
```python
import types
def describe(x):
    if isinstance(x, types.NoneType):
        return "none"
    return "value"
```

**Example 3: Read-only dict view**
Input: Expose internal state as immutable to callers.
Output:
```python
import types
_data = {"a": 1, "b": 2}
public_view = types.MappingProxyType(_data)
# public_view["a"] = 5  -> raises TypeError
```

**Example 4: isinstance check for coroutine functions**
Input: Distinguish a coroutine object from a plain generator.
Output:
```python
import types, inspect
async def foo(): pass
coro = foo()
print(isinstance(coro, types.CoroutineType))  # True
```

## Best Practices

- Prefer `types.SimpleNamespace` over `dict` when attribute-style access reads cleaner, but don't overuse it as a class replacement.
- Use `types.MappingProxyType` to protect internal dict state instead of returning copies.
- When checking "is this a function" broadly, remember `types.FunctionType` doesn't include builtins or methods — combine with `types.BuiltinFunctionType`/`types.MethodType` as needed, or use `callable()` if you just need "can be called".
- Use `types.NoneType`, `types.EllipsisType`, `types.NotImplementedType` for readability instead of `type(None)`, `type(...)`, `type(NotImplemented)`.
- Use `types.new_class()` instead of manually calling `type()` when the class hierarchy involves `__init_subclass__`, `__set_name__`, or non-trivial metaclasses.

## Common Pitfalls

- Don't confuse `types.GenericAlias` (runtime object for `list[int]`) with `typing.Generic` — they serve different layers (runtime container vs. static typing).
- Don't mutate a `types.MappingProxyType` — it's read-only by design; mutate the underlying dict instead.
- Don't assume `types.FunctionType` covers lambdas separately — `types.LambdaType` is just an alias for `types.FunctionType`.
- Avoid relying on exact `types` members across major Python versions without checking `docs.python.org` for the specific version (e.g., 3.16) since some members are added/deprecated over time.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-copy-module
description: Provides guidance on Python's copy module for shallow and deep copying of objects. Use when duplicating mutable objects (lists, dicts, custom classes), avoiding aliasing bugs, or implementing __copy__/__deepcopy__ methods on custom classes.
---

## Quick Start

```python
import copy

# Shallow copy: new outer object, but nested objects are shared references
shallow = copy.copy(original)

# Deep copy: new outer object AND recursively copies all nested objects
deep = copy.deepcopy(original)
```

## Workflow

1. **Identify the problem**: Are you seeing unexpected mutations propagate between two variables that should be independent? This is an aliasing bug — assignment (`b = a`) does not copy, it just binds a new name to the same object.

2. **Decide copy depth needed**:
   - Flat structure (no nested mutables) → `copy.copy()` is sufficient and cheaper.
   - Nested structures (list of lists, dict of objects, etc.) → use `copy.deepcopy()`.

3. **Check for built-in shortcuts first** (often faster/clearer than importing `copy`):
   - `list(original)` or `original[:]` for shallow list copy
   - `dict(original)` for shallow dict copy
   - `original.copy()` — most built-in containers have this method

4. **For custom classes**, decide if default behavior is enough:
   - Default `copy.copy()`/`copy.deepcopy()` copies the `__dict__` (shallow/deep respectively).
   - Override `__copy__(self)` and/or `__deepcopy__(self, memo)` when the class manages external resources (file handles, locks, sockets) that shouldn't be blindly duplicated.

5. **Handle circular references**: `deepcopy` automatically tracks already-copied objects via the `memo` dict to avoid infinite recursion — no extra work needed unless implementing `__deepcopy__` yourself, in which case pass `memo` through to recursive `copy.deepcopy(x, memo)` calls.

6. **Test the copy**: mutate the original after copying and confirm the copy is unaffected (for deepcopy) or that only top-level independence holds (for shallow copy).

## Examples

**Example 1: Shallow copy pitfall**
Input:
```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0].append(99)
print(original)
```
Output:
```python
[[1, 2, 99], [3, 4]]  # inner list mutated because it's shared by reference
```

**Example 2: Deep copy fixes it**
Input:
```python
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(99)
print(original)
```
Output:
```python
[[1, 2], [3, 4]]  # unaffected, inner lists were fully duplicated
```

**Example 3: Custom `__deepcopy__`**
Input:
```python
import copy

class Connection:
    def __init__(self, socket):
        self.socket = socket  # unpicklable/unshareable resource

    def __deepcopy__(self, memo):
        # Don't duplicate the actual socket; share the reference
        new = Connection.__new__(Connection)
        memo[id(self)] = new
        new.socket = self.socket
        return new

conn2 = copy.deepcopy(conn1)
```
Output:
```python
# conn2 is a new Connection object, but conn2.socket is conn1.socket (same object)
```

## Best Practices

- Prefer built-in `.copy()`, slicing, or constructor calls (`list()`, `dict()`, `set()`) over `copy.copy()` for simple containers — they're idiomatic and slightly faster.
- Use `copy.deepcopy()` whenever objects contain nested mutable structures and true independence is required.
- When implementing `__deepcopy__`, always accept and thread through the `memo` dictionary to correctly handle shared/circular references.
- For classes holding non-copyable resources (files, sockets, locks, threads), implement `__copy__`/`__deepcopy__` explicitly rather than relying on defaults.
- Remember atomic/immutable types (int, str, tuple of immutables, frozenset) are returned as-is by `copy`/`deepcopy` — no need to copy them manually.
- Use `copy.deepcopy(obj, memo={})` manually only in rare cases where you need to pre-seed the memo (e.g., to force sharing of a specific sub-object).

## Common Pitfalls

- **Assuming `b = a` copies**: it doesn't — both names reference the identical object.
- **Using shallow copy on nested structures**: leads to subtle bugs where mutating a "copy" affects the original's nested data.
- **Forgetting `__deepcopy__` needs `memo`**: skipping it breaks cycle detection and can cause infinite recursion or duplicate objects that should be shared.
- **Deep-copying unpicklable/unshareable resources by default**: sockets, file handles, and thread locks generally cannot (and should not) be deep-copied — override `__deepcopy__` to handle them explicitly.
- **Overusing `deepcopy` for performance-critical code**: it's recursive and can be slow on large or deeply nested structures; use shallow copy or restructure data when full independence isn't needed.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: pretty-printing-python-data
description: Formats and displays Python data structures (dicts, lists, tuples, nested objects) in a readable, well-indented layout using the pprint module. Use when output contains deeply nested or wide data structures that are hard to read as plain repr/print output, when writing debug output, or when a user asks to "pretty print" or format Python data for readability.
---

## Quick Start

```python
from pprint import pprint, pformat

data = {"name": "Alice", "roles": ["admin", "editor"], "meta": {"age": 30, "active": True}}

pprint(data)
# {'meta': {'active': True, 'age': 30},
#  'name': 'Alice',
#  'roles': ['admin', 'editor']}
```

For getting a string instead of printing directly, use `pformat(data)`.

## Workflow

Progress:
- [ ] Step 1: Identify the data structure to display (dict, list, tuple, set, dataclass, or nested combination)
- [ ] Step 2: Choose the right function — `pprint()` to print directly, `pformat()` to get a string (e.g., for logging)
- [ ] Step 3: Tune parameters based on structure size/shape
- [ ] Step 4: Verify output width/depth is readable; adjust `width`, `depth`, `indent`, `compact`, `sort_dicts` as needed

### Key Parameters

- `indent=N` — spaces per nesting level (default 1)
- `width=N` — max line width before wrapping (default 80)
- `depth=N` — max nesting levels shown; deeper levels collapse to `...`
- `compact=True` — pack as many items per line as fit within `width`
- `sort_dicts=False` — preserve insertion order instead of alphabetical sorting (default `True` sorts keys!)
- `underscore_numbers=True` — insert `_` every 3 digits in large numbers (e.g., `1_234_567`)
- `stream=` — file object to write to instead of stdout (for `pprint()`)

### Other Useful Functions

- `pprint.pp(obj, *args, sort_dicts=False, **kwargs)` — shorthand for `pprint()` with `sort_dicts=False` by default (better for preserving dict order)
- `pprint.isreadable(obj)` — checks if the formatted repr can be `eval()`'d back
- `pprint.isrecursive(obj)` — checks if the object contains a recursive reference
- `pprint.saferepr(obj)` — repr that handles recursive structures without raising

## Examples

**Example 1: Deeply nested structure with default settings**

Input:
```python
from pprint import pprint
data = {"a": {"b": {"c": {"d": [1, 2, 3, {"e": "deep"}]}}}}
pprint(data)
```
Output:
```
{'a': {'b': {'c': {'d': [1, 2, 3, {'e': 'deep'}]}}}}
```

**Example 2: Limiting depth for large nested objects**

Input:
```python
pprint(data, depth=2)
```
Output:
```
{'a': {'b': {...}}}
```

**Example 3: Preserving insertion order (avoiding alphabetical resort)**

Input:
```python
pprint({"z": 1, "a": 2, "m": 3}, sort_dicts=False)
```
Output:
```
{'z': 1, 'a': 2, 'm': 3}
```

**Example 4: Using pformat for logging**

Input:
```python
import logging
from pprint import pformat
logging.debug("Payload:\n%s", pformat(large_dict))
```
Output: Logs the formatted structure as a single string, no direct printing to stdout.

**Example 5: Wide list of tuples, compact mode**

Input:
```python
pprint([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')], compact=True, width=40)
```
Output:
```
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

## Best Practices

- Default `sort_dicts=True` reorders keys alphabetically — use `sort_dicts=False` (or `pprint.pp`) when key order matters (e.g., JSON-like configs, ordered results).
- Use `depth=` to truncate huge nested structures instead of dumping everything.
- Use `pformat()` when integrating with logging or writing to files; reserve `pprint()` for interactive/debug console output.
- For custom objects, implement `__repr__` well — pprint relies on repr for leaf values.
- Increase `width` for structures with long strings to avoid excessive wrapping; decrease it for narrow terminals.

## Common Pitfalls

- Assuming `pprint` preserves dict insertion order by default — it does not (sorts keys unless `sort_dicts=False`).
- Using `pprint` on objects with circular references without knowing it handles them safely (it will show `<Recursion on ... with id=...>` rather than crashing — no need to pre-check, but be aware of the output format).
- Forgetting `pformat()` returns a string — calling `print(pprint(x))` prints `None` because `pprint()` already prints and returns `None`.
- Expecting pprint to "fix" unreadable custom objects — it only pretty-formats structure, not the repr of leaf objects.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: using-reprlib
description: Provides utilities for generating alternate implementations of repr() with size-limited output, useful for truncated debug representations and recursive repr protection. Use when repr() output for large containers, strings, or deeply nested/recursive data structures needs to be shortened or made safe from infinite recursion.
---

## Quick Start

```python
import reprlib

# Truncated repr for large data
r = reprlib.Repr()
r.maxlist = 3
print(r.repr(list(range(100))))
# [0, 1, 2, ...]

# Quick one-off truncated repr
print(reprlib.repr(list(range(100))))
# [0, 1, 2, ...]

# Protect custom repr methods from infinite recursion
class Tree:
    def __init__(self, children=None):
        self.children = children or []

    @reprlib.recursive_repr()
    def __repr__(self):
        return f"Tree({self.children!r})"

t = Tree()
t.children = [t]  # self-referential
print(repr(t))
# Tree([...])
```

## Workflow

Progress:
- [ ] Identify whether the need is (a) truncated repr for built-in-like containers/strings, or (b) recursion-safety for a custom `__repr__`
- [ ] For (a): use `reprlib.repr()` for a quick default, or subclass/configure `reprlib.Repr` for custom limits
- [ ] For (b): decorate `__repr__` with `@reprlib.recursive_repr()`
- [ ] Verify output length/behavior matches expectations
- [ ] Integrate into logging/debugging code where output size matters

### Using `reprlib.Repr` for custom limits

1. Instantiate `r = reprlib.Repr()` (or subclass it for reusable config).
2. Set relevant `max*` attributes before calling `.repr()`:
   - `maxlevel` — max recursion depth (default 6)
   - `maxtuple`, `maxlist`, `maxarray`, `maxdict`, `maxset`, `maxfrozenset`, `maxdeque` — max elements shown per container type
   - `maxstring` — max characters shown for `str`
   - `maxlong` — max digits shown for `int`
   - `maxother` — max chars for other objects' repr
3. Call `r.repr(obj)` for the general dispatcher, or type-specific methods like `r.repr_list(obj, level)` directly.
4. To customize behavior for a specific type, subclass `Repr` and override `repr_<typename>(self, obj, level)`.

### Using `recursive_repr` decorator

1. Import `reprlib.recursive_repr`.
2. Apply as a decorator directly above `__repr__` (must decorate `__repr__` specifically, or any method returning a string representation).
3. Optionally pass a fill-in string: `@reprlib.recursive_repr(fillvalue='...')` (default is `'...'`).
4. When a recursive call to the same object's `__repr__` is detected (via a thread-local set of ids), the decorator returns the fill-in value instead of recursing infinitely.

## Examples

**Example 1: Truncated list repr**
Input:
```python
reprlib.repr(list(range(1000)))
```
Output:
```python
'[0, 1, 2, 3, 4, 5, 6, ...]'
```

**Example 2: Custom Repr subclass**
Input:
```python
class MyRepr(reprlib.Repr):
    def __init__(self):
        super().__init__()
        self.maxstring = 10
        self.maxlist = 2

aRepr = MyRepr()
aRepr.repr(["hello world this is long", "b", "c", "d"])
```
Output:
```python
"['hello wor...', 'b', ...]"
```

**Example 3: Recursive structure protection**
Input:
```python
class Node:
    def __init__(self):
        self.next = None

    @reprlib.recursive_repr()
    def __repr__(self):
        return f"Node(next={self.next!r})"

n = Node()
n.next = n
repr(n)
```
Output:
```python
'Node(next=...)'
```

**Example 4: Nested container truncation with maxlevel**
Input:
```python
r = reprlib.Repr()
r.maxlevel = 2
r.repr([1, [2, [3, [4, [5]]]]])
```
Output:
```python
'[1, [2, [...]]]'
```

## Best Practices

- Use the module-level `reprlib.repr()` for quick, one-off truncation with sensible defaults — no need to instantiate `Repr` for simple cases.
- Instantiate and configure a `Repr` object (or subclass) once and reuse it when truncation settings need to be consistent across many calls (e.g., in a logging utility).
- Always apply `@reprlib.recursive_repr()` to `__repr__` methods of classes that can form cycles or self-references (trees, graphs, linked structures, or containers that may hold themselves).
- Prefer subclassing `Repr` and overriding `repr_<type>` methods when default truncation for a specific type isn't sufficient, rather than writing truncation logic manually.
- Remember `reprlib.repr()` is meant for *display/debug* purposes — the output is not necessarily valid Python that can be `eval()`'d back into the original object once truncated.

## Common Pitfalls

- Don't confuse `reprlib.Repr.maxlevel` behavior — it counts down levels, and nested containers beyond the limit collapse to `...`, not to an empty container.
- Don't apply `@reprlib.recursive_repr()` to methods other than the string-producing repr method — it's specifically designed to guard against recursive string conversion, using a thread-local + id-based guard.
- Don't expect `reprlib.repr()` truncated output to be safe for `eval()`; it's for human-readable debugging only.
- Don't forget that `maxstring` and `maxlong` apply per-value, not per-container — a container of many short strings can still produce a long overall output if `maxlist`/`maxdict` etc. are large.
- Don't manually implement recursion guards with global mutable state when `reprlib.recursive_repr()` already handles thread-safety via thread-local storage.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: resolving-dependency-graphs
description: Performs topological sorting and dependency resolution using graphlib.TopologicalSorter. Use when ordering tasks with dependencies, detecting cycles in dependency graphs, or determining safe parallel execution batches (build systems, task schedulers, import resolution, package installers).
---

## Quick Start

```python
from graphlib import TopologicalSorter, CycleError

graph = {
    "deploy": {"test", "build"},
    "test": {"build"},
    "build": {"lint"},
    "lint": set(),
}

ts = TopologicalSorter(graph)
print(list(ts.static_order()))
# ['lint', 'build', 'test', 'deploy']
```

`graph[node] = {dependencies}` — keys depend on their values (values must be resolved first).

## Workflow

Progress:
- [ ] Build the dependency dict: `{node: set_of_prerequisites}`
- [ ] Choose API: `static_order()` for a simple full sort, or the manual protocol for streaming/parallel execution
- [ ] Handle `CycleError` if the graph might contain cycles
- [ ] (If parallel) drive the sorter manually with `prepare()`/`get_ready()`/`done()`

**Simple case — full ordering:**
```python
ts = TopologicalSorter(graph)
order = list(ts.static_order())
```

**Parallel/streaming case — process ready nodes as they unblock:**
```python
ts = TopologicalSorter(graph)
ts.prepare()  # raises CycleError here if cyclic
while ts.is_active():
    ready = ts.get_ready()      # tuple of nodes with no unresolved deps
    for node in ready:
        do_work(node)
        ts.done(node)           # mark complete, unblocks dependents
```

`get_ready()` returns *all* currently unblocked nodes — dispatch them concurrently (thread pool, async tasks, subprocess batch) for real parallelism.

**Adding edges incrementally:**
```python
ts = TopologicalSorter()
ts.add(node, *predecessors)   # can call repeatedly to build up graph
ts.add("build", "lint")
ts.add("test", "build")
```

## Examples

**Example 1: Detecting a cycle**
Input:
```python
graph = {"a": {"b"}, "b": {"c"}, "c": {"a"}}
ts = TopologicalSorter(graph)
ts.static_order()
```
Output:
```
graphlib.CycleError: ('nodes are in a cycle', ['a', 'b', 'c', 'a'])
```

**Example 2: Parallel build batches**
Input:
```python
graph = {"link": {"a.o", "b.o"}, "a.o": {"a.c"}, "b.o": {"b.c"}, "a.c": set(), "b.c": set()}
ts = TopologicalSorter(graph)
ts.prepare()
batches = []
while ts.is_active():
    ready = ts.get_ready()
    batches.append(sorted(ready))
    for n in ready:
        ts.done(n)
```
Output:
```
batches == [['a.c', 'b.c'], ['a.o', 'b.o'], ['link']]
```

**Example 3: Independent nodes (no dependencies)**
Input:
```python
graph = {"x": set(), "y": set()}
list(TopologicalSorter(graph).static_order())
```
Output: `['x', 'y']` (order among unrelated nodes is arbitrary but valid)

## Best Practices

- Call `prepare()` explicitly when using the manual protocol — it finalizes the graph and does the upfront cycle check.
- Never mutate the graph (via `add()`) after calling `prepare()`; it raises `ValueError`.
- Each node returned by `get_ready()` must eventually get a matching `done()` call, or `is_active()` stays true forever.
- Nodes must be hashable; they don't need to be pre-declared as dict keys — referencing them as a dependency is enough.
- Use `static_order()` when you just need a single sequential list; it's a thin convenience wrapper around the manual protocol.

## Common Pitfalls

- Don't confuse edge direction: `graph[x] = {y}` means **x depends on y** (y runs first), not the reverse.
- Don't call `get_ready()` again without calling `done()` on previously returned nodes — already-returned nodes won't reappear, but forgetting `done()` stalls the sort.
- Don't assume `get_ready()` order is deterministic/meaningful — treat it as an unordered ready-set.
- Don't reuse a `TopologicalSorter` instance after exhausting it — create a new one per sort.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---