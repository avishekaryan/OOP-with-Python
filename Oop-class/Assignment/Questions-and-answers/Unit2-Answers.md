# Unit 2 — Object-Oriented Programming

## Short Questions (2 Marks)

### Q1. Define a class in Python and state its purpose in object-oriented programming.

- Think of a class like a cookie cutter — it is not a cookie itself, just the shape used to make cookies. In code, a class is a blueprint that defines what data and behaviour every object made from it will have.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

### Q2. Explain the difference between a class and an object with reference to the notes.

- The class is the cookie cutter (the shape); the object is an actual cookie made using it. `Student` is the class; `avhi = Student("Avhi")` is one real object with real data.

```python
class Student:          # the cutter (blueprint)
    def __init__(self, name):
        self.name = name
avhi = Student("Avhi")   # the cookie (real object)
```

---

### Q3. State the four pillars of object-oriented programming.

- Encapsulation (keep data and its methods together, hide the messy details), Inheritance (reuse another class instead of rewriting it), Polymorphism (same action word, different result depending on who does it), and Abstraction (show a simple button, hide the complicated wiring behind it).

---

### Q4. Define encapsulation as explained in the notes.

- Encapsulation just means locking an object's data inside it and only allowing it to be changed through the object's own methods — like a vending machine where you press buttons instead of reaching inside to grab items directly.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # hidden inside, changed only via methods
    def get_balance(self):
        return self._balance
```

---

### Q5. Define inheritance with an example from the notebook.

- Inheritance is like a child inheriting traits from a parent — a new class gets everything an existing class already has, for free, and can then add its own extra bits.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):   # "child" of BankAccount
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
```

---

### Q6. Define polymorphism as given in the notes.

- Polymorphism just means "same word, different result" — calling `.attack()` on a Warrior and a Mage does two completely different things, even though you typed the exact same instruction.

---

### Q7. Explain the role of `__init__` and `self` in a class.

- `__init__` is the setup step that runs automatically the moment an object is created — like filling out a form the instant you walk in the door. `self` simply means "this particular object," so each object keeps its own separate data.

```python
class Student:
    def __init__(self, name):   # runs automatically
        self.name = name         # self = this one student
```

---

### Q8. Differentiate between instance variables and class variables.

- An instance variable is personal to one object — every student has their own name. A class variable is shared by everyone made from that class — every student in the same school shares the same school name.

```python
class BankAccount:
    bank_name = "National Bank"   # shared by everyone
    def __init__(self, balance):
        self.balance = balance      # personal to each account
```

---

### Q9. Describe the purpose of `__str__` in Python classes.

- `__str__` decides what gets shown when you print an object — without it, `print(obj)` shows an ugly, unhelpful default instead of something readable.

```python
class Student:
    def __init__(self, name): self.name = name
    def __str__(self): return f"Student: {self.name}"
print(Student("Avhi"))   # Student: Avhi
```

---

### Q10. State the purpose of `__len__`, `__contains__`, and `__eq__` in custom classes.

- `__len__` makes `len(obj)` work on your own object. `__contains__` makes `"apple" in cart` work. `__eq__` decides what counts as "equal" when comparing two objects with `==`, instead of Python's default (which just checks if they're literally the same object in memory).

---

### Q11. Explain the purpose of `super()` in inheritance.

- `super()` is how a child class says "first, do whatever the parent already does" — most often used inside `__init__` so the setup code does not have to be copy-pasted from the parent class.

```python
class SavingsAccount(BankAccount):
    def __init__(self, balance, rate):
        super().__init__(balance)   # let the parent handle this part
        self.rate = rate
```

---

### Q12. State the use of `isinstance()` in Python.

- `isinstance(obj, ClassName)` simply asks "is this object one of these?" and returns `True`/`False` — a `SavingsAccount` still counts as a `BankAccount`, since it's built from it.

```python
acc = SavingsAccount(1000, 0.05)
print(isinstance(acc, BankAccount))   # True
```

---

### Q13. Define a custom exception hierarchy as explained in the notes.

- This is just a family tree of error types — a general `BankError` at the top, with more specific errors like `InsufficientFundsError` below it. Code can catch one specific error, or catch the whole family at once through the parent.

```python
class BankError(Exception): pass
class InsufficientFundsError(BankError): pass
```

---

### Q14. Describe the purpose of `try`, `except`, `else`, and `finally`.

- `try`: attempt something that might go wrong. `except`: what to do if it does go wrong. `else`: what to do only if nothing went wrong. `finally`: runs no matter what — success, failure, doesn't matter — usually used for cleanup.

---

### Q15. Explain the iterator protocol in Python.

- An object follows the iterator protocol if it has `__iter__()` ("here I am, ready to be looped over") and `__next__()` ("here's the next value" — or "I'm done" via `StopIteration`). This is exactly what lets a custom object be used in a `for` loop.

```python
class CountDown:
    def __init__(self, start): self.n = start
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
```

---

### Q16. Define a generator function and explain the role of `yield`.

- A generator is a function that hands out values one at a time, pausing in between, instead of building the whole list up front. `yield` is what pauses it and hands back the next value.

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1
for i in count_down(3):   # 3, 2, 1
    print(i)
```

---

### Q17. Differentiate between `*args` and `**kwargs`.

- `*args` scoops up any extra plain arguments into a tuple. `**kwargs` scoops up any extra `name=value` arguments into a dictionary. Both exist so a function can accept "however many arguments you want to give me."

```python
def demo(*args, **kwargs):
    print(args, kwargs)
demo(1, 2, name="Avhi")   # (1, 2) {'name': 'Avhi'}
```

---

### Q18. State the LEGB rule in Python scope resolution.

```
LEGB is just the order Python checks when looking for a variable name: Local (right here) → Enclosing (the function wrapped around this one) → Global (the whole file) → Built-in (Python's own words like `print`). It stops at the first place it finds a match.
```

---

### Q19. Define a module and a package as described in the notes.

- A module is just one `.py` file you can `import` elsewhere. A package is a folder full of related modules (with an `__init__.py` file) grouped together under one name.

---

### Q20. Explain the purpose of the `if __name__ == "__main__":` guard.

- This is a simple check: "was this file run directly, or was it just imported by another file?" Code inside the guard only runs when the file itself is the one being run.

```python
def main():
    print("Running directly")
if __name__ == "__main__":
    main()
```

---

## Medium Questions (6 Marks)

### Q1. Compare procedural programming and object-oriented programming as presented in the notes. Why was OOP considered a better solution?

- Procedural code keeps your data and the functions that use it as two separate piles — like a filing cabinet in one room and the person who knows how to use the files in another room. It works fine for a small script, but gets messy fast as things grow.

```python
# procedural style - data and logic live apart
student_name = "Avhi"
student_marks = [78, 91]
def print_report(name, marks):
    print(name, sum(marks)/len(marks))
```

- OOP instead puts the data and the logic that uses it in the same box — a class. Nothing gets separated or lost track of.

```python
class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks
    def average(self):
        return sum(self.marks) / len(self.marks)
```

- OOP wins for bigger programs for two simple reasons: everything related stays together in one place, and inheritance means you can reuse a class instead of retyping it for every similar case.

---

### Q2. Explain the four pillars of OOP with examples from the notes.

- Encapsulation: keep `_balance` locked inside `BankAccount`, only touchable through `deposit()`/`withdraw()` — never changed directly from outside.

```python
class BankAccount:
    def __init__(self, balance): self._balance = balance
    def deposit(self, amt): self._balance += amt
```

- Inheritance: `SavingsAccount` and `LoanAccount` don't rewrite `BankAccount` — they just build on top of it.

```python
class SavingsAccount(BankAccount):
    def __init__(self, balance, rate):
        super().__init__(balance); self.rate = rate
```

- Polymorphism: every `GameCharacter` has `.attack()`, but a Warrior and a Mage each do something different when it's called.
- Abstraction: calling `account.withdraw(100)` is simple to use — you don't need to see the validation and math happening behind that one line.

---

### Q3. Describe the use of `__init__`, `self`, instance variables, and class variables in the `BankAccount` example.

- `__init__` runs the instant a new `BankAccount` is made — it's the setup step. `self` just means "this one account," so each account keeps its own separate numbers.

```python
class BankAccount:
    bank_name = "National Bank"          # shared by every account
    def __init__(self, owner, balance):
        self.owner = owner                # personal to this account
        self.balance = balance

a1 = BankAccount("Avhi", 1000)
a2 = BankAccount("Sita", 500)
print(a1.bank_name, a2.bank_name)   # same - shared
print(a1.balance, a2.balance)       # different - personal
```

- Simple rule to remember: instance variables are things that differ per object (balance, owner); class variables are things that stay the same for every object (bank_name).

---

### Q4. Discuss the role of special methods or dunder methods in custom classes. Use the `LibraryBook` and `ShoppingCart` examples.

- Dunder methods let your own class plug into Python's normal syntax, instead of you inventing new custom method names for everything.
- For `LibraryBook`: `__str__` controls what `print(book)` looks like, and `__eq__` decides what counts as "the same book" — usually matching ISBN, not just checking if it's literally the same object in memory.

```python
class LibraryBook:
    def __init__(self, title, isbn):
        self.title, self.isbn = title, isbn
    def __str__(self):
        return f"Book: {self.title}"
    def __eq__(self, other):
        return self.isbn == other.isbn
```

- For `ShoppingCart`: `__len__` makes `len(cart)` work, and `__contains__` makes `"apple" in cart` work — exactly like a normal list.

```python
class ShoppingCart:
    def __init__(self): self.items = []
    def __len__(self): return len(self.items)
    def __contains__(self, item): return item in self.items
```

- Simple way to remember it: dunder methods are how you teach Python's built-in words (`print`, `len`, `in`, `==`) to understand your own custom objects.

---

### Q5. Explain inheritance in the `BankAccount` hierarchy. Include the meaning of `super()`, method overriding, and `isinstance()`.

- `SavingsAccount` and `LoanAccount` both build on top of `BankAccount` instead of starting from scratch.

```python
class BankAccount:
    def __init__(self, balance): self.balance = balance
    def withdraw(self, amt): self.balance -= amt

class SavingsAccount(BankAccount):
    def __init__(self, balance, rate):
        super().__init__(balance)   # reuse the parent's setup
        self.rate = rate
    def withdraw(self, amt):        # override: do it differently
        print("Savings withdrawal fee applies")
        super().withdraw(amt)        # then still do the normal part
```

- `super()` means "let the parent handle this bit." Method overriding means the child writes its own version of a method that replaces the parent's version. `isinstance(acc, BankAccount)` just checks "is this thing a kind of BankAccount?" — and a `SavingsAccount` counts as yes.

---

### Q6. Discuss method resolution order (MRO) and explain the diamond structure example using `A`, `B`, `C`, and `D`. Explain with an example.

- MRO is simply the order Python checks classes in when looking for a method — this only really matters once a class inherits from more than one parent.
- A "diamond" happens when `B` and `C` both come from `A`, and `D` comes from both `B` and `C` — so there are two paths back up to `A`.

```python
class A:
    def greet(self): print("A")
class B(A):
    def greet(self): print("B")
class C(A):
    def greet(self): print("C")
class D(B, C):
    pass

D().greet()          # "B" - Python checks D, then B, then C, then A
print(D.__mro__)     # (D, B, C, A, object)
```

- You don't need to memorise the algorithm behind this — just remember `D.__mro__` will always show you the exact search order Python actually used, so when in doubt, print it and check.

---

### Q7. Explain polymorphism and duck typing using the notes' `GameCharacter` and report examples. Explain with an example.

- Polymorphism: same method name, different result depending on the object.

```python
class GameCharacter:
    def attack(self): print("Generic attack")
class Warrior(GameCharacter):
    def attack(self): print("Sword slash!")
class Mage(GameCharacter):
    def attack(self): print("Fireball!")

for char in [Warrior(), Mage()]:
    char.attack()   # same line of code, different outcome each time
```

- Duck typing: "if it walks like a duck and quacks like a duck, treat it like a duck" — Python doesn't check what class an object is, only whether it has the method being called.

```python
def print_report(obj):
    print(obj.generate())   # works for ANY object with a .generate() method
```

- Easy way to tell them apart: polymorphism (here) usually comes from a shared parent class; duck typing needs no shared parent at all — just a matching method name.

---

### Q8. Explain how custom exception classes are created and used in the bank example. Why do the notes recommend inheriting from `Exception` rather than `BaseException`?

- Making a custom exception is just making a small class that inherits from `Exception`, sometimes adding a bit of extra info.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
```

- It gets `raise`d when the problem happens, and caught with `except InsufficientFundsError as e:` where `e.balance` and `e.amount` are ready to use directly.
- `Exception` is used instead of `BaseException` because `BaseException` also covers things like the program being deliberately stopped (`SystemExit`, Ctrl+C) — those aren't "errors" in the normal sense, and a regular `except` block usually shouldn't accidentally swallow them. `Exception` is simply the safe, standard starting point for your own error types.

---

### Q9. Describe the `try` / `except` / `else` / `finally` structure and explain its importance in the `safe_transaction()` function. Explain with an example.

- Think of it in four plain steps: try it, catch it if it breaks, celebrate if it worked, clean up no matter what.

```python
def safe_transaction(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        new_balance = balance - amount
    except InsufficientFundsError as e:
        print("Transaction failed:", e)
        return balance
    else:
        print("Transaction successful")
        return new_balance
    finally:
        print("Transaction attempt logged")
```

- This keeps four different jobs from getting tangled together: the risky code, what to do on failure, what to do only on success, and cleanup that must happen either way — each has its own clearly separated home.

---

### Q10. Explain the iterator protocol using the `CountDown` and `StudentRoster` examples. How does it relate to the `for` loop? Explain with an example.

- A class becomes loop-friendly by adding `__iter__()` (return itself) and `__next__()` (hand back the next value, or say "I'm done" with `StopIteration`).

```python
class CountDown:
    def __init__(self, start): self.current = start
    def __iter__(self): return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(3):   # 3, 2, 1
    print(n)
```

- `StudentRoster` can do the same thing more simply, just by handing off to its own list.

```python
class StudentRoster:
    def __init__(self, students): self.students = students
    def __iter__(self): return iter(self.students)
```

- Here's the connection worth remembering: writing `for x in obj:` is really Python quietly doing `iter(obj)` once, then `next()` again and again until it hits `StopIteration`. Adding these two methods is what unlocks the `for` loop for your own class.

---

### Q11. Explain generator functions with `yield`, and compare them with lists using the examples in the notes. Explain with an example.

- A generator is a shortcut for writing that same "give me the next value" behaviour, without needing a whole class — `yield` pauses the function and remembers exactly where it left off.

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1
for i in count_down(3):   # 3, 2, 1
    print(i)
```

- A list builds and stores every value immediately; a generator makes each value only when you actually ask for it — which matters a lot for huge or endless sequences.

```python
def all_evens():          # a list version of this is literally impossible
    n = 0
    while True:
        yield n
        n += 2
```

- Simple trade-off to remember: lists can be looped over again and again, and you can jump to any index directly — a generator can only be used once, start to finish, and then it's empty.

---

### Q12. Discuss `*args`, `**kwargs`, the LEGB scope rule, and module imports using the notebook examples. Explain with an example.

- `*args` and `**kwargs` let a function accept "as many arguments as you want to give me" — `*args` for plain values, `**kwargs` for `name=value` pairs.

```python
def create_student(*args, **kwargs):
    print(args, kwargs)
create_student("Avhi", 20, course="AI")   # ('Avhi', 20) {'course': 'AI'}
```

- LEGB is just "where does Python look for a name, and in what order": right here (Local), then the function wrapped around this one (Enclosing), then the whole file (Global), then Python's own words (Built-in).

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)     # "local" - found immediately, no need to look further
    inner()
```

- Modules and packages just let you split code across files instead of jamming everything into one giant script — `import module_name` brings in what you need, and that's really all there is to it.

---

## Long Questions (12 Marks)

### Q1. Discuss how object-oriented programming solves the problem of procedural code. Explain how the `Student` example bundles data and behaviour and show how the four pillars of OOP are reflected in the unit.

**Introduction**

In plain procedural code, data and the functions that use it just sit apart from each other — like keeping a recipe in one drawer and the ingredients in a completely different room. It works for something small, but the further apart they get, the easier it is to lose track of what belongs with what.

**Body**

```python
# procedural: data and logic live apart
name, marks = "Avhi", [78, 91, 85]
def average(marks): return sum(marks)/len(marks)
```

- OOP fixes this simply by putting the data and its logic in the same box. The `Student` class keeps a student's name and marks right next to the methods that actually use them.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def __str__(self):
        return f"{self.name}: avg {self.average():.1f}"
```

- This one small class already shows all four pillars if you know where to look: encapsulation (the marks and the logic for them live together), abstraction (`student.average()` hides the actual math behind one simple call), inheritance (a `GraduateStudent` subclass could reuse all of this and just add a thesis field), and polymorphism (a `.summary()` method could look different for each subclass, while still being called the exact same way).
- The payoff shows up as the project grows: adding a brand new kind of student later just means writing a small new subclass, instead of hunting down and editing scattered functions everywhere.

**Conclusion**

The `Student` example is really a small, complete demonstration of what OOP is for — not a stylistic preference, but a practical fix for the way procedural code tends to fall apart as a project gets bigger.

---

### Q2. Explain inheritance in depth using the `BankAccount`, `SavingsAccount`, and `LoanAccount` examples. Discuss `super()`, method overriding, and inheritance checks. Explain with an example.

**Introduction**

Inheritance is simply reusing a class instead of retyping it — a new class gets everything the old one already had, and only needs to add what's actually different.

**Body**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
```

- `SavingsAccount` reuses this directly, letting `super()` handle the shared setup and just adding its own extra bit.

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)   # let the parent do this part
        self.rate = rate
    def add_interest(self):
        self.balance += self.balance * self.rate
```

- `LoanAccount` shows overriding more clearly — a loan works differently enough that `withdraw()` needs to be rewritten completely, allowing the balance to go negative up to a limit instead of blocking it.

```python
class LoanAccount(BankAccount):
    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.limit = limit
    def withdraw(self, amount):         # completely replaces the parent's version
        if self.balance - amount < -self.limit:
            raise ValueError("Loan limit exceeded")
        self.balance -= amount
```

- Simple way to remember each piece: `super()` means "let the parent do this part too"; overriding means "actually, my version works differently here"; and `isinstance(loan, BankAccount)` is just asking "is this still a kind of BankAccount?" — the answer is yes, even though it's a `LoanAccount`.

**Conclusion**

All three classes tell the same story: `super()` avoids retyping shared setup, overriding lets a subclass change only what genuinely needs to change, and `isinstance()` lets the rest of the program treat every account type the same way whenever their shared behaviour is enough.

---

### Q3. Analyze polymorphism using the `GameCharacter` hierarchy and contrast it with duck typing using the report example. Discuss how operator overloading is also implemented in the notes.

**Introduction**

Polymorphism, the classic version, means a group of related classes all share a method name, but each does its own thing when that method is actually called.

**Body**

```python
class GameCharacter:
    def attack(self): print("Generic attack")
class Warrior(GameCharacter):
    def attack(self): print("Sword slash!")
class Mage(GameCharacter):
    def attack(self): print("Fireball!")

characters = [Warrior(), Mage()]
for c in characters:
    c.attack()   # same instruction, different result each time
```

- The calling code never needs to check which subclass it's actually dealing with — it just calls `.attack()` and trusts the right version runs.
- Duck typing gets a similar result without any shared parent class at all — Python only checks whether the method exists, not what class the object officially belongs to.

```python
class SalesReport:
    def generate(self): return "Sales: $10,000"
class WeatherReport:
    def generate(self): return "Sunny, 25C"

def print_report(obj):
    print(obj.generate())   # works for either - no shared parent needed
```

- Easy rule of thumb: polymorphism (GameCharacter) leans on a shared parent class; duck typing (the reports) doesn't need one — it only cares that the right method happens to exist.
- Operator overloading is the same basic idea applied to symbols instead of method names — a dunder method decides what `+`, `==`, or `<` should actually do for your own class.

```python
class Money:
    def __init__(self, amount): self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __str__(self): return f"${self.amount}"
print(Money(10) + Money(5))   # $15 - '+' now works on your own objects
```

**Conclusion**

All three — polymorphism, duck typing, and operator overloading — are the same trick at heart: letting the same simple piece of syntax (`.attack()`, `.generate()`, `+`) do the right thing automatically, no matter which specific object it's used on.

---

### Q4. Evaluate the custom exception design in the bank system and explain how `try`, `except`, and custom classes work together to produce clear error handling. Explain with an example.

**Introduction**

A good exception setup for a bank app starts with one general error at the top, and more specific errors branching off it — so code can catch one exact problem, or catch the whole family at once.

**Body**

```python
class BankError(Exception):
    pass
class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} cannot cover withdrawal of {amount}")
        self.balance, self.amount = balance, amount
class InvalidAmountError(BankError):
    pass
```

- The account's own methods `raise` the exact exception that matches what actually went wrong, instead of one vague generic error for everything.

```python
class BankAccount:
    def __init__(self, balance): self.balance = balance
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
```

- The calling code handles each situation on its own terms, checking the most specific error first.

```python
acc = BankAccount(500)
try:
    acc.withdraw(1000)
except InsufficientFundsError as e:
    print("Not enough funds:", e.balance, "available, needed", e.amount)
except InvalidAmountError as e:
    print("Bad amount:", e)
except BankError as e:
    print("Some other bank error:", e)   # catches anything else in the family
```

- This turns out clear for a simple reason: each `except` block only fires for the exact problem it's meant to handle, the extra attributes (`e.balance`, `e.amount`) hand over useful details directly, and the shared `BankError` still catches anything unexpected in the family.

**Conclusion**

Custom exceptions and `try`/`except` work well together because the exception classes describe *what* went wrong, and the `except` chain decides *what to do* about each one — keeping detection and response cleanly separate is what makes this style of error handling easy to follow rather than one tangled mess of if-checks.

---

### Q5. Discuss the iterator protocol and generator functions in Python as explained in the notes. Explain how they differ from ordinary lists and why they are useful. Explain with an example.

**Introduction**

The iterator protocol is simply the two things a class needs so it can be used in a `for` loop: `__iter__()` ("I'm ready to be looped over") and `__next__()` ("here's the next value," or `StopIteration` to say "I'm done").

**Body**

```python
class CountDown:
    def __init__(self, start): self.current = start
    def __iter__(self): return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(3):   # 3, 2, 1
    print(n)
```

- A generator function gets the exact same result with far less code — `yield` pauses the function and remembers exactly where it stopped, instead of tracking state by hand.

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1
for n in count_down(3):   # 3, 2, 1 - same output, much simpler
    print(n)
```

- The real difference from a list comes down to memory: a list like `[3, 2, 1]` builds and stores every value up front. Both `CountDown` and the generator make each value only when it's actually asked for.

```python
def all_evens():             # truly endless
    n = 0
    while True:
        yield n
        n += 2
gen = all_evens()
print(next(gen), next(gen), next(gen))   # 0 2 4
```

- This matters whenever the full sequence would be too big to fit in memory at once, or doesn't even have an end — a list of "every even number" is simply impossible to build, but a generator can hand them out forever, one at a time, using barely any memory.
- The trade-off: both a hand-written iterator and a generator usually only work once — once they're used up, they just stop, unlike a list which can be looped over again and again or jumped into at any position.

**Conclusion**

Both the iterator protocol and generators solve the exact same problem — handing out values lazily, one at a time — and generators are simply the much easier way to write that same behaviour in practice.

---

### Q6. Explain the `*args`, `**kwargs`, and LEGB scope rules with examples from the notes. Discuss how closures and the `nonlocal` keyword affect variable access.

**Introduction**

`*args` and `**kwargs` exist for one simple reason: sometimes you don't know in advance exactly how many arguments a function will be given. `*args` grabs extra plain values into a tuple; `**kwargs` grabs extra `name=value` pairs into a dictionary.

**Body**

```python
def register_student(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)
register_student("Avhi", 20, course="AI", year=1)
# positional: ('Avhi', 20)
# keyword: {'course': 'AI', 'year': 1}
LEGB is just the order Python checks when it needs to find a variable: Local (right here) → Enclosing (the function wrapped around this one) → Global (the whole file) → Built-in (Python's own words like `len`).
x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)   # "enclosing" - nothing local, so it checks the next level up
    inner()
outer()
```

- A closure is just an inner function that "remembers" a variable from the function wrapped around it, even after that outer function has already finished running.

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count   # without this line, Python gets confused
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2 - it remembered!
```

- By default, an inner function can *read* a variable from outside it, but not *change* it — trying `count += 1` without `nonlocal` would create a brand new local `count` instead, and Python would complain because that new local `count` hasn't been given a value yet. `nonlocal` simply says "no, I mean the outside one — let me actually change that."

**Conclusion**

LEGB, closures, and `nonlocal` are really just one idea in three parts — where a name lives, and who's allowed to change it — and once that clicks, patterns like a counter function that remembers its own count stop feeling like magic.

---

### Q7. Describe the role of modules, packages, and imports in Python as explained in the notes. Explain why the `__name__ == "__main__"` guard is important.

**Introduction**

A module is just one `.py` file — anything defined in it (functions, classes, variables) becomes usable elsewhere with `import`.

**Body**

```python
# file: bank_utils.py
def calculate_interest(balance, rate):
    return balance * rate

# file: main.py
import bank_utils
print(bank_utils.calculate_interest(1000, 0.05))
```

- A package is just a folder full of related modules (with an `__init__.py` file), so they can be imported together under one shared name — like a `bank/` folder holding `accounts.py` and `transactions.py`.
- Imports come in a few flavours depending on how much you want: `import module` (use `module.name` every time), `from module import name` (use `name` directly), or `import module as alias` (a shorter nickname).

```python
from bank_utils import calculate_interest
print(calculate_interest(1000, 0.05))   # no prefix needed now
```

- The `if __name__ == "__main__":` guard exists because every file secretly has a `__name__` variable — Python sets it to `"__main__"` only for the file you actually ran, and to the module's own name for any file that just got imported.

```python
# bank_utils.py
def calculate_interest(balance, rate):
    return balance * rate

if __name__ == "__main__":
    print(calculate_interest(1000, 0.05))   # only runs if this file is run directly
```

- Without this guard, any test or example code sitting at the bottom of `bank_utils.py` would run every single time someone else just tries to import it — which almost never makes sense, since importing a file should just make its tools available, not fire off its demo code as a surprise side effect.

**Conclusion**

Modules and packages are what let a project grow past a single file without turning into a mess, and the `__name__` guard is what stops a file's own test code from running unexpectedly the moment someone else reuses it.

---

### Q8. Write a comprehensive discussion of the complete Unit 2 content by integrating classes, instance variables, inheritance, dunder methods, exceptions, iterators, generators, scope, and modules in a single coherent explanation.

**Introduction**

Unit 2 is really one continuous story, not a list of separate topics — each new idea solves a specific gap left by the one before it.

**Body**

- It starts with the class itself — a blueprint that finally keeps data (instance variables, set through `self` inside `__init__`) and the logic that uses it (methods) in the same place, fixing the procedural habit of keeping them apart.

```python
class BankAccount:
    bank_name = "National Bank"              # shared by everyone
    def __init__(self, owner, balance):
        self.owner, self.balance = owner, balance  # personal to each account
```

- Dunder methods then let these custom classes speak Python's own language — `__str__` for `print()`, `__eq__` for `==`, `__len__` for `len()` — so a `BankAccount` or `ShoppingCart` feels like a normal, built-in-feeling object instead of something foreign.
- Inheritance builds on this — `SavingsAccount` and `LoanAccount` reuse `BankAccount` through `super()`, only rewriting the specific method (like `withdraw()`) that genuinely needs to behave differently. This is also exactly where polymorphism shows up, since the same `withdraw()` call still works correctly no matter which subclass it's called on.

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate
```

- Custom exceptions apply this exact same class-thinking to errors — a `BankError` family lets `try`/`except` respond precisely to what actually went wrong, using the same `super().__init__()` pattern already familiar from the account classes.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"{balance} < {amount}")
```

- The iterator protocol (`__iter__`/`__next__`) and generator functions (`yield`) then show how a custom object can hand out a whole *sequence* of values, connecting straight back to the `for` loop — generators being the much shorter way to write the same one-at-a-time behaviour.

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1
```

- Underneath everything sits Python's scope rules — LEGB, `*args`/`**kwargs` for flexible functions, and `nonlocal` for closures — which quietly govern how every function and method actually finds the variable names it uses.
- Finally, modules, packages, and the `if __name__ == "__main__":` guard are what let all of these classes live across multiple files as a real project grows, without one file's own test code firing off unexpectedly whenever it gets reused elsewhere.

```
[Class: data + methods] -> [Inheritance: reuse + override] -> [Dunders: fit into Python's syntax] -> [Exceptions: structured error handling] -> [Iterators/Generators: lazy sequences] -> [Scope/LEGB: how names are found] -> [Modules/Packages: organising it all]
```

**Conclusion**

Read together, Unit 2 is one long argument for organising code around objects — every later topic either extends what a class can do, or supports the machinery that keeps classes working cleanly once a real project grows past a single script.

---
