# Unit 06 — SQL Exercise Test Bank
## BT151CO · Object-Oriented Programming

This file contains step-by-step SQL exercises based on Unit 06.  
Students should complete the SQL questions first using standard SQL syntax.  
After each question, they should convert the same logic to Python using the `sqlite3` module.

---

# Part A — Questions

## Exercise 1 — Create a Table
Write the SQL statement to create a table called `students` with the following columns:

- `student_id` — integer primary key
- `name` — text, not null
- `gpa` — decimal number, default `0.0`
- `enrolled_on` — date

Write the statement in standard SQL.

SQLite conversion task:
- Write the equivalent Python `sqlite3` code to create the same table.

---

## Exercise 2 — Insert Data
Insert the following 4 students into the `students` table:

- `Alice`, GPA `3.8`, enrolled on `2024-09-01`
- `Bob`, GPA `2.9`, enrolled on `2024-09-01`
- `Charlie`, GPA `3.5`, enrolled on `2024-09-01`
- `Diana`, GPA `3.7`, enrolled on `2024-09-01`

Write the SQL insert statements.

SQLite conversion task:
- Write the equivalent Python `sqlite3` code using parameterised queries.

---

## Exercise 3 — Read All Rows
Write a SQL query to display all rows from the `students` table.

SQLite conversion task:
- Write the Python code to fetch and print all rows.

---

## Exercise 4 — Filter with WHERE
Write a SQL query to display all students whose GPA is greater than `3.5`.

SQLite conversion task:
- Write the equivalent Python code using a parameterised query.

---

## Exercise 5 — Sort and Limit
Write a SQL query to display the top 3 students by GPA in descending order.

SQLite conversion task:
- Write the equivalent Python code.

---

## Exercise 6 — Aggregate Functions
Write SQL queries to answer the following:

1. Count how many students exist.
2. Find the average GPA.
3. Find the highest GPA.

SQLite conversion task:
- Write the Python code to calculate the same values.

---

## Exercise 7 — Update Records
Update Alice’s GPA to `3.95`.

Write the SQL statement that changes only Alice’s record.

SQLite conversion task:
- Write the equivalent Python code using `UPDATE ... WHERE ...`.

---

## Exercise 8 — Delete Records
Delete the student with the name `Bob`.

Write the SQL statement.

SQLite conversion task:
- Write the equivalent Python code using `DELETE FROM ... WHERE ...`.

---

## Exercise 9 — Transaction Control
Create a simple bank-style example:

- Table: `accounts`
  - `account_id` integer primary key
  - `owner_name` text not null
  - `balance` decimal not null

Insert two accounts:

- Account 1: `Alice`, balance `500.00`
- Account 2: `Bob`, balance `300.00`

Write the SQL statements needed to transfer `100.00` from Alice to Bob.

Your answer should show:
- the `UPDATE` for deduction
- the `UPDATE` for addition
- the transaction logic using `BEGIN`, `COMMIT`, and `ROLLBACK`

SQLite conversion task:
- Write the equivalent Python `sqlite3` code using a transaction.

---

## Exercise 10 — Constraints
Create a table called `members` with the following columns:

- `member_id` — integer primary key
- `name` — text not null
- `email` — text not null and unique

Then write the SQL statements to insert:

- `Alice`, `alice@example.com`
- `Alicia`, `alice@example.com`

Explain what should happen on the second insert.

SQLite conversion task:
- Write the Python code that would catch the duplicate email error.

---

## Exercise 11 — Multi-Table Design
Create a small library database with three tables:

- `books`
  - `book_id` primary key
  - `title` not null
  - `author` not null
  - `copies` default `1`
- `members`
  - `member_id` primary key
  - `name` not null
  - `email` unique and not null
- `loans`
  - `loan_id` primary key
  - `book_id` foreign key reference
  - `member_id` foreign key reference
  - `loan_date` not null
  - `return_date` nullable

Write the SQL statements to create these tables.

SQLite conversion task:
- Write the Python `sqlite3` code that creates the same tables.

---

## Exercise 12 — Capstone Exercise
A library wants to manage books and members.

Write the SQL statements needed to:

1. Create the `books` table.
2. Insert 3 books:
   - `Clean Code` by `Robert C. Martin`
   - `The Pragmatic Programmer` by `David Thomas`
   - `Python Tricks` by `Dan Bader`
3. Insert 2 members:
   - `Alice`
   - `Bob`
4. Find all books by `Dan Bader`.
5. Update the availability of a book after it is borrowed.
6. Delete a member who has been removed from the system.

SQLite conversion task:
- Write the equivalent Python `sqlite3` program that performs the same actions.

---