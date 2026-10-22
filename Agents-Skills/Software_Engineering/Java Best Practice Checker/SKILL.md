---
name: java-best-practice-checker
description: Performs an exhaustive review of Java code (SE 8–24) and flags violations of best practices with corrected examples. Use this skill whenever the user shares Java code and asks for a review, audit, code check, or improvement. Also trigger for questions like "is this good Java?", "what's wrong with my code?", "how can I improve this?", "check my Java", or "review this snippet". Covers every major area: modern Java features (SE 21–24), wrapper classes, String handling, text blocks, String Pool, conditionals, loops, arrays, var, records, OOP principles, design patterns, dependency injection, JVM internals, garbage collection, memory leaks, and the full Collections Framework (List, Set, Queue, Map, SequencedCollection). Always use this skill — do not attempt a Java review without it.
_agensi: "a66ec45e-cf46-4c7a-958d-a15604ba1df2"
---

# Java Best Practice Checker

Perform a thorough, structured review of Java code. Flag every violation with a clear explanation of *why* it matters and a corrected code example. Work through all applicable categories below — skip only those genuinely irrelevant to the submitted code.

---

## Review Protocol

1. Read the entire snippet before commenting. Understand the intent.
2. Work through each applicable category in order.
3. For each issue found, output exactly:
   - 🔴 / 🟡 / 🟢 **Issue N — Short title** (`ClassName.method` or relevant location)
   - One sentence explaining the root cause and why it matters.
   - A corrected code block labelled `// ✅ Fix`.
4. If a category is clean, skip it silently — do not pad with "no issues here".
5. If the code is entirely clean, say so and highlight what was done well.
6. Always end with the **Summary Table**.

### Severity Guide
| Icon | Level | When to use |
|---|---|---|
| 🔴 | High | Correctness bug, thread-safety hazard, security issue, or severe performance problem |
| 🟡 | Medium | Bad practice degrading maintainability, readability, or moderate performance |
| 🟢 | Low | Modernisation opportunity, minor style improvement |

---

## Category 1 — Modern Java Features (SE 21–24)

### 1.1 Pattern Matching for Switch (Java 21)
Flag verbose `if-instanceof-cast` chains or unguarded switch on types. Use type-safe switch with deconstruction patterns instead.
```java
// ❌ Verbose pre-21
if (msg instanceof TextMessage) {
    TextMessage t = (TextMessage) msg;
    System.out.println(t.text());
} else if (msg instanceof Ticket) { ... }

// ✅ Java 21+
String response = switch (msg) {
    case TextMessage(String text) -> "Text: " + text;
    case Ticket(int n)            -> "Ticket: " + n;
};
```

### 1.2 Unnamed Variables & Patterns (Java 22)
Flag unused variables in catch blocks and loop counters. Replace with `_`.
```java
// ❌ Noise — e is never used
try {
    int v = Integer.parseInt(input);
} catch (NumberFormatException e) {
    System.out.println("Invalid.");
}
// ✅ Java 22+
try {
    int v = Integer.parseInt(input);
} catch (NumberFormatException _) {
    System.out.println("Invalid.");
}

// ❌ Unused loop variable
for (String ignored : list) { count++; }
// ✅
for (var _ : list) { count++; }
```

### 1.3 Markdown Doc Comments (Java 23)
Flag raw HTML inside Javadoc (`<pre>`, `<b>`, `<ul>`, `<code>`, etc.). Suggest Markdown syntax when targeting Java 23+.

### 1.4 Stream Gatherers (Java 24)
Flag manual imperative loops that implement sliding windows, fixed chunks, or custom stream aggregations. Use `stream.gather()` instead.
```java
// ❌ Manual sliding window
List<List<Integer>> windows = new ArrayList<>();
for (int i = 0; i <= numbers.size() - 3; i++) {
    windows.add(numbers.subList(i, i + 3));
}

// ✅ Java 24+
import java.util.stream.Gatherers;
var windows = numbers.stream()
    .gather(Gatherers.windowSliding(3))
    .toList();
```

---

## Category 2 — Reducing Boilerplate (Modern Conciseness)

### 2.1 Records Instead of Data Classes (Java 16+)
Flag classes that are pure data holders with only fields, constructor, getters, `equals`, `hashCode`, and `toString`. Replace with `record`.
```java
// ❌ Boilerplate class
public class Person {
    private final String name;
    private final int age;
    public Person(String name, int age) { this.name = name; this.age = age; }
    public String getName() { return name; }
    public int getAge()     { return age; }
    // + equals, hashCode, toString ...
}

// ✅ Record — generates all of the above
public record Person(String name, int age) {}
// Accessor: person.name(), person.age() — NOT getName()
```

Do NOT suggest records for: mutable domain objects, classes needing inheritance, or classes with complex business logic beyond the record components.

### 2.2 Switch Expressions (Java 14+)
Flag multi-branch `if-else` or old `switch` with fall-through that assigns or returns a value.
```java
// ❌ Verbose
String result;
if (day.equals("Monday") || day.equals("Tuesday")) { result = "Workday"; }
else { result = "Weekend"; }

// ✅
String result = switch (day) {
    case "Monday", "Tuesday" -> "Workday";
    default -> "Weekend";
};
```

### 2.3 Instance Main Methods (Java 21 Preview)
Flag unnecessary `public class` + `public static void main` boilerplate for trivial programs targeting Java 21+ preview mode.

---

## Category 3 — Cloud & Concurrency (Virtual Threads / Project Loom)

### 3.1 Virtual Threads (Java 21+)
Flag `new Thread(runnable).start()` or large thread pools used for I/O-bound work.
```java
// ❌ Platform thread — heavyweight for I/O tasks
new Thread(() -> callExternalApi()).start();

// ✅ Virtual thread — millions can run concurrently
Thread.startVirtualThread(() -> callExternalApi());
```

### 3.2 BlockingQueue for Producer-Consumer
Flag manual `wait()`/`notify()` patterns for producer-consumer. Use `BlockingQueue.put()` / `take()`.
```java
// ✅
BlockingQueue<String> queue = new ArrayBlockingQueue<>(100);
queue.put("task");           // blocks if full
String task = queue.take();  // blocks if empty
```

---

## Category 4 — Wrapper Classes

### 4.1 Deprecated Constructor
Flag `new Integer(x)`, `new Double(x)`, etc. — deprecated since Java 9.
```java
// ❌
Integer num = new Integer(10);
// ✅
Integer num = Integer.valueOf(10); // reuses cache for -128..127
```

### 4.2 Reference Equality on Wrapper Objects
Flag `==` comparisons between wrapper objects (`Integer`, `Long`, `Short`, `Byte`, `Character`, `Boolean`). The integer cache covers only −128 to 127; `==` is unreliable outside that range.
```java
// ❌ Unreliable — outside cache range
Integer x = Integer.valueOf(200);
Integer y = Integer.valueOf(200);
System.out.println(x == y); // false

// ✅
System.out.println(x.equals(y)); // true
```

Cached ranges for reference:
| Wrapper | Cached range |
|---|---|
| Byte | All (−128..127) |
| Short / Integer / Long | −128..127 |
| Character | 0..127 |
| Boolean | true and false |
| Float / Double | No caching |

### 4.3 Unnecessary Boxing in Hot Paths
Flag repeated auto-boxing inside tight loops (e.g., accumulating into `List<Integer>` with `+=`). Prefer primitive arrays or streams for numeric aggregations.

---

## Category 5 — String Immutability & the String Pool

### 5.1 Concatenation in Loops
Flag `result += x` inside any loop. Every `+=` on a `String` allocates a new object — O(n²).
```java
// ❌
String result = "";
for (int i = 0; i < 1000; i++) { result += i; }

// ✅
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) { sb.append(i); }
String result = sb.toString();
```

### 5.2 Reference Equality on Strings
Flag `==` or `!=` used to compare `String` content.
```java
// ❌
if (s1 == s2) { ... }
// ✅
if (s1.equals(s2)) { ... }
if (s1.equalsIgnoreCase(s2)) { ... }  // case-insensitive
```

### 5.3 Heap Allocation Bypassing the Pool
Flag `new String("literal")` — bypasses the String Pool and wastes heap.
```java
// ❌
String s = new String("Hello");
// ✅
String s = "Hello";
// To pool an existing heap string:
String pooled = heapString.intern();
```

### 5.4 String vs StringBuilder vs StringBuffer
| Use Case | Correct Choice |
|---|---|
| Immutable constant / config key | `String` |
| Building a string in a single thread | `StringBuilder` |
| Building a string across multiple threads | `StringBuffer` |

Flag `StringBuffer` in single-threaded contexts (unnecessary synchronisation overhead).
Flag `String` mutation in multi-step building (use `StringBuilder`).

---

## Category 6 — Text Blocks (JDK 15+)

Flag multiline strings assembled with `\n`, `\"`, and `+` concatenation.
```java
// ❌
String json = "{\n" +
    "  \"name\": \"John\",\n" +
    "  \"age\": 30\n" +
    "}";

// ✅ Text block — no escape sequences, auto-aligned
String json = """
        {
          "name": "John",
          "age": 30
        }
        """;
```
Text blocks are ideal for JSON, HTML, SQL, and XML snippets.

---

## Category 7 — Conditionals Best Practices

### 7.1 Independent `if` Chains for Mutually Exclusive Conditions
Flag sequences of `if` blocks where only one branch can ever be true.
```java
// ❌ All three evaluated even after a match
if (age < 18) { System.out.println("Minor"); }
if (age >= 18 && age < 60) { System.out.println("Adult"); }
if (age >= 60) { System.out.println("Senior"); }

// ✅ else-if short-circuits correctly
if (age < 18) {
    System.out.println("Minor");
} else if (age < 60) {
    System.out.println("Adult");
} else {
    System.out.println("Senior");
}
```

### 7.2 Unnamed Boolean Conditions
Flag complex boolean expressions used inline without a descriptive variable.
```java
// ❌
if (age > 18 && hasLicense && !hasViolations && insuranceValid) { ... }

// ✅
boolean isLegalDriver = age > 18 && hasLicense && !hasViolations && insuranceValid;
if (isLegalDriver) { ... }
```

### 7.3 Verbose Value Assignment with if-else
Flag `if-else` blocks whose sole purpose is to assign one of two values.
```java
// ❌
String label;
if (x > 10) { label = "High"; } else { label = "Low"; }

// ✅
String label = (x > 10) ? "High" : "Low";
```

---

## Category 8 — Loops Best Practices

### 8.1 Expensive Call Inside Loop Condition
Flag method calls in the loop condition that return a stable value.
```java
// ❌ list.size() called every iteration
for (int i = 0; i < list.size(); i++) { process(list.get(i)); }

// ✅ Cache it
int size = list.size();
for (int i = 0; i < size; i++) { process(list.get(i)); }

// ✅ Modern — no index needed
list.forEach(this::process);
```

### 8.2 Wrong Loop Type for the Job
| Scenario | Best Loop Type |
|---|---|
| Fixed number of iterations | `for` loop |
| Loop until condition met | `while` loop |
| Iterating a collection | Enhanced `for-each` |
| Large dataset processing | `parallelStream()` |

Flag index-based `for` loops over collections when the index is never used.

### 8.3 Parallel Streams on Shared Mutable State
Flag `parallelStream()` with lambdas that write to a shared variable — race condition.
```java
// ❌ Race condition
List<String> results = new ArrayList<>();
list.parallelStream().forEach(results::add);

// ✅
List<String> results = list.parallelStream().collect(Collectors.toList());
```

---

## Category 9 — Arrays Best Practices

### 9.1 Printing Arrays Directly
Flag `System.out.println(array)` — prints the reference address, not content.
```java
// ❌
System.out.println(arr);           // [I@1b6d3586

// ✅ 1D
System.out.println(Arrays.toString(arr));
// ✅ Multi-dimensional
System.out.println(Arrays.deepToString(matrix));
```

### 9.2 Comparing Arrays with ==
Flag `array1 == array2` for content equality.
```java
// ✅ 1D
Arrays.equals(array1, array2);
// ✅ Multi-dimensional
Arrays.deepEquals(matrix1, matrix2);
```

### 9.3 Manual Array Copy
Flag manual index-copy loops.
```java
// ❌
int[] copy = new int[original.length];
for (int i = 0; i < original.length; i++) { copy[i] = original[i]; }

// ✅ Idiomatic
int[] copy    = Arrays.copyOf(original, original.length);
int[] partial = Arrays.copyOf(original, 3);
int[] grown   = Arrays.copyOf(original, original.length + 2); // pads with 0

// ✅ High-performance bulk
System.arraycopy(src, 0, dest, 0, src.length);
```

### 9.4 Manual Array Aggregations
Flag manual loops for sum/max/min over arrays.
```java
// ❌
int sum = 0;
for (int n : arr) { sum += n; }

// ✅
int sum = Arrays.stream(arr).sum();
int max = Arrays.stream(arr).max().orElse(0);
```

### 9.5 Fixed Array Where Dynamic Collection Is Needed
Flag fixed-size arrays used where dynamic resizing or Collection APIs are needed.
```java
// ✅ Convert to mutable List
List<String> list = new ArrayList<>(Arrays.asList(array));
```

---

## Category 10 — Local Variable Type Inference (`var`, Java 10+)

### 10.1 Redundant Type Repetition
Flag declarations where the type is obvious from the right-hand side.
```java
// ❌
ArrayList<String> names = new ArrayList<String>();
HashMap<Integer, String> map = new HashMap<Integer, String>();

// ✅
var names = new ArrayList<String>();
var map   = new HashMap<Integer, String>();
```

### 10.2 Misuse of `var` Where Type Is Opaque
Flag `var` where the inferred type is not obvious to a reader.
```java
// ❌ What type is result?
var result = process(getData());

// ✅ Explicit type adds clarity
ProcessedData result = process(getData());
```

`var` is only valid for local variables with an initialiser. Flag attempts to use it for method parameters, return types, or fields.

---

## Category 11 — Records (Java 16+)

### 11.1 Missing Compact Constructor Validation
Flag records whose components could receive null or blank values without any guard.
```java
// ❌ No validation
public record Person(String name, String email) {}

// ✅
public record Person(String name, String email) {
    public Person {
        if (name == null || name.isBlank())
            throw new IllegalArgumentException("Name cannot be empty");
    }
}
```

### 11.2 Wrong Accessor Syntax
Flag `record.getName()` — records generate accessors without the `get` prefix.
```java
Person p = new Person("Alice", 30);
// ❌
p.getName();
// ✅
p.name();
```

### 11.3 Record Pattern Matching (Java 21+)
Flag manual instanceof + cast + field access when the subject is a record.
```java
// ❌ Verbose
if (obj instanceof Contact c) {
    String name = c.person().name();
    String city = c.address().city();
}

// ✅ Nested deconstruction
if (obj instanceof Contact(Person(var name, var age), Address(var street, var city))) {
    System.out.println(name + " lives in " + city);
}
```

---

## Category 12 — OOP: Structured vs Object-Oriented Design

Flag procedural-style Java:
- Free-floating `static` utility classes doing everything with no encapsulation.
- Global state stored in `static` fields, mutated by `static` methods.
- Data and behaviour separated into different classes with no cohesion.

Prefer: encapsulate data as instance state, keep related behaviour in the same class.

---

## Category 13 — Encapsulation

### 13.1 Public Mutable Fields
Flag any non-`final` `public` field on a class (records and deliberate value objects excluded).
```java
// ❌
class BankAccount {
    public double balance; // anyone can set balance = -99999
}

// ✅ Private field + validated mutators
class BankAccount {
    private double balance;
    public void deposit(double amount)  { if (amount > 0) balance += amount; }
    public void withdraw(double amount) { if (amount > 0 && amount <= balance) balance -= amount; }
    public double getBalance()          { return balance; }
}
```

### 13.2 Returning Mutable Internal Collections
Flag `return this.items` where `items` is a mutable `List`/`Set`/`Map` field.
```java
// ❌ Caller can mutate internal state
public List<String> getItems() { return items; }

// ✅ Defensive unmodifiable view
public List<String> getItems() { return Collections.unmodifiableList(items); }
```

---

## Category 14 — Inheritance, Abstract Classes & Interfaces

### 14.1 Wrong Abstraction Choice
| Need | Correct choice |
|---|---|
| Parent-child "is-a" with shared concrete logic | `extends` (inheritance) |
| Common behaviour with mandatory customisation | `abstract class` |
| Contract for unrelated classes / multiple inheritance | `interface` |

Flag `abstract class` used only for constants — should be an `interface`.
Flag classes extending multiple base classes (compile error) — refactor to interfaces.

### 14.2 Template Method Pattern
Validate that abstract hook methods in an abstract class are `protected`, not `public`.

### 14.3 Interface Default Methods Misuse
Flag `default` methods in interfaces used to share complex stateful behaviour — that belongs in an abstract class.

---

## Category 15 — Design Patterns

### 15.1 Singleton — Thread Safety
Flag the naive `if (instance == null) { instance = new X(); }` — race condition under concurrent access.
```java
// ❌ Not thread-safe
public static Logger getInstance() {
    if (instance == null) { instance = new Logger(); }
    return instance;
}

// ✅ Enum singleton — thread-safe, serialization-safe, preferred
public enum Logger {
    INSTANCE;
    public void log(String msg) { System.out.println(msg); }
}
```

### 15.2 Strategy Pattern
Flag hard-coded algorithm selection via `if-else` or `instanceof` chains. Extract behind an interface.
```java
// ❌
if (type.equals("bubble")) { bubbleSort(data); }
else if (type.equals("quick")) { quickSort(data); }

// ✅
interface Sortable { int[] sort(int[] data); }
class Context {
    private final Sortable sorter;
    Context(Sortable sorter) { this.sorter = sorter; }
    void execute(int[] data) { sorter.sort(data); }
}
```

### 15.3 Factory Method
Flag `new ConcreteType()` scattered in business logic when the type depends on a runtime parameter.
```java
// ✅ Factory with switch expression (Java 14+)
public static Shape getShape(String type) {
    return switch (type.toUpperCase()) {
        case "CIRCLE" -> new Circle();
        case "SQUARE" -> new Square();
        default -> throw new IllegalArgumentException("Unknown: " + type);
    };
}
```

### 15.4 Observer Pattern
Flag polling loops that check for state changes. Suggest the Listener/Observer pattern.
```java
// ✅
interface Listener { void onClick(); }
class Button {
    private Listener listener;
    public void setListener(Listener l) { this.listener = l; }
    public void click() { if (listener != null) listener.onClick(); }
}
```

---

## Category 16 — Dependency Injection

Flag `new ConcreteImplementation()` inside a class body (not factories/builders).
```java
// ❌ Tightly coupled — impossible to swap or unit-test
class Application {
    private Database db = new MySQLDatabase();
}

// ✅ Constructor injection
class Application {
    private final Database db;
    Application(Database db) { this.db = db; }
}
// Swap implementations at the call site:
new Application(new MySQLDatabase());
new Application(new MongoDBDatabase());
new Application(mockDb); // testable
```

---

## Category 17 — Object Lifecycle & `finalize()`

Flag any override of `finalize()` — deprecated Java 9, strongly discouraged Java 18+.
```java
// ❌
@Override
protected void finalize() throws Throwable { closeResource(); }

// ✅ Use try-with-resources
try (MyResource r = new MyResource()) { r.use(); }
// Or Cleaner API for non-AutoCloseable resources
```

---

## Category 18 — JIT Compilation Awareness

Flag patterns that defeat common JIT optimisations:

| Anti-pattern | JIT optimisation defeated | Fix |
|---|---|---|
| Trivial methods never inlined due to unnecessary virtual dispatch | Method Inlining | Mark as `final` where appropriate |
| Invariant computation inside a loop | Loop hoisting | Move outside the loop |
| Short-lived objects allocated inside hot loops | Escape Analysis (stack allocation) | Reuse objects or use primitives |
| Unreachable branches in code | Dead Code Elimination | Remove dead branches |
| Constant expressions computed at runtime | Constant Folding | Use `static final` constants |

---

## Category 19 — Memory Management & Leaks

### 19.1 Unclosed Resources
Flag `Connection`, `InputStream`, `OutputStream`, `ResultSet`, `FileReader`, etc. opened outside try-with-resources.
```java
// ❌ Leaks connection if execute() throws
Connection conn = dataSource.getConnection();
conn.execute(sql);

// ✅
try (Connection conn = dataSource.getConnection()) {
    conn.execute(sql);
}
```

### 19.2 Static References to Large Objects
Flag `static` fields holding large collections, caches, or heavy objects with no eviction — they live for the JVM's entire lifetime.

### 19.3 `System.gc()` in Application Code
Flag explicit `System.gc()` calls — this is only a hint to the JVM, causes unpredictable Stop-the-World pauses, and is almost never appropriate in production.

---

## Category 20 — Garbage Collection Awareness

### 20.1 Circular References
Java uses Mark-and-Sweep (not reference counting), so circular references are handled correctly. Flag comments or docs that incorrectly claim they cause leaks in Java.

### 20.2 GC Selection (JVM Config / Dockerfiles)
When reviewing startup scripts or container configs, flag missing or inappropriate GC flags:
| Workload | Recommended GC | JVM Flag |
|---|---|---|
| Small / single-threaded | Serial GC | `-XX:+UseSerialGC` |
| Throughput-focused | Parallel GC | `-XX:+UseParallelGC` |
| Large app, low latency | G1 GC (default since Java 9) | `-XX:+UseG1GC` |
| Very large heap / real-time / cloud | ZGC | `-XX:+UseZGC` |

Flag missing `-Xms` / `-Xmx` in containerised apps — heap can grow unbounded.

---

## Category 21 — Collections: Choosing the Right Type

### 21.1 List Implementations
| Situation | Use | Avoid |
|---|---|---|
| Random access, iteration | `ArrayList` | `LinkedList` |
| Frequent add/remove at head/tail | `LinkedList` | `ArrayList` |
| Thread-safe, read-heavy | `CopyOnWriteArrayList` | `Vector` |

Flag `LinkedList` used only as a plain list with no head/tail operations.
Flag `Vector` or `Stack` in any new code.

### 21.2 Set Implementations
| Situation | Use |
|---|---|
| Fast lookup, no order | `HashSet` |
| Insertion-ordered iteration | `LinkedHashSet` |
| Sorted / range queries | `TreeSet` |
| Concurrent reads | `CopyOnWriteArraySet` |
| Concurrent + sorted | `ConcurrentSkipListSet` |

### 21.3 Queue / Deque Implementations
Flag `Stack` in new code — use `ArrayDeque` as a `Deque` instead.
Flag `add()`/`remove()` when exception-on-failure is not desired.

| Operation | Throws on failure | Returns null/false |
|---|---|---|
| Insert | `add(e)` | `offer(e)` |
| Remove | `remove()` | `poll()` |
| Examine | `element()` | `peek()` |

### 21.4 Map Implementations
| Situation | Use |
|---|---|
| General key-value | `HashMap` |
| Insertion-ordered iteration | `LinkedHashMap` |
| Sorted keys / range queries | `TreeMap` |
| High-concurrency | `ConcurrentHashMap` |
| Concurrent + sorted keys | `ConcurrentSkipListMap` |

Flag `Hashtable` in any new code — use `ConcurrentHashMap`.
Flag `null` key/value insertion in `TreeMap` or `ConcurrentHashMap` — throws `NullPointerException`.

### 21.5 Immutable Collections (Java 9+)
Flag `Collections.unmodifiableList(new ArrayList<>(...))` for truly immutable collections.
```java
// ❌ Verbose
List<String> list = Collections.unmodifiableList(new ArrayList<>(Arrays.asList("a", "b")));

// ✅ Java 9+
List<String>        list = List.of("a", "b");
Set<String>         set  = Set.of("x", "y");
Map<String,Integer> map  = Map.of("key", 1);
```

---

## Category 22 — SequencedCollection (Java 21+)

Flag manual workarounds for first/last element access on ordered collections.
```java
// ❌ Pre-Java 21 workarounds
String first = list.get(0);
String last  = list.get(list.size() - 1);

// ✅ SequencedCollection API (Java 21+)
String first = list.getFirst();
String last  = list.getLast();
list.addFirst("x");
list.addLast("z");
List<String> rev = list.reversed();
```

Also flag missing use of `SequencedMap` methods: `firstEntry()`, `lastEntry()`, `pollFirstEntry()`, `pollLastEntry()`, `putFirst()`, `putLast()`, `reversed()`.

---

## Category 23 — Sorting Collections

### 23.1 Natural Order via `Comparable`
Flag classes used as sort keys that don't implement `Comparable` and have no `Comparator` provided.
```java
// ✅
class Cricketer implements Comparable<Cricketer> {
    int runs;
    @Override
    public int compareTo(Cricketer other) {
        return Integer.compare(this.runs, other.runs); // ascending
    }
}
```

### 23.2 Overflow-Prone Manual Comparison
Flag subtraction-based comparators — overflows for large integers.
```java
// ❌ Overflow risk
list.sort((c1, c2) -> c2.runs - c1.runs);

// ✅ Safe
list.sort((c1, c2) -> Integer.compare(c2.runs, c1.runs));
// Or with method reference
list.sort(Comparator.comparingInt(Cricketer::runs).reversed());
```

---

## Summary Table Format

Always end every review with this table, even if only one issue was found:

| # | Location | Category | Issue | Severity |
|---|---|---|---|---|
| 1 | `ClassName.method()` | Strings | Concatenation in loop | 🔴 High |
| 2 | `ClassName` field | Encapsulation | Public mutable field | 🔴 High |
| 3 | `ClassName` | DI | Hard-coded dependency | 🟡 Medium |
| 4 | `ClassName.method()` | Modern Java | Use `var` for local type | 🟢 Low |

---

## Full Example Review

**User submits:**
```java
public class OrderService {
    private List<String> orders = new ArrayList<>();
    private Database db = new MySQLDatabase();

    public List<String> getOrders() {
        return orders;
    }

    public String buildReport() {
        String report = "";
        for (String order : orders) {
            report += order + "\n";
        }
        return report;
    }

    public void processOrder(Object event) {
        if (event instanceof OrderCreated) {
            OrderCreated e = (OrderCreated) event;
            System.out.println("Created: " + e.id());
        } else if (event instanceof OrderCancelled) {
            OrderCancelled e = (OrderCancelled) event;
            System.out.println("Cancelled: " + e.id());
        }
    }
}
```

**Expected response:**

🔴 **Issue 1 — String concatenation in loop** (`OrderService.buildReport`)  
`report += order + "\n"` allocates a new `String` on every iteration — O(n²) for large lists.
```java
// ✅ Fix
public String buildReport() {
    StringBuilder sb = new StringBuilder();
    for (String order : orders) { sb.append(order).append('\n'); }
    return sb.toString();
}
```

🔴 **Issue 2 — Mutable internal state exposed** (`OrderService.getOrders`)  
Returning `orders` directly lets callers add/remove items, breaking internal invariants.
```java
// ✅ Fix
public List<String> getOrders() {
    return Collections.unmodifiableList(orders);
}
```

🟡 **Issue 3 — Hard-coded dependency** (`OrderService` field)  
`new MySQLDatabase()` tightly couples the service and makes unit testing impossible.
```java
// ✅ Fix — constructor injection
public class OrderService {
    private final Database db;
    public OrderService(Database db) { this.db = db; }
}
```

🟡 **Issue 4 — Verbose instanceof-cast chain** (`OrderService.processOrder`)  
Java 21 pattern matching for switch eliminates the manual cast boilerplate.
```java
// ✅ Fix
public void processOrder(Object event) {
    switch (event) {
        case OrderCreated(var id)   -> System.out.println("Created: " + id);
        case OrderCancelled(var id) -> System.out.println("Cancelled: " + id);
        default -> {}
    }
}
```

| # | Location | Category | Issue | Severity |
|---|---|---|---|---|
| 1 | `OrderService.buildReport()` | Strings | Concatenation in loop | 🔴 High |
| 2 | `OrderService.getOrders()` | Encapsulation | Mutable state exposed | 🔴 High |
| 3 | `OrderService` field | DI | Hard-coded dependency | 🟡 Medium |
| 4 | `OrderService.processOrder()` | Modern Java | Verbose instanceof-cast chain | 🟡 Medium |
