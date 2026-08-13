# Unit 8 — Regex, Threads, and Django

## Short Questions (2 Marks)

### Q1. Define a regular expression.

- A regular expression (regex) is a pattern written in a small special-purpose language that describes the *shape* of the text being searched for — much like a form template where a box shape tells you what kind of value goes there.

```python
import re
re.findall(r"\d+", "Room 12, Floor 3")   # ['12', '3']
```

---

### Q2. State the purpose of using raw strings in Python regular expressions.

- A raw string (`r"..."`) tells Python not to process backslashes before the regex engine ever sees the pattern — without it, something like `\s` would be interpreted as a tab character rather than the whitespace class.

```python
print(len("\s"))    # 1  - backslash + s collapses to a tab-like escape
print(len(r"\s"))   # 2  - stays as backslash then s, correct for regex
```

---

### Q3. List the meanings of the regex symbols `\d`, `\w`, and `\s`.

- `\d` matches any digit, equivalent to `[0-9]`.
- `\w` matches any word character — letters, digits, or underscore — equivalent to `[a-zA-Z0-9_]`.
- `\s` matches any whitespace character — space, tab, or newline.

---

### Q4. Explain the role of quantifiers in regular expressions.

- Quantifiers control how many times the thing right before them is allowed to repeat — without one, a pattern only matches exactly one occurrence.

```python
import re
re.findall(r"go*gle", "ggle google gogle")   # ['ggle', 'google', 'gogle']
re.findall(r"\d{4}", "2024")                 # ['2024'] - exactly 4 digits
```

---

### Q5. Differentiate between `re.match()` and `re.search()`.

- `re.match()` only checks for the pattern right at the start of the string, while `re.search()` scans the entire string for the pattern occurring anywhere.

```python
import re
text = "Your ID is BT2024"
print(re.match(r"[A-Z]{2}\d{4}", text))    # None - not at position 0
print(re.search(r"[A-Z]{2}\d{4}", text))   # matches 'BT2024'
```

---

### Q6. State what `re.sub()` returns.

- `re.sub()` returns a brand-new string with every match replaced — it never modifies the original string, so the result must always be assigned to a variable to be kept.

```python
import re
text = "cat sat"
new_text = re.sub(r"cat", "dog", text)   # "dog sat"
print(text)   # still "cat sat" - unchanged
```

---

### Q7. Define a Django model.

- A Django model is a Python class that automatically becomes a database table — each attribute on the class becomes a column, and Django's ORM handles the underlying SQL.

```python
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
```

---

### Q8. State the role of the ORM in Django.

- The ORM (Object-Relational Mapper) lets the database be queried using plain Python method calls instead of writing SQL directly — Django generates the SQL behind the scenes.

```python
Student.objects.filter(name="Avhi")   # generates a SELECT ... WHERE name = 'Avhi'
```

---

### Q9. List the four main components of Django's MVT architecture.

- Model (`models.py`) — defines the data structure and talks to the database.
- View (`views.py`) — handles the HTTP request and applies the logic.
- Template (`templates/*.html`) — renders the final HTML page.
- URL configuration (`urls.py`) — maps a URL path to the right view function.

---

### Q10. Explain the purpose of URL routing in Django.

- URL routing is what decides which view function should handle a given incoming request path — it is the very first step of the request cycle, before any logic or database access happens.

```python
# urls.py
urlpatterns = [path("search/", views.book_search, name="search")]
```

---

### Q11. Define a thread.

- A thread is a separate line of execution within the same process, sharing that process's memory with every other thread in it — which is what makes threads lightweight compared to starting a whole new process.

---

### Q12. State one reason why threads are useful for I/O-bound tasks.

- While one thread is waiting on something external — a network response, a disk read — another thread can keep running instead of the program sitting idle, so the total time ends up closer to the longest single wait rather than the sum of all of them.

---

### Q13. Explain what a race condition is.

- A race condition happens when two or more threads read and write the same shared data at the same time, and the final result ends up depending on the unpredictable order in which their operations happened to interleave — often producing an incorrect result.

---

### Q14. State the function of a Lock in thread programming.

- A `Lock` ensures that only one thread at a time can execute a particular section of code — the "critical section" — forcing every other thread to wait until it is released.

```python
lock = threading.Lock()
with lock:
    balance += amount   # only one thread here at a time
```

---

### Q15. Describe the three-step pattern for using threads.

```
The standard pattern is Create → Start → Join: first create the `Thread` object, then call `.start()` to begin running it in the background, and finally call `.join()` so the main program waits for it to finish.
[Create Thread] -> [.start()] -> [.join()]
```

---

### Q16. State the purpose of `thread.join()`.

- `join()` makes the calling thread (usually the main thread) pause and wait until the target thread has completely finished running, before continuing on.

---

### Q17. Define a template variable in Django.

- A template variable is a placeholder inside an HTML template, written as `{{ variable }}`, that gets replaced with an actual value passed in from the view when the page is rendered.

---

### Q18. List two template syntax forms described in the notes.

- `{{ variable }}` — outputs a value directly into the HTML.
- `{% if condition %} ... {% endif %}` (or `{% for item in list %} ... {% endfor %}`) — a logic tag for conditionals and loops.

---

### Q19. State the role of a view in Django.

- A view is a Python function (or class) that receives the HTTP request, runs whatever logic or database queries are needed, and returns a rendered template as the response.

---

### Q20. Explain the purpose of a template in Django.

- A template is the HTML file responsible for actually presenting the data the view prepared — it keeps the visual layout separate from the application's logic, so each can be changed independently.

---

## Medium Questions (6 Marks)

### Q1. Explain how character classes and boundaries are used in regular expressions.

- A character class, written in square brackets like `[aeiou]`, matches any single character from that set — and putting `^` right after the opening bracket flips it to mean "none of these."

```python
import re
re.findall(r"[aeiouAEIOU]", "Bartholomew")   # ['a', 'o', 'o', 'e', 'o']
re.findall(r"[^aeiou ]", "cat dog")          # consonants only
```

- Predefined shorthand classes cover the most common cases without spelling out a full set: `\d` for digits, `\w` for word characters, and `\s` for whitespace, each with an uppercase inverse (`\D`, `\W`, `\S`).
- A boundary, `\b`, is different from a character class in that it matches a *position* rather than a character — specifically, the zero-width point between a word character and a non-word character.

```python
text = "the cat scattered"
print(re.findall(r"cat", text))     # ['cat', 'cat'] - matches inside 'scattered' too
print(re.findall(r"\bcat\b", text)) # ['cat'] - only the whole word
```

- Together, character classes narrow down *what* can appear at a position, while boundaries control *where* a match is allowed to start or end — combining both is what makes patterns like whole-word or whole-token matching reliable.

---

### Q2. Describe how `re.findall()` can be used to extract phone numbers and student records from text.

- `re.findall()` scans the whole string and returns every match it finds, which makes it the natural tool whenever there could be more than one occurrence of a pattern in the text.
- For phone numbers, a UK mobile always starts with `07` followed by nine more digits, sometimes with a space after the first few — so the notes use `\b07\d{3}\s?\d{6}\b` to capture that shape directly.

```python
import re
text = "Call Alice on 07700 900123 or Bob on 07911654321."
phones = re.findall(r"\b07\d{3}\s?\d{6}\b", text)
print(phones)   # ['07700 900123', '07911654321']
```

- For student records in the form `NAME: SCORE / GRADE`, named groups make the pattern self-documenting, and `re.finditer()` (or `findall()`) can then pull out each named piece.

```python
pattern = r"(?P<name>[\w ]+):\s*(?P<score>\d+)\s*/\s*(?P<grade>[A-F])"
for m in re.finditer(pattern, "Alice Smith: 78 / B\nBob Jones: 91 / A"):
    print(m.group("name"), m.group("score"), m.group("grade"))
# Alice Smith 78 B
# Bob Jones 91 A
```

- In both cases, the pattern is built by describing the exact shape of the data — digits, separators, letter ranges — and `findall()`/`finditer()` does the work of locating every occurrence of that shape in the text.

---

### Q3. Compare `re.match()`, `re.search()`, and `re.findall()` with reference to their outputs.

- All three functions look for the same kind of pattern, but they differ in *where* they look and *what* they hand back.
- `re.match()` only checks the very start of the string, and returns a single Match object (or `None`) — it answers "does this string begin with the pattern?"
- `re.search()` scans the whole string but still stops and returns just the first Match object it finds (or `None`) — it answers "does this pattern appear anywhere?"
- `re.findall()` also scans the whole string, but instead of stopping at the first hit, it keeps going and returns a list of every match — plain strings if there are no groups, or tuples if there is more than one group.

```python
import re
text = "BT2024 and CS1999 are valid IDs"
pattern = r"[A-Z]{2}\d{4}"
print(re.match(pattern, text))      # None - 'BT2024' isn't at position 0... actually it is here
print(re.search(pattern, text))     # <Match object; span=(0, 6), match='BT2024'>
print(re.findall(pattern, text))    # ['BT2024', 'CS1999']
```

- So the choice between them really comes down to intent: `match()` for whole-string validation, `search()` for a single "is it in here somewhere," and `findall()` whenever every occurrence matters.

---

### Q4. Discuss the importance of non-greedy matching in regular expressions.

- By default, quantifiers in regex are greedy — they try to match as much text as possible, which can badly overshoot when there are multiple similar pieces of text on the same line.
- Adding a `?` right after a quantifier switches it to non-greedy, so it instead matches as little text as possible while still satisfying the pattern.

```python
import re
html = "<b>Name</b> and <b>Score</b>"
greedy = re.findall(r"<b>.*</b>", html)
lazy   = re.findall(r"<b>.*?</b>", html)
print(greedy)   # ['<b>Name</b> and <b>Score</b>']  - way too much!
print(lazy)     # ['<b>Name</b>', '<b>Score</b>']    - correct
```

- Without non-greedy matching here, `.*` would stretch from the very first `<b>` all the way to the very last `</b>`, swallowing everything in between — which is almost never what is actually wanted when extracting repeated, similarly-tagged pieces of text.
- This is exactly the kind of subtle bug that shows up constantly in real text-processing code, which is why recognising when to add that extra `?` is a genuinely practical skill, not just a syntax detail.

---

### Q5. Explain the request flow in Django from a browser request to a rendered webpage.

- A Django request moves through a fixed, predictable sequence of stages, each handled by one of the MVT components.
- It starts when the browser sends a request, e.g. `GET /search/?q=Python`.
- `urls.py` matches that path against its `urlpatterns` list and routes it to the corresponding view function.
- The view then runs whatever logic is needed — here, querying the model: `Book.objects.filter(title__icontains='Python')`.
- The view passes its results into a template using `render(request, 'search.html', {'results': results})`.
- The template fills in its `{{ }}` and `{% %}` placeholders with that data, producing final HTML, which is sent back and displayed in the browser.

```
[Browser Request] -> [URL Routing (urls.py)] -> [View (views.py)] -> [Model/DB query] -> [Template renders HTML] -> [Browser displays page]
```

---

### Q6. Describe how a Django model maps to a database table and how ORM queries work.

- Every Django model is a plain Python class that inherits from `models.Model`, and each attribute defined on it becomes one column of the corresponding database table.

```python
from django.db import models
class Book(models.Model):
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    copies = models.IntegerField(default=1)
```

- This one class definition is what Django uses to generate the matching `CREATE TABLE` statement — the class name becomes the table, and each field becomes a column with the matching SQL type.
- Once the table exists, the ORM lets every typical operation be written in pure Python instead of SQL.

```python
Book.objects.create(title="Fluent Python", author="Ramalho")   # INSERT
Book.objects.all()                                              # SELECT *
Book.objects.filter(author="Ramalho")                          # SELECT ... WHERE
book.copies = 5; book.save()                                    # UPDATE
book.delete()                                                   # DELETE
```

- A `ForeignKey` field, like `student = models.ForeignKey(Student, on_delete=models.CASCADE)`, maps directly onto the relational concept of a foreign key from earlier database work — just expressed as a Python class attribute instead of a raw SQL constraint.

---

### Q7. Compare the roles of Model, View, Template, and URL configuration in Django's MVT architecture.

- Each of these four pieces owns exactly one responsibility, which is really the whole point of the MVT pattern — keeping data, logic, and presentation cleanly separated.
- The Model (`models.py`) owns the data — it defines the structure and talks to the database, with no knowledge of HTTP or HTML at all.
- The View (`views.py`) owns the logic — it receives the request, decides what data is needed, asks the Model for it, and hands the result to a Template.
- The Template (`templates/*.html`) owns the presentation — it only knows how to turn data it is given into HTML, with no direct database access of its own.
- The URL configuration (`urls.py`) owns the routing — it is the very first stop for any request, deciding which View should even handle it.

```
[URL Routing] -> [View (Logic)] -> [Model (Database)] -> back to [View] -> [Template (HTML)] -> [Response]
```

- This separation means each piece can change independently — the HTML can be redesigned without touching the database logic, or the database schema can change without rewriting every template.

---

### Q8. Discuss the difference between a process and a thread as described in the notes.

- The clearest way to see the difference is the bank-branch analogy from the notes: one cashier serving customers one at a time is like a process with a single thread, while five cashiers serving customers at once is like a process running many threads concurrently.
- A process has its own private memory, completely separate from other processes, so communication between processes is comparatively slow — files, pipes, or sockets are needed.
- A thread, by contrast, shares memory with every other thread in the same process, so communicating between threads is fast — they can simply read and write the same variables directly.
- Threads are also cheaper to start than processes, which matters when many concurrent tasks are needed quickly.
- This difference in memory sharing is also exactly what makes threads better suited to I/O-heavy tasks (waiting on a network or disk) while CPU-heavy tasks are better handled by separate processes using `multiprocessing`.

---

### Q9. Explain why shared data must be protected when multiple threads run concurrently.

- Since threads in the same process share memory, more than one of them can end up reading and writing the very same variable at the same time — and if that happens without any coordination, the result becomes a race condition.

```python
balance = 0
def deposit(amount, count):
    global balance
    for _ in range(count):
        current = balance          # READ  <- gap where another thread can interleave
        balance = current + amount # WRITE
```

- The danger sits in the gap between reading a value and writing it back — if another thread reads the same old value before the first thread has finished writing its update, one of the two updates simply gets lost.
- This is exactly why it is unpredictable rather than always broken: results can differ from run to run, and the bug can even seem to disappear when debugging output like `print()` is added, since that changes the timing.
- Protecting shared data — typically with a `Lock` — closes that gap by only ever letting one thread execute the read-modify-write sequence at a time, guaranteeing the final result is correct regardless of how the threads happen to interleave.

---

### Q10. Describe the use of a Lock, Semaphore, and Event in thread-based programs.

- These three tools all coordinate threads, but each solves a different kind of coordination problem.
- A `Lock` allows only one thread into a critical section at a time — used with `with lock:` so it is always released, even if an exception occurs inside the block.

```python
lock = threading.Lock()
with lock:
    balance += amount
```

- A `Semaphore(n)` is a generalised lock that allows up to `n` threads in at once, like a venue bouncer letting in a fixed maximum number of people.

```python
lab = threading.Semaphore(2)   # only 2 students in the lab at once
with lab:
    do_lab_work()
```

- An `Event` is different again — it is a one-to-many signal rather than a limit on access, like a starting gun that tells every waiting thread to go at once.

```python
game_over = threading.Event()
# worker thread: while not game_over.is_set(): ...
game_over.set()   # signals all waiting/checking threads
```

- So the choice depends on the problem: `Lock` for exclusive access, `Semaphore` for limited concurrent access, and `Event` for broadcasting a state change to multiple threads at once.

---

### Q11. Illustrate how a threaded search can be implemented using threads and a shared results list.

- The pattern is to give each search its own thread, and have every thread append its own result to one shared list, protected by a single shared `Lock`.

```python
import threading, time

def search_database(db_name, query, results, lock):
    time.sleep(0.5)   # simulate the search taking time
    result = f"{db_name}: found '{query}'"
    with lock:                # protect the shared list
        results.append(result)

databases = ["Local DB", "National DB", "Archive DB", "Digital DB"]
results = []
lock = threading.Lock()
threads = [threading.Thread(target=search_database, args=(db, "Python", results, lock))
           for db in databases]

for t in threads: t.start()   # start ALL first
for t in threads: t.join()    # then join ALL
print(results)
```

- Starting every thread before joining any of them is what makes the searches genuinely concurrent — if `start()` and `join()` were called together inside the same loop, each search would finish before the next one even began, defeating the purpose of using threads at all.
- The `Lock` around `results.append()` exists because even a "simple" list append is not guaranteed to be safe if two threads reach it at exactly the same moment — wrapping it protects the shared list the same way it would protect a shared counter.

---

### Q12. Evaluate the relevance of Django to the earlier units in this course.

- Django is really presented in the notes as the point where everything from earlier units comes together into one real, working framework, rather than a completely new topic on its own.
- Models are Python classes, directly building on the OOP concepts from earlier in the course — a Model IS-A Python class, just one that Django also knows how to turn into a database table.
- The ORM builds on the relational database and SQLite work — the same tables, primary keys, and foreign keys are still there, just expressed as Python attributes and method calls instead of raw SQL.
- Views and URL routing build on the networking and HTTP concepts from the sockets unit — a Django view is, underneath, still just something that receives a request and sends back a response, the same request-response idea as a socket server.
- Django also handles concurrency automatically behind the scenes, which connects back to this unit's own threading material, even though a Django developer rarely manages threads directly.

```
[Unit 2: OOP] -> [Models] | [Unit 6: SQLite] -> [ORM] | [Unit 7: Networking] -> [Views + URLs] | [Unit 8: Threads] -> [Django concurrency]
```

---

## Long Questions (12 Marks)

### Q1. Discuss the main regex concepts from the notes, including raw strings, character classes, predefined classes, quantifiers, boundaries, and regex functions such as match, search, findall, and sub.

**Introduction**

Regular expressions give Python a compact, pattern-based way to search, validate, and transform text, and the notes build this up through a consistent set of core building blocks.

**Body**

- Every pattern should be written as a raw string, `r"..."`, so that Python passes backslashes through untouched to the regex engine — without it, something like `\s` would be silently turned into a tab character before the pattern is even compiled.

```python
import re
print(len("\s"))    # 1 - wrong, becomes an escape sequence
print(len(r"\s"))   # 2 - correct, stays as backslash + s
```

- Character classes, `[...]`, match any single character from a defined set, and placing `^` right after the opening bracket flips the meaning to "none of these."

```python
re.findall(r"[aeiou]", "hello world")    # ['e', 'o', 'o']
re.findall(r"[^aeiou ]", "hi there")     # consonants only
```

- Predefined classes shortcut the most common sets: `\d` for digits, `\w` for word characters, `\s` for whitespace, each with an uppercase inverse — and `\b` marks a word boundary, a zero-width position rather than an actual character.

```python
re.findall(r"\bcat\b", "the cat scattered")   # ['cat'] only, not the 'cat' inside 'scattered'
```

- Quantifiers control repetition: `*` for zero or more, `+` for one or more, `?` for optional, `{n}` for exactly n, and `{n,m}` for a range — and appending `?` after any of these switches it from greedy (matches as much as possible) to non-greedy (matches as little as possible).

```python
html = "<b>Name</b> and <b>Score</b>"
print(re.findall(r"<b>.*</b>", html))    # greedy - one huge match
print(re.findall(r"<b>.*?</b>", html))   # non-greedy - two correct matches
```

- On top of these building blocks sit the core functions: `re.match()` checks only the start of the string; `re.search()` scans the whole string but stops at the first hit; `re.findall()` returns every match as a list (or list of tuples, if there are multiple groups); and `re.sub()` returns a brand-new string with every match replaced, never modifying the original.

```python
text = "15/03/2024"
iso = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)
print(iso)   # 2024-03-15
```

**Conclusion**

These building blocks — raw strings, character classes, quantifiers, boundaries, and the core functions — combine to make regex genuinely practical for real tasks like validation and extraction, which is exactly why they are tested so thoroughly and appear constantly in the practice exercises.

---

### Q2. Explain the debugging exercises in the notes and show how each bug is corrected.

**Introduction**

The notes include four deliberately broken examples, each illustrating a mistake that is easy to make with regex or threads even when the surrounding logic looks correct.

**Body**

- Debug 1 — the `sub()` result is discarded: `re.sub()` was called but its return value was never assigned, so the original string never actually changed.

```python
records = "Meeting on 15/03/2024"
re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", records)   # BUG: result thrown away
# FIX: assign the result back
records = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", records)
```

- Debug 2 — a greedy pattern captures too much: `<b>.*</b>` stretched from the first `<b>` all the way to the very last `</b>` in the string, swallowing everything in between instead of matching each tag pair separately.

```python
html = "<b>Name</b> and <b>Score</b>"
re.findall(r"<b>.*</b>", html)     # BUG: one huge match
# FIX: make it non-greedy
re.findall(r"<b>.*?</b>", html)    # ['<b>Name</b>', '<b>Score</b>']
```

- Debug 3 — a missing `join()`: threads were started but the main program printed the results immediately afterward, before the threads had actually finished writing to the shared list.

```python
for i in range(5):
    t = threading.Thread(target=fetch_data, args=(i,))
    threads.append(t); t.start()
print(results)   # BUG: often empty or incomplete
# FIX: join every thread before reading the shared result
for t in threads: t.join()
print(results)
```

- Debug 4 — a race condition from an unprotected shared counter: `counter += 1` looks atomic but is actually a read-modify-write sequence, so concurrent threads can lose updates.

```python
counter = 0
def increment(times):
    global counter
    for _ in range(times):
        counter += 1   # BUG: not thread-safe
# FIX: protect it with a Lock
lock = threading.Lock()
def increment(times):
    global counter
    for _ in range(times):
        with lock:
            counter += 1
```

**Conclusion**

Each of these four bugs looks like a small, easy-to-miss detail — a forgotten assignment, a missing `?`, a missing `join()`, a missing `Lock` — but each one produces a program that runs without crashing while still silently giving the wrong answer, which is exactly why they are worth studying individually rather than dismissing as minor syntax slips.

---

### Q3. Discuss threads in detail, including process versus thread, shared memory, the GIL, I/O-bound work, race conditions, locks, joins, semaphores, events, and silent thread exceptions.

**Introduction**

Threads let a single program do more than one thing at once, but understanding them well means understanding several connected ideas together, not just the `Thread` class in isolation.

**Body**

- A process has its own private memory, completely separate from other processes, whereas a thread shares memory with every other thread inside the same process — which is what makes threads lightweight and fast to communicate between, but also what introduces the risk of two threads touching the same data at once.
- Python's Global Interpreter Lock (GIL) only allows one thread to execute Python bytecode at a time, which means threads do not actually speed up CPU-heavy work — but for I/O-bound work (waiting on a network response, a disk read, a database query), threads still help, because while one thread is waiting, another can run.

```python
# I/O-bound: threads help because most time is spent waiting, not computing
t = threading.Thread(target=download_file, args=("file.zip",))
t.start(); t.join()
The basic three-step pattern for using a thread is Create → Start → Join, and for multiple threads, every thread must be started first and only then joined — starting and joining inside the same loop accidentally makes the threads run sequentially instead of concurrently.
for t in threads: t.start()   # start ALL first
for t in threads: t.join()    # then join ALL
```

- A race condition happens when shared data is read and written by more than one thread without coordination — the classic example is a shared balance where two threads both read the old value before either writes back its update, so one deposit is silently lost.
- A `Lock`, used as `with lock:`, fixes this by only letting one thread execute the critical section at a time, and releasing the lock automatically even if an exception occurs inside the block.
- A `Semaphore(n)` generalises this idea to allow up to `n` threads in at once, like a room with a fixed number of seats, while an `Event` is used differently again — as a one-to-many signal, where `event.set()` wakes every thread that is checking `is_set()` or blocked on `event.wait()`.
- One more subtlety worth remembering: exceptions raised inside a thread do not crash the main program and do not print automatically — they terminate that thread silently, so thread functions should generally be wrapped in their own `try/except` to avoid a failure going unnoticed.

```python
def safe_task():
    try:
        risky_work()
    except Exception as e:
        print("Thread failed:", e)
```

**Conclusion**

Threads are a genuinely powerful tool for I/O-bound programs, but every one of these pieces — shared memory, the GIL, locks, joins, and silent exceptions — exists because concurrency introduces real risks that sequential code never has to deal with, which is why this topic is tested as a connected whole rather than isolated facts.

---

### Q4. Explain the Django MVT architecture with reference to models, views, templates, and URL configuration, and describe a complete request cycle.

**Introduction**

Django organises a web application around the Model–View–Template (MVT) pattern, which is really just a disciplined way of keeping data, logic, and presentation separate from one another.

**Body**

- The Model, defined in `models.py`, is a Python class that maps directly onto a database table, with each attribute becoming a column.

```python
from django.db import models
class Book(models.Model):
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
```

- The View, in `views.py`, receives the incoming HTTP request, decides what needs to happen — often querying the Model — and hands the result off to a Template.

```python
def book_search(request):
    query = request.GET.get("q", "")
    results = Book.objects.filter(title__icontains=query)
    return render(request, "search.html", {"results": results})
```

- The Template, an HTML file under `templates/`, uses `{{ variable }}` and `{% tag %}` syntax to turn the data it was given into the actual page the browser shows.

```html
{% for book in results %}
  <li>{{ book.title }} - {{ book.author }}</li>
{% endfor %}
```

- The URL configuration, in `urls.py`, is what ties a specific URL path to the correct view function in the first place.

```python
urlpatterns = [path("search/", views.book_search, name="search")]
```

- Putting all four together, a complete request cycle runs as follows: the browser sends a request such as `GET /search/?q=Python`; `urls.py` matches that path and routes it to `book_search`; the view queries the Model with `Book.objects.filter(title__icontains='Python')`; the view passes the results into the Template via `render()`; the Template fills in its placeholders and produces HTML; and that HTML is sent back to the browser, which displays the finished page.

```
[Browser Request] -> [urls.py: URL Routing] -> [views.py: View/Logic] -> [models.py: Database] -> [Template: HTML] -> [Response to Browser]
```

**Conclusion**

The MVT pattern's real value is this separation of concerns — the database structure, the request-handling logic, and the visual presentation can each be changed independently, which is exactly the kind of maintainable design a full request-cycle question is testing understanding of.

---

### Q5. Compare Django's model, ORM, view, template, and URL routing with the concepts introduced in earlier units as described in the notes.

**Introduction**

The notes present Django less as a brand-new topic and more as the place where the ideas from every earlier unit finally combine into one working system — which is worth explaining piece by piece.

**Body**

- A Model is, first and foremost, a Python class — the same class-based thinking from the OOP unit, just with the added twist that Django automatically maps its attributes onto a database table.

```python
class Student(models.Model):   # IS-A models.Model, HAS-A name attribute
    name = models.CharField(max_length=100)
```

- The ORM builds directly on the relational database and SQLite material — tables, primary keys, and foreign keys are all still there conceptually, just expressed as Python method calls instead of raw SQL statements.

```python
# ORM (Django)                         vs   # Raw SQL (Unit 6)
Book.objects.filter(author="Ramalho")  #   SELECT * FROM book WHERE author = 'Ramalho'
```

- Views and URL routing build on the networking and HTTP concepts from the sockets unit — a Django view still fundamentally receives a request and returns a response, the same request-response shape as a socket server, just with Django handling the low-level socket work automatically.
- Templates connect back to the idea of separating structure from content, echoing how a line-based protocol separated the message format from the actual data being sent.
- Threading, this unit's own earlier topic, is also present — Django handles concurrent requests automatically behind the scenes, so a Django developer benefits from the same concurrency concepts without needing to manage `Thread` objects directly.

```
[Unit 2 OOP: classes] -> [Django Models] | [Unit 6 SQLite: tables/FKs] -> [Django ORM] | [Unit 7 Sockets: request/response] -> [Django Views + URLs] | [Unit 8 Threads] -> [Django's automatic concurrency]
```

**Conclusion**

Seen this way, Django is not really extra material bolted onto the end of the course — it is presented as the destination the whole course was building toward, where OOP, databases, and networking concepts each reappear in a more polished, framework-provided form.

---

### Q6. Illustrate how regex can be used to solve the practice tasks on phone number extraction, student record parsing, password checking, and log analysis using patterns from the notes.

**Introduction**

Each of these four practice tasks is really the same skill — describing the shape of the target text as a pattern — applied to a different real-world format.

**Body**

- Phone number extraction: UK mobiles start with `07` followed by nine more digits, sometimes with a space after the first few, captured with `\b07\d{3}\s?\d{6}\b`.

```python
import re
text = "Call Alice on 07700 900123 or Bob on 07911654321."
print(re.findall(r"\b07\d{3}\s?\d{6}\b", text))
# ['07700 900123', '07911654321']
```

- Student record parsing: each line follows `NAME: SCORE / GRADE`, which named groups turn into self-documenting, directly usable pieces.

```python
pattern = r"(?P<name>[\w ]+):\s*(?P<score>\d+)\s*/\s*(?P<grade>[A-F])"
for m in re.finditer(pattern, "Alice Smith: 78 / B\nBob Jones: 91 / A"):
    print({"name": m.group("name"), "score": m.group("score"), "grade": m.group("grade")})
```

- Password strength checking: rather than one pattern, each requirement becomes its own `re.search()` check, and a failing check adds a message to a results list.

```python
def check_password(password):
    failures = []
    if len(password) < 8:
        failures.append("Too short")
    if not re.search(r"[A-Z]", password):
        failures.append("Missing uppercase letter")
    if not re.search(r"\d", password):
        failures.append("Missing digit")
    if not re.search(r"[!@#$%^&*]", password):
        failures.append("Missing special character")
    return failures

print(check_password("Str0ng!Pass"))   # []  - strong
print(check_password("password123"))   # ['Missing uppercase letter', 'Missing special character']
```

- Log file analysis: different pieces of the same log line are pulled out with different patterns — `findall()` for every ERROR line and every timestamp, and `search()` scoped to just the WARNING lines to find their IP addresses.

```python
error_lines = re.findall(r"^.*ERROR.*$", log, re.MULTILINE)
timestamps  = re.findall(r"\d{2}:\d{2}:\d{2}", log)
warning_lines = re.findall(r"^.*WARNING.*$", log, re.MULTILINE)
warning_ips = [re.search(r"\d+\.\d+\.\d+\.\d+", line).group() for line in warning_lines]
level_counts = Counter(re.findall(r"INFO|WARNING|ERROR", log))
```

**Conclusion**

What ties all four tasks together is the same underlying approach — identify the fixed and variable parts of the text's shape, express the fixed parts literally and the variable parts as character classes/quantifiers/groups, then let `findall()`, `search()`, or `finditer()` do the scanning.

---

### Q7. Describe how a multi-threaded word frequency counter or library search can be implemented using threads and a Lock, and explain why the Lock is necessary.

**Introduction**

Both of these tasks share the same shape: split the work across several threads, let each thread do its piece independently, and then have every thread safely merge its own result into one shared structure.

**Body**

- For a word frequency counter, each "chapter" of text is handled by its own thread, which counts its own words locally first — this local counting needs no protection at all, since nothing is shared yet at that point.

```python
import threading, re
from collections import Counter

def count_words_in_chapter(chapter_text, shared_counts, lock):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", chapter_text.lower())
    local_counts = Counter(words)
    with lock:                         # only the merge step needs protecting
        shared_counts.update(local_counts)

chapters = ["Alice studied Python...", "Bob practiced threading..."]
shared_word_counts = Counter()
lock = threading.Lock()
threads = [threading.Thread(target=count_words_in_chapter, args=(c, shared_word_counts, lock))
           for c in chapters]
for t in threads: t.start()
for t in threads: t.join()
print(shared_word_counts.most_common(10))
```

- A threaded library search follows the identical shape — each thread searches its own database and only touches the shared `results` list at the very end, inside the lock, to append its finding.

```python
def search_database(db_name, query, results, lock):
    result = do_search(db_name, query)   # independent work, no lock needed
    with lock:
        results.append(result)           # shared write, lock needed
```

- The `Lock` is necessary specifically at the merge/append step, because that is the one moment where more than one thread touches the *same* shared object — without it, two threads updating `shared_counts` (or appending to `results`) at the exact same instant could interleave and silently lose one of the updates, exactly like the earlier race-condition example with a shared bank balance.

**Conclusion**

The pattern worth remembering here is to keep as much work as possible thread-local (no locking needed) and shrink the locked section down to just the final merge — this keeps the threads genuinely concurrent for the expensive part of the work, while still guaranteeing a correct final result.

---

### Q8. Evaluate the significance of the unit summary and checklist themes: regex, threads, and Django, and explain how the topics connect to one another in the course.

**Introduction**

At first glance, regex, threads, and Django look like three unrelated topics bundled into one unit, but the notes' own summary table frames them instead as three layers of the same underlying skill: handling real, messy, concurrent, networked data.

**Body**

- Regex is the tool for making sense of unstructured text — extracting phone numbers, parsing log lines, validating passwords — which is exactly the kind of raw input a real web application constantly has to deal with, whether it comes from a form field or an uploaded file.
- Threads are the tool for handling more than one thing happening at once — and a real web server, like the one Django runs on, is inherently handling many simultaneous requests from different users, which is precisely a concurrency problem.
- Django then draws directly on both: it uses regex-like URL patterns internally for routing, and it depends on concurrency (handled automatically, but still built on the same threading ideas from this unit) to serve many users at the same time without one request blocking another.
- Beyond that, Django is also where the earlier units resurface — Models as OOP classes, the ORM as a friendlier face on SQLite's relational concepts, and Views/URLs as a structured version of the request-response pattern first seen with raw sockets.

```
[Regex: parse messy text] + [Threads: handle concurrency] -> [Django: a real web framework using both, on top of OOP + databases + networking]
```

**Conclusion**

Read this way, the unit's checklist themes are not three separate topics to memorise in isolation, but three converging skills that together explain what it actually takes to build and run a real, functioning web application — which is a fitting close to a course that started with the basics of OOP.

---
