---
name: using-python-numeric-module
description: Explains and applies Python's numeric abstract base classes and decimal/fraction/statistics modules (numbers, decimal, fractions, random, statistics). Use when writing code that requires precise decimal arithmetic, rational number handling, statistical calculations, or type-checking numeric hierarchies in Python.
---

## Quick Start

```python
from decimal import Decimal
from fractions import Fraction
import statistics as stats

# Precise decimal arithmetic (avoids float rounding issues)
price = Decimal("19.99") * 3
print(price)  # 59.97

# Exact rational arithmetic
half = Fraction(1, 2)
third = Fraction(1, 3)
print(half + third)  # 5/6

# Statistical summary
data = [2, 4, 4, 4, 5, 5, 7, 9]
print(stats.mean(data), stats.median(data), stats.stdev(data))
```

## Workflow

Progress checklist for choosing/using the right numeric tool:

- [ ] Step 1: Identify the problem type (exact decimal money math, exact rational fractions, general stats, or random sampling).
- [ ] Step 2: Pick the module — `decimal` for base-10 precision, `fractions` for exact ratios, `statistics` for descriptive stats, `random` for sampling/simulation.
- [ ] Step 3: Set context/precision if using `decimal` (`getcontext().prec`).
- [ ] Step 4: Perform operations using module-native types; avoid mixing raw `float` into `Decimal`/`Fraction` ops without explicit conversion.
- [ ] Step 5: Validate results (check rounding mode, denominator reduction, or statistical assumptions like normality).
- [ ] Step 6: Convert back to desired output type (`float`, `str`, `int`) only at the boundary (display/storage).

## Examples

**Example 1: Financial calculation avoiding float error**
Input:
```python
0.1 + 0.2
```
Output:
```
0.30000000000000004  # float imprecision
```
Fix:
```python
from decimal import Decimal
Decimal("0.1") + Decimal("0.2")
# Decimal('0.3')
```

**Example 2: Exact fraction reduction**
Input:
```python
from fractions import Fraction
Fraction(6, 8)
```
Output:
```
Fraction(3, 4)  # auto-reduced to lowest terms
```

**Example 3: Statistics with outliers**
Input:
```python
import statistics as stats
data = [10, 12, 11, 13, 100]
stats.mean(data), stats.median(data)
```
Output:
```
(29.2, 12)  # median is robust to the outlier; mean is skewed
```

## Best Practices

- Use `Decimal` for money/financial data — never `float`.
- Set `decimal.getcontext().prec` explicitly when precision matters beyond the default 28 digits.
- Construct `Decimal` from strings (`Decimal("0.1")`), not floats (`Decimal(0.1)`), to avoid inheriting float imprecision.
- Use `Fraction.from_float()` or `.limit_denominator()` when converting floats to fractions to prevent unwieldy denominators.
- Prefer `statistics.median` over `mean` when data has outliers or skew.
- Use `statistics.fmean` for faster float-based mean when precision of `Decimal`-level accuracy isn't required.
- Check `isinstance(x, numbers.Number)` (from the `numbers` ABC hierarchy) when writing generic numeric code that should accept int, float, Decimal, complex, etc.

## Common Pitfalls

- Don't mix `float` and `Decimal` in arithmetic — raises `TypeError`. Convert explicitly first.
- Don't assume `Fraction` arithmetic is fast for large-denominator chains — it can grow numerators/denominators unboundedly; consider periodic `.limit_denominator()`.
- Don't use `statistics.stdev` (sample stdev) when you mean `pstdev` (population stdev) — they differ and silently give wrong results for full-population data.
- Don't rely on default `Decimal` context precision across threads without setting `localcontext()` — context is thread-local and can cause inconsistent precision in concurrent code.
- Don't use `random` module functions for cryptographic purposes — use `secrets` instead.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: implementing-numeric-tower
description: Implements and works with Python's numeric abstract base class hierarchy (numbers.Number, Complex, Real, Rational, Integral) for creating custom numeric types that integrate with isinstance checks, arithmetic operators, and the standard library. Use when creating custom number-like classes, registering third-party numeric types with the ABC hierarchy, or deciding which numeric ABC to inherit from or check against.
---

## Quick Start

```python
from numbers import Integral, Rational, Real, Complex, Number
from fractions import Fraction

# Check numeric type generically instead of using int/float/complex directly
def process(x):
    if isinstance(x, Integral):
        return x << 1          # bitwise ops only valid for Integral
    elif isinstance(x, Rational):
        return x.numerator / x.denominator
    elif isinstance(x, Real):
        return float(x)
    elif isinstance(x, Complex):
        return x.real, x.imag
    raise TypeError(f"{x!r} is not a number")

process(3)              # Integral
process(Fraction(1, 2)) # Rational
process(3.14)           # Real
process(2 + 3j)         # Complex
```

## The Numeric Tower

```
Number
 └── Complex
      └── Real
           └── Rational
                └── Integral
```

Each ABC is a superclass of the one below it. Built-in registrations:

| ABC        | Registered built-ins        |
|------------|------------------------------|
| `Complex`  | `complex`                    |
| `Real`     | `float`                      |
| `Rational` | `fractions.Fraction`         |
| `Integral` | `int`                        |

`int` is also `Real`, `Complex`, and `Number` (inherited transitively). No built-in implements `Rational` except `Fraction`.

## Workflow

Progress:
- [ ] Step 1: Decide which ABC matches the semantics of your custom type
- [ ] Step 2: Subclass that ABC directly (don't just duck-type)
- [ ] Step 3: Implement all abstract methods required by that ABC (see table below)
- [ ] Step 4: Decide `__eq__`/`__hash__` semantics consistent with numeric equality
- [ ] Step 5: Test `isinstance()` against the ABC and against mixed-type arithmetic
- [ ] Step 6: If wrapping a third-party type you can't subclass, use `ABC.register()`

### Required abstract methods per ABC

**`Complex`**
- `__complex__`, `real`, `imag`, `__add__`, `__radd__`, `__neg__`, `__pos__`
- `__mul__`, `__rmul__`, `__truediv__`, `__rtruediv__`, `__pow__`, `__rpow__`
- `__abs__`, `__eq__`

**`Real`** (adds to Complex)
- `__float__`, `__trunc__`, `__floor__`, `__ceil__`, `__round__`
- `__floordiv__`, `__rfloordiv__`, `__mod__`, `__rmod__`
- `__lt__`, `__le__`
- (`real`/`imag` become trivial: `real = self`, `imag = 0`)

**`Rational`** (adds to Real)
- `numerator`, `denominator` (as properties)
- Default `__float__` is provided as `numerator / denominator`

**`Integral`** (adds to Rational)
- `__int__`, `__index__`
- `__pow__` with optional modulo third argument
- Bitwise ops: `__lshift__`, `__rshift__`, `__and__`, `__xor__`, `__or__`, `__invert__`
- Default `numerator = self`, `denominator = 1`

## Examples

**Example 1: Registering a third-party type without subclassing**
Input: You have `mpmath.mpf` or a custom C-extension float-like type you cannot modify to subclass `Real`.
Output:
```python
from numbers import Real
Real.register(mpmath.mpf)

isinstance(mpmath.mpf(1.5), Real)  # True
issubclass(mpmath.mpf, Real)       # True
```
Note: `register()` grants `isinstance`/`issubclass` compatibility only — it does NOT provide any of the mixin methods or operator implementations. The type must already implement the needed behavior itself.

**Example 2: Choosing the right ABC for a type check**
Input: Writing a function `def scale(x, factor)` that should accept any number type but reject non-numeric input, and must support both integer bit-shifting fast paths and general float fallback.
Output:
```python
from numbers import Integral, Complex

def scale(x, factor):
    if not isinstance(x, Complex):
        raise TypeError("x must be numeric")
    if isinstance(factor, Integral) and factor >= 0:
        # fast path only valid for non-negative integers
        return x * (1 << factor)
    return x * (2 ** factor)
```

**Example 3: Implementing a minimal custom Rational-like type**
Input: A `Money` class representing exact cents that should behave like a Rational.
Output:
```python
from numbers import Rational
from math import gcd

class Money(Rational):
    def __init__(self, cents, denom=1):
        g = gcd(cents, denom) or 1
        self._num = cents // g
        self._den = denom // g

    @property
    def numerator(self): return self._num
    @property
    def denominator(self): return self._den

    def __add__(self, other):
        return Money(self._num * other.denominator + other.numerator * self._den,
                      self._den * other.denominator)
    def __radd__(self, other): return self.__add__(other)
    # ... implement remaining Complex/Real abstract methods ...
```

## Best Practices

- **Check against the ABC, never the concrete type.** Use `isinstance(x, Integral)` instead of `isinstance(x, int)` so `numpy` ints, `Fraction`s used as integers, etc., aren't rejected.
- **Pick the most specific ABC that matches semantics**, not the most permissive. If your type has no meaningful ordering or is inherently complex-valued, stop at `Complex` — don't force `Real`.
- **Prefer subclassing over `register()`** when you control the code; subclassing gives you the default mixin implementations (e.g., `Rational.__float__`) for free. Use `register()` only for types you can't modify.
- **`hash()` consistency**: numbers that compare equal (e.g. `1 == 1.0 == Fraction(1,1) == (1+0j)`) should hash equally where the type supports hashing at all.
- **Implement `__eq__` to accept cross-tower comparisons** (e.g. your `Rational` type should equal a plain `int` or `float` with the same value), mirroring how `Fraction(2,1) == 2.0` works.

## Common Pitfalls

- **Registering a type without implementing arithmetic**: `register()` only affects `isinstance`/`issubclass`; calling `+`, `-`, etc. on the registered type still fails unless those dunder methods actually exist.
- **Subclassing `Integral` but forgetting `__index__`**: without it, your type can't be used as a sequence index or in `range()`, `bin()`, etc.
- **Assuming `Rational` implies exact base-10 decimal representation** — it means exact numerator/denominator representation, not decimal precision (that's `decimal.Decimal`, which deliberately does NOT register under this tower's `Real`/`Rational` due to differing semantics around exactness/precision).
- **Comparing `Decimal` and `float`/`Fraction` via the tower**: `decimal.Decimal` is intentionally not part of the numeric ABC tower (not registered as `Real`), so `isinstance(Decimal("1.5"), Real)` is `False` — don't assume it participates.
- **Forgetting `__hash__` when defining `__eq__`**: Python sets `__hash__` to `None` if you override `__eq__` without also defining `__hash__`, silently breaking use in sets/dicts.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: debugging-float-precision-issues
description: Diagnoses and fixes floating-point precision bugs in Python numeric code using the math module's specialized functions. Use when comparisons like `a == b` unexpectedly fail, accumulated sums drift from expected values, calculations near zero lose precision, or large-integer square roots produce wrong results.
---

## Quick Start

Bug report: "My test `assert total == 1.0` fails but `total` prints as `1.0`."

```python
import math

total = sum([0.1] * 10)
print(total)              # 1.0 (displayed, but actually 0.9999999999999999)
print(total == 1.0)       # False — the bug

# Fix: use fsum for accurate accumulation, isclose for comparison
total = math.fsum([0.1] * 10)
print(total == 1.0)       # True
```

## Workflow

Use this decision process when a numeric result is "wrong" but looks right:

Progress:
- [ ] Step 1: Reproduce — print `repr(x)` or `f"{x:.20f}"`, not `str(x)`, to see hidden precision error
- [ ] Step 2: Classify the bug (see decision tree below)
- [ ] Step 3: Apply the targeted fix
- [ ] Step 4: Re-verify with `math.isclose()` — never re-add a raw `==` check
- [ ] Step 5: Add a regression test using the same tolerance

### Decision Tree

**Symptom: equality comparison fails unexpectedly**
→ Never compare floats with `==`. Use `math.isclose(a, b, rel_tol=1e-9)`.
- If comparing against zero, `rel_tol` is useless (relative to 0 is always 0) — pass `abs_tol` explicitly: `math.isclose(x, 0, abs_tol=1e-9)`.

**Symptom: summing many floats drifts from the mathematically exact answer**
→ Built-in `sum()` accumulates rounding error one addition at a time. Replace with `math.fsum()`, which uses Shewchuk's algorithm for a correctly-rounded result.
```python
values = [1e16, 1.0, -1e16]
sum(values)        # 0.0  (wrong — 1.0 got lost)
math.fsum(values)  # 1.0  (correct)
```

**Symptom: `int(math.sqrt(n))` gives the wrong integer for large n**
→ `math.sqrt` converts to float, which loses precision above ~2^53. Use `math.isqrt(n)` for exact integer results, no float roundtrip.
```python
n = 10**30
int(math.sqrt(n)) ** 2 == n   # False — precision lost
math.isqrt(n) ** 2 <= n       # True — isqrt is exact
```

**Symptom: computing `exp(x) - 1` or `log(1 + x)` for small x gives noisy/zero results**
→ Catastrophic cancellation: subtracting two nearly-equal large-magnitude floats destroys precision. Use `math.expm1(x)` and `math.log1p(x)`, which compute these directly without the cancellation step.
```python
x = 1e-15
math.exp(x) - 1     # 1.1102230246251565e-15 (noisy, wrong-ish)
math.expm1(x)       # 1.0000000000000007e-15 (accurate)
```

**Symptom: combinatorics or factorial results overflow or lose precision**
→ Don't compute `n! / (k! * (n-k)!)` manually with floats. Use `math.comb(n, k)` / `math.perm(n, k)`, which stay in exact integer arithmetic.

**Symptom: distance/norm calculation is unstable for very large or small coordinates**
→ Manual `sqrt(x**2 + y**2)` can overflow/underflow for extreme values. Use `math.hypot(x, y, ...)`, which scales internally to avoid overflow.

## Examples

**Example 1: Financial-style running total that never quite hits zero**

Input:
```python
balance = 0.0
for amount in [10.10, -3.30, -6.80]:
    balance += amount
print(balance == 0.0)   # expected True, got False
```
Diagnosis: repeated `+=` on floats accumulates rounding error.
Output (fix):
```python
import math
balance = math.fsum([10.10, -3.30, -6.80])
print(math.isclose(balance, 0.0, abs_tol=1e-9))  # True
```

**Example 2: Integer square root for cryptography-scale numbers**

Input:
```python
n = 123456789123456789123456789123456789
root = int(n ** 0.5)
print(root * root <= n)   # False — overflowed float precision
```
Output (fix):
```python
import math
root = math.isqrt(n)
print(root * root <= n)          # True
print((root + 1) ** 2 > n)       # True — confirms floor sqrt is correct
```

**Example 3: Probability computed as ratio of factorials blows up**

Input:
```python
n, k = 1000, 500
p = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
# works but wastefully computes huge intermediate factorials
```
Output (fix):
```python
import math
p = math.comb(n, k)   # same result, computed more efficiently, no huge intermediates
```

## Best Practices

- Treat `==` on floats as a code smell during review — always ask "should this be `isclose`?"
- When precision matters near zero, always set `abs_tol` explicitly in `isclose`; the default `abs_tol=0.0` makes the check meaningless there.
- Prefer `math.fsum` over `sum` in any loop that accumulates more than a handful of floats, especially in financial or scientific accumulation code.
- Prefer `math.isqrt`, `math.comb`, `math.perm` over float-based equivalents whenever inputs are integers — they avoid the float precision ceiling (~2^53) entirely.
- For values near a singularity (x near 0 in exp/log), reach for `expm1`/`log1p` before assuming a bug elsewhere.

## Common Pitfalls

- Don't "fix" a float bug by rounding with `round(x, 2)` — this masks the symptom without addressing accumulated error, and can reintroduce bugs at different scales.
- Don't use `math.isclose()` with defaults when comparing to zero — it will always return `False` for any nonzero `a` since relative tolerance scales with the compared values.
- Don't convert large integers to float for sqrt/pow just for convenience — verify the magnitude first (`n.bit_length() > 53` is a red flag) and switch to `math.isqrt`.
- Don't assume `math.fsum` is needed everywhere — for small lists of similar-magnitude numbers, the overhead isn't worth it; reserve it for precision-sensitive accumulation.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-math-integer-operations
description: Provides guidance on using Python's integer-related mathematical functions and operations (from the math module and built-in integer arithmetic). Use when performing operations like GCD/LCM computation, integer square roots, factorial calculations, bit-length analysis, or exact integer arithmetic in Python.
---

## Quick Start

```python
import math

# Greatest common divisor / least common multiple
math.gcd(48, 18)          # 6
math.lcm(4, 6)            # 12

# Integer square root (floor of sqrt)
math.isqrt(50)            # 7

# Factorial
math.factorial(5)         # 120

# Combinatorics
math.comb(5, 2)           # 10  (combinations)
math.perm(5, 2)           # 20  (permutations)

# Integer bit length
(255).bit_length()        # 8
(255).bit_count()         # 8  (number of set bits)
```

## Workflow

Progress:
- [ ] Identify whether the task needs exact integer math (avoid float rounding issues)
- [ ] Choose the correct function: `gcd`/`lcm` for divisibility, `isqrt` for roots, `factorial`/`comb`/`perm` for counting
- [ ] Validate input types — these functions require non-negative integers (raise `ValueError` on negatives where applicable)
- [ ] Use built-in `int` methods (`bit_length`, `bit_count`) for binary-level analysis instead of manual bit-shifting loops
- [ ] Test edge cases: zero, one, and large numbers (Python ints are arbitrary precision, so no overflow — but performance may degrade)

## Examples

**Example 1:**
Input: Find the GCD and LCM of 24 and 36.
Output:
```python
math.gcd(24, 36)  # 12
math.lcm(24, 36)  # 72
```

**Example 2:**
Input: Compute the integer square root of 99 without floating-point error.
Output:
```python
math.isqrt(99)  # 9  (since 9*9=81 <= 99 < 100=10*10)
```

**Example 3:**
Input: Count how many ways to choose 3 items from 7 (combinations), and how many ordered arrangements (permutations).
Output:
```python
math.comb(7, 3)  # 35
math.perm(7, 3)  # 210
```

**Example 4:**
Input: Determine the number of bits needed to represent 1023 in binary.
Output:
```python
(1023).bit_length()  # 10
```

## Best Practices

- Prefer `math.isqrt()` over `int(math.sqrt(n))` for exact results on large integers — floating-point `sqrt` loses precision beyond ~2^53.
- Use `math.gcd(*args)` with multiple arguments to compute GCD across more than two numbers at once.
- Use `math.comb`/`math.perm` instead of manually computing factorials and dividing — they're faster and avoid intermediate overflow-like slowdowns.
- For bitwise integer inspection, prefer `int.bit_length()` and `int.bit_count()` over string conversion (`bin()`) or manual loops.
- Remember Python integers have arbitrary precision — no need for overflow checks, but be mindful of performance with very large numbers (e.g., `factorial(100000)`).

## Common Pitfalls

- Don't pass negative numbers to `math.isqrt()`, `math.factorial()`, `math.comb()`, or `math.perm()` — they raise `ValueError`.
- Don't use `math.sqrt(n) ** 2 == n` to check perfect squares — use `math.isqrt(n) ** 2 == n` instead to avoid float precision errors.
- Don't confuse `math.comb(n, k)` (order doesn't matter) with `math.perm(n, k)` (order matters).
- Don't manually implement GCD/LCM with loops — the built-in `math.gcd`/`math.lcm` are optimized (C-implemented) and handle edge cases like zero correctly (`gcd(0, 0) == 0`).
- Don't assume `bit_length()` counts set bits — it returns the number of bits needed to represent the number, not the population count (use `bit_count()` for that).
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: computing-complex-math
description: Performs mathematical operations on complex numbers using Python's cmath module, including trigonometric, hyperbolic, exponential, logarithmic, and polar/rectangular conversions. Use when working with complex numbers, solving equations with negative square roots, signal processing math, or when math module functions raise errors on complex inputs.
---

## Quick Start

```python
import cmath

# Basic operations
cmath.sqrt(-1)              # 1j
cmath.exp(1j * cmath.pi)    # -1+1.2246e-16j (Euler's identity)
cmath.log(1j)               # 1.5707963267948966j

# Polar conversion
z = 3 + 4j
r, phi = cmath.polar(z)     # (5.0, 0.9272952180016122)
z2 = cmath.rect(r, phi)     # (3+4j) reconstructed
```

## Workflow

Progress:
- [ ] Identify if input/output involves complex numbers (vs. real-only `math` module)
- [ ] Choose the right function category (conversion, power/log, trig, hyperbolic, classification)
- [ ] Handle edge cases (infinities, NaN) if inputs may be non-finite
- [ ] Verify results with `isclose()` instead of `==` for float comparisons

### Function Categories

**Conversions to/from polar coordinates:**
```python
cmath.phase(z)          # argument (angle) of z, range (-pi, pi]
cmath.polar(z)          # returns (r, phi) tuple
cmath.rect(r, phi)      # builds complex number from polar coords
```

**Power and logarithmic functions:**
```python
cmath.exp(z)            # e**z
cmath.log(z)            # natural log; cmath.log(z, base) for other bases
cmath.log10(z)          # base-10 log
cmath.sqrt(z)           # square root, principal branch
```

**Trigonometric functions:**
```python
cmath.sin(z), cmath.cos(z), cmath.tan(z)
cmath.asin(z), cmath.acos(z), cmath.atan(z)
```

**Hyperbolic functions:**
```python
cmath.sinh(z), cmath.cosh(z), cmath.tanh(z)
cmath.asinh(z), cmath.acosh(z), cmath.atanh(z)
```

**Classification functions:**
```python
cmath.isfinite(z)       # True if both real and imag parts finite
cmath.isinf(z)          # True if either part is infinite
cmath.isnan(z)          # True if either part is NaN
cmath.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)  # safe comparison
```

**Constants:**
```python
cmath.pi, cmath.e, cmath.tau, cmath.inf, cmath.infj, cmath.nan, cmath.nanj
```

## Examples

**Example 1: Solving a quadratic with negative discriminant**
Input: Solve `x^2 + 2x + 5 = 0` (discriminant = -16)
Output:
```python
import cmath
a, b, c = 1, 2, 5
disc = b**2 - 4*a*c
x1 = (-b + cmath.sqrt(disc)) / (2*a)
x2 = (-b - cmath.sqrt(disc)) / (2*a)
# x1 = (-1+2j), x2 = (-1-2j)
```

**Example 2: Converting rectangular to polar and back**
Input: `z = 1 + 1j`
Output:
```python
r, phi = cmath.polar(z)   # (1.4142135623730951, 0.7853981633974483)
cmath.rect(r, phi)        # (1.0000000000000002+0.9999999999999999j)
```

**Example 3: Checking for special values**
Input: `z = complex(cmath.inf, 0)`
Output: `cmath.isinf(z)` → `True`; `cmath.isfinite(z)` → `False`

## Best Practices

- Use `cmath` instead of `math` whenever a value could be negative under a square root/log, or whenever inputs are already typed as `complex`.
- Always use `cmath.isclose()` for equality checks — never compare complex floats with `==`.
- `cmath.phase(z)` returns radians in `(-pi, pi]`; convert to degrees with `math.degrees()` if needed.
- Prefer `cmath.rect(r, phi)` over manually computing `r * (cos(phi) + 1j*sin(phi))`.
- Remember `cmath.sqrt` and `cmath.log` return the **principal branch** — expect one specific root/value, not all solutions.

## Common Pitfalls

- Don't use `math.sqrt()` on a value that might be negative — it raises `ValueError`; use `cmath.sqrt()` instead.
- Don't assume `cmath.phase(0j)` is meaningful — phase of zero is `0.0` but is mathematically undefined; treat with care in downstream logic.
- Don't forget that `cmath` functions always return `complex` type, even when the mathematical result is real (e.g., `cmath.sqrt(4)` returns `(2+0j)`, not `2.0`).
- Don't use `==` to compare `nan` components — `cmath.isnan(z)` follows IEEE 754 semantics where `nan != nan`.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-decimal-arithmetic
description: Provides guidance on Python's decimal module for exact decimal floating-point arithmetic. Use when precise decimal representation is required (financial calculations, currency, tax computations), when binary floating-point rounding errors are unacceptable, or when explicit control over precision, rounding modes, and significant figures is needed.
---

# Using Decimal Arithmetic

## Quick Start

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Create Decimals from strings (not floats!) for exactness
price = Decimal("19.99")
tax_rate = Decimal("0.075")

tax = (price * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
total = price + tax

print(total)  # Decimal('21.49')

# Compare: float arithmetic introduces error
print(0.1 + 0.2)          # 0.30000000000000004
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
```

## Workflow

Progress:
- [ ] Step 1: Identify why float is insufficient (money, exact decimal rules, auditability)
- [ ] Step 2: Construct Decimals from strings or integers, never from floats directly
- [ ] Step 3: Set global context precision if defaults (28 digits) are insufficient
- [ ] Step 4: Perform arithmetic — operators (`+`, `-`, `*`, `/`) work naturally
- [ ] Step 5: Round/quantize results to the desired number of decimal places
- [ ] Step 6: Choose an explicit rounding mode matching business/legal requirements
- [ ] Step 7: Handle exceptional conditions (DivisionByZero, InvalidOperation, Overflow) if inputs are untrusted
- [ ] Step 8: Use `localcontext()` for temporary precision/rounding changes scoped to a block

### Step 1: Constructing Decimals correctly

```python
# CORRECT — exact
d1 = Decimal("0.1")
d2 = Decimal(10)
d3 = Decimal((0, (3, 1, 4), -2))  # sign, digits tuple, exponent -> 3.14

# WRONG — inherits binary float imprecision
d_bad = Decimal(0.1)  # Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

### Step 2: Setting precision

```python
from decimal import getcontext

getcontext().prec = 50  # global precision (significant digits), default 28
```

### Step 3: Scoped precision with localcontext

```python
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 6
    result = Decimal(1) / Decimal(7)  # only affects this block
# outside the block, precision reverts to previous setting
```

### Step 4: Rounding and quantizing

```python
from decimal import (
    ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP, ROUND_HALF_EVEN,
    ROUND_DOWN, ROUND_UP, ROUND_05UP
)

value = Decimal("2.675")
value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)   # 2.68
value.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)  # 2.67 (banker's rounding, module default)
```

### Step 5: Handling exceptions

```python
from decimal import Decimal, DivisionByZero, InvalidOperation, localcontext

with localcontext() as ctx:
    ctx.traps[DivisionByZero] = True  # raise instead of returning Infinity
    try:
        Decimal(1) / Decimal(0)
    except DivisionByZero:
        print("cannot divide by zero")
```

## Examples

**Example 1: Currency total with tax**
Input:
```python
items = [Decimal("12.50"), Decimal("7.25"), Decimal("3.10")]
subtotal = sum(items)
tax = (subtotal * Decimal("0.08")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```
Output:
```
subtotal = Decimal('22.85')
tax = Decimal('1.83')
```

**Example 2: Setting precision for scientific-style computation**
Input:
```python
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 10
    result = Decimal(22) / Decimal(7)
```
Output:
```
result = Decimal('3.142857143')
```

**Example 3: Comparing Decimal to float safely**
Input:
```python
Decimal("0.1") == 0.1
```
Output:
```
False  # never mix Decimal and float directly in comparisons/arithmetic;
       # convert float via str first: Decimal(str(0.1))
```

## Best Practices

- Always construct `Decimal` from a **string** or **integer**; converting from `float` propagates binary imprecision.
- Use `quantize()` for fixed-point rounding to a specific number of decimal places (e.g., cents).
- Prefer `ROUND_HALF_UP` for typical financial rounding, `ROUND_HALF_EVEN` (default) for statistically unbiased rounding.
- Use `localcontext()` to scope temporary precision/rounding changes instead of mutating the global context permanently.
- Set `prec` high enough for intermediate calculations; only round/quantize the final displayed or stored value.
- Never mix `Decimal` and `float` in arithmetic or equality comparisons — convert explicitly first.
- Use `Decimal.is_nan()`, `.is_infinite()`, `.is_zero()` for safe special-value checks instead of comparisons.
- For serialization, use `str(decimal_value)` to preserve exact representation.

## Common Pitfalls

- Passing a `float` literal to `Decimal()` (e.g., `Decimal(0.1)`) — silently imports float's imprecision.
- Forgetting that `getcontext().prec` sets **significant digits**, not decimal places — use `quantize()` for decimal-place control.
- Assuming `round()` behaves like `quantize()` — `round()` on Decimal follows context rounding but doesn't fix exponent/decimal places the same way.
- Ignoring `InvalidOperation`, `Overflow`, or `DivisionByZero` traps when processing untrusted input, causing NaN/Infinity to propagate silently.
- Mutating the global context (`getcontext().prec = X`) instead of using `localcontext()`, causing precision leaks across unrelated code.
- Comparing `Decimal` and `float` directly, which can raise errors or produce misleading equality results.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-python-fractions
description: Provides exact rational number arithmetic using Python's fractions module. Use when precise fractional calculations are needed, avoiding floating-point rounding errors, or converting between decimals/floats and exact ratios.
---

## Quick Start

```python
from fractions import Fraction

# Create fractions
f1 = Fraction(1, 3)          # 1/3
f2 = Fraction('3.14')        # 157/50 (from decimal string)
f3 = Fraction('22/7')        # from string ratio
f4 = Fraction(0.5)           # 1/2 (exact binary float conversion)
f5 = Fraction(Decimal('1.1'))  # from Decimal, exact

# Arithmetic stays exact
result = Fraction(1, 3) + Fraction(1, 6)  # Fraction(1, 2)
print(result)  # 1/2
```

## Workflow

1. **Choose the right constructor input**
   - `Fraction(numerator, denominator)` — two integers, auto-reduced via GCD
   - `Fraction(other_fraction)` — copy
   - `Fraction(float)` — exact value of the float (not the "nice" decimal you'd expect)
   - `Fraction(decimal.Decimal)` — exact value, preferred over float for decimal-like input
   - `Fraction(string)` — parses `"3/4"`, `"-3/4"`, `"1.5"`, `"1.5e3"`, with optional whitespace and underscores in numbers

2. **Use arithmetic operators normally** — `+ - * / **` all return `Fraction` (or complex/float when mixed with those types).

3. **Access components** when needed:
   ```python
   f = Fraction(6, 8)   # auto-reduces to Fraction(3, 4)
   f.numerator          # 3
   f.denominator        # 4
   ```

4. **Convert to/from other numeric types**:
   ```python
   float(Fraction(1, 3))          # 0.3333333333333333
   Fraction(1, 3).limit_denominator(10)  # Fraction(1, 3) — best approx with denom <= 10
   f.as_integer_ratio()           # (3, 4)
   ```

5. **Round, floor, ceil** — Fractions support `round()`, `math.floor()`, `math.ceil()`, `math.trunc()` natively.

## Examples

**Example 1: Avoiding float imprecision**
Input:
```python
0.1 + 0.2 == 0.3  # False due to float rounding
Fraction('0.1') + Fraction('0.2') == Fraction('0.3')
```
Output: `True` — exact decimal-string parsing avoids binary float error.

**Example 2: Approximating an irrational-ish float as a simple fraction**
Input:
```python
import math
Fraction(math.pi).limit_denominator(1000)
```
Output: `Fraction(355, 113)` — best rational approximation with denominator ≤ 1000.

**Example 3: Parsing user input safely**
Input:
```python
Fraction("  -3/4 ")
Fraction("1_000/2_000")
```
Output: `Fraction(-3, 4)`, `Fraction(1, 2)`

**Example 4: GCD reduction happens automatically**
Input: `Fraction(10, 4)`
Output: `Fraction(5, 2)`

## Best Practices

- Always construct `Fraction` from a **string** or **Decimal** when the source is a decimal literal you typed (e.g., `Fraction('1.1')`), never `Fraction(1.1)`, unless you specifically want the float's exact (ugly) binary value.
- Use `.limit_denominator(max_denominator)` to get human-friendly approximations, e.g. for displaying measurements.
- Fractions are hashable and immutable — safe to use as dict keys or in sets.
- Comparisons (`<`, `==`, etc.) work exactly against `int`, `float`, `Decimal`, and other `Fraction`s.
- For repeated heavy numeric computation, convert to `float` or `Decimal` at the boundary — `Fraction` arithmetic is exact but slower due to GCD reduction on every operation.

## Common Pitfalls

- **`Fraction(0.1)` is NOT `Fraction(1, 10)`** — it's the exact (ugly) binary representation of the float `0.1`, e.g. `Fraction(3602879701896397, 36028797018963968)`. Use `Fraction('0.1')` instead.
- Don't assume `numerator`/`denominator` reflect what you passed in — they're always stored in lowest terms with a positive denominator.
- Division by zero raises `ZeroDivisionError`, same as normal Python numbers.
- Mixing `Fraction` with `float` in arithmetic returns a `float` (losing exactness) — keep operations within `Fraction`/`Decimal`/`int` to stay exact.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: using-random-module
description: Generates pseudo-random numbers and performs random selections, shuffling, and sampling using Python's random module. Use when implementing randomization, simulations, games, sampling algorithms, or testing scenarios that require reproducible or non-reproducible random behavior.
---

## Quick Start

```python
import random

# Random float in [0.0, 1.0)
random.random()

# Random integer in inclusive range
random.randint(1, 10)

# Random choice from a sequence
random.choice(['rock', 'paper', 'scissors'])

# Shuffle a list in place
deck = list(range(52))
random.shuffle(deck)

# Sample without replacement
random.sample(range(100), k=5)

# Reproducible results
random.seed(42)
```

## Workflow

Progress:
- [ ] Identify the randomization need (number, choice, sequence, distribution)
- [ ] Pick the correct function (see table below)
- [ ] Seed the generator if reproducibility is required (tests, simulations)
- [ ] Use `secrets` instead if cryptographic security is needed
- [ ] Validate ranges/inputs (e.g., `k <= len(population)` for `sample`)

### Function Reference

| Goal | Function | Notes |
|---|---|---|
| Float in [0.0, 1.0) | `random.random()` | Base generator |
| Float in [a, b] | `random.uniform(a, b)` | |
| Int in [a, b] inclusive | `random.randint(a, b)` | |
| Int in range with step | `random.randrange(start, stop, step)` | |
| Single random element | `random.choice(seq)` | Raises `IndexError` if empty |
| Multiple elements w/ replacement | `random.choices(population, weights=None, k=1)` | Supports weights |
| Unique elements w/o replacement | `random.sample(population, k)` | `k` must be ≤ population size |
| Shuffle in place | `random.shuffle(seq)` | Mutates list; no return value |
| Gaussian/normal distribution | `random.gauss(mu, sigma)` or `random.normalvariate(mu, sigma)` | |
| Other distributions | `random.expovariate`, `random.betavariate`, `random.gammavariate`, `random.lognormvariate`, `random.triangular`, `random.vonmisesvariate`, `random.weibullvariate` | |
| Reproducibility | `random.seed(a=None)` | Same seed → same sequence |
| Save/restore state | `random.getstate()` / `random.setstate(state)` | |
| Independent generator instance | `random.Random(seed)` | Use when isolating streams (e.g., multithreading) |
| Cryptographically secure random | Use `secrets` module instead | `random` is NOT secure for security tokens/passwords |

## Examples

**Example 1: Reproducible shuffle for testing**
Input:
```python
import random
random.seed(0)
items = ['a', 'b', 'c', 'd']
random.shuffle(items)
print(items)
```
Output: `['b', 'a', 'd', 'c']` (deterministic given seed 0; exact output depends on Python version)

**Example 2: Weighted random choice**
Input:
```python
import random
random.seed(1)
random.choices(['red', 'green', 'blue'], weights=[10, 1, 1], k=5)
```
Output: `['red', 'red', 'blue', 'red', 'green']` (red heavily favored due to weight)

**Example 3: Sampling without replacement**
Input:
```python
import random
random.seed(2)
random.sample(range(1, 50), k=6)  # lottery-style draw
```
Output: `[27, 15, 45, 8, 33, 3]` (6 unique numbers, no duplicates)

## Best Practices

- Always seed (`random.seed(n)`) in tests and simulations that need reproducible output.
- Use `random.sample()` for unique picks; use `random.choices()` when duplicates/weights are needed.
- Use `random.Random()` instances to create isolated generators for concurrent/multithreaded code instead of the global default instance.
- Prefer `secrets.token_hex()`, `secrets.choice()`, etc. for tokens, passwords, or anything security-sensitive.
- For large populations, `random.sample()` is more memory-efficient than shuffling the entire population.

## Common Pitfalls

- **Do NOT use `random` for cryptography** — it is a Mersenne Twister PRNG, predictable and unsuitable for security purposes. Use `secrets` instead.
- **Do NOT call `random.sample()` with `k > len(population)`** — raises `ValueError`.
- **Do NOT expect `random.shuffle()` to return a value** — it shuffles in place and returns `None`.
- **Do NOT forget that unseeded runs differ every execution** — seed explicitly when deterministic output matters (tests, reproducible research).
- **Avoid reusing the same seed across unrelated randomization calls** — this can introduce unintended correlations between "independent" random draws.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

---
name: computing-statistics
description: Computes descriptive and inferential statistics on numeric data using Python's built-in statistics module. Use when calculating averages, medians, variance, standard deviation, correlation, regression, or distributions without requiring NumPy/pandas dependencies.
---

# Computing Statistics with Python's `statistics` Module

## Quick Start

```python
import statistics as stats

data = [2.5, 3.6, 4.1, 4.1, 5.8, 6.2, 7.0]

stats.mean(data)        # 4.757142857142857
stats.median(data)      # 4.1
stats.mode(data)        # 4.1
stats.stdev(data)       # sample standard deviation
stats.variance(data)    # sample variance
```

Use this module for quick, dependency-free statistical calculations on small-to-medium datasets. For heavy numerical work (large arrays, matrix ops), prefer NumPy/SciPy instead.

## Workflow

Progress:
- [ ] Step 1: Identify whether data is a full population or a sample
- [ ] Step 2: Choose the right averaging function (mean, median, mode, or variants)
- [ ] Step 3: Choose variance/stdev function matching population vs sample
- [ ] Step 4: Handle multiple datasets (correlation, covariance, linear regression) if needed
- [ ] Step 5: Consider `NormalDist` for distribution-based calculations
- [ ] Step 6: Validate results and handle edge cases (empty data, single value, non-numeric input)

### Step 1: Population vs Sample

- **Sample** (subset of a larger population, most common case): use `stdev`, `variance`
- **Population** (complete dataset): use `pstdev`, `pvariance`

### Step 2: Averages

| Function | Use case |
|---|---|
| `mean(data)` | Arithmetic mean |
| `fmean(data, weights=None)` | Faster float-based mean, supports weights (3.11+) |
| `geometric_mean(data)` | Mean of ratios/growth rates |
| `harmonic_mean(data, weights=None)` | Rates (e.g. speed, price/earnings) |
| `median(data)` | Middle value, robust to outliers |
| `median_low(data)` / `median_high(data)` | Median with even-length tie-breaking |
| `mode(data)` | Most common value |
| `multimode(data)` | All values tied for most common |

### Step 3: Spread

| Function | Use case |
|---|---|
| `variance(data, xbar=None)` | Sample variance |
| `stdev(data, xbar=None)` | Sample standard deviation |
| `pvariance(data, mu=None)` | Population variance |
| `pstdev(data, mu=None)` | Population standard deviation |

Pass a precomputed mean via `xbar`/`mu` to avoid recomputation across multiple calls.

### Step 4: Relationships Between Datasets

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

stats.covariance(x, y)              # joint variability
stats.correlation(x, y)             # Pearson correlation, -1 to 1
stats.correlation(x, y, method="ranked")  # Spearman rank correlation (3.12+)
stats.linear_regression(x, y)       # LinearRegression(slope, intercept)
```

### Step 5: Distributions with `NormalDist`

```python
from statistics import NormalDist

nd = NormalDist.from_samples(data)   # fit from data
nd = NormalDist(mu=100, sigma=15)    # or specify directly

nd.pdf(110)          # probability density at x
nd.cdf(110)          # P(X <= 110)
nd.inv_cdf(0.95)     # value at 95th percentile
nd.zscore(120)       # standardized score

# Combining/comparing distributions
nd1 = NormalDist(90, 12)
nd2 = NormalDist(100, 15)
(nd1 + nd2)                      # sum of independent normals
nd1.overlap(nd2)                 # overlap coefficient (0-1)
```

Also available: `quantiles(data, n=4)` for quartiles/percentiles without fitting a full distribution.

### Step 6: Edge Cases

- Empty data → raises `StatisticsError`
- `mode`/`multimode` work on any hashable data, not just numbers
- Functions accept `Decimal` and `Fraction` for exact arithmetic
- `variance`/`stdev` require at least 2 data points (sample stats need N-1 denominator)

## Examples

**Example 1: Grade analysis (sample stats)**
Input:
```python
grades = [88, 92, 79, 93, 85, 91, 76]
```
Output:
```python
stats.mean(grades)    # 86.28571428571429
stats.median(grades)  # 88
stats.stdev(grades)   # 6.626...
```

**Example 2: Quartile-based outlier detection**
Input:
```python
data = [5, 7, 8, 8, 9, 10, 12, 13, 100]
q1, q2, q3 = stats.quantiles(data, n=4)
```
Output:
```
q1 ≈ 7.5, q2 (median) = 9, q3 ≈ 12.5
# Values far beyond [q1 - 1.5*IQR, q3 + 1.5*IQR] flagged as outliers (e.g., 100)
```

**Example 3: Probability from a fitted normal distribution**
Input:
```python
heights = [168, 172, 175, 180, 165, 170, 178]
nd = stats.NormalDist.from_samples(heights)
p = nd.cdf(175)
```
Output:
```
p ≈ probability that a random height in this distribution is <= 175 cm
```

## Best Practices

- Use `fmean` instead of `mean` when data is all floats and speed matters.
- Prefer `median` over `mean` for skewed data or when outliers are present.
- Always match variance/stdev function to whether data is a sample or full population.
- Use `Fraction`/`Decimal` inputs when exact (non-floating-point) results are required.
- Reuse precomputed `xbar`/`mu` when calling variance/stdev repeatedly on the same dataset.
- For anything beyond simple stats (large-scale numerical computing, hypothesis testing, ANOVA), switch to NumPy/SciPy/pandas.

## Common Pitfalls

- Don't use `stdev`/`variance` (sample versions) when data represents the entire population — use `pstdev`/`pvariance` instead.
- Don't call statistics functions on empty lists — check length first or catch `StatisticsError`.
- Don't assume `mode` always returns one value — ties return the first encountered; use `multimode` for all ties.
- Don't confuse `correlation`'s default (Pearson, linear relationships) with ranked/Spearman correlation needed for monotonic but non-linear relationships.
- Don't manually reimplement mean/stdev with floating-point loops — this module handles precision issues (e.g., using exact fractions internally) better than naive code.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---

