# Unit 6: Questions

1. What is a relational database and how does it differ from plain text files?
2. Explain the roles of tables, rows, columns, primary keys, and foreign keys in a relational database.
3. Why is SQLite a good choice for teaching database access in Python?
4. What are the five most common SQL commands used in this unit?
5. How do you connect to a SQLite database file using Python?
6. What is the purpose of `conn.cursor()` in `sqlite3`?
7. Why should you use parameterised queries with `?` placeholders?
8. What is SQL injection and how do parameterised queries prevent it?
9. Why must a single-element tuple include a trailing comma in Python database code?
10. What does `cursor.lastrowid` return after an `INSERT`?
11. What are the main SQLite data types and when should each be used?
12. How do `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` constraints work?
13. What is the benefit of `CREATE TABLE IF NOT EXISTS`?
14. How do you insert multiple rows efficiently in one call?
15. What is the difference between `fetchone()`, `fetchmany(n)`, and `fetchall()`?
16. How do you filter query results with `WHERE` and sort them with `ORDER BY`?
17. What is the purpose of `LIMIT` in a `SELECT` query?
18. When should you use `COUNT(*)`, `AVG()`, `SUM()`, `MAX()`, and `MIN()`?
19. Why is it dangerous to run `UPDATE` or `DELETE` without a `WHERE` clause?
20. How does `cursor.rowcount` help after an `UPDATE` or `DELETE`?
21. What does `conn.commit()` do and why is it necessary?
22. What does `conn.rollback()` do and when should you use it?
23. How does the `with sqlite3.connect(...) as conn:` context manager improve safety?
24. What are ACID properties and why are they important for transactions?
25. Give an example of a multi-step transaction and explain why it must be atomic.
26. What is `sqlite3.IntegrityError` and when is it raised?
27. What is `sqlite3.OperationalError` and when is it raised?
28. Why should database helper functions return status flags instead of raw exceptions?
29. What is the purpose of a seed or setup function in database examples?
30. How can a library management system use related tables and joins to avoid data duplication?