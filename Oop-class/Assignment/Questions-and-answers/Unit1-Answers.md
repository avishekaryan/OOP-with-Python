# Unit 1 — Introduction to Python

## Short Questions (2 Marks)

### Q1. Define Python.

- Python is a high-level, interpreted, general-purpose programming language known for its readable syntax and large standard library, used widely in web development, data science, automation, and AI.

---

### Q2. Define High-level language.

- A high-level language is a programming language written in a form close to human-readable English, which is translated (compiled or interpreted) into machine code — it hides low-level details like memory management and CPU registers from the programmer.

---

### Q3. State why python is called a high-level language.

- Python is called high-level because its syntax reads close to plain English, it manages memory automatically (via garbage collection), and it lets the programmer focus on logic rather than hardware-level details like registers or memory addresses.

---

## Medium Questions (6 Marks)

### Q1. Explain the python data structures and data types.

- Python's built-in data types fall into a few core categories, each suited to a different kind of data.
- Numeric types: `int` (whole numbers), `float` (decimals), `complex` (complex numbers).
- Text type: `str`, an immutable sequence of characters.
- Boolean type: `bool`, either `True` or `False`.
- Python's main built-in data structures are `list` (ordered, mutable), `tuple` (ordered, immutable), `dict` (key-value pairs), and `set` (unordered, unique values).

```python
age = 20            # int
gpa = 8.5            # float
name = "Avhi"        # str
marks = [78, 91, 85] # list
point = (3, 4)       # tuple
student = {"name": "Avhi", "age": 20}  # dict
unique_ids = {1, 2, 3}                  # set
```

- Choosing the right structure matters: a `list` suits ordered, changeable data; a `tuple` suits fixed data that should not change; a `dict` suits lookups by key; and a `set` suits fast membership checks with no duplicates.

---

### Q2. Explain the process of inputting in python.

- Python reads input from the keyboard using the built-in `input()` function, which always returns the entered value as a string, regardless of what was typed.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # convert to int explicitly
print(f"{name} is {age} years old")
```

- Because `input()` always returns a `str`, converting to `int`, `float`, or another type must be done explicitly with a function like `int()` or `float()` — forgetting this is a common source of `TypeError` when the value is later used in arithmetic.

---

### Q3. Explain output formatting in Python.

- Python offers several ways to control how values are displayed, ranging from the basic `print()` call to precise formatting of numbers and text.

```python
name, gpa = "Avhi", 8.567
print(name, gpa)                         # basic - space separated
print(f"{name} has a GPA of {gpa:.2f}")  # f-string, 2 decimal places
print("{} has a GPA of {:.2f}".format(name, gpa))  # .format()
print("%s has a GPA of %.2f" % (name, gpa))        # % formatting (older style)
```

- f-strings (`f"..."`) are the modern, preferred approach since Python 3.6 — they are the most readable and allow inline expressions and format specifiers (like `:.2f` for 2 decimal places) directly inside the string.

---

### Q4. Write about the If statement in Python and its usage.

- The `if` statement lets a program make decisions, running a block of code only when a condition evaluates to `True`.

```python
marks = 78
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

- `elif` allows checking several conditions in sequence, and `else` catches anything that did not match any prior condition — Python relies on indentation (not braces) to define which statements belong to each block.

---

### Q5. Differentiate between If statement and switch statements in python.

- Traditional Python (before 3.10) has no `switch` statement at all — every conditional choice, however many branches, is written using a chain of `if`/`elif`/`else` statements.

```python
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Other day")
```

- Python 3.10 introduced `match`/`case`, which behaves similarly to a switch statement in other languages, matching a value against several patterns directly.

```python
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")
```

- The key difference is that `if`/`elif` tests arbitrary boolean conditions (`marks >= 90`, `x > y and y < z`), while `switch`-style constructs (and Python's `match`) typically compare one value against several fixed patterns.

---

### Q6. Write short notes on the different loops used in python, and their usage.

- Python provides two loop constructs, each suited to a different kind of repetition.
- A `for` loop iterates over a known sequence — a list, string, range, or any iterable — running once per item.

```python
for name in ["Alice", "Bob"]:
    print(name)
```

- A `while` loop repeats as long as a condition stays `True`, which suits situations where the number of repetitions is not known in advance.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

- In short, `for` is used when iterating over a fixed collection or a known range, while `while` is used when the loop should continue until some condition changes, such as user input or a running total.

---

### Q7. Why do we use break and continue statements in python? Why do we use one over another? Explain with an example.

- Both statements change a loop's normal flow, but in opposite ways: `break` exits the loop entirely, while `continue` skips only the current iteration and moves on to the next one.

```python
for n in range(1, 6):
    if n == 4:
        break        # stops the loop completely at 4
    print(n)
# prints 1, 2, 3

for n in range(1, 6):
    if n == 4:
        continue     # skips just this iteration
    print(n)
# prints 1, 2, 3, 5
```

- `break` is used when the loop's purpose is already fulfilled and continuing is pointless — like stopping a search once the item is found. `continue` is used when a particular item should simply be skipped, but the loop still has more useful work to do.

---

### Q8. Explain the usage of range statement in python. Explain with an example.

- `range()` generates a sequence of numbers, most commonly used to control how many times a `for` loop runs.

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)
for i in range(2, 6):    # 2, 3, 4, 5 (start, stop)
    print(i)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (start, stop, step)
    print(i)
```

- `range(stop)` starts at 0 by default; `range(start, stop)` sets a custom start; and `range(start, stop, step)` also controls the increment — in every case, the `stop` value itself is never included.

---

### Q9. What is the difference between a while loop and a for loop? Explain with an example.

- A `for` loop is used when iterating over a known collection or a fixed number of steps, while a `while` loop is used when the number of repetitions depends on a condition that may change unpredictably.

```python
# for loop - known number of items
for book in ["Python", "Java", "C++"]:
    print(book)

# while loop - repeats until a condition changes
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")
```

- In practice, a `for` loop is generally preferred whenever the data being iterated over is already known, since it is less error-prone — a `while` loop always carries the risk of an infinite loop if the condition never becomes `False`.

---

### Q10. Write short notes on Python operators and their precedence.

- Python groups operators into categories: arithmetic (`+ - * / // % **`), comparison (`== != > < >= <=`), logical (`and or not`), assignment (`= += -= *=`), and membership/identity (`in`, `is`).

```python
result = 2 + 3 * 4        # 14, not 20 - * runs before +
result2 = (2 + 3) * 4     # 20 - parentheses override precedence
print(10 > 5 and 3 < 4)   # True - comparisons evaluated before 'and'
```

- Precedence (highest to lowest, roughly): parentheses `()` first, then exponent `**`, then unary `-`, then `* / // %`, then `+ -`, then comparisons, then `not`, then `and`, then `or`.
- When operators are mixed without parentheses, Python evaluates according to this fixed precedence order — which is exactly why `2 + 3 * 4` evaluates the multiplication first — and parentheses are the safest way to make the intended order explicit and readable.

---
