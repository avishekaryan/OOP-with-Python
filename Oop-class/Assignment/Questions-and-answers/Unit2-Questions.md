# Unit 2 — Object-Oriented Programming

## Short Questions

1. Define a class in Python and state its purpose in object-oriented programming.
2. Explain the difference between a class and an object with reference to the notes.
3. State the four pillars of object-oriented programming.
4. Define encapsulation as explained in the notes.
5. Define inheritance with an example from the notebook.
6. Define polymorphism as given in the notes.
7. Explain the role of `__init__` and `self` in a class.
8. Differentiate between instance variables and class variables.
9. Describe the purpose of `__str__` in Python classes.
10. State the purpose of `__len__`, `__contains__`, and `__eq__` in custom classes.
11. Explain the purpose of `super()` in inheritance.
12. State the use of `isinstance()` in Python.
13. Define a custom exception hierarchy as explained in the notes.
14. Describe the purpose of `try`, `except`, `else`, and `finally`.
15. Explain the iterator protocol in Python.
16. Define a generator function and explain the role of `yield`.
17. Differentiate between `*args` and `**kwargs`.
18. State the LEGB rule in Python scope resolution.
19. Define a module and a package as described in the notes.
20. Explain the purpose of the `if __name__ == "__main__":` guard.

## Medium Questions

1. Compare procedural programming and object-oriented programming as presented in the notes. Why was OOP considered a better solution?
2. Explain the four pillars of OOP with examples from the notes.
3. Describe the use of `__init__`, `self`, instance variables, and class variables in the `BankAccount` example.
4. Discuss the role of special methods or dunder methods in custom classes. Use the `LibraryBook` and `ShoppingCart` examples.
5. Explain inheritance in the `BankAccount` hierarchy. Include the meaning of `super()`, method overriding, and `isinstance()`.
6. Discuss method resolution order (MRO) and explain the diamond structure example using `A`, `B`, `C`, and `D`. Explain with an example.
7. Explain polymorphism and duck typing using the notes’ `GameCharacter` and report examples. Explain with an example.
8. Explain how custom exception classes are created and used in the bank example. Why do the notes recommend inheriting from `Exception` rather than `BaseException`?
9. Describe the `try` / `except` / `else` / `finally` structure and explain its importance in the `safe_transaction()` function. Explain with an example.
10. Explain the iterator protocol using the `CountDown` and `StudentRoster` examples. How does it relate to the `for` loop? Explain with an example.
11. Explain generator functions with `yield`, and compare them with lists using the examples in the notes.  Explain with an example.
12. Discuss `*args`, `**kwargs`, the LEGB scope rule, and module imports using the notebook examples. Explain with an example.

## Long Questions

1. Discuss how object-oriented programming solves the problem of procedural code. Explain how the `Student` example bundles data and behaviour and show how the four pillars of OOP are reflected in the unit.
2. Explain inheritance in depth using the `BankAccount`, `SavingsAccount`, and `LoanAccount` examples. Discuss `super()`, method overriding, and inheritance checks. Explain with an example.
3. Analyze polymorphism using the `GameCharacter` hierarchy and contrast it with duck typing using the report example. Discuss how operator overloading is also implemented in the notes.
4. Evaluate the custom exception design in the bank system and explain how `try`, `except`, and custom classes work together to produce clear error handling. Explain with an example.
5. Discuss the iterator protocol and generator functions in Python as explained in the notes. Explain how they differ from ordinary lists and why they are useful. Explain with an example.
6. Explain the `*args`, `**kwargs`, and LEGB scope rules with examples from the notes. Discuss how closures and the `nonlocal` keyword affect variable access.
7. Describe the role of modules, packages, and imports in Python as explained in the notes. Explain why the `__name__ == "__main__"` guard is important.
8. Write a comprehensive discussion of the complete Unit 2 content by integrating classes, instance variables, inheritance, dunder methods, exceptions, iterators, generators, scope, and modules in a single coherent explanation.