# Unit 08: Regex, Threads, and Django

## Short Questions — 20

1. Define a regular expression.
2. State the purpose of using raw strings in Python regular expressions.
3. List the meanings of the regex symbols `\d`, `\w`, and `\s`.
4. Explain the role of quantifiers in regular expressions.
5. Differentiate between `re.match()` and `re.search()`.
6. State what `re.sub()` returns.
7. Define a Django model.
8. State the role of the ORM in Django.
9. List the four main components of Django’s MVT architecture.
10. Explain the purpose of URL routing in Django.
11. Define a thread.
12. State one reason why threads are useful for I/O-bound tasks.
13. Explain what a race condition is.
14. State the function of a Lock in thread programming.
15. Describe the three-step pattern for using threads.
16. State the purpose of `thread.join()`.
17. Define a template variable in Django.
18. List two template syntax forms described in the notes.
19. State the role of a view in Django.
20. Explain the purpose of a template in Django.

---

## Medium Questions — 12

1. Explain how character classes and boundaries are used in regular expressions.
2. Describe how `re.findall()` can be used to extract phone numbers and student records from text.
3. Compare `re.match()`, `re.search()`, and `re.findall()` with reference to their outputs.
4. Discuss the importance of non-greedy matching in regular expressions.
5. Explain the request flow in Django from a browser request to a rendered webpage.
6. Describe how a Django model maps to a database table and how ORM queries work.
7. Compare the roles of Model, View, Template, and URL configuration in Django’s MVT architecture.
8. Discuss the difference between a process and a thread as described in the notes.
9. Explain why shared data must be protected when multiple threads run concurrently.
10. Describe the use of a Lock, Semaphore, and Event in thread-based programs.
11. Illustrate how a threaded search can be implemented using threads and a shared results list.
12. Evaluate the relevance of Django to the earlier units in this course.

---

## Long Questions — 8

1. Discuss the main regex concepts from the notes, including raw strings, character classes, predefined classes, quantifiers, boundaries, and regex functions such as match, search, findall, and sub.
2. Explain the debugging exercises in the notes and show how each bug is corrected.
3. Discuss threads in detail, including process versus thread, shared memory, the GIL, I/O-bound work, race conditions, locks, joins, semaphores, events, and silent thread exceptions.
4. Explain the Django MVT architecture with reference to models, views, templates, and URL configuration, and describe a complete request cycle.
5. Compare Django’s model, ORM, view, template, and URL routing with the concepts introduced in earlier units as described in the notes.
6. Illustrate how regex can be used to solve the practice tasks on phone number extraction, student record parsing, password checking, and log analysis using patterns from the notes.
7. Describe how a multi-threaded word frequency counter or library search can be implemented using threads and a Lock, and explain why the Lock is necessary.
8. Evaluate the significance of the unit summary and checklist themes: regex, threads, and Django, and explain how the topics connect to one another in the course.