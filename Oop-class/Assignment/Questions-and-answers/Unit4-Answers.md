# Unit 4 — Advanced Data Structures

## Definition Type Questions (2 Marks)

### Q1. Define a comprehension in Python.

- A comprehension is Python's shorthand for building a new list, dict, or set in a single line — instead of writing a full loop with `.append()`, the expression, the loop, and an optional filter are all combined into one compact statement.

```python
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```

---

### Q2. State the syntax of a list comprehension.

- The general pattern is `[expression for item in iterable if condition]` — read left to right as "compute this, for each item, keeping only the ones that pass the condition."

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]
```

---

### Q3. Differentiate between the two positions of `if` in a comprehension.

- Where the `if` sits changes what it does: placed at the end (after `for`), it filters — it simply skips elements. Placed before the `for` as part of a ternary, it transforms instead — every element stays, but its value changes.

```python
nums = [-2, -1, 0, 1, 2]
filtered = [x for x in nums if x > 0]        # filter
transformed = [x if x > 0 else 0 for x in nums]  # transform
print(filtered)      # [1, 2]
print(transformed)   # [0, 0, 0, 1, 2]
```

---

### Q4. State one common use of nested list comprehensions.

- A very common use is flattening — turning a list of lists into one flat list in a single line.

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

---

### Q5. Define a dictionary comprehension.

- It works the same way as a list comprehension, just producing key-value pairs instead: `{key_expr: value_expr for item in iterable}` builds a dictionary directly.

```python
squares = {x: x**2 for x in range(5)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

### Q6. What is a set comprehension?

- Using `{expression for item in iterable}` builds a set instead of a list, which is useful whenever only the unique values are needed and duplicates should be dropped automatically.

```python
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in nums}
print(unique_squares)   # {1, 4, 9}
```

---

### Q7. Define a default parameter.

- A default parameter is simply a fallback value written into the function definition itself, so the caller is not forced to supply that argument every time.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Avhi"))              # Hello, Avhi!
print(greet("Avhi", "Hi"))        # Hi, Avhi!
```

---

### Q8. What is the mutable default argument trap?

- The trap shows up when a mutable object like a list is used as a default value — since Python only creates that default once, at definition time, every call that skips the argument ends up sharing and modifying the very same object.

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  <- unexpected! same list reused
```

---

### Q9. What does `*args` receive in a function?

- `*args` scoops up any extra positional arguments the caller passes and packs them into a tuple.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))   # 6
```

---

### Q10. What does `**kwargs` receive in a function?

- `**kwargs` does the same thing but for keyword arguments, collecting them into a dictionary.

```python
def show_info(**kwargs):
    print(kwargs)

show_info(name="Avhi", year=1)   # {'name': 'Avhi', 'year': 1}
```

---

### Q11. What is the purpose of the `key` parameter in `sorted()` and `list.sort()`?

- Rather than comparing elements directly, `key` tells Python exactly what value to compare instead — useful whenever the natural order of the objects themselves is not what you want to sort by.

```python
words = ["banana", "kiwi", "apple"]
by_length = sorted(words, key=len)
print(by_length)   # ['kiwi', 'apple', 'banana']
```

---

### Q12. How is `lambda` used in sorting?

- A `lambda` is usually the quickest way to write that `key` function inline, without needing a separate named function.

```python
students = [("Ravi", 82), ("Sita", 91), ("Anil", 76)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks)   # [('Sita', 91), ('Ravi', 82), ('Anil', 76)]
```

---

### Q13. List any two operations supported by `deque`.

- `append()` and `appendleft()` add to either end; `pop()` and `popleft()` remove from either end.

```python
from collections import deque
dq = deque([2, 3])
dq.appendleft(1)
dq.append(4)
print(dq)   # deque([1, 2, 3, 4])
```

---

### Q14. Why is `deque` preferred over `list` for left-side operations?

- Because a `list` has to shift every remaining element whenever something is added or removed from the front, which costs O(n) time — a `deque` avoids this entirely and does it in O(1).

```python
from collections import deque
dq = deque([1, 2, 3])
dq.popleft()          # O(1) - fast
lst = [1, 2, 3]
lst.pop(0)            # O(n) - every remaining item shifts left
```

---

### Q15. Define a `namedtuple`.

- A `namedtuple` is best thought of as a tuple with labels — it behaves exactly like a normal tuple, except its fields can also be accessed by name instead of only by position.

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y, p[0])   # 3 4 3
```

---

### Q16. What does `._asdict()` do for a `namedtuple`?

- It converts the namedtuple into a dictionary, mapping each field name to its value.

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p._asdict())   # {'x': 3, 'y': 4}
```

---

### Q17. How does a `ChainMap` search for keys?

- It checks its list of mappings one at a time, in the order they were given, and simply returns the value from the first one that has that key.

```python
from collections import ChainMap
defaults = {"color": "blue"}
user = {"size": "L"}
combined = ChainMap(user, defaults)
print(combined["size"])    # L  (from user)
print(combined["color"])   # blue (from defaults)
```

---

### Q18. What happens when a missing key is accessed in a `Counter`?

- Rather than raising a `KeyError` like a normal dict would, a `Counter` quietly returns `0`, since a missing key just means that item was never counted.

```python
from collections import Counter
c = Counter("aab")
print(c["a"])   # 2
print(c["z"])   # 0  (no error)
```

---

### Q19. State one unique feature of `OrderedDict`.

- It keeps track of insertion order in a way that also matters for equality — two `OrderedDict`s with the same items in a different order are considered unequal.

```python
from collections import OrderedDict
a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print(a == b)   # False - order matters
```

---

### Q20. What does `defaultdict` do when a key does not exist?

- Instead of raising `KeyError`, it automatically creates that key using the factory function it was given, so the key is always ready to use.

```python
from collections import defaultdict
d = defaultdict(list)
d["fruits"].append("apple")
print(d)   # defaultdict(<class 'list'>, {'fruits': ['apple']})
```

---

## 6 Mark Questions

### Q1. Explain list comprehensions and give one example from the notes.

- A list comprehension exists mainly to replace a repetitive pattern — writing a `for` loop that repeatedly calls `.append()` — with something shorter and more direct.
- The syntax `[expression for item in iterable if condition]` reads almost like a sentence: take this expression, for every item in the iterable, but only where the condition holds.
- Because the loop, the condition, and the transformation all sit on one line, comprehensions tend to be both more readable and, in most cases, faster than the equivalent explicit loop.

```python
# without comprehension
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# with comprehension - same result
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)   # [0, 4, 16, 36, 64]
[Iterable] -> [for item] -> [if condition: filter] -> [expression: transform] -> [New List]
```

---

### Q2. Explain nested list comprehensions with reference to flattening and building 2-D structures.

- A nested comprehension is simply what happens when one `for` clause is placed inside another, which naturally lets it walk through nested iterables.
- One common use is flattening: `[x for row in matrix for x in row]` walks through each row, and then through each value inside that row, collapsing a list of lists into a single flat list.

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

- The same idea works in reverse too — building a 2-D structure — where the outer comprehension builds each row and the inner one fills in its values.

```python
grid = [[i*j for j in range(3)] for i in range(3)]
print(grid)   # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

- One detail worth remembering is that the order of the `for` clauses always mirrors the order of equivalent nested loops — outer loop first, inner loop second.

```
[matrix: list of lists] -> [outer: for row in matrix] -> [inner: for x in row] -> [flat list of x]
```

---

### Q3. Describe dictionary comprehensions and explain one example of filtering and one example of transformation.

- A dictionary comprehension follows the same idea as a list comprehension, just producing key-value pairs using `{key: value for item in iterable if condition}`.
- When used for filtering, the goal is to keep only some of the existing entries.

```python
scores = {"Ravi": 45, "Sita": 78, "Anil": 60}
passed = {k: v for k, v in scores.items() if v > 50}
print(passed)   # {'Sita': 78, 'Anil': 60}
```

- When used for transformation, the goal shifts instead to changing the values while keeping every key.

```python
bonus_marks = {k: v + 5 for k, v in scores.items()}
print(bonus_marks)   # {'Ravi': 50, 'Sita': 83, 'Anil': 65}
```

- The two can also be combined in the same expression, filtering and transforming at once.

---

### Q4. Explain default parameters and the mutable default argument trap. Also state the safe fix.

- A default parameter simply lets a function be called with fewer arguments than it defines, by supplying a ready-made value whenever the caller leaves one out.
- The subtlety is in when that default value is actually created — it happens exactly once, at the moment the function is defined, not fresh on every call.
- This becomes a genuine trap the moment the default is something mutable, like a list: since the same object is reused every time, changes made in one call quietly carry over into the next.

```python
def add_item(item, lst=[]):   # BUGGY
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  <- unexpected!
```

- The safe fix is to default to `None` instead, and only create the mutable object inside the function body.

```python
def add_item(item, lst=None):   # FIXED
    lst = [] if lst is None else lst
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [2]  <- correct, fresh list each time
```

---

### Q5. Explain the use of `*args` and `**kwargs` in Python functions.

- Both of these exist to solve the same underlying problem: writing a function that can accept an arguments list whose length is not known in advance.
- `*args` collects any extra positional arguments into a tuple, while `**kwargs` does the equivalent for keyword arguments, collecting them into a dictionary.

```python
def describe(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)

describe(1, 2, name="Avhi", year=1)
# positional: (1, 2)
# keyword: {'name': 'Avhi', 'year': 1}
```

- The same `*` and `**` symbols also work in reverse at the call site — unpacking an existing list or dictionary into individual arguments.

```python
nums = [1, 2, 3]
print(sum(*[nums]))   # not typical; more common: print(sum(nums))
info = {"name": "Avhi", "year": 1}
describe(**info)   # keyword: {'name': 'Avhi', 'year': 1}
```

---

### Q6. Discuss sorting with `sorted()`, `key`, `lambda`, and `itemgetter`.

- `sorted(iterable)` returns a brand-new sorted list without touching the original, whereas `list.sort()` rearranges the list itself, in place.
- The real flexibility comes from `key`, which tells Python what value to actually compare, instead of comparing the elements directly.

```python
students = [{"name": "Ravi", "age": 20}, {"name": "Sita", "age": 19}]
by_age = sorted(students, key=lambda s: s["age"])
print(by_age)   # [{'name': 'Sita', 'age': 19}, {'name': 'Ravi', 'age': 20}]
```

- `operator.itemgetter(n)` achieves much the same result, often a little faster and more readable.

```python
from operator import itemgetter
data = [("apple", 3), ("banana", 1)]
print(sorted(data, key=itemgetter(1)))   # [('banana', 1), ('apple', 3)]
```

- `reverse=True` can be added on top of any of these to sort in descending order without needing to invert the key manually.

---

### Q7. Describe `namedtuple` and explain its advantages.

- A `namedtuple`, created from `collections` with something like `Point = namedtuple('Point', ['x', 'y'])`, behaves just like a normal tuple, but its fields also have names.

```python
from collections import namedtuple
Student = namedtuple("Student", ["name", "marks"])
s = Student("Avhi", 88)
print(s.name, s.marks)      # Avhi 88
print(s._asdict())          # {'name': 'Avhi', 'marks': 88}
print(s._replace(marks=90)) # Student(name='Avhi', marks=90)
```

- Since it is still a tuple underneath, it remains immutable and hashable, so it stays lightweight and memory-efficient — most useful exactly where a small class would otherwise be created purely to hold data with no real behaviour attached.

---

### Q8. Explain `deque` and compare it with `list`.

- A `deque` (double-ended queue), from the `collections` module, is built specifically to make operations at both ends of a sequence fast.

```python
from collections import deque
dq = deque([1, 2, 3], maxlen=3)
dq.append(4)          # oldest (1) is dropped automatically
print(dq)             # deque([2, 3, 4], maxlen=3)
dq.appendleft(0)      # deque([0, 2, 3], maxlen=3)
```

- `append()`, `appendleft()`, `pop()`, and `popleft()` all run in O(1) time, regardless of which end they touch — a `list` is only fast at its right end, since removing from the front forces every remaining element to shift.
- The trade-off runs the other way for indexing though: a `list` supports fast random access by position, while a `deque` does not, which is exactly why a `deque` suits queue- or stack-like use rather than indexed access.

---

### Q9. Explain how `ChainMap` works and how it is used.

- `ChainMap` takes several dictionaries and presents them as one combined view, without ever actually copying or merging their contents.

```python
from collections import ChainMap
defaults = {"theme": "light", "lang": "en"}
user_settings = {"theme": "dark"}
settings = ChainMap(user_settings, defaults)
print(settings["theme"])   # dark  (found in user_settings first)
print(settings["lang"])    # en    (falls back to defaults)
```

- Writing to a `ChainMap`, however, only ever touches the very first mapping in the chain — this makes it a natural fit for layered configuration, where each layer should be allowed to override the one beneath it.
- `new_child()` adds a fresh mapping to the front of the chain, which is handy for representing nested scopes.

---

### Q10. Explain the `Counter` container and its uses.

- `Counter` is a dictionary built specifically for counting — its keys are the items being counted, and its values are how many times each one appeared.

```python
from collections import Counter
words = "the cat sat on the mat the cat ran".split()
c = Counter(words)
print(c)                 # Counter({'the': 3, 'cat': 2, ...})
print(c.most_common(2))  # [('the', 3), ('cat', 2)]
```

- Unlike a normal dict, asking about a key that was never counted simply returns `0`, rather than raising an error, and it also supports arithmetic between two Counters (`+`, `-`), useful for comparing word frequencies across two texts.

---

### Q11. Differentiate between `OrderedDict` and `defaultdict`.

- Although both extend the standard `dict`, they were designed to solve two entirely different problems.
- `OrderedDict` is concerned with order.

```python
from collections import OrderedDict
od = OrderedDict()
od["b"] = 2
od["a"] = 1
od.move_to_end("b")
print(list(od.keys()))   # ['a', 'b']
```

- `defaultdict` is concerned with missing keys — accessing one that does not exist triggers its factory function to create it automatically.

```python
from collections import defaultdict
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("mango")
print(groups)   # defaultdict(<class 'list'>, {'fruits': ['apple', 'mango']})
```

---

### Q12. Explain the purpose of `UserDict`, `UserList`, and `UserString`.

- These three classes exist mainly to solve a subtle problem with subclassing Python's built-in types directly — the built-in's own internal C code does not always call an overridden method consistently, so custom behaviour can silently fail to apply.
- `UserDict`, `UserList`, and `UserString` sidestep this by wrapping the real data in an accessible `.data` attribute instead, so every operation reliably passes through the overridden methods.

```python
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = CaseInsensitiveDict()
d["Name"] = "Avhi"
print(d["name"])   # Avhi
```

- In short, they are the safer starting point whenever a dict-, list-, or string-like type needs genuinely custom behaviour layered on top.

---

## 12 Mark Questions

### Q1. Discuss comprehensions in Python, including list comprehensions, nested list comprehensions, and dictionary comprehensions.

**Introduction**

Comprehensions exist to answer one recurring need in Python: building a new collection from an existing iterable without writing a full multi-line loop every time.

**Body**

- A list comprehension follows the pattern `[expression for item in iterable if condition]`.

```python
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```

- Where the `if` sits changes its role: placed at the end, it filters out elements that fail the condition; placed before the `for` as a ternary, it transforms every element's value instead of removing any of them.

```python
nums = [-2, -1, 0, 1, 2]
print([x for x in nums if x > 0])              # [1, 2] - filter
print([x if x > 0 else 0 for x in nums])       # [0, 0, 0, 1, 2] - transform
```

- Nested comprehensions extend this same idea across more than one `for` clause. One common use is flattening.

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

- The same nesting can build 2-D structures too, with the outer comprehension building each row and the inner one filling it in.

```python
grid = [[i*j for j in range(3)] for i in range(3)]
print(grid)   # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

- Dictionary comprehensions apply the identical logic to key-value pairs, and can filter existing entries or transform them, both in the same expression.

```python
scores = {"Ravi": 45, "Sita": 78}
print({k: v for k, v in scores.items() if v > 50})   # {'Sita': 78}
```

- Set comprehensions round out the family, useful whenever duplicates genuinely should not appear in the result.

```python
print({x % 3 for x in range(10)})   # {0, 1, 2}
```

- It is worth adding, though, that comprehensions are a readability tool as much as a convenience one — pushed beyond two levels of nesting, they tend to become harder to follow than an explicit loop, at which point the loop is usually the better choice.

**Conclusion**

Comprehensions make Python code shorter and more idiomatic, and because they test both syntax and judgement about when a comprehension is actually the right tool, they come up often in exams.

---

### Q2. Discuss default parameters in Python and explain the mutable default argument trap with the correct approach to avoid it.

**Introduction**

Default parameters exist to make functions more convenient to call — they let a function be invoked with fewer arguments than it technically defines, falling back on a preset value whenever one is left out.

**Body**

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Avhi"))         # Hello, Avhi!
```

- The detail that matters here is timing: that default value is created exactly once, the moment the function is defined — not freshly on every single call. This is harmless for immutable defaults, but becomes a genuine trap the moment the default is something mutable, like a list.

```python
def add_item(item, lst=[]):   # BUGGY
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  <- unexpected!
```

- The reason is that both calls were quietly operating on the exact same list object in memory, one that was created only once, back when the function was defined.
- The safe fix is to use `None` as a sentinel default, and only build the mutable object fresh inside the function body.

```python
def add_item(item, lst=None):   # FIXED
    lst = [] if lst is None else lst
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [2]  <- correct now
```

- As a general rule worth remembering: only immutable values — numbers, strings, tuples, or `None` — should ever be used as default parameter values.

**Conclusion**

Understanding the mutable default trap, and being able to explain the `None`-based fix, is a favourite exam question precisely because it tests real conceptual understanding rather than memorised syntax.

---

### Q3. Discuss `*args` and `**kwargs` in Python and explain how they are used in functions and call sites.

**Introduction**

`*args` and `**kwargs` both exist to answer the same basic question: how can a function accept an arguments list whose exact size is not known in advance?

**Body**

- `*args` handles the positional side of this — any extra positional arguments passed to the function are automatically packed into a tuple.

```python
def total(*args):
    return sum(args)
print(total(1, 2, 3, 4))   # 10
```

- `**kwargs` handles the keyword side in the same way, packing any extra keyword arguments into a dictionary.

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_profile(name="Avhi", course="AI")
# name: Avhi
# course: AI
```

- The two are frequently combined in a single definition, where anything beyond the required parameters is simply gathered up automatically.

```python
def full(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
full(1, 2, 3, 4, x=5)   # 1 2 (3, 4) {'x': 5}
```

- The same `*` and `**` symbols also work in reverse at the call site — unpacking an existing sequence or dictionary into individual arguments, which is especially useful for forwarding arguments transparently.

```python
def wrapper(*args, **kwargs):
    return full(*args, **kwargs)
print(wrapper(1, 2, 3, x=9))   # 1 2 (3,) {'x': 9}
```

- One ordering rule is worth keeping in mind: a definition should list ordinary positional parameters first, then `*args`, then any keyword-only parameters, and finally `**kwargs`.

**Conclusion**

Being comfortable with `*args` and `**kwargs` is essential for writing genuinely flexible, reusable functions, which is exactly why they are so often tested — they reveal whether Python's argument-passing model is properly understood.

---

### Q4. Evaluate the importance of sorting with `key`, `lambda`, and `itemgetter` in Python.

**Introduction**

By default, `sorted()` and `list.sort()` compare elements directly, which works fine for plain numbers but quickly breaks down for anything more complex, like tuples, dictionaries, or custom objects.

**Body**

- The `key` parameter solves this by letting the programmer specify exactly what value should actually be compared.

```python
people = [{"name": "Ravi", "age": 25}, {"name": "Sita", "age": 19}]
print(sorted(people, key=lambda p: p["age"]))
# [{'name': 'Sita', 'age': 19}, {'name': 'Ravi', 'age': 25}]
```

- `operator.itemgetter` and `attrgetter` offer an equivalent, often slightly faster alternative.

```python
from operator import itemgetter
print(sorted(people, key=itemgetter("age")))
```

- Multiple sort criteria can be handled by having the key function return a tuple instead of a single value.

```python
data = [("CS", 25), ("CS", 19), ("AI", 30)]
print(sorted(data, key=lambda p: (p[0], -p[1])))
# [('AI', 30), ('CS', 25), ('CS', 19)] - by dept, then descending age
```

- `reverse=True` reverses the overall sort order without needing to manually negate the key, though negating is still useful when ascending and descending fields need to be mixed together.
- It also helps to know that Python's sort (Timsort) is stable, meaning elements that compare equal under the key keep their original relative order.

**Conclusion**

Using `key` with `lambda` or `itemgetter` is the standard, Pythonic way to perform custom sorting, and because it comes up constantly in real code, it is one of the most practically useful skills tested in this unit.

---

### Q5. Describe the `collections` module with emphasis on `namedtuple` and `deque`.

**Introduction**

The `collections` module exists because Python's general-purpose `dict`, `list`, `set`, and `tuple` are not always the best fit — it offers specialized alternatives built for specific, common problems.

**Body**

- `namedtuple` addresses the problem of plain tuples being unreadable.

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)        # 3 4
print(p._asdict())     # {'x': 3, 'y': 4}
```

- `deque` addresses a different problem — the fact that a plain `list` is slow at its left-hand end — by supporting appends and pops from either end in O(1) time.

```python
from collections import deque
history = deque(maxlen=3)
for page in ["home", "about", "shop", "cart"]:
    history.append(page)
print(history)   # deque(['about', 'shop', 'cart'], maxlen=3)
```

- A `deque` also supports `maxlen`, turning it into a rolling buffer that automatically discards the oldest item once full, ideal for things like a sliding-window history log.

```
[deque] left: appendleft()/popleft() <-> [ ... items ... ] <-> right: append()/pop()
```

**Conclusion**

`namedtuple` and `deque` are a good illustration of what the `collections` module is really for — taking a built-in type and extending it to solve one specific, recurring problem cleanly.

---

### Q6. Discuss `ChainMap` and `Counter` as specialized containers in the `collections` module.

**Introduction**

`ChainMap` and `Counter` both extend the standard dictionary, but each was built to solve a distinctly different problem.

**Body**

- `ChainMap` groups several existing mappings into a single combined view, searched in the order they were originally given.

```python
from collections import ChainMap
cli_args = {}
env_vars = {"THEME": "dark"}
defaults = {"THEME": "light", "LANG": "en"}
config = ChainMap(cli_args, env_vars, defaults)
print(config["THEME"])   # dark  (found in env_vars)
print(config["LANG"])    # en    (falls back to defaults)
```

- `Counter`, on the other hand, is built purely for counting hashable items.

```python
from collections import Counter
votes = ["A", "B", "A", "C", "A", "B"]
tally = Counter(votes)
print(tally.most_common(1))   # [('A', 3)]
```

- It also supports set-like and arithmetic operations (`+`, `-`, `&`, `|`) between two Counters, which makes comparing or combining counts noticeably simpler than doing it manually.

**Conclusion**

Although both extend `dict`, `ChainMap` solves a layered-lookup problem while `Counter` solves a frequency-counting problem — recognising that distinction is really the key to using either one correctly.

---

### Q7. Explain `OrderedDict` and `defaultdict` and discuss their uses in Python.

**Introduction**

`OrderedDict` and `defaultdict` are both dictionary subclasses, but they were designed to solve two genuinely separate problems.

**Body**

- `OrderedDict` is concerned with sequence.

```python
from collections import OrderedDict
cache = OrderedDict()
cache["a"] = 1
cache["b"] = 2
cache.move_to_end("a")   # mark 'a' as most recently used
print(list(cache.keys()))   # ['b', 'a']
```

- `defaultdict`, by contrast, is concerned with missing keys — it takes a factory function, and whenever a key that does not yet exist is accessed, that factory is called automatically.

```python
from collections import defaultdict
word_groups = defaultdict(list)
for word in ["cat", "car", "dog", "do"]:
    word_groups[word[0]].append(word)
print(word_groups)
# defaultdict(<class 'list'>, {'c': ['cat', 'car'], 'd': ['dog', 'do']})
```

- So the key difference to remember is that `OrderedDict` solves an ordering problem while `defaultdict` solves a default-value problem — they rarely overlap, and the two can even be combined where both behaviours are genuinely needed.

**Conclusion**

Since both classes solve different problems — ordering versus default values — mixing them up is a common source of exam confusion, which is exactly why keeping the distinction clear is worth the extra care.

---

### Q8. Discuss `UserDict`, `UserList`, and `UserString` and explain why they are used in Python programs.

**Introduction**

`UserDict`, `UserList`, and `UserString`, all from the `collections` module, exist specifically to be subclassed when a programmer wants to build a custom dict-, list-, or string-like type.

**Body**

- Rather than inheriting directly from `dict`, `list`, or `str`, each of these wraps the real underlying data in an accessible `.data` attribute instead.
- The reason this matters is a subtle one: subclassing a built-in type directly and overriding a method like `__setitem__` does not always work reliably, because the built-in type's own internal (C-implemented) methods sometimes bypass the overridden version entirely.

```python
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = CaseInsensitiveDict()
d["Name"] = "Avhi"
print(d["NAME"])   # Avhi - works regardless of case
```

- By subclassing `UserDict`, `UserList`, or `UserString` instead of the built-ins directly, every operation is guaranteed to pass through the wrapped `.data` object consistently, so any overridden method reliably takes effect.
- In general, these classes are the right starting point whenever custom validation, logging, or transformation behaviour needs to sit on top of standard dict, list, or string operations, while still keeping a familiar, drop-in interface.

**Conclusion**

These wrapper classes are a useful reminder of a broader Python design principle — that subclassing a built-in type directly is not always safe, and that the standard library often provides a purpose-built alternative for exactly this situation.

---
