---
name: working-with-binary-data
description: Provides guidance on Python's binary data handling modules (struct, pickle, copyreg, shelve, marshal) for converting between Python objects and binary representations. Use when packing/unpacking C structs, serializing objects, persisting data to disk, or working with binary file formats and network protocols.
---

## Quick Start

```python
import struct

# Pack integers into binary data (big-endian, 2 ints)
packed = struct.pack('>2i', 1, 2)  # b'\x00\x00\x00\x01\x00\x00\x00\x02'

# Unpack binary data back to Python values
values = struct.unpack('>2i', packed)  # (1, 2)

# Serialize any Python object with pickle
import pickle
data = pickle.dumps({'key': 'value', 'nums': [1, 2, 3]})
obj = pickle.loads(data)
```

## Workflow

Choose the right module based on the task:

Progress:
- [ ] Identify data source/target: fixed-format binary (C structs, network protocols) vs. arbitrary Python objects
- [ ] Choose module: `struct` for binary layouts, `pickle` for object serialization, `shelve` for persistent dict-like storage, `marshal` only for internal .pyc use (never for untrusted/external data)
- [ ] For custom classes with `pickle`, implement `__reduce__` or register with `copyreg` if default pickling fails
- [ ] Define format strings (`struct`) or protocol version (`pickle`)
- [ ] Handle byte order, size, and alignment explicitly for `struct`
- [ ] Never unpickle data from untrusted sources — treat like `eval()`

### struct — Binary layouts

Format strings define byte order + field types:

| Char | Byte order | Size/align |
|------|-----------|-----------|
| `@`  | native    | native, aligned (default) |
| `=`  | native    | standard, no align |
| `<`  | little-endian | standard, no align |
| `>`  | big-endian | standard, no align |
| `!`  | network (big-endian) | standard, no align |

Common format codes: `b`/`B` (signed/unsigned char), `h`/`H` (short), `i`/`I` (int), `l`/`L` (long), `q`/`Q` (long long), `f`/`d` (float/double), `s` (char array), `?` (bool).

```python
struct.pack('<3sB', b'abc', 255)     # bytes with prefix count
struct.calcsize('>4i')               # size in bytes without packing
struct.unpack_from(buffer, offset=0) # unpack from a slice of a larger buffer
```

Use `struct.Struct(fmt)` when reusing the same format repeatedly — precompiles it for speed.

### pickle — Object serialization

```python
with open('data.pkl', 'wb') as f:
    pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('data.pkl', 'rb') as f:
    obj = pickle.load(f)
```

- Use `pickle.HIGHEST_PROTOCOL` unless cross-version compatibility is required.
- Not all objects are picklable by default (open files, sockets, lambdas, some C extension objects). Implement `__getstate__`/`__setstate__` or `__reduce__` on the class.

### copyreg — Extending pickle for classes you don't control

```python
import copyreg

def pickle_point(p):
    return (Point, (p.x, p.y))

copyreg.pickle(Point, pickle_point)
```

### shelve — Persistent dict-backed storage

```python
import shelve

with shelve.open('mydata') as db:
    db['key'] = {'complex': 'object'}
    value = db['key']
```

Values are pickled automatically; keys must be strings.

### marshal — Internal use only

Reserved for Python's own `.pyc` bytecode serialization. Not stable across versions, not safe for untrusted input. **Do not use for application-level serialization — use `pickle` instead.**

## Examples

**Example 1: Parsing a binary file header**
Input: A binary file starts with a 4-byte magic number, 2-byte version (uint16), 4-byte length (uint32), all big-endian.
Output:
```python
import struct
HEADER_FMT = '>4sHI'
HEADER_SIZE = struct.calcsize(HEADER_FMT)  # 10 bytes

with open('file.bin', 'rb') as f:
    magic, version, length = struct.unpack(HEADER_FMT, f.read(HEADER_SIZE))
```

**Example 2: Caching computed results to disk across runs**
Input: An expensive function whose results should persist between program executions, keyed by input string.
Output:
```python
import shelve

def get_cached(key, compute_fn):
    with shelve.open('cache.db') as db:
        if key not in db:
            db[key] = compute_fn(key)
        return db[key]
```

**Example 3: Deep-copying a complex nested object graph**
Input: An object with circular references and custom classes that needs a full deep copy.
Output:
```python
import pickle
def deep_copy(obj):
    return pickle.loads(pickle.dumps(obj))
```

## Best Practices

- Prefer explicit byte order (`<`, `>`, `!`) over `@`/native to ensure portability across machines.
- Use `struct.Struct` objects for repeated pack/unpack in hot loops.
- Always open files in binary mode (`'rb'`/`'wb'`) when working with `struct` or `pickle`.
- For network protocols, use `!` (network byte order = big-endian) by convention.
- Version your pickle protocol explicitly in long-lived storage formats to control forward/backward compatibility.
- Use `shelve` for simple persistent key-value needs; use `sqlite3` or a database for anything requiring queries or concurrent access.

## Common Pitfalls

- **Never `pickle.load()` untrusted or unauthenticated data** — arbitrary code execution risk, equivalent to `eval()`.
- Forgetting struct alignment/padding differences between `@` (native, padded) and `<`/`>`/`=` (no padding) causes size mismatches.
- Mixing up format string repeat counts, e.g. `'3s'` (one 3-byte string) vs `'sss'` (three 1-byte strings).
- Using `marshal` for application data persistence — it's undocumented/unstable across Python versions.
- Forgetting `shelve` requires closing (or using `with`) to flush writes to disk.
- Assuming all Python objects are picklable by default — sockets, file handles, generators, and some lambdas are not.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---
---
name: packing-binary-data-with-struct
description: Converts between Python values and C-style packed binary data using the struct module. Use when reading/writing binary file formats, parsing network protocols, interfacing with C structs, or handling fixed-layout binary blobs.
---

## Quick Start

```python
import struct

# Pack: 1 unsigned short, 1 signed int, 4-byte string
data = struct.pack('>Hi4s', 512, -42, b'ABCD')

# Unpack back
h, i, s = struct.unpack('>Hi4s', data)
# h=512, i=-42, s=b'ABCD'

# Calculate size before allocating buffers
size = struct.calcsize('>Hi4s')  # 10
```

## Workflow

Progress:
- [ ] Identify the binary layout (field order, types, sizes) — from spec/docs/C struct definition
- [ ] Choose byte order/alignment prefix
- [ ] Build the format string
- [ ] Pack or unpack; verify with `calcsize`
- [ ] Handle variable-length data (strings, arrays) explicitly
- [ ] Test round-trip (pack → unpack → compare)

### 1. Choose byte order & alignment prefix

| Prefix | Byte order | Size | Alignment |
|--------|-----------|------|-----------|
| `@` (default) | native | native | native (padded) |
| `=` | native | standard | none |
| `<` | little-endian | standard | none |
| `>` | big-endian | standard | none |
| `!` | network (big-endian) | standard | none |

**Default recommendation:** use `<` or `>` explicitly (never rely on `@`) when the data is persisted to disk or sent over a network — native alignment causes portability bugs.

### 2. Map format characters

| Char | C type | Python type | Size |
|------|--------|-------------|------|
| `x` | pad byte | none | 1 |
| `c` | char | bytes (len 1) | 1 |
| `b`/`B` | signed/unsigned char | int | 1 |
| `?` | _Bool | bool | 1 |
| `h`/`H` | short | int | 2 |
| `i`/`I` | int | int | 4 |
| `l`/`L` | long | int | 4 |
| `q`/`Q` | long long | int | 8 |
| `n`/`N` | ssize_t/size_t | int | native only (`@`) |
| `e` | half float | float | 2 |
| `f` | float | float | 4 |
| `d` | double | float | 8 |
| `s` | char[] | bytes | N (prefix count, e.g. `4s`) |
| `p` | pascal string | bytes | N |
| `P` | void* | int | native only |

Repeat count prefix applies per-field (e.g. `4h` = 4 shorts), except `s`/`p` where the count is the field length, not a repeat.

### 3. Pack / unpack

```python
struct.pack(fmt, v1, v2, ...)        # -> bytes
struct.unpack(fmt, buffer)           # -> tuple, buffer size must match calcsize(fmt)
struct.unpack_from(fmt, buffer, offset=0)  # unpack from a larger buffer without slicing
struct.pack_into(fmt, buffer, offset, *values)  # write into an existing mutable buffer
```

### 4. Reuse compiled formats for performance

```python
Header = struct.Struct('<4sHHI')  # magic, ver_major, ver_minor, length
data = Header.pack(b'MAGC', 1, 0, 128)
magic, vmaj, vmin, length = Header.unpack(data)
print(Header.size)  # equivalent to calcsize
```

Use `Struct` objects instead of repeated `struct.pack(fmt, ...)` calls when the same format is used many times (e.g. parsing many records in a loop).

## Examples

**Example 1: Reading a fixed-size binary file header**
Input: File header spec — 4-byte magic, uint32 version (little-endian), uint32 payload length.
Output:
```python
HEADER_FMT = '<4sII'
HEADER_SIZE = struct.calcsize(HEADER_FMT)  # 12

with open('file.bin', 'rb') as f:
    magic, version, length = struct.unpack(HEADER_FMT, f.read(HEADER_SIZE))
    payload = f.read(length)
```

**Example 2: Parsing a network packet with mixed types**
Input: Packet = 1 byte type, 1 byte flags, 2-byte big-endian sequence number, 8-byte big-endian timestamp.
Output:
```python
PKT_FMT = '!BBHQ'
pkt_type, flags, seq, ts = struct.unpack(PKT_FMT, raw_bytes)
```

**Example 3: Packing an array of records**
Input: 3 points, each `(x: float, y: float)` little-endian.
Output:
```python
fmt = '<' + 'ff' * 3
data = struct.pack(fmt, 0.0, 0.0, 1.5, 2.5, -1.0, 3.0)
```

**Example 4: Unpacking from a larger buffer at an offset**
Input: A 1024-byte buffer where a 16-byte record starts at offset 100.
Output:
```python
record = struct.unpack_from('<4sIII', buffer, offset=100)
```

## Best Practices

- Always specify byte order (`<`, `>`, `!`) explicitly for file/network formats; only use native `@`/no-prefix when interoperating with the local C compiler's ABI.
- Use `Struct` objects for repeated pack/unpack in hot loops — avoids re-parsing the format string.
- Validate `len(buffer) == struct.calcsize(fmt)` before calling `unpack`, or use `unpack_from`/`pack_into` with buffers of arbitrary size.
- For variable-length strings, unpack the fixed header first, read the length field, then read the variable payload separately — `struct` itself only handles fixed-size fields.
- Strip trailing null padding from `s` fields manually: `s.rstrip(b'\x00')`.
- Use `bytearray`/`memoryview` with `pack_into`/`unpack_from` to avoid unnecessary copies when processing large buffers.

## Common Pitfalls

- **Relying on native alignment (`@`) for cross-platform/file data** — introduces padding bytes that differ across platforms/compilers, breaking round-trips.
- **Confusing `s` count with repeat count** — `4s` is one 4-byte bytes field, not four 1-byte fields; `4h` is four shorts.
- **Forgetting `calcsize` mismatches** — passing a buffer of the wrong length to `unpack` raises `struct.error`; always compute or check size.
- **Using `n`/`N`/`P` with non-native byte order prefixes** — these are only valid with `@`, not `<`/`>`/`!`/`=`.
- **Ignoring endianness of multi-byte fields from network sources** — most network protocols are big-endian (`!` or `>`); using host byte order silently corrupts values.
- **Not stripping padding from fixed-width string fields**, leading to comparisons failing against expected values.
- 
---
End Of Part
===========🔐™️®️©️🔐===========

---