# Unit 01 - Questions

**Short Questions (2 Marks)**

- Define a syntax error and give an example from the notes.
- What is a runtime exception and how does it differ from a syntax error?
- List four common built-in exceptions in Python as shown in the notes.
- Explain what a logical error is and why it is harder to detect than other errors.
- State the basic syntax of a try/except block.
- Explain the purpose of the else clause in exception handling.
- What is the purpose of the finally clause?
- Why is catching a bare except: considered bad practice?
- Define a custom exception and explain its purpose.
- What does it mean to "raise" an exception?
- List the six file modes discussed in the notes.
- Explain the difference between text mode and binary mode in file operations.
- What is the difference between .read(), .readline(), and .readlines()?
- Explain what the with statement does in file operations.
- State the dangers of using mode "w" when opening a file.
- What is a FileNotFoundError and in which mode does it occur?
- What does .write() do and how does it differ from .writelines()?
- Explain the difference between append mode ("a") and write mode ("w").
- Why should you always specify encoding="utf-8" when opening a file?
- What is the difference between handling multiple exceptions with separate except blocks versus combining them in a tuple?

**Medium Questions (5 Marks)**

- Explain the complete structure of try/except/else/finally and describe when each clause runs.
- Discuss custom exceptions as shown in the notes. Explain how to create one, why they are useful, and how to add custom attributes.
- Explain how to build an exception hierarchy with a base exception and specific subclasses.
- Describe the three ways to read a file and explain when each is most appropriate.
- Explain writing and appending to files. Use examples from the notes to show the difference.
- Discuss file exceptions and how to handle them. Include common exceptions and recommended strategies.
- Explain the advantages of the with statement and show how it compares to manual file closing.
- Discuss how to handle multiple exceptions in Python, including both separate blocks and tuple grouping.
- Explain the concept of "raising exceptions intentionally" using an example from the notes.
- Describe how to safely use print() to write to files and explain when this approach is useful.
- Explain exception handling in the context of file operations and show a comprehensive example.
- Discuss the golden rules for exception handling and file I/O as listed in the notes.

**Long Questions (10 Marks)**

- Explain all three types of errors in Python (syntax, runtime, logical) using examples from the notes. Discuss how each is detected and prevented.
- Discuss custom exceptions in depth. Explain why they are useful, how to create them, how to add attributes, and how to build a hierarchy.
- Analyze the complete file handling workflow in Python. Discuss the three ways to read files, the two ways to write, the use of modes, and how the with statement ensures safety.
- Write a comprehensive analysis of exception handling in file operations. Include handling multiple file-specific exceptions, using finally for cleanup, and combining try/except with the with statement.
- Compare and contrast the three core features of this unit: exception types, exception handling, and file I/O. Show how they work together.
- Explain how to design a robust file handling application using all the concepts from Unit 3. Include error handling, multiple file operations, and best practices.
- Analyze the relationship between exception handling and the design of custom exceptions. Show how this connects to Unit 2 concepts of inheritance and OOP.
- Create a detailed summary of Unit 3 that explains how exception handling and file I/O work together as professional practices. Include golden rules, connections to previous units, and real-world applications.