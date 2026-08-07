# SQLite vs. MySQL: Important Differences for Python Beginners

If you're learning databases with Python, you'll most likely start with **SQLite** because it's built into Python through the `sqlite3` module. Later, you may work with databases like **MySQL**.

Although SQLite and MySQL both use SQL, there are several important differences. Understanding them early will help you avoid confusion when you switch from SQLite to a server-based database.

---

## Quick Comparison

| Feature | SQLite | MySQL |
|---------|---------|--------|
| String type | `TEXT` (preferred) | `VARCHAR(n)` is common |
| Length limit | `VARCHAR(n)` is **not enforced** | `VARCHAR(n)` is enforced |
| Auto increment | `INTEGER PRIMARY KEY AUTOINCREMENT` | `AUTO_INCREMENT` |
| Boolean | No separate `BOOLEAN` type (`0` and `1`) | `BOOLEAN` (`TINYINT(1)` internally) |
| Date/Time | Store as `TEXT`, `INTEGER`, or `REAL` | Native `DATE`, `TIME`, `DATETIME`, `TIMESTAMP` |
| Type checking | Flexible | Much stricter |
| Database | Embedded | Client-server |

---

# 1. TEXT vs. VARCHAR(n)

One of the biggest surprises for beginners is that SQLite treats `TEXT` and `VARCHAR(n)` almost the same.

For example:

```sql
CREATE TABLE students (
    name VARCHAR(20)
);
```

You might expect SQLite to reject names longer than 20 characters.

It doesn't.

```sql
INSERT INTO students
VALUES ('Christopher Johnson');
```

This works even though the name exceeds 20 characters.

SQLite ignores the `(20)` part because it uses a flexible type system.

Instead, most SQLite developers simply write:

```sql
name TEXT
```

### If you need a maximum length

Use a `CHECK` constraint instead.

```sql
CREATE TABLE students (
    name TEXT,
    CHECK(length(name) <= 20)
);
```

Now SQLite will reject longer names.

---

# 2. SQLite Uses Flexible Typing

Unlike MySQL, SQLite does not strictly enforce data types.

For example:

```sql
CREATE TABLE demo (
    age INTEGER
);

INSERT INTO demo VALUES ('25');
INSERT INTO demo VALUES (25);
```

Both statements work.

SQLite automatically converts values when possible.

MySQL is generally much stricter and may reject invalid values depending on its SQL mode.

---

# 3. Dates Are Stored Differently

SQLite does not have a dedicated `DATE` data type.

Instead, dates are commonly stored as text.

```sql
birth_date TEXT
```

Store dates using the ISO format:

```text
2026-07-28
```

This format has two advantages:

- It is easy for humans to read.
- It sorts correctly as a string.

For example:

```sql
ORDER BY birth_date
```

correctly sorts the dates from oldest to newest.

### MySQL

MySQL has native date types:

```sql
birth_date DATE
```

It also supports:

- `TIME`
- `DATETIME`
- `TIMESTAMP`

---

# 4. Auto-Increment Columns

SQLite uses:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

MySQL uses:

```sql
id INT AUTO_INCREMENT PRIMARY KEY
```

Although the syntax differs, both automatically generate unique IDs.

---

# 5. Boolean Values

SQLite has no dedicated Boolean type.

Instead, use integers.

```sql
is_admin INTEGER
```

Convention:

- `0` = False
- `1` = True

MySQL allows:

```sql
is_admin BOOLEAN
```

Internally, MySQL stores this as `TINYINT(1)`.

---

# 6. Foreign Keys

SQLite supports foreign keys, but they are **disabled by default**.

Always enable them after connecting to the database.

```python
cursor.execute("PRAGMA foreign_keys = ON")
```

Without this statement, SQLite will not enforce foreign key constraints.

MySQL enables foreign key enforcement by default (when using a storage engine such as InnoDB).

---

# 7. Type Affinity

SQLite doesn't enforce strict column types.

For example:

```sql
CREATE TABLE products (
    price REAL
);
```

SQLite will even accept:

```sql
INSERT INTO products VALUES ('19.99');
```

It converts the value automatically when possible.

MySQL is much stricter about the values that can be stored in each column.

---

# 8. SQLite Doesn't Need a Database Server

SQLite is an embedded database.

Your entire database lives in a single file.

```
library.db
```

or even entirely in memory:

```python
sqlite3.connect(":memory:")
```

No installation or server setup is required.

MySQL, however, runs as a database server.

Applications connect to it over a network or through a local server process.

---

# Key Takeaways

If you're using Python's `sqlite3` module, remember these differences:

- Prefer `TEXT` over `VARCHAR(n)`.
- SQLite does **not** enforce the length of `VARCHAR(n)`.
- Store dates as `TEXT` using the `YYYY-MM-DD` format.
- Use `INTEGER PRIMARY KEY AUTOINCREMENT` for auto-incrementing IDs.
- Represent Boolean values with `0` and `1`.
- Enable foreign keys using `PRAGMA foreign_keys = ON`.
- SQLite uses flexible typing, while MySQL is generally much stricter.

SQLite is intentionally lightweight and easy to use, making it an excellent database for learning SQL and building small to medium-sized applications. Once you're comfortable with SQLite, transitioning to MySQL is much easier because the core SQL concepts remain the same.
