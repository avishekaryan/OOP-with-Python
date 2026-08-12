# Unit 6 — SQLite and Databases with Python

## Definition Type Questions (2 Marks)

### Q1. What are the five most common SQL commands used in this unit?

- The five commands that come up repeatedly are `SELECT` (read data), `INSERT` (add data), `UPDATE` (modify data), `DELETE` (remove data), and `CREATE TABLE` (define a new table).

```sql
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO students VALUES (1, 'Avhi');
SELECT * FROM students;
UPDATE students SET name = 'Avhi K' WHERE id = 1;
DELETE FROM students WHERE id = 1;
```

---

### Q2. How do you connect to a SQLite database file using Python?

- After `import sqlite3`, a single line does the job: `conn = sqlite3.connect("database.db")` — and conveniently, if that file does not already exist, SQLite simply creates it.

```python
import sqlite3
conn = sqlite3.connect("school.db")
print("Connected!")
conn.close()
```

---

### Q3. What is the purpose of `conn.cursor()`?

- A connection on its own cannot run SQL — it needs a cursor object for that, created with `conn.cursor()`, which is then used to execute statements and pull back results.

```python
cur = conn.cursor()
cur.execute("SELECT * FROM students")
print(cur.fetchall())
```

---

### Q4. Why must a single-element tuple include a trailing comma in Python database code?

- Without the comma, `(value)` is just `value` wrapped in ordinary parentheses, not a tuple at all — Python only reads it as a genuine one-element tuple once the trailing comma is added, e.g. `(value,)`.

```python
cur.execute("SELECT * FROM students WHERE id = ?", (1,))   # correct - tuple
# cur.execute("SELECT * FROM students WHERE id = ?", (1))  # wrong - just an int
```

---

### Q5. What does `cursor.lastrowid` return after an `INSERT`?

- It hands back the row ID — effectively the primary key — of whichever row was just inserted, which is convenient when that ID is needed right away, e.g. for a related insert.

```python
cur.execute("INSERT INTO students (name) VALUES (?)", ("Avhi",))
conn.commit()
print(cur.lastrowid)   # e.g. 5
```

---

### Q6. What is the benefit of `CREATE TABLE IF NOT EXISTS`?

- It quietly does nothing if the table is already there, instead of raising an error — which is exactly what makes it safe to run a setup script more than once.

```sql
CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT);
```

---

### Q7. What is the purpose of `LIMIT` in a `SELECT` query?

- `LIMIT` simply caps how many rows come back from a query, which is handy for previewing data or building pagination without pulling back everything at once.

```sql
SELECT * FROM students ORDER BY name LIMIT 5;   -- only first 5 rows
```

---

### Q8. How does `cursor.rowcount` help after an `UPDATE` or `DELETE`?

- It reports back exactly how many rows were actually affected by the last statement, which is a quick way to confirm the change did what was expected.

```python
cur.execute("DELETE FROM students WHERE id = ?", (1,))
print(cur.rowcount)   # e.g. 1 - one row deleted
```

---

### Q9. What does `conn.commit()` do and why is it necessary?

- Nothing written during a transaction is actually permanent until `conn.commit()` is called — it is this call that saves the changes to the database file for good. Skip it, and the changes can simply be lost or later rolled back.

```python
cur.execute("INSERT INTO students (name) VALUES (?)", ("Avhi",))
conn.commit()   # without this, the insert is not saved
```

---

### Q10. What does `conn.rollback()` do and when should you use it?

- `conn.rollback()` undoes everything done since the last commit, returning the database to where it stood before. It is used whenever something goes wrong mid-transaction, so a half-finished change never gets left behind.

```python
try:
    cur.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    raise ValueError("something went wrong")
    conn.commit()
except Exception:
    conn.rollback()   # undoes the balance update above
```

---

### Q11. What is `sqlite3.IntegrityError` and when is it raised?

- This is what Python raises whenever a constraint is broken — `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, or `FOREIGN KEY` — such as trying to insert a duplicate primary key value.

```python
cur.execute("INSERT INTO students (id, name) VALUES (1, 'A')")
conn.commit()
cur.execute("INSERT INTO students (id, name) VALUES (1, 'B')")  # duplicate id
# raises sqlite3.IntegrityError
```

---

### Q12. What is `sqlite3.OperationalError` and when is it raised?

- This one shows up for problems with running the operation itself — a malformed SQL statement, a table or column that does not exist, or a database file that is locked.

```python
cur.execute("SELECT * FROM no_such_table")
# raises sqlite3.OperationalError: no such table: no_such_table
```

---

### Q13. What is the purpose of a seed or setup function in database examples?

- Its job is to get the database into a known, ready state — creating the required tables and inserting some starting data, so the application always has something consistent to work with from the very first run.

```python
def setup():
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO students (name) VALUES ('Avhi')")
    conn.commit()
```

---

## 6 Mark Questions

### Q1. What is a relational database and how does it differ from plain text files?

- A relational database organizes data into structured tables of rows and columns, and — importantly — enforces relationships between those tables rather than leaving them as separate, disconnected files.
- It also enforces a schema, meaning data types and constraints are checked automatically, which is not something a plain text file does at all — a text file has no built-in structure enforcement whatsoever.
- This structure is also what makes SQL possible — filtering, sorting, joining, and aggregating data through queries, instead of manually parsing text line by line.
- On top of that, relational databases add concurrency control, transactions, and integrity guarantees, none of which a plain text file offers on its own.
- Foreign keys are what tie related tables together, which is exactly what avoids the repeated, duplicated data that quickly becomes unmanageable in flat text files.

```sql
-- relational: structured, related tables
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);
-- vs. a plain text file: "1,Avhi\n2,Sita\n" with no enforced structure
```

---

### Q2. Explain the roles of tables, rows, columns, primary keys, and foreign keys in a relational database.

- These five terms work together, so it helps to see how each one builds on the last.
- A table holds a collection of related records — much like a single spreadsheet dedicated to one type of data.
- A row is one individual record within that table — one specific entry.
- A column is one attribute shared by every row, with its own defined data type — the same "field" repeated down the table.
- A primary key is what makes each row uniquely identifiable — it cannot be null, and it cannot be duplicated across rows.
- A foreign key then connects two tables together, by referencing another table's primary key, and this is exactly what keeps the data consistent across related tables.

```sql
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE marks (id INTEGER PRIMARY KEY, student_id INTEGER, score INTEGER,
  FOREIGN KEY(student_id) REFERENCES students(id));
```

---

### Q3. Why is SQLite a good choice for teaching database access in Python?

- Part of the appeal is how little setup it needs — SQLite is serverless and file-based, so there is no separate installation or server configuration standing between a beginner and writing their first query.
- It also comes built into Python already, through the `sqlite3` module, so nothing extra needs to be installed just to get started.
- Since the whole database lives in a single file, it is trivially easy to share, copy, or reset while testing.
- And because it still follows standard SQL and supports the same core relational concepts — tables, keys, constraints, transactions — the skills learned on it transfer directly to larger database systems later.

---

### Q4. Why should you use parameterised queries with `?` placeholders?

- The core idea is separation — parameterised queries keep the SQL code itself completely separate from whatever data the user actually supplies.
- The `?` placeholder is filled in safely by the database driver itself, with proper escaping handled automatically behind the scenes.
- This is exactly what prevents SQL injection — an attack that becomes possible the moment user input is concatenated directly into a query string.
- It also quietly solves a second problem: special characters like quotes in the data no longer need to be manually escaped, since the driver takes care of that too.

```python
name = "Avhi"
cur.execute("SELECT * FROM students WHERE name = ?", (name,))   # safe
# cur.execute(f"SELECT * FROM students WHERE name = '{name}'") # unsafe
```

---

### Q5. What is SQL injection and how do parameterised queries prevent it?

- SQL injection happens when malicious input is crafted specifically to change the structure of a query, potentially exposing, altering, or deleting data it was never meant to touch.
- It usually creeps in when user input is concatenated straight into a query string, e.g. `"SELECT * FROM users WHERE name = '" + name + "'"`.
- Given that, something as simple as typing `' OR '1'='1` as input can trick the query into bypassing its intended logic entirely.
- Parameterised queries close this gap because the `?` placeholder always treats whatever value is passed in strictly as data — never as part of the SQL syntax — which removes the vulnerability altogether.

```python
malicious_input = "' OR '1'='1"
# unsafe: cur.execute(f"SELECT * FROM users WHERE name = '{malicious_input}'")
# safe:
cur.execute("SELECT * FROM users WHERE name = ?", (malicious_input,))
```

---

### Q6. What are the main SQLite data types and when should each be used?

- SQLite keeps this simple with just five core types, each suited to a different kind of value.
- `NULL` — used to represent a value that is missing or unknown.
- `INTEGER` — for whole numbers, such as IDs and counts.
- `REAL` — for numbers with decimals, like prices or measurements.
- `TEXT` — for character/string data, such as names or descriptions.
- `BLOB` — for binary data, stored exactly as given, such as an image or file.

```sql
CREATE TABLE files (
  id INTEGER PRIMARY KEY,
  price REAL,
  name TEXT,
  data BLOB
);
```

---

### Q7. How do `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` constraints work?

- Each of these constraints protects the data in a slightly different way, though they are often used together on the same table.
- `PRIMARY KEY` uniquely identifies each row, and — importantly — automatically implies both `NOT NULL` and uniqueness on its own.
- `NOT NULL` simply refuses to let a column be left empty.
- `UNIQUE` ensures no two rows share the same value in that column, though — unlike a primary key — it can still allow a null value.
- `DEFAULT` supplies a fallback value automatically whenever an insert does not specify one.
- `CHECK` enforces a custom rule that every value in that column must satisfy, e.g. `CHECK(age >= 0)`.

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  status TEXT DEFAULT 'active',
  age INTEGER CHECK(age >= 0)
);
```

---

### Q8. How do you insert multiple rows efficiently in one call?

- Rather than looping and calling `execute()` once per row, `cursor.executemany(sql, list_of_tuples)` handles the whole batch in one call.
- For example, `cursor.executemany("INSERT INTO students VALUES (?, ?)", [(1, 'A'), (2, 'B')])` inserts both rows in a single step.
- This cuts down the number of individual statement executions considerably, making it both faster and more concise than the equivalent loop.
- It is still worth noting that it uses the same `?` placeholders throughout, so it stays just as protected against SQL injection.

---

### Q9. What is the difference between `fetchone()`, `fetchmany(n)`, and `fetchall()`?

- The three methods differ mainly in how much of the result set they hand back at once.
- `fetchone()` returns just the next single row, or `None` once nothing is left.
- `fetchmany(n)` returns the next `n` rows together as a list, which is useful for processing results in manageable batches.
- `fetchall()` returns every remaining row at once, which is simplest for small results but can use significant memory once the dataset grows large.
- So the choice really comes down to result size — `fetchone()`/`fetchmany()` scale far better for large datasets, while `fetchall()` stays the easiest option for small ones.

```python
cur.execute("SELECT * FROM students")
print(cur.fetchone())     # one row: (1, 'Avhi')
print(cur.fetchmany(2))   # next 2 rows as a list
print(cur.fetchall())     # all remaining rows
```

---

### Q10. How do you filter query results with `WHERE` and sort them with `ORDER BY`?

- `WHERE condition` narrows the result down to only the rows that satisfy it — for example, `SELECT * FROM students WHERE age > 18` keeps only students above 18.
- `ORDER BY column [ASC|DESC]` then sorts whatever rows remain, ascending by default unless `DESC` is specified.
- Both clauses combine naturally in one query, e.g. `SELECT * FROM students WHERE age > 18 ORDER BY name ASC`.
- It helps to remember the order these actually apply in: filtering happens first, and only the surviving rows are then sorted.

```sql
[Table rows] -> [WHERE: filter] -> [ORDER BY: sort] -> [LIMIT: restrict count] -> [Final Result]
SELECT * FROM students WHERE age > 18 ORDER BY name ASC;
```

---

### Q11. When should you use `COUNT(*)`, `AVG()`, `SUM()`, `MAX()`, and `MIN()`?

- Each of these aggregate functions answers a different kind of summary question about a column.
- `COUNT(*)` — how many rows matched, e.g. the total number of students.
- `AVG()` — the average value of a numeric column, e.g. average marks.
- `SUM()` — the running total of a numeric column, e.g. total sales.
- `MAX()` — the single highest value present, e.g. the highest score.
- `MIN()` — the single lowest value present, e.g. the lowest price.

```sql
SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students;
```

---

### Q12. Why is it dangerous to run `UPDATE` or `DELETE` without a `WHERE` clause?

- Leaving out `WHERE` means the statement no longer targets specific rows — it simply applies to every single row in the table.
- That can silently overwrite or permanently wipe out an entire table's worth of data, and unlike many other tools, SQLite does not stop to ask for confirmation first.
- This makes it a genuinely costly mistake, especially in a production system where the loss is real and often irreversible.
- For that reason, it is good practice to first run a `SELECT` with the same `WHERE` condition, just to see exactly which rows would be affected, before ever running the actual `UPDATE`/`DELETE`.

```sql
-- DANGEROUS: wipes every row in the table
DELETE FROM students;
-- SAFE: targets only the intended row
DELETE FROM students WHERE id = 5;
```

---

### Q13. How does the `with sqlite3.connect(...) as conn:` context manager improve safety?

- Using `with` here means the transaction is automatically committed if the block finishes successfully, or automatically rolled back if an exception interrupts it.
- This removes a common source of bugs — manually remembering to call `conn.commit()`/`conn.rollback()` in every function — since forgetting either one is exactly how data ends up lost or left inconsistent.
- One detail worth remembering, though, is that it does not automatically close the connection the way file objects do — `conn.close()` may still be needed separately — but the transactional safety within the block is guaranteed regardless.

```python
with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name) VALUES (?)", ("Avhi",))
    # auto-commits here if no error, auto-rollback if an exception occurs
```

---

### Q14. What are ACID properties and why are they important for transactions?

- ACID names four properties that together define what a genuinely reliable transaction looks like.
- Atomicity — every operation in a transaction succeeds together, or the whole transaction fails together, with nothing left half-done.
- Consistency — a transaction only ever moves the database from one valid state to another, respecting every rule and constraint along the way.
- Isolation — transactions running at the same time do not interfere with each other's in-progress changes.
- Durability — once a transaction is committed, it stays committed, even through a crash or power failure.
- Together, these are what make it possible to trust critical operations — like a banking transfer or an order being processed — to actually behave correctly, every time.

---

### Q15. Why should database helper functions return status flags instead of raw exceptions?

- Returning something simple, like `True`/`False` or a result code, lets the calling code check for success or failure without needing a `try/except` wrapped around every single call.
- It also keeps the actual error-handling logic centralized inside the helper function itself, which tends to make the rest of the codebase noticeably cleaner.
- This matters especially in GUI or web applications, where an unhandled exception bubbling up could crash the whole interface rather than just failing gracefully.
- None of this stops the helper function from logging or handling the real exception internally — it simply gives the caller a much simpler, more predictable interface to work with.

```python
def insert_student(name):
    try:
        cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        return True        # success flag
    except sqlite3.IntegrityError:
        return False       # failure flag, no raw exception leaked
```

---

## 12 Mark Questions

### Q1. Give an example of a multi-step transaction and explain why it must be atomic.

**Introduction**

A good way to see why atomicity matters is through a case where a single logical action is actually made up of more than one database operation.

**Body**

- Transferring money between two bank accounts is a classic example — it genuinely requires two separate steps: deducting the amount from Account A, and then adding that same amount to Account B.

```python
with sqlite3.connect("bank.db") as conn:
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
```

- If both statements succeed, the `with` block's automatic `commit()` saves both changes together, permanently.
- But suppose the second statement fails — an invalid account ID, say, or a constraint violation — after the first has already gone through. If both changes are not treated as one unit, money would simply vanish from Account A without ever reaching Account B.
- This is exactly why the transaction has to be atomic: it must be treated as one indivisible unit of work, where either both updates happen, or neither does.
- Without that guarantee, any crash or error partway through would leave the database in a state that does not correspond to any valid real-world outcome.
- The `with sqlite3.connect(...)` context manager (or an explicit `try/except` using `commit()`/`rollback()`) is what enforces this all-or-nothing behaviour automatically.

```
[Deduct from A] -> [Add to B] -> both ok? -> yes -> [COMMIT: both saved] | no -> [ROLLBACK: undo deduction too]
```

**Conclusion**

This example shows why atomicity is essential for any multi-step operation involving real data, and it is a genuinely useful way to explain ACID properties using a concrete, relatable case.

---

### Q2. How can a library management system use related tables and joins to avoid data duplication?

**Introduction**

The question here is really about design: how should a system record who borrowed which book, without repeating the same book and member details over and over again?

**Body**

- The answer is to split the data into separate, related tables instead of one large flat one — typically `Books`, `Members`, and `Loans`.
- The `Books` table stores each book's details exactly once — id, title, author, ISBN — using `book_id` as its primary key.
- The `Members` table does the same for member details — id, name, email — using `member_id` as its primary key.
- The `Loans` table then stores only the transactional part: `loan_id`, `book_id` (a foreign key back to Books), `member_id` (a foreign key back to Members), `loan_date`, and `return_date`.
- This is exactly what avoids duplication — no matter how many times a particular book gets borrowed, its details are stored only once, in the `Books` table.

```sql
CREATE TABLE Books (book_id INTEGER PRIMARY KEY, title TEXT, author TEXT);
CREATE TABLE Members (member_id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE Loans (loan_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER,
  loan_date TEXT, FOREIGN KEY(book_id) REFERENCES Books(book_id),
  FOREIGN KEY(member_id) REFERENCES Members(member_id));
```

- Of course, splitting the data up this way means a `JOIN` is now needed to bring it back together — for instance, to see which member borrowed which book.

```sql
SELECT Members.name, Books.title, Loans.loan_date
FROM Loans
JOIN Members ON Loans.member_id = Members.member_id
JOIN Books ON Loans.book_id = Books.book_id;
[Books] <-FK(book_id)- [Loans] -FK(member_id)-> [Members]
```

- This normalized design — related tables plus joins — is really the standard relational approach to avoiding duplication, and its benefit becomes obvious the moment something changes: updating a book's title only ever needs one change, in the `Books` table, rather than in every single loan record that mentions it.

**Conclusion**

This normalized design with foreign keys and joins is the standard relational-database solution for avoiding duplication, and is a very commonly asked practical exam question.

---
