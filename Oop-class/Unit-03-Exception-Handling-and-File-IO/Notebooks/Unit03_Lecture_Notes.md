# Unit 3 — Exception Handling and File I/O
### BT151CO · Detailed Lecture Notes

---

| | |
|---|---|
| **Duration** | 5 Hours |
| **OBjectives** | Handle runtime errors and perform file-based I/O operations |
| **Pre-requisite** | Unit 2 — Classes, functions, and OOP principles |

---

## 📋 Table of Contents

1. [Types of Errors](#1-types-of-errors)
2. [Exception Handling with try / except](#2-exception-handling-with-try--except)
3. [Handling Multiple Exceptions](#3-handling-multiple-exceptions)
4. [Writing Custom Exceptions](#4-writing-custom-exceptions)
5. [File Handling Modes](#5-file-handling-modes)
6. [Reading Files](#6-reading-files)
7. [Writing and Appending to Files](#7-writing-and-appending-to-files)
8. [Handling File Exceptions](#8-handling-file-exceptions)
9. [The with Statement](#9-the-with-statement)
10. [Summary and Key Takeaways](#10-summary-and-key-takeaways)

---

---

# 1. Types of Errors

---

## 1.1 What is an Error?

When you write a program, things can go wrong. Python distinguishes between **two broad categories** of problems:

| Category | When it Happens | Example |
|---|---|---|
| **Syntax Error** | Before the program runs | Missing colon, wrong indentation |
| **Exception (Runtime Error)** | While the program is running | Dividing by zero, file not found |
| **Logical Error** | The program runs without crashing, but produces wrong results. | `a-b` instead of `b-a`

Understanding the difference is the first step to writing **robust, professional code**.

---

## 1.2 Syntax Errors

A **syntax error** means Python cannot even understand your code. It is like writing a sentence with completely broken grammar — the reader gives up before they start.

Python will refuse to run the program and immediately show you what went wrong.

**Analogy:** Imagine texting a friend: *"Can you pick from the car me up?"* — they cannot understand the sentence at all.

```python
# SYNTAX ERROR — missing colon after if
if score > 50
    print("Pass")
```

**Output:**
```
  File "example.py", line 1
    if score > 50
                ^
SyntaxError: expected ':'
```

> **Key Point:** Syntax errors are caught **before** your program runs. Fix the grammar first.

---

## 1.3 Runtime Errors (Exceptions)

A **runtime error** — also called an **exception** — occurs **while** the program is running. The syntax is correct, but something unexpected happens during execution.

**Analogy:** You give someone perfectly clear directions: *"Turn left at the traffic light."* The directions are valid, but the traffic light has been removed. You only discover the problem when you actually make the journey.

### Common Built-in Exceptions

| Exception | Cause | Example |
|---|---|---|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Wrong type of value | `int("hello")` |
| `TypeError` | Operation on wrong type | `"abc" + 5` |
| `IndexError` | List index out of range | `my_list[99]` |
| `KeyError` | Dictionary key not found | `d["missing_key"]` |
| `FileNotFoundError` | File does not exist | `open("ghost.txt")` |
| `AttributeError` | Object has no such attribute | `"hello".push("!")` |
| `NameError` | Variable not defined | `print(undefined_var)` |
| `PermissionError` | No access rights to a file | Reading a locked file |

---

### Example — ZeroDivisionError

```python
# A student divides their total marks by the number of subjects
total_marks = 450
num_subjects = 0  # Oops — no subjects recorded

# This will crash!
average = total_marks / num_subjects
print(f"Average marks: {average}")
```

**Output:**
```
ZeroDivisionError: division by zero
```

---

### Example — ValueError

```python
# A library system asks for the number of books to borrow
user_input = "five"  # User typed a word instead of a number

# Trying to convert a non-numeric string to int crashes here
num_books = int(user_input)
print(f"You want to borrow {num_books} books.")
```

**Output:**
```
ValueError: invalid literal for int() with base 10: 'five'
```

---

### Example — IndexError

```python
# A game stores player scores in a list
scores = [100, 250, 180]

# Trying to access a player that does not exist
print(scores[5])  # Only indices 0, 1, 2 are valid
```

**Output:**
```
IndexError: list index out of range
```

---

## 1.4 Logical Errors

There is a third type — **logical errors**. The program runs without crashing, but produces **wrong results**. Python cannot detect these for you.

```python
# Calculating a student's percentage — but the formula is wrong
marks_obtained = 430
total_marks = 500

# BUG: Should be (marks_obtained / total_marks) * 100
percentage = (total_marks / marks_obtained) * 100
print(f"Percentage: {percentage:.2f}%")
```

**Output:**
```
Percentage: 116.28%
```

> This is clearly wrong — percentages cannot exceed 100% here — but Python does not know that. Logical errors are the hardest to find and require careful testing.

---

## 1.5 Key Takeaways — Types of Errors

- **Syntax errors** stop your program before it starts; fix them first.
- **Runtime exceptions** happen during execution and can be caught and handled.
- **Logical errors** produce wrong results silently; only careful testing reveals them.
- Python provides many **built-in exception types** — learning them helps you write better error messages.

---

---

# 2. Exception Handling with try / except

---

## 2.1 Why Handle Exceptions?

Imagine a bank ATM. If the ATM crashes with an ugly error every time a customer enters a wrong PIN, that is terrible design. Instead, it catches the mistake, shows a polite message, and gives the customer another chance.

**Exception handling** lets your program:
- Survive unexpected inputs without crashing
- Show helpful messages instead of Python's raw error output
- Continue running or shut down gracefully

---

## 2.2 The try / except Block — Basic Structure

```python
try:
    # Code that might cause an exception
    risky_code()
except ExceptionType:
    # Code that runs if the exception occurs
    handle_the_problem()
```

**How it works step by step:**
1. Python attempts to run the code inside `try`
2. If **no exception** occurs → `except` is skipped entirely
3. If an exception **does** occur → Python jumps immediately to `except`
4. The program continues after the `try/except` block

---

## 2.3 Your First try / except

**Without exception handling:**
```python
# Student enters their score — but types text instead of a number
score = int(input("Enter your score: "))  # Crashes if input is not a number
print(f"Your score is: {score}")
```

**With exception handling:**
```python
# Safely reading a student's score
try:
    score = int(input("Enter your score: "))
    print(f"Your score is: {score}")
except ValueError:
    print("Invalid input. Please enter a number.")
```

**Output (if user types 'hello'):**
```
Enter your score: hello
Invalid input. Please enter a number.
```

The program no longer crashes — it responds politely.

---

## 2.4 The else Clause

The `else` clause runs **only when no exception occurred** inside `try`. Think of it as the "everything went well" path.

```python
# Library book borrowing system
try:
    book_id = int(input("Enter book ID to borrow: "))
except ValueError:
    print("Book ID must be a number.")
else:
    # This only runs if int() succeeded
    print(f"Book ID {book_id} has been reserved for you.")
```

**Output (if user types 42):**
```
Enter book ID to borrow: 42
Book ID 42 has been reserved for you.
```

---

## 2.5 The finally Clause

The `finally` clause **always runs** — whether an exception occurred or not. It is perfect for cleanup tasks like closing connections, releasing resources, or printing a farewell message.

**Analogy:** A shop assistant always says *"Have a nice day!"* whether the customer bought something or walked out empty-handed.

```python
# Bank transaction simulation
print("Starting bank transaction...")

try:
    amount = float(input("Enter withdrawal amount: £"))
    balance = 1000.00
    if amount > balance:
        raise ValueError("Insufficient funds.")
    balance -= amount
    print(f"Withdrawal successful. New balance: £{balance:.2f}")
except ValueError as e:
    print(f"Transaction failed: {e}")
finally:
    # Always runs — good place for cleanup
    print("Transaction session ended.")
```

**Output (if user enters 1500):**
```
Starting bank transaction...
Enter withdrawal amount: £1500
Transaction failed: Insufficient funds.
Transaction session ended.
```

**Output (if user enters 200):**
```
Starting bank transaction...
Enter withdrawal amount: £200
Withdrawal successful. New balance: £800.00
Transaction session ended.
```

---

## 2.6 Full Structure: try / except / else / finally

```
try:
    [code that might fail]
except SomeError:
    [handle the error]
else:
    [runs only if NO exception occurred]
finally:
    [always runs, no matter what]
```

---

## 2.7 Accessing the Exception Object

You can capture the exception object itself using `as`. This lets you read the exact error message.

```python
# Shopping cart — adding item quantity
try:
    quantity = int(input("How many items do you want to add? "))
    cart_total = 5 * quantity
    print(f"Cart updated. Total items: {cart_total}")
except ValueError as error:
    # 'error' holds the actual exception object
    print(f"Error caught: {error}")
    print("Please enter a whole number.")
```

**Output (if user types 'three'):**
```
How many items do you want to add? three
Error caught: invalid literal for int() with base 10: 'three'
Please enter a whole number.
```

---

## 2.8 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Catching all exceptions with bare `except:` | Hides bugs, catches even keyboard interrupts | Always specify the exception type |
| Silencing exceptions with empty `except` | Makes debugging impossible | At minimum, print the error |
| Putting too much code in `try` | Makes it unclear which line caused the error | Keep `try` blocks short and focused |
| Forgetting `finally` for cleanup | Resources stay open / locked | Use `finally` or the `with` statement |

---

## 2.9 Key Takeaways — try / except

- `try` wraps code that **might** fail.
- `except` handles the failure gracefully.
- `else` runs only when try **succeeds**.
- `finally` **always** runs — use it for cleanup.
- Always **name the exception type** in `except`.

---

---

# 3. Handling Multiple Exceptions

---

## 3.1 Real Programs Have Many Things That Can Go Wrong

A single user action can trigger multiple different kinds of failures. A well-written program anticipates all of them and responds appropriately.

**Analogy:** A librarian has different responses for different problems: *"That book doesn't exist"* vs. *"That book is already borrowed"* vs. *"You've exceeded your borrowing limit."*

---

## 3.2 Multiple except Clauses

You can attach **multiple `except` blocks** to a single `try`. Python checks them in order and uses the first one that matches.

```python
# Library search system
def find_book(library, book_index):
    """
    Searches for a book in the library catalogue.
    library: a list of book titles
    book_index: the index the user entered (as a string)
    """
    try:
        index = int(book_index)          # Could raise ValueError
        book  = library[index]           # Could raise IndexError
        print(f"Found: '{book}'")

    except ValueError:
        print("Error: Please enter a valid number for the book index.")

    except IndexError:
        print("Error: That book number does not exist in our catalogue.")


catalogue = ["Python Basics", "Data Structures", "Algorithms 101"]

find_book(catalogue, "abc")   # ValueError
find_book(catalogue, "99")    # IndexError
find_book(catalogue, "1")     # Success
```

**Output:**
```
Error: Please enter a valid number for the book index.
Error: That book number does not exist in our catalogue.
Found: 'Data Structures'
```

---

## 3.3 Catching Multiple Exceptions in One Line

If two or more exceptions should be handled **the same way**, group them in a tuple:

```python
# Game score entry — handles both type and value errors the same way
def record_score(player_name, raw_score):
    try:
        score = int(raw_score)
        scores = [50, 75, 90]
        print(f"{player_name} matched score: {scores[score]}")

    except (ValueError, IndexError):
        print(f"Could not record score for {player_name}. Invalid entry.")


record_score("Alice", "two")   # ValueError
record_score("Bob",   "100")   # IndexError
record_score("Carol", "1")     # Success
```

**Output:**
```
Could not record score for Alice. Invalid entry.
Could not record score for Bob. Invalid entry.
Carol matched score: 75
```

---

## 3.4 Exception Hierarchy — Broad vs. Specific

Python exceptions are organised in a **hierarchy**. More specific exceptions are subclasses of broader ones.

```
BaseException
└── Exception
    ├── ValueError
    ├── TypeError
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    └── OSError
        └── FileNotFoundError
```

> **Rule:** Always put **specific** exceptions **before** broad ones. If you put `Exception` first, it catches everything and the specific handlers below it are never reached.

```python
# WRONG — specific handler is unreachable
try:
    result = 10 / 0
except Exception:
    print("Something went wrong.")
except ZeroDivisionError:          # Never reached!
    print("Cannot divide by zero.")


# CORRECT — specific first, broad last
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 3.5 Practical Example — Bank Account Withdrawal

```python
def withdraw(balance, amount_str):
    """
    Processes a bank withdrawal.
    balance   : current account balance (float)
    amount_str: withdrawal amount entered by user (string)
    """
    try:
        amount = float(amount_str)       # Might raise ValueError

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > balance:
            raise ValueError(
                f"Insufficient funds. Available balance: £{balance:.2f}"
            )

        balance -= amount
        print(f"Withdrawn: £{amount:.2f}. New balance: £{balance:.2f}")
        return balance

    except ValueError as e:
        print(f"Withdrawal error: {e}")
        return balance

    finally:
        print("--- End of transaction ---")


# Test the function
withdraw(500.00, "abc")     # ValueError from float()
withdraw(500.00, "-50")     # ValueError from custom check
withdraw(500.00, "600")     # ValueError — insufficient funds
withdraw(500.00, "200")     # Success
```

**Output:**
```
Withdrawal error: could not convert string to float: 'abc'
--- End of transaction ---
Withdrawal error: Withdrawal amount must be positive.
--- End of transaction ---
Withdrawal error: Insufficient funds. Available balance: £500.00
--- End of transaction ---
Withdrawn: £200.00. New balance: £300.00
--- End of transaction ---
```

---

## 3.6 Key Takeaways — Multiple Exceptions

- Use **multiple `except` blocks** for different error responses.
- Group exceptions in a **tuple** when they share the same handler.
- Order matters: **specific before broad**.
- You can `raise` exceptions intentionally to enforce business rules.

---

---

# 4. Writing Custom Exceptions

---

## 4.1 Why Create Custom Exceptions?

Built-in exceptions like `ValueError` and `TypeError` are generic. In a real application, you want exceptions that **describe your specific domain**.

Compare:
- `ValueError: invalid value` ← vague
- `InsufficientFundsError: Balance too low for this withdrawal` ← clear, professional

Custom exceptions make your code:
- Easier to read and maintain
- More debuggable (you know exactly what went wrong)
- More professional (domain-specific error types)

---

## 4.2 Creating a Custom Exception

All custom exceptions **inherit from the built-in `Exception` class** (or a subclass of it). This is the OOP concept of inheritance applied directly to error handling.

```python
# Define a custom exception for a banking application
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass  # 'pass' means we add no extra behaviour — inheriting is enough


# Use the custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw £{amount:.2f}. Balance is only £{balance:.2f}."
        )
    return balance - amount


# Test it
try:
    new_balance = withdraw(300.00, 500.00)
except InsufficientFundsError as e:
    print(f"Bank Error: {e}")
```

**Output:**
```
Bank Error: Cannot withdraw £500.00. Balance is only £300.00.
```

---

## 4.3 Adding Custom Attributes

Custom exceptions can store **extra information** beyond just a message. This is useful when code that catches the exception needs to know more details.

```python
class InsufficientFundsError(Exception):
    """
    Raised when a withdrawal exceeds the available balance.
    Stores both the attempted amount and the actual balance.
    """
    def __init__(self, amount, balance):
        self.amount  = amount
        self.balance = balance
        # Call the parent class constructor with a formatted message
        super().__init__(
            f"Cannot withdraw £{amount:.2f}. "
            f"Available balance: £{balance:.2f}."
        )


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount


# Test with custom exception
try:
    new_balance = withdraw(200.00, 350.00)
except InsufficientFundsError as e:
    print(f"Transaction declined: {e}")
    print(f"You tried: £{e.amount:.2f} | Available: £{e.balance:.2f}")
except ValueError as e:
    print(f"Invalid input: {e}")
```

**Output:**
```
Transaction declined: Cannot withdraw £350.00. Available balance: £200.00.
You tried: £350.00 | Available: £200.00
```

---

## 4.4 Building an Exception Hierarchy

For larger applications, you can create a **family of related exceptions** — all inheriting from one application-level base exception.

```python
# Base exception for a student management system
class StudentSystemError(Exception):
    """Base exception for all student system errors."""
    pass


class StudentNotFoundError(StudentSystemError):
    """Raised when a student ID does not exist."""
    pass


class GradeOutOfRangeError(StudentSystemError):
    """Raised when a grade is outside the valid 0–100 range."""
    pass


class EnrolmentError(StudentSystemError):
    """Raised when a student cannot be enrolled in a course."""
    pass
```

Now your application code can:
- Catch **all** student system errors with `except StudentSystemError`
- Catch **specific** ones individually

```python
# Student grade assignment
def assign_grade(student_id, grade, students):
    """
    Assigns a grade to a student.
    students: dict mapping student_id -> student_name
    """
    if student_id not in students:
        raise StudentNotFoundError(
            f"No student found with ID: {student_id}"
        )
    if not (0 <= grade <= 100):
        raise GradeOutOfRangeError(
            f"Grade {grade} is invalid. Must be between 0 and 100."
        )

    print(f"Grade {grade} assigned to {students[student_id]}.")


# Sample data
students = {101: "Alice", 102: "Bob", 103: "Carol"}

# Test the function
test_cases = [
    (999, 85),   # StudentNotFoundError
    (101, 110),  # GradeOutOfRangeError
    (102, 75),   # Success
]

for sid, grade in test_cases:
    try:
        assign_grade(sid, grade, students)
    except StudentNotFoundError as e:
        print(f"[Not Found] {e}")
    except GradeOutOfRangeError as e:
        print(f"[Grade Error] {e}")
```

**Output:**
```
[Not Found] No student found with ID: 999
[Grade Error] Grade 110 is invalid. Must be between 0 and 100.
Grade 75 assigned to Bob.
```

---

## 4.5 Re-raising Exceptions

Sometimes you want to **catch** an exception to log it, then **re-raise** it so the caller can handle it too.

```python
import logging

class ShoppingCartError(Exception):
    """Base exception for shopping cart errors."""
    pass


def add_to_cart(item, quantity):
    """Adds an item to the shopping cart."""
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        print(f"Added {quantity}x {item} to cart.")
    except ValueError as e:
        # Log the error for the developer
        print(f"[LOG] add_to_cart failed: {e}")
        # Re-raise so the calling code also knows about it
        raise ShoppingCartError(f"Cart update failed: {e}") from e


# Calling code
try:
    add_to_cart("Python Book", -3)
except ShoppingCartError as e:
    print(f"Shopping error: {e}")
```

**Output:**
```
[LOG] add_to_cart failed: Quantity must be at least 1.
Shopping error: Cart update failed: Quantity must be at least 1.
```

---

## 4.6 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Not inheriting from `Exception` | Your exception won't integrate with Python's error system | Always subclass `Exception` |
| Using generic names like `MyError` | Unclear in large codebases | Use domain-specific names: `InsufficientFundsError` |
| Forgetting `super().__init__(message)` | The exception has no message | Always call the parent `__init__` |
| Over-creating exceptions | One exception per tiny scenario clutters the code | Group related errors under a base exception |

---

## 4.7 Key Takeaways — Custom Exceptions

- Custom exceptions **inherit from `Exception`**.
- They make error messages **domain-specific and meaningful**.
- Add **custom attributes** to store extra failure context.
- Build an **exception hierarchy** for large systems.
- Use `raise ... from e` to chain exceptions and preserve the original cause.

---

---

# 5. File Handling Modes

---

## 5.1 What is File Handling?

So far, all data in your programs disappears when the program ends. **File handling** lets you:
- **Persist data** — save it between program runs
- **Read stored data** — load it back when needed
- **Exchange data** — share information between programs

**Analogy:** Your program's variables are like a whiteboard — easy to write on, but erased when class ends. Files are like a notebook — you can close it, come back tomorrow, and the notes are still there.

---

## 5.2 Opening a File — the open() Function

Every file operation starts with `open()`:

```python
file_object = open("filename.txt", "mode")
```

- `"filename.txt"` — the path to the file
- `"mode"` — what you intend to do with the file

---

## 5.3 File Modes Reference

| Mode | Symbol | Description | File Must Exist? | Overwrites? |
|---|---|---|---|---|
| Read | `"r"` | Read only; default mode | Yes | No |
| Write | `"w"` | Write (creates or overwrites) | No | **Yes** |
| Append | `"a"` | Add to end without overwriting | No | No |
| Read + Write | `"r+"` | Read and write | Yes | No |
| Write + Read | `"w+"` | Write and read (overwrites) | No | **Yes** |
| Append + Read | `"a+"` | Append and read | No | No |
| Binary Read | `"rb"` | Read binary files (images, PDFs) | Yes | No |
| Binary Write | `"wb"` | Write binary files | No | **Yes** |

> **Warning:** Mode `"w"` **completely erases** the file if it already exists. Always double-check before using it.

---

## 5.4 Text vs. Binary Mode

- **Text mode** (default): reads/writes strings; newlines are translated automatically
- **Binary mode** (`"b"`): reads/writes raw bytes; used for images, audio, PDFs

```python
# Text mode — for .txt, .csv, .json files
text_file = open("students.txt", "r")

# Binary mode — for images, PDFs, etc.
image_file = open("photo.jpg", "rb")
```

---

## 5.5 Key Takeaways — File Modes

- Always specify the **correct mode** before opening a file.
- `"w"` is **destructive** — it erases the file first.
- Use `"a"` when you want to add to existing content.
- Use binary mode (`"b"`) for non-text files.

---

---

# 6. Reading Files

---

## 6.1 Three Ways to Read a File

Python gives you three methods for reading file content:

| Method | Returns | Best For |
|---|---|---|
| `.read()` | Entire file as one string | Small files |
| `.readline()` | One line at a time | Large files, line-by-line processing |
| `.readlines()` | List of all lines (with `\n`) | When you need all lines as a list |

---

## 6.2 Setup — Creating a Sample File

Before reading, let's create a sample file to work with. Run this once:

```python
# Create a sample student records file
with open("students.txt", "w") as f:
    f.write("Alice,85,Pass\n")
    f.write("Bob,42,Fail\n")
    f.write("Carol,91,Pass\n")
    f.write("David,67,Pass\n")

print("students.txt created successfully.")
```

**Output:**
```
students.txt created successfully.
```

---

## 6.3 Reading the Entire File with .read()

```python
# Read the entire file at once
with open("students.txt", "r") as f:
    content = f.read()

print("--- File Contents ---")
print(content)
```

**Output:**
```
--- File Contents ---
Alice,85,Pass
Bob,42,Fail
Carol,91,Pass
David,67,Pass
```

> **Best practice:** Always use the `with` statement (covered in Section 9). It automatically closes the file when done.

---

## 6.4 Reading Line by Line with .readline()

`.readline()` reads **one line** each time it is called. When there are no more lines, it returns an empty string `""`.

```python
# Read the file one line at a time
with open("students.txt", "r") as f:
    line = f.readline()          # Read first line
    while line:                  # Empty string is falsy — stops the loop
        print(line.strip())      # .strip() removes the trailing \n
        line = f.readline()      # Read next line
```

**Output:**
```
Alice,85,Pass
Bob,42,Fail
Carol,91,Pass
David,67,Pass
```

---

## 6.5 Reading All Lines with .readlines()

`.readlines()` returns a **list** where each element is one line (including `\n`).

```python
# Read all lines into a list
with open("students.txt", "r") as f:
    lines = f.readlines()

# Each line is a string with \n at the end
print(f"Number of students: {len(lines)}")

for line in lines:
    # .strip() removes whitespace and newline characters
    name, score, result = line.strip().split(",")
    print(f"Student: {name:10s} | Score: {score:3s} | Result: {result}")
```

**Output:**
```
Number of students: 4
Student: Alice      | Score: 85  | Result: Pass
Student: Bob        | Score: 42  | Result: Fail
Student: Carol      | Score: 91  | Result: Pass
Student: David      | Score: 67  | Result: Pass
```

---

## 6.6 Iterating Directly Over a File Object

The cleanest and most Pythonic way to read a file line by line:

```python
# Most Pythonic approach — iterate directly over the file object
print("--- Library Book Catalogue ---")
with open("students.txt", "r") as f:
    for line in f:
        name, score, result = line.strip().split(",")
        status = "✓" if result == "Pass" else "✗"
        print(f"  {status} {name} — {score}%")
```

**Output:**
```
--- Library Book Catalogue ---
  ✓ Alice — 85%
  ✗ Bob — 42%
  ✓ Carol — 91%
  ✓ David — 67%
```

---

## 6.7 Reading a Specific Number of Characters

`.read(n)` reads exactly `n` characters:

```python
with open("students.txt", "r") as f:
    first_ten = f.read(10)   # Read only the first 10 characters
    print(repr(first_ten))   # repr() shows hidden characters like \n
```

**Output:**
```
'Alice,85,P'
```

---

## 6.8 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Not closing the file | Keeps a lock on the file, wastes memory | Use `with` statement |
| Forgetting `.strip()` | Lines contain `\n`, causing layout issues | Always strip lines when parsing |
| Using `.read()` on huge files | Loads entire file into RAM | Use line-by-line iteration instead |
| Hardcoding paths | Breaks on different machines | Use relative paths or `os.path` |

---

## 6.9 Key Takeaways — Reading Files

- `.read()` → entire file as string; use for small files only.
- `.readline()` → one line at a time; memory efficient.
- `.readlines()` → list of all lines.
- Iterating directly over a file object is the **most Pythonic** approach.
- Always use `.strip()` to remove trailing newline characters.

---

---

# 7. Writing and Appending to Files

---

## 7.1 Writing to a File — Mode "w"

Mode `"w"` creates the file if it does not exist, or **completely overwrites it** if it does.

**Analogy:** Mode `"w"` is like using a whiteboard eraser first, then writing fresh content.

```python
# Save a shopping list to a file
shopping_list = [
    "Apples",
    "Bread",
    "Milk",
    "Cheese",
    "Eggs",
]

with open("shopping_list.txt", "w") as f:
    for item in shopping_list:
        f.write(item + "\n")    # Write each item on a new line

print("Shopping list saved.")
```

**File content of shopping_list.txt:**
```
Apples
Bread
Milk
Cheese
Eggs
```

---

## 7.2 Writing Multiple Lines with writelines()

`.writelines()` writes a list of strings — but **does not add newlines automatically**:

```python
# Game leaderboard
leaderboard = [
    "1. Alice - 9500\n",
    "2. Bob   - 8750\n",
    "3. Carol - 8200\n",
]

with open("leaderboard.txt", "w") as f:
    f.writelines(leaderboard)   # Each string must contain its own \n

print("Leaderboard saved.")
```

**File content of leaderboard.txt:**
```
1. Alice - 9500
2. Bob   - 8750
3. Carol - 8200
```

---

## 7.3 Appending to a File — Mode "a"

Mode `"a"` opens the file and places the cursor **at the end**. Existing content is preserved.

**Analogy:** Mode `"a"` is like adding a new entry to the bottom of a notebook — all previous pages stay untouched.

```python
# Add a new student to the records file
new_entry = "Eve,88,Pass\n"

with open("students.txt", "a") as f:
    f.write(new_entry)

print("New student added.")

# Verify the result
with open("students.txt", "r") as f:
    print(f.read())
```

**Output:**
```
New student added.
Alice,85,Pass
Bob,42,Fail
Carol,91,Pass
David,67,Pass
Eve,88,Pass
```

---

## 7.4 Appending Multiple Records

```python
# Daily transaction log — append each day's transactions
new_transactions = [
    "2026-05-21,Alice,Deposit,£500\n",
    "2026-05-21,Bob,Withdrawal,£200\n",
]

with open("bank_log.txt", "a") as f:
    f.writelines(new_transactions)

print("Transactions logged.")
```

---

## 7.5 Using print() to Write Files

Python's `print()` function has a `file` parameter — a convenient alternative to `.write()` that adds newlines automatically:

```python
# Using print() to write to a file
students = [
    ("Alice",  85, "Pass"),
    ("Bob",    42, "Fail"),
    ("Carol",  91, "Pass"),
]

with open("report.txt", "w") as f:
    print("=== Student Report ===", file=f)
    print(f"{'Name':<10} {'Score':>5} {'Result':>8}", file=f)
    print("-" * 28, file=f)
    for name, score, result in students:
        print(f"{name:<10} {score:>5} {result:>8}", file=f)

print("Report written to report.txt")
```

**File content of report.txt:**
```
=== Student Report ===
Name       Score   Result
----------------------------
Alice         85     Pass
Bob           42     Fail
Carol         91     Pass
```

---

## 7.6 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Using `"w"` when you meant `"a"` | Destroys existing data | Double-check the mode before opening |
| Forgetting `\n` in `.write()` | All content runs together on one line | Add `\n` explicitly or use `print(..., file=f)` |
| Writing non-string data directly | `f.write(42)` raises `TypeError` | Convert: `f.write(str(42))` |

---

## 7.7 Key Takeaways — Writing and Appending

- `"w"` mode **erases** existing content before writing.
- `"a"` mode **preserves** existing content and adds to the end.
- `.write(string)` writes a single string — include `\n` manually.
- `.writelines(list)` writes a list — each element needs its own `\n`.
- `print(..., file=f)` is a convenient alternative that adds newlines automatically.

---

---

# 8. Handling File Exceptions

---

## 8.1 What Can Go Wrong With Files?

File operations are one of the most common sources of runtime exceptions because they depend on the **external world** — the filesystem, disk space, permissions — factors your code cannot fully control.

| Exception | Cause |
|---|---|
| `FileNotFoundError` | The file does not exist (mode `"r"`) |
| `PermissionError` | No read/write permission on the file |
| `IsADirectoryError` | Tried to open a directory as a file |
| `OSError` | General OS-level file error (disk full, etc.) |
| `UnicodeDecodeError` | File contains characters Python cannot decode |

---

## 8.2 Handling FileNotFoundError

```python
def read_student_records(filename):
    """
    Reads and prints student records from a file.
    Handles missing files gracefully.
    """
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        print("Please check the filename and try again.")


# Test with a file that doesn't exist
read_student_records("missing_records.txt")

# Test with a file that exists
read_student_records("students.txt")
```

**Output:**
```
Error: 'missing_records.txt' was not found.
Please check the filename and try again.
Alice,85,Pass
Bob,42,Fail
Carol,91,Pass
David,67,Pass
Eve,88,Pass
```

---

## 8.3 Handling PermissionError

```python
def save_report(filename, content):
    """
    Saves content to a file.
    Handles permission errors gracefully.
    """
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"Report saved to '{filename}'.")

    except PermissionError:
        print(f"Error: No permission to write to '{filename}'.")
        print("Try saving to a different location.")

    except OSError as e:
        print(f"OS error while saving: {e}")


save_report("report.txt", "Student report data...")
```

---

## 8.4 Checking if a File Exists Before Opening

Sometimes you want to **check first** rather than catch an exception. Use `os.path.exists()`:

```python
import os

filename = "students.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"'{filename}' does not exist. Creating a new file.")
    with open(filename, "w") as f:
        f.write("# Student Records\n")
```

> **Note:** Using `try/except` is generally preferred over `os.path.exists()` because there is a small window between the check and the open where the file could be deleted (a race condition). For simple scripts, either approach works fine.

---

## 8.5 Handling UnicodeDecodeError

```python
# Reading a file with a specific encoding
try:
    with open("library_catalogue.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

except UnicodeDecodeError:
    print("Error: Cannot read file — unexpected character encoding.")
    print("Try opening with encoding='latin-1' or encoding='utf-8-sig'.")

except FileNotFoundError:
    print("Error: File not found.")
```

> **Best practice:** Always specify `encoding="utf-8"` when opening text files to avoid encoding surprises, especially on Windows.

---

## 8.6 Comprehensive File Handler

```python
def load_game_save(filename):
    """
    Loads a game save file.
    Handles all common file errors with helpful messages.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        print("Game save loaded successfully!")
        return data

    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None

    except PermissionError:
        print("Cannot access save file. Check file permissions.")
        return None

    except UnicodeDecodeError:
        print("Save file is corrupted or in wrong format.")
        return None

    except OSError as e:
        print(f"Unexpected file error: {e}")
        return None


# Test the function
load_game_save("save_game.dat")
load_game_save("students.txt")
```

---

## 8.7 Key Takeaways — File Exceptions

- `FileNotFoundError` is the most common file exception — always handle it.
- `PermissionError` matters in production environments with restricted file access.
- Always specify `encoding="utf-8"` when opening text files.
- Use `os.path.exists()` for pre-checks; use `try/except` for robust handling.

---

---

# 9. The with Statement

---

## 9.1 The Problem with Manual File Closing

When you open a file without `with`, you are responsible for closing it:

```python
# FRAGILE approach — without with
f = open("students.txt", "r")
content = f.read()
f.close()    # What if an exception occurs before this line?
```

If an exception happens between `open()` and `close()`, the file **never gets closed**. This is a resource leak — the file stays locked, and other programs (or your own code) may not be able to access it.

---

## 9.2 How with Solves This

The `with` statement creates a **context manager** — a block of code that **automatically cleans up** after itself, whether an exception occurred or not.

```python
# ROBUST approach — with statement
with open("students.txt", "r") as f:
    content = f.read()
# File is automatically closed here — even if an exception occurred inside
```

**Analogy:** The `with` statement is like hiring a professional who always locks up the office on the way out, no matter what. You don't have to remember — it's their job.

---

## 9.3 How the with Statement Works

Under the hood, `with` uses two special methods:
- `__enter__`: runs when entering the `with` block (opens the file)
- `__exit__`: runs when leaving the `with` block (closes the file, even on error)

You don't need to implement these yourself for files — Python's file objects already support them.

---

## 9.4 Practical Example — Student Report Writer

```python
# Write a formatted student report using with
students = [
    ("Alice",  85, "Pass"),
    ("Bob",    42, "Fail"),
    ("Carol",  91, "Pass"),
    ("David",  67, "Pass"),
]

# Writing the report
with open("student_report.txt", "w", encoding="utf-8") as report:
    report.write("=============================\n")
    report.write("     STUDENT REPORT CARD     \n")
    report.write("=============================\n")
    for name, score, result in students:
        report.write(f"{name:<10}: {score:3d}% — {result}\n")
    report.write("=============================\n")

print("Report written successfully.")

# Reading it back to verify
with open("student_report.txt", "r", encoding="utf-8") as report:
    print(report.read())
```

**Output:**
```
Report written successfully.
=============================
     STUDENT REPORT CARD     
=============================
Alice     :  85% — Pass
Bob       :  42% — Fail
Carol     :  91% — Pass
David     :  67% — Pass
=============================
```

---

## 9.5 Opening Multiple Files at Once

You can open multiple files in a single `with` statement:

```python
# Copy student records from one file to another
with open("students.txt", "r", encoding="utf-8") as source, \
     open("students_backup.txt", "w", encoding="utf-8") as backup:

    for line in source:
        backup.write(line)

print("Backup created successfully.")
```

---

## 9.6 with and Exception Handling Together

`with` and `try/except` work beautifully together:

```python
def process_library_records(filename):
    """
    Processes library book records from a file.
    The with statement ensures the file is always closed.
    try/except handles errors gracefully.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"Processing: {filename}")
            for line_number, line in enumerate(f, start=1):
                title, author, copies = line.strip().split(",")
                print(
                    f"  Line {line_number}: '{title}' "
                    f"by {author} — {copies} copies"
                )

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

    except ValueError:
        print(f"Error: '{filename}' has unexpected data format.")


# Create a test file first
with open("library.txt", "w") as f:
    f.write("Python Crash Course,Eric Matthes,5\n")
    f.write("Clean Code,Robert Martin,3\n")
    f.write("The Pragmatic Programmer,Hunt & Thomas,4\n")

process_library_records("library.txt")
process_library_records("missing_file.txt")
```

**Output:**
```
Processing: library.txt
  Line 1: 'Python Crash Course' by Eric Matthes — 5 copies
  Line 2: 'Clean Code' by Robert Martin — 3 copies
  Line 3: 'The Pragmatic Programmer' by Hunt & Thomas — 4 copies
Error: 'missing_file.txt' not found.
```

---

## 9.7 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Not using `with` | File may never close if exception occurs | Always use `with open(...)` |
| Using `f.close()` inside `with` | Redundant — `with` already closes it | Remove the manual `close()` |
| Forgetting `as f` | You have no variable to read/write through | Always include `as file_variable` |
| Not specifying encoding | Causes `UnicodeDecodeError` on some systems | Always add `encoding="utf-8"` |

---

## 9.8 Key Takeaways — The with Statement

- `with open(...) as f` **automatically closes** the file when the block ends.
- This happens even if an **exception** occurs inside the block.
- It is the **recommended** way to work with files in Python.
- You can open **multiple files** in one `with` statement.
- Combine `with` and `try/except` for safe and clean file operations.

---

---

# 10. Summary and Key Takeaways

---

## 10.1 Unit Summary

Unit 3 covered two closely related topics: **handling things that go wrong** (exceptions) and **persisting data beyond a program's lifetime** (file I/O). Together, these skills are essential for building programs that behave professionally in the real world.

---

## 10.2 Exception Handling — Summary Table

| Concept | What it Does | When to Use |
|---|---|---|
| `try` | Wraps risky code | Always, around any operation that might fail |
| `except ExceptionType` | Catches a specific error | Name the exact exception(s) you expect |
| `except (E1, E2)` | Catches multiple errors with one handler | When two errors deserve the same response |
| `else` | Runs if no exception occurred | For code that only makes sense after success |
| `finally` | Always runs | Cleanup: closing connections, logging, etc. |
| `raise` | Throws an exception intentionally | Enforcing business rules |
| Custom exceptions | Domain-specific error types | Any non-trivial application |

---

## 10.3 File Handling — Summary Table

| Concept | What it Does |
|---|---|
| `open(file, "r")` | Open for reading |
| `open(file, "w")` | Open for writing (overwrites!) |
| `open(file, "a")` | Open for appending |
| `.read()` | Read entire file as string |
| `.readline()` | Read one line |
| `.readlines()` | Read all lines into a list |
| `for line in f:` | Iterate line by line (most Pythonic) |
| `.write(string)` | Write a string to the file |
| `.writelines(list)` | Write a list of strings |
| `with open(...) as f:` | Auto-close file; always preferred |
| `encoding="utf-8"` | Specify character encoding |

---

## 10.4 Golden Rules for This Unit

1. **Always name the exception** — never use a bare `except:`.
2. **Keep `try` blocks short** — only wrap the line(s) that might fail.
3. **Always use `with`** for file operations.
4. **Always specify `encoding="utf-8"`** when opening text files.
5. **Use `"a"` not `"w"`** when adding to existing files.
6. **Create custom exceptions** for domain-specific errors.
7. **Test failure paths** as much as success paths.

---

## 10.5 How This Unit Connects to the Course

| Connection | Detail |
|---|---|
| **Unit 2 → Unit 3** | Custom exceptions are subclasses — direct application of OOP inheritance |
| **Unit 3 → Unit 6** | Database error handling uses the same `try/except` patterns |
| **Unit 3 → Unit 7** | Network programming requires robust exception handling for connection failures |
| **Unit 3 → Unit 8** | Thread safety and file locking become relevant in multithreaded file I/O |

---

## 10.6 Self-Check Questions

Test your understanding before moving on:

1. What is the difference between a `SyntaxError` and a `RuntimeError`?
2. When does the `finally` block run?
3. Why is bare `except:` considered bad practice?
4. What happens to a file opened with `"w"` mode if it already exists?
5. What is the difference between `.read()` and `.readlines()`?
6. Why is the `with` statement preferred over manually calling `.close()`?
7. How do you create a custom exception class in Python?
8. Which exception would you get if you called `open("file.txt", "r")` on a file that doesn't exist?

---

## 10.7 Practice Exercises

### Exercise 1 — Safe Calculator
Write a function `safe_divide(a, b)` that:
- Takes two string inputs from the user
- Converts them to floats
- Divides `a` by `b`
- Handles `ValueError` (non-numeric input) and `ZeroDivisionError`
- Uses `finally` to print `"Calculation complete."`

---

### Exercise 2 — Student Grade File
Write a program that:
- Creates a file `grades.txt` with at least 5 student records (name, score)
- Reads the file and calculates the class average
- Handles `FileNotFoundError` and `ValueError`

---

### Exercise 3 — Shopping List Manager
Write a program with three functions:
- `add_item(item)` — appends an item to `shopping_list.txt`
- `view_list()` — reads and prints all items
- `clear_list()` — overwrites the file with an empty list
All functions must handle file exceptions.

---

### Exercise 4 — Custom Exception
Create a `BankAccount` class with:
- A custom `InsufficientFundsError` exception
- A `withdraw(amount)` method that raises the exception if the balance is too low
- A `deposit(amount)` method that raises `ValueError` for negative amounts
- Demonstrate the class with at least 4 test cases

---

### Exercise 5 — Game Score Logger
Write a program that:
- Asks the player for their name and score after each round
- Appends the score to `game_scores.txt`
- Handles `ValueError` for non-numeric scores
- Reads and displays the all-time top score from the file at the end

---

*End of Unit 3 Lecture Notes*

---
