# Unit 3 — Exception Handling and File I/O

## Short Questions (2 Marks)

### Q1. Define a syntax error and give an example from the notes.

- A syntax error means Python literally cannot understand what you typed — like a sentence missing a full stop. Python catches this before the program even starts running.

```python
if True
    print("hi")
# SyntaxError: expected ':'
```

---

### Q2. What is a runtime exception and how does it differ from a syntax error?

- A runtime exception happens while the program is actually running — the code was written correctly, but something went wrong during execution, like dividing by zero. A syntax error stops the program before it even starts; a runtime exception stops it partway through.

```python
print(10 / 0)   # ZeroDivisionError - only shows up when this line runs
```

---

### Q3. List four common built-in exceptions in Python as shown in the notes.

- `ZeroDivisionError` (dividing by zero), `ValueError` (right type, wrong value — e.g. `int("abc")`), `TypeError` (wrong type entirely — e.g. adding a string and a number), and `IndexError` (asking for a list position that doesn't exist).

---

### Q4. Explain what a logical error is and why it is harder to detect than other errors.

- A logical error means the code runs perfectly fine — no crash, no error message — but produces the wrong answer, because the logic itself was flawed. It's harder to catch because Python has nothing to complain about; the program looks completely healthy while quietly giving the wrong result.

```python
def average(a, b):
    return a + b / 2   # BUG: should be (a + b) / 2
```

---

### Q5. State the basic syntax of a try/except block.

```python
try:
    risky_code()
except SomeError:
    handle_it()
```

---

### Q6. Explain the purpose of the else clause in exception handling.

- `else` runs only if the `try` block finished with no errors at all — it keeps "what happens on success" separate from the risky code itself, so the two don't get mixed together.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success:", result)
```

---

### Q7. What is the purpose of the finally clause?

- `finally` always runs no matter what happened — error or no error — which makes it the natural place for cleanup, like closing a file.

```python
try:
    f = open("data.txt")
finally:
    f.close()   # always runs
```

---

### Q8. Why is catching a bare except: considered bad practice?

- A bare `except:` catches absolutely everything — including mistakes in your own code (like a typo causing a `NameError`) — and quietly hides them instead of letting you find and fix the real problem. It's always better to catch the specific error you're actually expecting.

---

### Q9. Define a custom exception and explain its purpose.

- A custom exception is your own error type, made by creating a small class that inherits from `Exception`. Its purpose is to give errors specific, meaningful names related to your own program, instead of using Python's generic built-in errors for everything.

```python
class InsufficientFundsError(Exception):
    pass
```

---

### Q10. What does it mean to "raise" an exception?

- "Raising" an exception means deliberately triggering an error yourself with the `raise` keyword, usually because you've detected a problem that the code shouldn't continue past.

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

### Q11. List the six file modes discussed in the notes.

- `"r"` (read), `"w"` (write — erases existing content), `"a"` (append — adds to the end), `"r+"` (read and write), `"rb"` (read binary), and `"wb"` (write binary).

---

### Q12. Explain the difference between text mode and binary mode in file operations.

- Text mode (the default) reads and writes ordinary readable text, automatically handling things like line endings. Binary mode (`"rb"`, `"wb"`) reads and writes raw bytes exactly as they are, used for non-text files like images or PDFs.

---

### Q13. What is the difference between .read(), .readline(), and .readlines()?

- `.read()` grabs the entire file as one single string. `.readline()` grabs just one line at a time. `.readlines()` grabs every line at once, but as a list of separate strings, one per line.

---

### Q14. Explain what the with statement does in file operations.

- `with` opens a file and guarantees it gets closed automatically once you're done with it — even if an error happens in between — so you never have to remember to call `.close()` yourself.

```python
with open("data.txt") as f:
    content = f.read()
# file is already closed here, automatically
```

---

### Q15. State the dangers of using mode "w" when opening a file.

- Mode `"w"` instantly wipes out whatever was already in the file the moment it's opened — even before you write anything new. If you meant to add to the file instead, this permanently deletes the old content by mistake.

---

### Q16. What is a FileNotFoundError and in which mode does it occur?

- `FileNotFoundError` happens when you try to open a file for reading (`"r"`) that doesn't actually exist. It's specific to reading — write mode (`"w"`) instead just creates the file if it isn't there.

---

### Q17. What does .write() do and how does it differ from .writelines()?

- `.write()` writes a single string to the file. `.writelines()` writes a whole list of strings at once — but note it does *not* automatically add newlines between them, so each string in the list needs its own `\n` if you want separate lines.

```python
f.write("Hello\n")
f.writelines(["Line1\n", "Line2\n"])
```

---

### Q18. Explain the difference between append mode ("a") and write mode ("w").

- Append mode (`"a"`) adds new content to the *end* of the file, keeping everything already there. Write mode (`"w"`) erases the file's entire existing content first, then starts writing fresh.

---

### Q19. Why should you always specify encoding="utf-8" when opening a file?

- Without it, Python falls back to whatever default encoding the operating system happens to use, which can differ between machines — this can cause a file that works fine on your computer to break with odd characters or errors on someone else's. Setting `encoding="utf-8"` explicitly makes the behaviour consistent everywhere.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

---

### Q20. What is the difference between handling multiple exceptions with separate except blocks versus combining them in a tuple?

- Separate `except` blocks let each error type get its own distinct response — useful when different errors genuinely need different handling. Combining them in a tuple, `except (TypeError, ValueError):`, treats several error types identically with one shared block — useful when the same fix applies to all of them.

```python
try:
    x = int("abc")
except (TypeError, ValueError) as e:   # same response for both
    print("Bad input:", e)
```

---

## Medium Questions (5 Marks)

### Q1. Explain the complete structure of try/except/else/finally and describe when each clause runs.

- This structure covers every possible outcome of a risky piece of code, with a separate, clearly labelled spot for each one.

```python
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("That wasn't a number")
else:
    print("Success! Result is", result)
finally:
    print("Done trying")
```

- `try` runs first and holds the code that might fail. If an error actually happens, the matching `except` block runs instead — and only that one, skipping the rest. If nothing went wrong at all, `else` runs, since it's specifically for the "everything worked" case. `finally` always runs last, no matter what happened above it — success, a caught error, even an uncaught one — which is why it's the natural place for cleanup like closing a file.
- Simple way to remember it: try it, catch it if needed, celebrate quietly if it worked, and clean up regardless.

---

### Q2. Discuss custom exceptions as shown in the notes. Explain how to create one, why they are useful, and how to add custom attributes.

- Making a custom exception is just making a small class that inherits from `Exception` — often just one line.

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

- They're useful because they let your errors say exactly what went wrong, in your own program's terms, instead of reusing a generic built-in error (like `ValueError`) for every unrelated problem — which makes both the code and the error messages far easier to understand later.
- Custom attributes can be added by overriding `__init__`, storing extra details directly on the exception object so the code that catches it can use them right away.

```python
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}")
        self.age = age

try:
    raise InvalidAgeError(-5)
except InvalidAgeError as e:
    print(e.age)   # -5 - available directly, no need to parse the message
```

---

### Q3. Explain how to build an exception hierarchy with a base exception and specific subclasses.

- An exception hierarchy is just a small family tree: one general exception at the top, and more specific ones branching off underneath it.

```python
class BankError(Exception):
    pass
class InsufficientFundsError(BankError):
    pass
class InvalidAmountError(BankError):
    pass
```

- This is useful because code can now catch one exact problem, or catch the whole family at once through the shared parent.

```python
try:
    raise InsufficientFundsError("Not enough balance")
except InsufficientFundsError:
    print("Handle the specific case")
except BankError:
    print("Handle any other bank error")
```

- The key thing to get right is order: Python checks `except` blocks from top to bottom, so the more specific exceptions always need to come before the more general parent one, otherwise the parent would catch everything first and the specific block would never run.

---

### Q4. Describe the three ways to read a file and explain when each is most appropriate.

- `.read()` grabs everything at once as one big string — appropriate for small files where you just want the whole content in one go.

```python
with open("notes.txt") as f:
    content = f.read()
```

- `.readline()` grabs just one line at a time — appropriate when you need to process a file line by line, in a controlled way, especially a very large file where reading everything at once would use too much memory.

```python
with open("notes.txt") as f:
    first_line = f.readline()
```

- `.readlines()` grabs every line at once, but returns them as a list — appropriate when you want each line available separately (e.g. to loop over or index into), but the file is still small enough to fit comfortably in memory.

```python
with open("notes.txt") as f:
    lines = f.readlines()   # ['line1\n', 'line2\n', ...]
```

- For genuinely large files, the best option is often simply looping over the file object directly (`for line in f:`), which reads one line at a time under the hood without loading everything into memory at once.

---

### Q5. Explain writing and appending to files. Use examples from the notes to show the difference.

- Writing (`"w"`) starts the file completely fresh — anything already in it is erased the instant the file is opened in this mode.

```python
with open("log.txt", "w") as f:
    f.write("First entry\n")   # old content, if any, is gone now
```

- Appending (`"a"`) instead adds new content onto the end, keeping everything that was already there.

```python
with open("log.txt", "a") as f:
    f.write("Second entry\n")   # added after 'First entry', nothing lost
```

- A simple way to remember the difference: `"w"` is like starting a new page and throwing away the old one; `"a"` is like continuing to write on the same page. If a file is opened in `"w"` mode by mistake when `"a"` was intended, previous data is lost permanently with no warning.

---

### Q6. Discuss file exceptions and how to handle them. Include common exceptions and recommended strategies.

- A few specific exceptions come up constantly when working with files, and each has its own typical cause.
- `FileNotFoundError` — trying to open a file for reading that doesn't exist.
- `PermissionError` — trying to open a file the program isn't allowed to access.
- `IsADirectoryError` — trying to open a folder as if it were a file.

```python
try:
    with open("missing.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("That file doesn't exist")
except PermissionError:
    print("No permission to open this file")
```

- The recommended strategy is to always wrap file operations in `try`/`except`, catching the specific exceptions that are actually likely, and to combine this with the `with` statement so the file still gets closed properly even if an error happens partway through.

---

### Q7. Explain the advantages of the with statement and show how it compares to manual file closing.

- Manually closing a file means remembering to call `.close()` yourself, on every path through the code — including if an error happens partway through, which is easy to forget.

```python
f = open("data.txt")
content = f.read()
f.close()   # skipped entirely if an error happens before this line!
```

- `with` handles this automatically — the file is guaranteed to close once the block ends, whether it finished normally or an error interrupted it.

```python
with open("data.txt") as f:
    content = f.read()
# closed here automatically, no matter what happened above
```

- This matters because a file left open by accident can waste system resources, or even block other programs from accessing that same file — `with` removes this risk entirely, with less code to write and nothing to remember.

---

### Q8. Discuss how to handle multiple exceptions in Python, including both separate blocks and tuple grouping.

- Separate `except` blocks are used when different error types genuinely need different responses.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

- Grouping exceptions in a tuple is used instead when several error types should all be handled the exact same way.

```python
try:
    data = process(user_input)
except (TypeError, ValueError) as e:
    print("Invalid input:", e)
```

- The choice really comes down to whether the errors need different handling (use separate blocks) or the same handling (use one tuple) — and as with any exception hierarchy, more specific exceptions should always be listed before more general ones.

---

### Q9. Explain the concept of "raising exceptions intentionally" using an example from the notes.

- Sometimes the safest thing a function can do is refuse to continue and clearly say why — that's exactly what `raise` is for, deliberately triggering an error the moment an invalid situation is detected.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print("Transaction failed:", e)
```

- This is useful because it stops bad data from quietly spreading further into the program — instead of continuing on with an obviously wrong value (like a negative balance), the function stops immediately and hands the caller a clear, specific reason why.

---

### Q10. Describe how to safely use print() to write to files and explain when this approach is useful.

- `print()` normally writes to the screen, but its `file=` argument can redirect that same output straight into an open file instead — a small, convenient shortcut.

```python
with open("log.txt", "a") as f:
    print("Event logged", file=f)
```

- This is useful anywhere `print()` was already being used for debugging or logging output, since it can be redirected to a file with almost no change to the code — genuinely handy for quick logging without writing a full `.write()` call with manual newline handling.

---

### Q11. Explain exception handling in the context of file operations and show a comprehensive example.

- Combining `try`/`except` with file operations means the program can respond sensibly to a missing file, bad permissions, or corrupted content, instead of crashing outright.

```python
def read_config(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} not found, using defaults")
        return ""
    except PermissionError:
        print(f"No permission to read {filename}")
        return ""
    finally:
        print("Read attempt finished")
```

- The pattern worth remembering: `with` guarantees the file is closed properly, `except` catches the specific things that can realistically go wrong, and `finally` (if used) still runs regardless — together they make file-handling code genuinely safe to run against files that might not even exist.

---

### Q12. Discuss the golden rules for exception handling and file I/O as listed in the notes.

- A short set of habits consistently separates safe, reliable file-and-error-handling code from fragile code.
- Always catch specific exceptions, never a bare `except:` — a bare except hides real bugs instead of fixing them.
- Always use `with` when working with files, so closing is never left to chance.
- Always specify `encoding="utf-8"` explicitly, so the code behaves the same on every machine.
- Use `finally` for cleanup that absolutely must happen either way.
- Raise custom exceptions with clear, specific names rather than overusing generic built-in errors for everything.
- Never silently swallow an exception — always at least log or print something, so a real problem doesn't go unnoticed.

---

## Long Questions (10 Marks)

### Q1. Explain all three types of errors in Python (syntax, runtime, logical) using examples from the notes. Discuss how each is detected and prevented.

**Introduction**

Python code can go wrong in three genuinely different ways, and telling them apart is the first step to actually fixing them.

**Body**

- A syntax error means Python cannot even understand what was typed — like a sentence with no full stop. Python catches this immediately, before the program ever starts running.

```python
if True
    print("hi")
# SyntaxError: expected ':'
```

- A runtime exception (or "runtime error") means the code was written correctly and starts running fine, but something goes wrong partway through — dividing by zero, or opening a file that doesn't exist.

```python
print(10 / 0)   # ZeroDivisionError - only appears once this exact line runs
```

- A logical error is the trickiest of the three: the program runs completely fine, with no error message at all, but produces the wrong result because the underlying logic was flawed.

```python
def average(a, b):
    return a + b / 2   # WRONG - should be (a + b) / 2
print(average(4, 6))   # 7.0, not the expected 5.0
```

- Detection differs sharply between the three: syntax errors are caught automatically by Python itself before execution; runtime exceptions are caught with `try`/`except` while the program runs; but logical errors are caught by neither — they require the programmer to actually test the code against expected results, or step through it with a debugger, since Python has no way of knowing what the "correct" answer was supposed to be.
- Prevention follows the same pattern: careful reading of error messages and consistent indentation avoids most syntax errors; anticipating what could realistically go wrong and wrapping it in `try`/`except` handles runtime exceptions; and writing test cases with known, expected answers is really the only reliable way to catch logical errors before they reach a user.

**Conclusion**

Recognising which of the three categories a bug falls into is often more than half the battle — a syntax error demands a fix to the code's structure, a runtime exception demands defensive handling, but a logical error demands re-checking the actual reasoning behind the code, and no error message will ever point that one out directly.

---

### Q2. Discuss custom exceptions in depth. Explain why they are useful, how to create them, how to add attributes, and how to build a hierarchy.

**Introduction**

Custom exceptions exist to make error handling speak the language of your own program, instead of reusing Python's generic built-in errors for every unrelated situation.

**Body**

- Creating one is simple — just a small class inheriting from `Exception`, often needing nothing more than `pass`.

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

- They're useful for two clear reasons: the error's name alone already explains what went wrong (`InvalidAgeError` is far clearer than a generic `ValueError` everywhere), and code that catches it can respond specifically to that one situation rather than guessing from a plain string message.
- Adding custom attributes means overriding `__init__` to store extra details directly on the exception object, so the code that catches it can use that information immediately, without needing to parse a message string.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} cannot cover {amount}")
        self.balance = balance
        self.amount = amount

try:
    raise InsufficientFundsError(100, 500)
except InsufficientFundsError as e:
    print(e.balance, e.amount)   # 100 500 - used directly
```

- Building a hierarchy means creating one general base exception, with more specific ones branching off it — so code can catch one exact problem, or catch the whole family through the shared parent.

```python
class BankError(Exception): pass
class InsufficientFundsError(BankError): pass
class InvalidAmountError(BankError): pass

try:
    raise InvalidAmountError("Amount must be positive")
except InsufficientFundsError:
    print("Specific: not enough funds")
except BankError:
    print("General: some other bank problem")   # this one runs
```

- The one rule that has to be respected here is ordering — since Python checks `except` blocks top to bottom, the more specific exceptions must always be listed before the general parent, or the parent would catch everything first and the specific block would never get a chance to run.

**Conclusion**

Custom exceptions, their attributes, and their hierarchy together turn error handling from a vague "something broke" into a precise, structured description of exactly what broke and what data was involved — which is exactly what makes larger programs easier to debug and maintain.

---

### Q3. Analyze the complete file handling workflow in Python. Discuss the three ways to read files, the two ways to write, the use of modes, and how the with statement ensures safety.

**Introduction**

Working with files in Python follows a fairly consistent workflow: choose the right mode, open the file safely, read or write using the right method, and let the file close automatically.

**Body**

- The mode chosen when opening a file decides what's actually allowed: `"r"` for reading only, `"w"` for writing (erasing existing content first), `"a"` for appending (keeping existing content), and `"r+"` for both reading and writing together.

```python
with open("data.txt", "r") as f:   # read only
    pass
```

- There are three ways to read a file, each suited to a different situation. `.read()` grabs the whole file as one string, good for small files. `.readline()` grabs just one line at a time, good for controlled, line-by-line processing. `.readlines()` grabs every line at once as a list, good when each line needs to be accessed separately.

```python
with open("data.txt") as f:
    whole = f.read()          # one big string
with open("data.txt") as f:
    one_line = f.readline()   # just the first line
with open("data.txt") as f:
    all_lines = f.readlines() # list of every line
```

- There are two main ways to write: `.write()` writes a single string, and `.writelines()` writes a whole list of strings at once — though it does not add newlines automatically, so each entry needs its own `\n` if separate lines are wanted.

```python
with open("out.txt", "w") as f:
    f.write("Line 1\n")
    f.writelines(["Line 2\n", "Line 3\n"])
```

- The `with` statement is what ties this whole workflow together safely — it guarantees the file is closed the moment the block ends, whether it finished normally or an error interrupted it, removing the risk of a file being left open by accident (which manual `.close()` calls do not protect against, since an early error would skip right past them).

**Conclusion**

Put together, the workflow is: pick the mode that matches the intended operation, always open with `with`, and choose the read/write method that matches how much of the file actually needs to be handled at once — following this consistently avoids the two most common file-handling mistakes: leaving files open, and accidentally erasing data with the wrong mode.

---

### Q4. Write a comprehensive analysis of exception handling in file operations. Include handling multiple file-specific exceptions, using finally for cleanup, and combining try/except with the with statement.

**Introduction**

File operations are a natural home for exception handling, since so many things can realistically go wrong — a missing file, no permission, a full disk — none of which the program can control in advance.

**Body**

- Multiple file-specific exceptions are handled by anticipating the realistic failure cases and giving each one its own `except` block.

```python
def read_config(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} not found")
        return ""
    except PermissionError:
        print(f"No permission for {filename}")
        return ""
    except UnicodeDecodeError:
        print(f"{filename} has an encoding problem")
        return ""
```

- `finally` adds a guaranteed cleanup step on top of this, running regardless of whether the read succeeded, failed with a caught exception, or even failed with something unexpected.

```python
def process_file(filename):
    try:
        f = open(filename)
        data = f.read()
    except FileNotFoundError:
        print("Missing file")
        data = None
    finally:
        print("Attempt finished, logging complete")
    return data
```

- Combining `try`/`except` with `with` is genuinely the safest overall pattern — `with` guarantees the file is closed properly no matter what, while `try`/`except` still catches and responds to problems that happen either during opening or while reading/writing, without needing separate manual `.close()` handling in every branch.

```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found - using empty content")
    content = ""
```

**Conclusion**

This layered approach — specific exceptions for specific failures, `finally` for guaranteed cleanup, and `with` for guaranteed closing — is what turns file handling from something that can crash unpredictably into something that fails gracefully and predictably, which matters enormously the moment code runs on files it does not fully control.

---

### Q5. Compare and contrast the three core features of this unit: exception types, exception handling, and file I/O. Show how they work together.

**Introduction**

These three topics are presented together in the unit for a good reason — exception types describe *what* can go wrong, exception handling decides *what to do* about it, and file I/O is one of the most common places both of those actually get used in practice.

**Body**

- Exception types are the vocabulary — built-in ones like `ValueError` and `FileNotFoundError`, or custom ones like `InsufficientFundsError` — each naming one specific kind of problem.

```python
class InsufficientFundsError(Exception): pass
```

- Exception handling (`try`/`except`/`else`/`finally`) is the mechanism that responds to those problems once they're named — catching the right type, doing the right thing about it, and cleaning up regardless of the outcome.

```python
try:
    risky()
except SpecificError:
    handle_it()
finally:
    cleanup()
```

- File I/O is where this all becomes genuinely practical — reading and writing files is exactly the kind of operation that depends on things outside the program's control (a file existing, having permission, the disk having space), which is precisely why it needs both a vocabulary of specific exceptions and a reliable mechanism for handling them.

```python
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    content = ""
```

- Put together, these three form a complete, working pattern: name the specific things that can realistically go wrong (exception types), decide how to respond to each one (exception handling), and apply that discipline to the operations — like file access — that fail the most unpredictably in real programs.

**Conclusion**

Seen as a set, this unit is not really three separate topics, but one connected skill: recognising what can go wrong, naming it precisely, and handling it gracefully — with file I/O simply being the clearest, most common place that skill gets exercised.

---

### Q6. Explain how to design a robust file handling application using all the concepts from Unit 3. Include error handling, multiple file operations, and best practices.

**Introduction**

Designing a genuinely robust file-handling application means applying every idea from this unit together, rather than any single one in isolation.

**Body**

- Start with `with` for every file operation, guaranteeing the file always closes properly, and always specify `encoding="utf-8"` so behaviour stays consistent across different machines.

```python
def load_students(filename):
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split(",")
                students.append((name, int(score)))
    except FileNotFoundError:
        print(f"{filename} not found, starting with an empty list")
    except ValueError:
        print("Some lines were badly formatted and were skipped")
    return students
```

- Handle multiple operations by wrapping each risky step in its own attempt, with specific exceptions for realistic failures, rather than one giant `try` block covering unrelated operations.

```python
def save_students(filename, students):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for name, score in students:
                f.write(f"{name},{score}\n")
        print("Saved successfully")
    except PermissionError:
        print("No permission to write to this file")
```

- Raise custom exceptions for problems specific to the application's own rules, not just built-in ones, and use `finally` for anything that absolutely must run regardless of outcome, such as logging that an attempt was made.

```python
class InvalidRecordError(Exception): pass

def validate_score(score):
    if not (0 <= score <= 100):
        raise InvalidRecordError(f"Score {score} out of range")
```

- Best practices worth following throughout: never use a bare `except:`; never silently ignore an exception without at least printing or logging it; prefer append mode over write mode unless erasing old data is genuinely intended; and test the application against a missing file, an empty file, and a badly formatted file, since these are exactly the situations real users will eventually create.

**Conclusion**

A robust file-handling application isn't one clever trick — it's the consistent, disciplined combination of `with`, specific exceptions, custom errors where they add clarity, and deliberate testing against the ways real files actually go wrong.

---

### Q7. Analyze the relationship between exception handling and the design of custom exceptions. Show how this connects to Unit 2 concepts of inheritance and OOP.

**Introduction**

Custom exceptions are really where Unit 3's exception handling and Unit 2's OOP ideas directly meet — a custom exception is, after all, simply a class, built using the exact same tools (inheritance, `__init__`, `super()`) already learned for classes like `BankAccount`.

**Body**

```python
class BankError(Exception):          # Exception itself is just a built-in class
    pass
class InsufficientFundsError(BankError):   # ordinary inheritance, same as SavingsAccount
    def __init__(self, balance, amount):
        super().__init__(f"{balance} < {amount}")   # same super() pattern as Unit 2
        self.balance = balance
        self.amount = amount
```

- This is exactly the same inheritance pattern used for `SavingsAccount(BankAccount)` in Unit 2 — a specific exception inherits from a more general one, reuses its constructor via `super()`, and adds its own extra attributes on top, just as `SavingsAccount` added its own `rate` attribute.
- It also relies on the same `isinstance()`-style thinking: catching `except BankError:` will catch an `InsufficientFundsError` too, for the same reason `isinstance(savings_acc, BankAccount)` returns `True` — a subclass is still considered a member of its parent class.

```python
try:
    raise InsufficientFundsError(100, 500)
except BankError as e:      # catches it, because InsufficientFundsError IS-A BankError
    print(e.balance, e.amount)
```

- So exception handling and custom exception design aren't really a separate skill from OOP — they're a direct, practical application of it: the exception hierarchy is a class hierarchy, `raise` is just creating an object of that class, and `except` is just a type check very similar to `isinstance()`.

**Conclusion**

Recognising that a custom exception is nothing more than a regular class built with familiar OOP tools makes this whole topic far less intimidating — everything learned about inheritance, `super()`, and `isinstance()` in Unit 2 carries over directly, just applied to describing errors instead of bank accounts.

---

### Q8. Create a detailed summary of Unit 3 that explains how exception handling and file I/O work together as professional practices. Include golden rules, connections to previous units, and real-world applications.

**Introduction**

Unit 3 brings together two ideas that, on the surface, look separate — handling errors, and reading/writing files — but in professional code, they are almost never used apart from each other.

**Body**

- Errors in Python fall into three categories: syntax errors (caught by Python before running), runtime exceptions (caught with `try`/`except` while running), and logical errors (caught only by testing, since nothing crashes). File operations are one of the most common sources of runtime exceptions specifically, since they depend on things outside the program's control — a file existing, having the right permissions, being in the expected format.

```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    content = ""
finally:
    print("Read attempt complete")
```

- Custom exceptions extend Unit 2's OOP ideas directly into this space — an exception is just a class, built with the same inheritance and `super()` patterns already used for something like `BankAccount`, letting errors be described precisely in the application's own terms rather than through generic built-in types.
- The golden rules worth carrying forward into real projects: always catch specific exceptions, never a bare `except:`; always use `with` for files, so closing is never left to chance; always specify `encoding="utf-8"` for consistent behaviour across machines; use `finally` for guaranteed cleanup; and never silently swallow an error without at least logging it.

```
[Errors happen] -> [Specific exception types name them] -> [try/except/finally handles them] -> [with + encoding keeps file operations safe] -> [Custom exceptions (built via OOP) add application-specific meaning]
```

- In real-world terms, this exact combination is what every professional application does constantly — reading a configuration file, saving user data, loading a dataset — all of it wrapped in careful exception handling, because a program that simply crashes the moment a file is missing or malformed is not considered production-ready.

**Conclusion**

Unit 3's real lesson is less about any single method or keyword, and more about a professional habit: assume things will go wrong — files will be missing, input will be malformed — and write code from the start that handles that gracefully, rather than trusting that everything will always go right.

---
