# Unit 6 — Python SQL Database Access
## BT151CO · Object-Oriented Programming

---

| | |
|---|---|
| **Duration** | 5 Hours |
| **CLO 6** | Write Python programs that store, retrieve, update, and delete data using a relational SQL database |
| **Pre-requisites** | Unit 1 (Python fundamentals), Unit 3 (error handling) |

---

## Table of Contents

1. [Introduction to Database Programming](#1-introduction-to-database-programming)
   - 1.1 What Is a Database?
   - 1.2 What Is SQL?
   - 1.3 What Is SQLite?
   - 1.4 The Python `sqlite3` Module
2. [Installation and Setup](#2-installation-and-setup)
   - 2.1 Checking Your Environment
   - 2.2 Using DB Browser for SQLite
3. [Establishing a Database Connection](#3-establishing-a-database-connection)
   - 3.1 `connect()` and the Database File
   - 3.2 The Cursor Object
   - 3.3 Context Managers — The Safer Way
4. [Creating Database Tables](#4-creating-database-tables)
   - 4.1 The `CREATE TABLE` Statement
   - 4.2 Data Types in SQLite
   - 4.3 Primary Keys and Constraints
   - 4.4 `CREATE TABLE IF NOT EXISTS`
   - 4.5 Full Table Design Walkthrough
5. [INSERT — Adding Records](#5-insert--adding-records)
   - 5.1 The `INSERT INTO` Statement
   - 5.2 Parameterised Queries — The Golden Rule
   - 5.3 Inserting Multiple Rows at Once
   - 5.4 Retrieving the Last Inserted Row ID
6. [READ — Querying Records](#6-read--querying-records)
   - 6.1 The `SELECT` Statement
   - 6.2 `fetchone()`, `fetchmany()`, `fetchall()`
   - 6.3 Filtering with `WHERE`
   - 6.4 Sorting with `ORDER BY`
   - 6.5 Limiting Results with `LIMIT`
   - 6.6 Aggregate Functions
7. [UPDATE — Modifying Records](#7-update--modifying-records)
   - 7.1 The `UPDATE` Statement
   - 7.2 Always Use a `WHERE` Clause
   - 7.3 Updating Multiple Columns
8. [DELETE — Removing Records](#8-delete--removing-records)
   - 8.1 The `DELETE FROM` Statement
   - 8.2 Deleting All Rows vs Dropping the Table
9. [COMMIT and ROLLBACK — Transaction Control](#9-commit-and-rollback--transaction-control)
   - 9.1 What Is a Transaction?
   - 9.2 `commit()` — Saving Changes
   - 9.3 `rollback()` — Undoing Changes
   - 9.4 Autocommit Mode
10. [Handling Database Errors](#10-handling-database-errors)
    - 10.1 The `sqlite3` Exception Hierarchy
    - 10.2 Wrapping Operations in `try / except`
    - 10.3 Logging Errors
    - 10.4 Re-raising and Custom Messages
11. [Putting It All Together — Capstone Example](#11-putting-it-all-together--capstone-example)
12. [Common Mistakes to Avoid](#12-common-mistakes-to-avoid)
13. [Summary and Key Takeaways](#13-summary-and-key-takeaways)
14. [Glossary](#14-glossary)

---

## Learning Objectives

By the end of this unit you will be able to:

1. Explain what a relational database is and why programs use one instead of a file
2. Connect to a SQLite database file using Python's `sqlite3` module
3. Create a database table with appropriate column types and constraints
4. Insert, read, update, and delete records using parameterised SQL queries
5. Explain what a transaction is and control it with `commit()` and `rollback()`
6. Handle database errors gracefully using `try / except` blocks
7. Build a small data-driven application that persists information between runs

---

## 1. Introduction to Database Programming

### 1.1 What Is a Database?

Every meaningful application eventually needs to **remember things**:
- A shopping app must remember products, prices, and purchase history.
- A library system must remember which books are available and which are on loan.
- A game must remember high scores, player progress, and unlocked items.
- A bank must remember account balances, transactions, and customer details.

You already know one way to persist data: write it to a file. But files have serious
limitations at scale:

| Approach | Problem |
|---|---|
| Plain text file | Hard to search. Hard to update one record without rewriting everything. |
| CSV file | No data types. No relationships. No concurrent access. |
| `pickle` / JSON file | Entire file must be loaded into memory. No query language. |
| **Database** | Structured, queryable, efficient, concurrent-safe, persistent. |

A **database** is an organised collection of data stored so that it can be
easily accessed, managed, and updated.

A **relational database** organises data into **tables** — like spreadsheets with
strict rules about the shape of each row.

**Real-world analogy:**  
Think of a database as a filing cabinet in a school office.
Each **drawer** is a **table** (one for students, one for courses, one for grades).
Each **folder** inside the drawer is a **row** (one folder per student).
Each **piece of paper** inside the folder is a **column** (name, ID, date of birth).
The cabinet lets you find any student's folder in seconds — much faster than
searching through a pile of loose papers on a desk.

---

### 1.2 What Is SQL?

**SQL** (Structured Query Language, pronounced *"sequel"* or *"S-Q-L"*) is the
standard language for communicating with relational databases.

SQL is made up of plain English-like commands:

```sql
-- Create a table
CREATE TABLE students (id INTEGER, name TEXT, gpa REAL);

-- Add a record
INSERT INTO students VALUES (1, 'Alice', 3.8);

-- Read records
SELECT name, gpa FROM students WHERE gpa > 3.0;

-- Update a record
UPDATE students SET gpa = 3.9 WHERE id = 1;

-- Delete a record
DELETE FROM students WHERE id = 1;
```

You do not need to be a database expert to use SQL in Python. The five commands
above — `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE` — cover the vast majority
of what application code ever needs.

**Note**: 

- Teaching SQL is not a part of the syllabus. Please refer to [https://sqlcrashcourse.com](https://sqlcrashcourse.com) for a crash course in SQL. 
- Or, refer to the [sql-cheet-sheet](https://www.geeksforgeeks.org/sql/sql-cheat-sheet/) by GeeksforGeeks. 
- PDF from [GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20240328180119/SQL-Cheat-Sheet-PDF.pdf)

---

### 1.3 What Is SQLite?

There are many SQL database systems: PostgreSQL, MySQL, MariaDB, SQL Server, Oracle.
They all speak SQL, but they require installation, configuration, and a running server.

**SQLite** is different:

- It stores the entire database in a **single `.db` file** on disk.
- There is **no server** to install or manage.
- It is built into Python's standard library — **zero dependencies**.
- It is the most widely deployed database engine in the world
  (used in Android, iOS, Firefox, Chrome, Dropbox, and countless others).

For learning, prototyping, small applications, and embedded use, SQLite is the
perfect choice. The SQL you learn with SQLite transfers directly to every other
database system.

```
Your Python script ───▶   sqlite3 (Python module) ───▶ library.db (file on disk)                    
```

---

### 1.4 The Python `sqlite3` Module

Python's `sqlite3` module is part of the standard library — no `pip install` needed.

```python
import sqlite3
```

The module follows the **DB-API 2.0** standard (PEP 249), which means the
same pattern works for PostgreSQL (`psycopg2`), MySQL (`mysql-connector-python`),
and others. Learning `sqlite3` teaches you the pattern for all of them.

The workflow for every database operation is the same four steps:

```
1. Connect    → sqlite3.connect('myfile.db')
2. Cursor     → connection.cursor()
3. Execute    → cursor.execute('SQL...')
4. Commit     → connection.commit()   (for write operations)
```

---

## 2. Installation and Setup

### 2.1 Checking Your Environment

`sqlite3` is built into Python. To verify it is available:

```python
import sqlite3
print(sqlite3.version)        # sqlite3 module version
print(sqlite3.sqlite_version)  # underlying SQLite library version
```

**Expected output:**
```
2.6.0
3.41.2
```

No installation is required. Any Python 3.x installation includes it.

---

### 2.2 Using DB Browser for SQLite

When learning, it helps to **see** inside your database file as well as query it.
**DB Browser for SQLite** (https://sqlitebrowser.org/) is a free, open-source GUI tool
that lets you open `.db` files, browse tables, and run SQL manually.

**Recommended learning workflow:**

1. Write Python code that creates/modifies the database.
2. Open the `.db` file in DB Browser to visually inspect the result.
3. This builds intuition about what your code is actually doing.

You do **not** need DB Browser to follow this unit — it is optional but helpful.

---

## 3. Establishing a Database Connection

### 3.1 `connect()` and the Database File

The first step in any database operation is creating a **connection** — an open
channel between your Python program and the database file.

```python
import sqlite3

# Connect to a file (creates it if it does not exist)
connection = sqlite3.connect('library.db')
```

When this line runs:
- If `library.db` does **not** exist → SQLite creates a blank database file.
- If `library.db` **does** exist → SQLite opens it, ready to read and write.

**Special value — in-memory database:**

```python
# Database lives entirely in RAM — gone when the program ends
connection = sqlite3.connect(':memory:')
```

An in-memory database is useful for testing and for temporary operations where
you do not need to persist data. It is also faster than a file-based database.

**Closing the connection:**

When you are finished, always close the connection to flush any pending data
and release the file lock:

```python
connection.close()
```

---

### 3.2 The Cursor Object

A **connection** is the open channel to the database. But to actually *run* SQL
statements, you need a **cursor** — think of it as the pen that writes to the database
or the pointer that reads from it.

```python
connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute("SELECT sqlite_version()")  # run a SQL statement
row = cursor.fetchone()                    # get the result
print(row)   # ('3.41.2',)
```

You can create multiple cursors from the same connection, but for most simple
programs a single cursor is all you need.

**Real-world analogy:**  
A connection is your library card — it authorises you to access the library.
A cursor is the librarian who carries out your requests. You ask the librarian
(cursor) to find books; the card (connection) proves you are allowed to be there.

---

### 3.3 Context Managers — The Safer Way

Manually calling `connection.close()` works, but what happens if an error
occurs before you reach that line? The connection stays open and the file lock
is never released.

The safe, Pythonic pattern is to use a **context manager** (`with` statement):

```python
import sqlite3

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    print(cursor.fetchone())
# Connection is automatically closed here, even if an error occurred
```

> **Best practice:** Always use `with sqlite3.connect(...)` so the connection
> is guaranteed to close, even when exceptions occur.

**Important nuance — `with` and `commit()`:**

When used as a context manager, `sqlite3` automatically calls `commit()` if no
exception occurred, or `rollback()` if an exception did occur.

This means for write operations inside a `with` block, you often do not need
to call `commit()` manually — but calling it explicitly never hurts and makes
the intent clear.

---

## 4. Creating Database Tables

### 4.1 The `CREATE TABLE` Statement

A **table** defines the structure of the data you want to store.
Creating a table is like designing a form: you decide how many fields there are
and what type of data each field holds.

```sql
CREATE TABLE students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    gpa     REAL    DEFAULT 0.0,
    enrolled DATE
);
```

In Python:

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE students (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            gpa      REAL    DEFAULT 0.0,
            enrolled TEXT
        )
    """)
```

---

### 4.2 Data Types in SQLite

SQLite uses a flexible type system called **type affinity**. It supports five storage classes:

| SQLite Type | Python equivalent | Use for |
|---|---|---|
| `INTEGER` | `int` | Whole numbers, IDs, counts |
| `REAL` | `float` | Decimal numbers, prices, scores |
| `TEXT` | `str` | Names, descriptions, dates as strings |
| `BLOB` | `bytes` | Binary data (images, files) |
| `NULL` | `None` | Missing / unknown value |

**Dates in SQLite:**  
SQLite has no native date type. Dates are stored as `TEXT` (e.g. `'2024-09-01'`)
in ISO 8601 format, or as `INTEGER` (Unix timestamp). Storing as `TEXT` in the
format `YYYY-MM-DD` is the most common practice because it sorts correctly
as a string and is human-readable.

---

### 4.3 Primary Keys and Constraints

A **primary key** uniquely identifies every row in a table.
No two rows can have the same primary key value.

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

- `PRIMARY KEY` — this column is the unique identifier for each row
- `AUTOINCREMENT` — SQLite assigns the next available integer automatically
  (you never provide the `id` when inserting a new row)

**Other constraints:**

| Constraint | Meaning |
|---|---|
| `NOT NULL` | This column must always have a value |
| `UNIQUE` | No two rows can have the same value in this column |
| `DEFAULT value` | Use this value if none is provided on insert |
| `CHECK (condition)` | Reject any row where the condition is false |

**Example with constraints:**

```sql
CREATE TABLE bank_accounts (
    account_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_name   TEXT    NOT NULL,
    balance      REAL    NOT NULL DEFAULT 0.0,
    account_type TEXT    NOT NULL DEFAULT 'current',
    CHECK (balance >= 0)          -- balance can never go below zero
);
```

---

### 4.4 `CREATE TABLE IF NOT EXISTS`

If you run a `CREATE TABLE` statement and the table already exists,
SQLite raises an error. Add `IF NOT EXISTS` to make it safe to run
on every application startup:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name     TEXT    NOT NULL,
        gpa      REAL    DEFAULT 0.0,
        enrolled TEXT
    )
""")
```

This is the recommended pattern for table creation code — it acts as
"create the table only if it is not already there."

---

### 4.5 Full Table Design Walkthrough

Let us design a small database for a **library** with two tables:
books and members.

```python
import sqlite3

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()

    # Table 1: books
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT    NOT NULL,
            author      TEXT    NOT NULL,
            year        INTEGER,
            available   INTEGER NOT NULL DEFAULT 1  -- 1 = yes, 0 = no
        )
    """)

    # Table 2: members
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            email       TEXT    UNIQUE NOT NULL,
            joined      TEXT    NOT NULL  -- stored as 'YYYY-MM-DD'
        )
    """)

print("Tables created successfully.")
```

**Expected output:**
```
Tables created successfully.
```

> **Teaching note:** Each `cursor.execute()` call runs exactly one SQL statement.
> For multiple table creations, call `execute()` multiple times — or use
> `executescript()` for a batch of statements separated by semicolons.

---

## 5. INSERT — Adding Records

### 5.1 The `INSERT INTO` Statement

Once a table exists, you add rows to it with `INSERT INTO`:

```sql
INSERT INTO students (name, gpa, enrolled)
VALUES ('Alice', 3.8, '2024-09-01');
```

Notice that `id` is not listed — it is `AUTOINCREMENT` so SQLite assigns it.

In Python:

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, gpa, enrolled) VALUES (?, ?, ?)",
        ('Alice', 3.8, '2024-09-01')
    )
    conn.commit()
    print("Row inserted.")
```

**Expected output:**
```
Row inserted.
```

---

### 5.2 Parameterised Queries — The Golden Rule

In the example above, notice the **`?` placeholders** in the SQL string
and the **tuple of values** passed as the second argument to `execute()`.

This pattern is called a **parameterised query** (also called a *prepared statement*).

**Why it matters — SQL Injection:**

Imagine you wrote this instead:

```python
# ❌ NEVER DO THIS
name = input("Enter name: ")
cursor.execute("INSERT INTO students (name) VALUES ('" + name + "')")
```

If the user types: `Alice'); DROP TABLE students; --`

Your query becomes:
```sql
INSERT INTO students (name) VALUES ('Alice'); DROP TABLE students; --')
```

This **deletes your entire table**. This attack is called **SQL injection** and
it is one of the most common security vulnerabilities in web applications
(OWASP Top 10 #3).

**Parameterised queries prevent SQL injection completely:**

```python
# ✅ ALWAYS DO THIS
name = input("Enter name: ")
cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
```

SQLite treats the `?` value as **data only** — it can never be interpreted
as SQL code, no matter what the user types.

> **Golden Rule:** Never concatenate or format user input directly into a SQL string.
> Always use `?` placeholders.

**Note the trailing comma:**  
`(name,)` — a single-element tuple in Python requires a trailing comma.
`(name)` without the comma is just `name` in parentheses, which is a string,
not a tuple. `execute()` expects a sequence (tuple or list).

```python
# ❌ Wrong — passes the string itself as the parameter sequence
cursor.execute("INSERT INTO students (name) VALUES (?)", ('Alice'))

# ✅ Correct — single-element tuple
cursor.execute("INSERT INTO students (name) VALUES (?)", ('Alice',))

# ✅ Also correct — a list works too
cursor.execute("INSERT INTO students (name) VALUES (?)", ['Alice'])
```

---

### 5.3 Inserting Multiple Rows at Once

To insert many rows efficiently, use `executemany()` with a list of tuples:

```python
import sqlite3

new_students = [
    ('Bob',     2.9, '2024-09-01'),
    ('Charlie', 3.5, '2024-09-01'),
    ('Diana',   3.7, '2024-09-01'),
    ('Eve',     3.1, '2024-09-01'),
]

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO students (name, gpa, enrolled) VALUES (?, ?, ?)",
        new_students
    )
    conn.commit()
    print(f"Inserted {cursor.rowcount} rows.")
```

**Expected output:**
```
Inserted 4 rows.
```

`executemany()` is more efficient than calling `execute()` in a loop because
it sends all the rows to the database in a single transaction.

---

### 5.4 Retrieving the Last Inserted Row ID

After an `INSERT`, you can find out the `id` that was automatically assigned:

```python
with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, gpa, enrolled) VALUES (?, ?, ?)",
        ('Frank', 3.3, '2024-09-01')
    )
    conn.commit()
    print(f"New student's id: {cursor.lastrowid}")
```

**Expected output:**
```
New student's id: 6
```

This is useful when you need the new row's ID to immediately create a related
record in another table (e.g. create a student, then create their first loan record).

---

## 6. READ — Querying Records

### 6.1 The `SELECT` Statement

`SELECT` retrieves rows from a table. It is the most used SQL command.

```sql
SELECT column1, column2 FROM table_name;   -- specific columns
SELECT * FROM table_name;                   -- all columns
```

In Python, after calling `execute()` on a `SELECT` query, you retrieve
the results using one of the `fetch` methods.

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, gpa FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

**Expected output:**
```
(1, 'Alice', 3.8)
(2, 'Bob', 2.9)
(3, 'Charlie', 3.5)
(4, 'Diana', 3.7)
(5, 'Eve', 3.1)
(6, 'Frank', 3.3)
```

Each row is returned as a **tuple**. The order of values matches the order
of columns you requested in the `SELECT` statement.

---

### 6.2 `fetchone()`, `fetchmany()`, `fetchall()`

After executing a `SELECT`, you have three options for retrieving results:

| Method | Returns | Use when |
|---|---|---|
| `fetchone()` | One row (tuple) or `None` | You expect exactly one result |
| `fetchmany(n)` | Up to `n` rows (list of tuples) | Processing in batches |
| `fetchall()` | All rows (list of tuples) | Small result sets |

```python
with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name, gpa FROM students")

    # fetchone — get the first row only
    first = cursor.fetchone()
    print("First:", first)          # ('Alice', 3.8)

    # fetchmany — get the next 2 rows
    some = cursor.fetchmany(2)
    print("Next two:", some)        # [('Bob', 2.9), ('Charlie', 3.5)]

    # fetchall — get all remaining rows
    rest = cursor.fetchall()
    print("Remaining:", rest)       # [('Diana', 3.7), ('Eve', 3.1), ('Frank', 3.3)]
```

> **Important:** The cursor maintains a **position** in the result set.
> Each `fetch` call advances the position. After `fetchall()`, calling any
> `fetch` method returns an empty list — there is nothing left to fetch.

**For large result sets**, avoid `fetchall()` — it loads every row into memory
at once. Instead, iterate directly over the cursor:

```python
# Memory-efficient: processes one row at a time
cursor.execute("SELECT * FROM students")
for row in cursor:
    print(row)
```

---

### 6.3 Filtering with `WHERE`

`WHERE` filters rows to only those that match a condition.

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()

    # Students with GPA above 3.5
    cursor.execute(
        "SELECT name, gpa FROM students WHERE gpa > ?",
        (3.5,)
    )
    print("High achievers:")
    for name, gpa in cursor.fetchall():
        print(f"  {name}: {gpa}")
```

**Expected output:**
```
High achievers:
  Alice: 3.8
  Diana: 3.7
```

Common `WHERE` operators:

| Operator | Example | Meaning |
|---|---|---|
| `=` | `WHERE name = 'Alice'` | Exact match |
| `!=` or `<>` | `WHERE gpa != 0` | Not equal |
| `>`, `<`, `>=`, `<=` | `WHERE gpa >= 3.5` | Comparison |
| `BETWEEN` | `WHERE gpa BETWEEN 3.0 AND 3.5` | Inclusive range |
| `LIKE` | `WHERE name LIKE 'A%'` | Pattern match (`%` = any chars) |
| `IN` | `WHERE id IN (1, 3, 5)` | One of a list |
| `IS NULL` | `WHERE enrolled IS NULL` | No value |
| `AND`, `OR`, `NOT` | `WHERE gpa > 3 AND enrolled = '2024-09-01'` | Combine conditions |

**Shopping example — find products under a price:**

```python
with sqlite3.connect('shop.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, price FROM products WHERE price < ?",
        (10.00,)
    )
    for name, price in cursor.fetchall():
        print(f"  {name}: £{price:.2f}")
```

---

### 6.4 Sorting with `ORDER BY`

Results are not guaranteed to be in any particular order unless you
specify `ORDER BY`:

```python
with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()

    # Sort by GPA descending (highest first)
    cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC")
    print("Rankings:")
    for i, (name, gpa) in enumerate(cursor.fetchall(), start=1):
        print(f"  {i}. {name} — {gpa}")
```

**Expected output:**
```
Rankings:
  1. Alice — 3.8
  2. Diana — 3.7
  3. Charlie — 3.5
  4. Frank — 3.3
  5. Eve — 3.1
  6. Bob — 2.9
```

- `ORDER BY column ASC` — ascending (A→Z, lowest→highest) — **default**
- `ORDER BY column DESC` — descending (Z→A, highest→lowest)

---

### 6.5 Limiting Results with `LIMIT`

`LIMIT` restricts how many rows are returned. Useful for top-N queries
and pagination:

```python
# Top 3 students by GPA
cursor.execute(
    "SELECT name, gpa FROM students ORDER BY gpa DESC LIMIT ?",
    (3,)
)
for name, gpa in cursor.fetchall():
    print(f"  {name}: {gpa}")
```

**Expected output:**
```
  Alice: 3.8
  Diana: 3.7
  Charlie: 3.5
```

**Game leaderboard example:**

```python
# Top 5 scores
cursor.execute("""
    SELECT player_name, score
    FROM high_scores
    ORDER BY score DESC
    LIMIT 5
""")
```

---

### 6.6 Aggregate Functions

SQL has built-in functions that compute a summary value over a set of rows:

| Function | Returns | Example |
|---|---|---|
| `COUNT(*)` | Number of rows | `SELECT COUNT(*) FROM students` |
| `SUM(col)` | Total of all values | `SELECT SUM(price) FROM orders` |
| `AVG(col)` | Average value | `SELECT AVG(gpa) FROM students` |
| `MAX(col)` | Largest value | `SELECT MAX(score) FROM scores` |
| `MIN(col)` | Smallest value | `SELECT MIN(price) FROM products` |

```python
with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(gpa) FROM students")
    avg_gpa = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(gpa) FROM students")
    top_gpa = cursor.fetchone()[0]

    print(f"Total students: {total}")
    print(f"Average GPA:    {avg_gpa:.2f}")
    print(f"Top GPA:        {top_gpa}")
```

**Expected output:**
```
Total students: 6
Average GPA:    3.38
Top GPA:        3.8
```

---

## 7. UPDATE — Modifying Records

### 7.1 The `UPDATE` Statement

`UPDATE` modifies the values of columns in existing rows:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

In Python:

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET gpa = ? WHERE name = ?",
        (3.95, 'Alice')
    )
    conn.commit()
    print(f"Rows updated: {cursor.rowcount}")
```

**Expected output:**
```
Rows updated: 1
```

`cursor.rowcount` tells you how many rows were actually changed.
If it returns `0`, your `WHERE` clause matched nothing.

---

### 7.2 Always Use a `WHERE` Clause

The single most dangerous mistake with `UPDATE` (and `DELETE`) is
**forgetting the `WHERE` clause**:

```python
# ❌ CATASTROPHIC — updates EVERY row in the table
cursor.execute("UPDATE students SET gpa = 0.0")

# ✅ Safe — updates only the targeted row
cursor.execute(
    "UPDATE students SET gpa = 0.0 WHERE id = ?",
    (2,)
)
```

Without `WHERE`, every row in the table is modified. This is one of the most
common and destructive mistakes in database programming.

> **Rule:** Before running any `UPDATE` or `DELETE`, test your `WHERE` clause
> with a `SELECT` first to verify it matches exactly the rows you intend to target.

```python
# Step 1: Verify with SELECT
cursor.execute("SELECT id, name, gpa FROM students WHERE id = ?", (2,))
print(cursor.fetchall())   # confirm this is the row you want

# Step 2: Only then UPDATE
cursor.execute("UPDATE students SET gpa = 0.0 WHERE id = ?", (2,))
conn.commit()
```

---

### 7.3 Updating Multiple Columns

You can update several columns at once by separating them with commas in `SET`:

```python
# Bank account: change balance AND record timestamp
cursor.execute(
    """
    UPDATE bank_accounts
    SET balance = ?, last_transaction = ?
    WHERE account_id = ?
    """,
    (2500.00, '2024-10-15', 101)
)
conn.commit()
```

**Shopping example — update stock after a purchase:**

```python
def buy_item(conn, product_id, quantity_sold):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET stock = stock - ? WHERE product_id = ?",
        (quantity_sold, product_id)
    )
    conn.commit()
    print(f"Stock updated. Rows affected: {cursor.rowcount}")
```

Notice `stock = stock - ?` — you can reference the current column value
in the `SET` expression. This is a common pattern for incrementing or
decrementing a counter.

---

## 8. DELETE — Removing Records

### 8.1 The `DELETE FROM` Statement

`DELETE FROM` removes rows that match a condition:

```python
import sqlite3

with sqlite3.connect('school.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (6,)
    )
    conn.commit()
    print(f"Deleted {cursor.rowcount} row(s).")
```

**Expected output:**
```
Deleted 1 row(s).
```

Again: `cursor.rowcount` tells you how many rows were deleted.
If it is `0`, the `WHERE` clause matched nothing and nothing was deleted.

---

### 8.2 Deleting All Rows vs Dropping the Table

There are two ways to remove all data from a table:

```python
# Remove all rows but keep the table structure
cursor.execute("DELETE FROM students")

# Remove the table entirely (structure and data)
cursor.execute("DROP TABLE students")
```

Use `DELETE FROM` (without `WHERE`) when you want to **clear all data**
but plan to insert new rows later.

Use `DROP TABLE` when you want to **remove the table permanently**.

**Safe version — `DROP TABLE IF EXISTS`:**

```python
# Does not raise an error if the table does not exist
cursor.execute("DROP TABLE IF EXISTS students")
```

**Library example — remove expired memberships:**

```python
def remove_expired_members(conn, expiry_date):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM members WHERE expiry_date < ?",
        (expiry_date,)
    )
    conn.commit()
    print(f"Removed {cursor.rowcount} expired member(s).")
```

---

## 9. COMMIT and ROLLBACK — Transaction Control

### 9.1 What Is a Transaction?

A **transaction** is a group of database operations that are treated as
a single, atomic unit — either **all** of them succeed, or **none** of them do.

**Real-world analogy — bank transfer:**  
Transferring £100 from Account A to Account B involves two operations:
1. Deduct £100 from Account A
2. Add £100 to Account B

If operation 1 succeeds but operation 2 fails (e.g. due to a power cut),
you lose £100 — it disappears from A but never arrives at B.

A transaction solves this: both operations are bundled together.
If anything fails, the entire bundle is undone — as if neither operation happened.

```
BEGIN TRANSACTION
    Deduct £100 from Account A   ← operation 1
    Add    £100 to Account B     ← operation 2
COMMIT  ← both succeeded: make changes permanent
         (if either failed: ROLLBACK — undo both)
```

This guarantee is known by the acronym **ACID**:

| Letter | Property | Meaning |
|---|---|---|
| **A** | Atomicity | All or nothing |
| **C** | Consistency | Database stays in a valid state |
| **I** | Isolation | Transactions don't interfere with each other |
| **D** | Durability | Committed changes survive crashes |

---

### 9.2 `commit()` — Saving Changes

Changes made by `INSERT`, `UPDATE`, and `DELETE` are **not saved permanently**
until you call `commit()`. Until then, they exist only in a temporary buffer.

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO students (name, gpa, enrolled) VALUES (?, ?, ?)",
    ('Grace', 3.6, '2024-09-01')
)

# At this point, the row EXISTS in the buffer but is NOT saved to disk.
# If the program crashes here, the row is lost.

conn.commit()  # ← now the row is permanently saved to the file

conn.close()
```

If you use the `with` context manager pattern, `commit()` is called
automatically when the `with` block exits without an error.

---

### 9.3 `rollback()` — Undoing Changes

`rollback()` discards all uncommitted changes and returns the database
to the state it was in at the start of the current transaction.

```python
import sqlite3

def transfer_funds(account_from, account_to, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    try:
        # Operation 1: deduct from sender
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance - ? WHERE account_id = ?",
            (amount, account_from)
        )

        # Simulate a failure (e.g. network error, validation error)
        # raise Exception("Network error during transfer")

        # Operation 2: add to recipient
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance + ? WHERE account_id = ?",
            (amount, account_to)
        )

        conn.commit()   # Both succeeded — save permanently
        print(f"Transfer of £{amount:.2f} completed successfully.")

    except Exception as e:
        conn.rollback()  # Something went wrong — undo BOTH operations
        print(f"Transfer failed: {e}. No changes were made.")

    finally:
        conn.close()
```

**What happens without rollback?**

If `commit()` is never called (because an exception was raised and caught),
`sqlite3` will automatically roll back uncommitted changes when the connection
is closed. However, explicitly calling `rollback()` makes the intent clear
and is considered better practice.

---

### 9.4 Autocommit Mode

By default, `sqlite3` begins a transaction automatically before the first
`INSERT`/`UPDATE`/`DELETE` and keeps it open until you call `commit()` or `rollback()`.

`SELECT` statements do **not** require a transaction or a `commit()`.

You can change this with `isolation_level=None`:

```python
# Autocommit — every statement commits immediately, no transactions
conn = sqlite3.connect('library.db', isolation_level=None)
```

Autocommit is occasionally useful for administrative operations, but for
most application code the default transactional mode is safer and preferred.

---

## 10. Handling Database Errors

### 10.1 The `sqlite3` Exception Hierarchy

`sqlite3` uses a hierarchy of exception classes, all inheriting from
`sqlite3.Error`:

```
sqlite3.Error (base)
├── sqlite3.DatabaseError
│   ├── sqlite3.IntegrityError   — constraint violation (e.g. UNIQUE, NOT NULL)
│   ├── sqlite3.OperationalError — file locked, table not found, syntax error
│   ├── sqlite3.DataError        — invalid data for the column type
│   └── sqlite3.InternalError    — internal SQLite error (rare)
├── sqlite3.InterfaceError       — misuse of the DB-API interface
└── sqlite3.Warning              — non-fatal issue (rare)
```

The two you encounter most often:

- **`IntegrityError`** — you tried to violate a constraint (duplicate primary key,
  `NOT NULL` column left empty, `UNIQUE` column with a duplicate value).
- **`OperationalError`** — you tried to operate on a table that does not exist,
  or the file is locked by another process.

---

### 10.2 Wrapping Operations in `try / except`

The correct pattern for any database write operation:

```python
import sqlite3

def add_member(name, email, joined):
    """Add a new library member. Returns True on success, False if email is duplicate."""
    try:
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO members (name, email, joined) VALUES (?, ?, ?)",
                (name, email, joined)
            )
            # conn commits automatically when the 'with' block exits cleanly
        return True

    except sqlite3.IntegrityError:
        # Triggered by UNIQUE constraint on email
        print(f"Error: A member with email '{email}' already exists.")
        return False

    except sqlite3.OperationalError as e:
        # Triggered if the table doesn't exist, file is locked, etc.
        print(f"Database error: {e}")
        return False
```

**Testing the error handling:**

```python
add_member('Alice', 'alice@example.com', '2024-09-01')   # succeeds
add_member('Alicia', 'alice@example.com', '2024-09-01')  # IntegrityError — duplicate email
```

**Expected output:**
```
Error: A member with email 'alice@example.com' already exists.
```

---

### 10.3 Logging Errors

For production-quality code, print statements for errors should be replaced
with proper logging. Python's `logging` module is the standard approach:

```python
import sqlite3
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s  %(levelname)s  %(message)s'
)

def safe_insert(conn, name, gpa):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, gpa) VALUES (?, ?)",
            (name, gpa)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.rollback()
        logging.error("IntegrityError inserting student '%s': %s", name, e)
    except sqlite3.Error as e:
        conn.rollback()
        logging.error("Database error inserting student '%s': %s", name, e)
```

---

### 10.4 Re-raising and Custom Messages

Sometimes you want to catch a database error, log it, and then raise
a more meaningful exception for the caller:

```python
class DuplicateEmailError(Exception):
    """Raised when a member email already exists in the database."""

def register_member(conn, name, email, joined):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO members (name, email, joined) VALUES (?, ?, ?)",
            (name, email, joined)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        raise DuplicateEmailError(
            f"Registration failed: '{email}' is already registered."
        )
```

This pattern keeps database internals hidden from the rest of the
application — the calling code only sees a clean, meaningful exception.

---

## 11. Putting It All Together — Capstone Example

### A Library Management System

This example brings together every concept from the unit: table creation,
INSERT, SELECT, UPDATE, DELETE, transactions, and error handling.

```python
"""
library_system.py
A simple library management system using SQLite.
Demonstrates: connect, create table, CRUD, transactions, error handling.
"""

import sqlite3
from datetime import date

DB_FILE = 'library.db'


# ── Database setup ────────────────────────────────────────────────────────────

def initialise_database():
    """Create tables if they do not already exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                title     TEXT    NOT NULL,
                author    TEXT    NOT NULL,
                copies    INTEGER NOT NULL DEFAULT 1,
                available INTEGER NOT NULL DEFAULT 1
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name      TEXT    NOT NULL,
                email     TEXT    UNIQUE NOT NULL,
                joined    TEXT    NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                loan_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id     INTEGER NOT NULL,
                member_id   INTEGER NOT NULL,
                loan_date   TEXT    NOT NULL,
                return_date TEXT
            )
        """)

    print("Database initialised.")


# ── INSERT ────────────────────────────────────────────────────────────────────

def add_book(title, author, copies=1):
    """Add a new book to the library."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, copies, available) VALUES (?, ?, ?, ?)",
            (title, author, copies, copies)
        )
    print(f"Added: '{title}' by {author}.")


def register_member(name, email):
    """Register a new library member."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO members (name, email, joined) VALUES (?, ?, ?)",
                (name, email, str(date.today()))
            )
        print(f"Member registered: {name}.")
    except sqlite3.IntegrityError:
        print(f"Error: '{email}' is already registered.")


# ── READ ──────────────────────────────────────────────────────────────────────

def list_available_books():
    """Print all books currently available to borrow."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT book_id, title, author, available
            FROM books
            WHERE available > 0
            ORDER BY title
        """)
        books = cursor.fetchall()

    if not books:
        print("No books currently available.")
        return

    print("\nAvailable Books:")
    print(f"  {'ID':<5} {'Title':<35} {'Author':<25} {'Copies'}")
    print("  " + "-" * 72)
    for book_id, title, author, available in books:
        print(f"  {book_id:<5} {title:<35} {author:<25} {available}")


def search_books(keyword):
    """Search books by title or author (case-insensitive)."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT book_id, title, author, available
            FROM books
            WHERE title LIKE ? OR author LIKE ?
            ORDER BY title
            """,
            (f'%{keyword}%', f'%{keyword}%')
        )
        results = cursor.fetchall()

    if not results:
        print(f"No books found matching '{keyword}'.")
        return

    print(f"\nSearch results for '{keyword}':")
    for book_id, title, author, available in results:
        status = "Available" if available > 0 else "On Loan"
        print(f"  [{book_id}] {title} — {author}  ({status})")


# ── UPDATE (via transaction) ──────────────────────────────────────────────────

def borrow_book(member_id, book_id):
    """
    Loan a book to a member.
    Uses a transaction: both the availability update and loan record
    must succeed or neither is saved.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Check availability
        cursor.execute(
            "SELECT available FROM books WHERE book_id = ?",
            (book_id,)
        )
        row = cursor.fetchone()
        if row is None:
            print(f"Error: Book ID {book_id} does not exist.")
            return
        if row[0] == 0:
            print(f"Error: Book ID {book_id} is not currently available.")
            return

        # Operation 1: reduce available count
        cursor.execute(
            "UPDATE books SET available = available - 1 WHERE book_id = ?",
            (book_id,)
        )

        # Operation 2: create loan record
        cursor.execute(
            "INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?)",
            (book_id, member_id, str(date.today()))
        )

        conn.commit()  # Both operations succeeded
        print(f"Book {book_id} loaned to member {member_id}.")

    except sqlite3.Error as e:
        conn.rollback()  # Either operation failed — undo both
        print(f"Loan failed (database error): {e}")

    finally:
        conn.close()


# ── DELETE ────────────────────────────────────────────────────────────────────

def return_book(loan_id):
    """Mark a loan as returned and restore book availability."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Find the loan
        cursor.execute(
            "SELECT book_id FROM loans WHERE loan_id = ? AND return_date IS NULL",
            (loan_id,)
        )
        row = cursor.fetchone()
        if row is None:
            print(f"Error: Active loan ID {loan_id} not found.")
            return
        book_id = row[0]

        # Operation 1: record return date
        cursor.execute(
            "UPDATE loans SET return_date = ? WHERE loan_id = ?",
            (str(date.today()), loan_id)
        )

        # Operation 2: restore available count
        cursor.execute(
            "UPDATE books SET available = available + 1 WHERE book_id = ?",
            (book_id,)
        )

        conn.commit()
        print(f"Loan {loan_id} returned. Book {book_id} is now available.")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Return failed: {e}")

    finally:
        conn.close()


def remove_member(member_id):
    """Remove a member by ID."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM members WHERE member_id = ?",
            (member_id,)
        )
    print(f"Member {member_id} removed. Rows deleted: {cursor.rowcount}")


# ── Main demo ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    initialise_database()

    # Add books
    add_book('Clean Code', 'Robert C. Martin', copies=2)
    add_book('The Pragmatic Programmer', 'David Thomas', copies=1)
    add_book('Python Tricks', 'Dan Bader', copies=3)

    # Register members
    register_member('Alice', 'alice@example.com')
    register_member('Bob', 'bob@example.com')
    register_member('Alice', 'alice@example.com')   # duplicate — should fail

    # List available books
    list_available_books()

    # Borrow and return
    borrow_book(member_id=1, book_id=1)
    borrow_book(member_id=2, book_id=1)
    list_available_books()

    return_book(loan_id=1)
    list_available_books()

    # Search
    search_books('Python')
```

**Expected output:**
```
Database initialised.
Added: 'Clean Code' by Robert C. Martin.
Added: 'The Pragmatic Programmer' by David Thomas.
Added: 'Python Tricks' by Dan Bader.
Member registered: Alice.
Member registered: Bob.
Error: 'alice@example.com' is already registered.

Available Books:
  ID    Title                               Author                    Copies
  ------------------------------------------------------------------------
  1     Clean Code                          Robert C. Martin          2
  3     Python Tricks                       Dan Bader                 3
  2     The Pragmatic Programmer            David Thomas              1

Book 1 loaned to member 1.
Book 1 loaned to member 2.

Available Books:
  ID    Title                               Author                    Copies
  ------------------------------------------------------------------------
  2     The Pragmatic Programmer            David Thomas              1
  3     Python Tricks                       Dan Bader                 3

Loan 1 returned. Book 1 is now available.

Available Books:
  ID    Title                               Author                    Copies
  ------------------------------------------------------------------------
  1     Clean Code                          Robert C. Martin          1
  2     The Pragmatic Programmer            David Thomas              1
  3     Python Tricks                       Dan Bader                 3

Search results for 'Python':
  [3] Python Tricks — Dan Bader  (Available)
```

---

## 12. Common Mistakes to Avoid

### Mistake 1 — String concatenation instead of parameterised queries

```python
# ❌ SQL injection vulnerability
name = input("Name: ")
cursor.execute("SELECT * FROM students WHERE name = '" + name + "'")

# ✅ Always use placeholders
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
```

---

### Mistake 2 — Forgetting to commit

```python
# ❌ Changes exist in memory but are never saved to disk
cursor.execute("INSERT INTO students (name, gpa) VALUES (?, ?)", ('Alice', 3.8))
conn.close()   # data lost!

# ✅ Always commit before closing
cursor.execute("INSERT INTO students (name, gpa) VALUES (?, ?)", ('Alice', 3.8))
conn.commit()
conn.close()
```

---

### Mistake 3 — Missing WHERE on UPDATE or DELETE

```python
# ❌ Updates EVERY student's GPA to 0.0
cursor.execute("UPDATE students SET gpa = 0.0")

# ✅ Target a specific row
cursor.execute("UPDATE students SET gpa = 0.0 WHERE id = ?", (2,))
```

---

### Mistake 4 — Single-element tuple missing the trailing comma

```python
# ❌ Passes the string 'Alice' as the parameter sequence (TypeError)
cursor.execute("SELECT * FROM students WHERE name = ?", ('Alice'))

# ✅ Trailing comma makes it a tuple
cursor.execute("SELECT * FROM students WHERE name = ?", ('Alice',))
```

---

### Mistake 5 — Calling `fetchall()` on a table with millions of rows

```python
# ❌ Loads everything into memory — crashes on large tables
cursor.execute("SELECT * FROM logs")
all_rows = cursor.fetchall()   # 10 million rows → memory error

# ✅ Iterate the cursor directly — processes one row at a time
cursor.execute("SELECT * FROM logs")
for row in cursor:
    process(row)
```

---

### Mistake 6 — Not closing the connection / not using context manager

```python
# ❌ If an exception occurs before conn.close(), the file stays locked
conn = sqlite3.connect('library.db')
cursor.execute("...")
conn.close()

# ✅ Context manager guarantees closure
with sqlite3.connect('library.db') as conn:
    cursor.execute("...")
```

---

### Mistake 7 — Assuming `rowcount` is reliable after SELECT

```python
# ❌ rowcount is -1 or undefined after SELECT — don't rely on it
cursor.execute("SELECT * FROM students WHERE gpa > 3.5")
print(cursor.rowcount)   # -1 — meaningless

# ✅ Use len(fetchall()) or COUNT(*)
results = cursor.fetchall()
print(len(results))
```

---

### Mistake 8 — Re-using a cursor across threads

A `cursor` is **not thread-safe**. Do not share a cursor (or connection)
between threads. Create a new connection per thread:

```python
# ✅ Each thread creates its own connection
import threading

def worker():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ...")
```

---

## 13. Summary and Key Takeaways

### Key Concepts

| Concept | Summary |
|---|---|
| **Database** | Organised, persistent storage — more powerful than files for structured data |
| **SQLite** | A file-based SQL database built into Python — no server required |
| **Connection** | Open channel to the database file (`sqlite3.connect()`) |
| **Cursor** | Executes SQL statements and holds query results |
| **`CREATE TABLE`** | Defines a table's columns and their types/constraints |
| **`INSERT INTO`** | Adds a new row — always use `?` placeholders |
| **`SELECT`** | Queries rows — filter with `WHERE`, sort with `ORDER BY` |
| **`UPDATE`** | Modifies existing rows — **always include `WHERE`** |
| **`DELETE FROM`** | Removes rows — **always include `WHERE`** |
| **`commit()`** | Saves changes permanently to disk |
| **`rollback()`** | Undoes all uncommitted changes |
| **Transaction** | A group of operations that succeed or fail together (ACID) |
| **Parameterised query** | `?` placeholders — prevents SQL injection |
| **Context manager** | `with sqlite3.connect(...)` — guarantees the connection closes |

---

### The CRUD Pattern

Every database-backed application follows **CRUD**:

| Letter | Operation | SQL Command |
|---|---|---|
| **C** | Create | `INSERT INTO` |
| **R** | Read | `SELECT` |
| **U** | Update | `UPDATE` |
| **D** | Delete | `DELETE FROM` |

---

### The Three Rules of Safe Database Programming

1. **Always parameterise.** Never concatenate user input into SQL strings.
2. **Always commit** (or use the context manager that does it for you).
3. **Always `WHERE`** in `UPDATE` and `DELETE` unless you genuinely mean every row.

---

### Best Practices Checklist

- [ ] Use `CREATE TABLE IF NOT EXISTS` so startup code is idempotent
- [ ] Use `with sqlite3.connect(...)` for guaranteed connection cleanup
- [ ] Use `?` placeholders for all variable values in queries
- [ ] Wrap multi-step write operations in a transaction with `commit/rollback`
- [ ] Check `cursor.rowcount` after `UPDATE`/`DELETE` to verify rows were affected
- [ ] Test `WHERE` clauses with a `SELECT` before running `UPDATE` or `DELETE`
- [ ] Store dates as `TEXT` in `YYYY-MM-DD` format for correct sorting
- [ ] Close connections promptly — do not leave connections open indefinitely
- [ ] Use `fetchone()` when you expect exactly one result, not `fetchall()[0]`
- [ ] Handle `IntegrityError` for unique/not-null constraint violations

---

## 14. Glossary

| Term | Definition |
|---|---|
| **Database** | An organised collection of structured data stored electronically |
| **Relational database** | A database that organises data into tables with rows and columns |
| **SQLite** | A file-based, serverless relational database built into Python |
| **SQL** | Structured Query Language — the standard language for querying databases |
| **Table** | A collection of rows with a fixed set of typed columns |
| **Row / Record** | A single entry in a table |
| **Column / Field** | A named, typed attribute shared by all rows in a table |
| **Primary key** | A column (or combination) that uniquely identifies each row |
| **AUTOINCREMENT** | Automatically assigns the next integer as the primary key |
| **Constraint** | A rule enforced by the database (NOT NULL, UNIQUE, CHECK, etc.) |
| **Connection** | An open channel between Python and the database file |
| **Cursor** | An object that executes SQL statements and retrieves results |
| **`execute()`** | Runs a single SQL statement |
| **`executemany()`** | Runs the same SQL statement for each item in a list |
| **Parameterised query** | A SQL query using `?` placeholders to safely inject values |
| **SQL injection** | An attack where malicious SQL is injected via unsanitised input |
| **Transaction** | A group of operations treated as a single atomic unit |
| **`commit()`** | Saves all pending changes permanently to disk |
| **`rollback()`** | Cancels all pending changes since the last commit |
| **ACID** | Atomicity, Consistency, Isolation, Durability — transaction properties |
| **CRUD** | Create, Read, Update, Delete — the four fundamental data operations |
| **`fetchone()`** | Retrieves the next single row from a query result |
| **`fetchall()`** | Retrieves all remaining rows from a query result |
| **`rowcount`** | Number of rows affected by the last `INSERT`/`UPDATE`/`DELETE` |
| **`lastrowid`** | The primary key of the most recently inserted row |
| **`IntegrityError`** | Raised when a database constraint is violated |
| **`OperationalError`** | Raised for file errors, syntax errors, or missing tables |
| **Context manager** | A `with` block that ensures cleanup (closing) happens automatically |

---

*BT151CO — Object-Oriented Programming · Unit 6 
