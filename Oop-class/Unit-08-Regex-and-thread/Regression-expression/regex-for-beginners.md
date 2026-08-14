# Regular Expressions: A Practical Guide for Beginners

Regular expressions, usually called **regex** or **regexp**, are a way of describing patterns in text.

At first, a regular expression can look almost like a secret language:

```text
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

But regex is not magic. It is a small language made from a handful of ideas. Once you understand those ideas, even complicated expressions become much easier to read.

This guide will teach you regex from the ground up.

---

## 1. What is a regular expression?

Suppose you have this text:

```text
My phone number is 9841234567.
```

You want to find the phone number.

You could search for the exact number:

```text
9841234567
```

But that only works for that particular number.

What if the text contains:

```text
9812345678
9801234567
9860123456
```

Instead of searching for one exact number, you can describe the **pattern**:

> Find ten digits in a row.

A regex for that pattern could be:

```text
\d{10}
```

Here:

* `\d` means a digit
* `{10}` means exactly 10 times

So:

```text
\d{10}
```

means:

> Match exactly ten digits.

That is the fundamental idea behind regex:

**You describe a pattern rather than a specific piece of text.**

---

# 2. Literal characters

The simplest regex is just ordinary text.

For example:

```text
hello
```

matches:

```text
hello
```

It can find `hello` inside:

```text
hello world
say hello
hello123
```

Regex becomes interesting when we introduce special characters.

For example:

```text
h.llo
```

The `.` has a special meaning.

It means:

> Match almost any single character.

Therefore:

```text
h.llo
```

can match:

```text
hello
hallo
hollo
h3llo
```

The important distinction is:

```text
hello
```

means the literal word `hello`.

While:

```text
h.llo
```

means a pattern where the third character can vary.

---

# 3. The dot `.`

The dot is one of the first regex symbols you should learn.

```text
.
```

usually means:

> Any single character except a newline.

For example:

```text
c.t
```

can match:

```text
cat
cot
cut
c9t
```

But it does not mean "any number of characters."

For example:

```text
c.t
```

does not match:

```text
coat
```

because there are two characters between `c` and `t`.

This distinction is important:

```text
.       one character
.*      zero or more characters
.+      one or more characters
```

We will learn `*` and `+ shortly.

---

# 4. Character classes

Sometimes you don't want to match just any character.

Suppose you want either `a`, `e`, `i`, `o`, or `u`.

You can write:

```text
[aeiou]
```

The square brackets create a **character class**.

For example:

```text
c[aeiou]t
```

matches:

```text
cat
cet
cit
cot
cut
```

but not:

```text
ct
cxt
```

because the middle character must be one of the characters inside the brackets.

---

## Character ranges

You can specify ranges inside a character class.

For example:

```text
[a-z]
```

means:

> Any lowercase letter from a through z.

Similarly:

```text
[A-Z]
```

means any uppercase letter.

And:

```text
[0-9]
```

means any digit.

You can combine ranges:

```text
[A-Za-z0-9]
```

means:

> Any uppercase letter, lowercase letter, or digit.

---

# 5. Negated character classes

You can also say:

> Match anything except these characters.

Use `^` immediately after `[`.

For example:

```text
[^0-9]
```

means:

> Any character that is not a digit.

Compare:

```text
[0-9]
```

with:

```text
[^0-9]
```

The first means "a digit."

The second means "not a digit."

The position of `^` matters.

```text
^hello
```

has a completely different meaning from:

```text
[^hello]
```

We'll discuss `^` as an anchor later.

---

# 6. Useful shortcuts

Regex provides shortcuts for common character classes.

## `\d` — digit

```text
\d
```

usually means a digit.

It is similar to:

```text
[0-9]
```

For example:

```text
\d\d\d
```

matches:

```text
123
456
987
```

---

## `\w` — word character

```text
\w
```

usually matches a letter, digit, or underscore.

For example:

```text
\w+
```

can match:

```text
hello
user123
hello_world
```

The exact definition of `\w` can vary between regex engines, especially with Unicode, so remember that it is an engine-dependent shortcut.

---

## `\s` — whitespace

```text
\s
```

matches whitespace such as:

* spaces
* tabs
* line breaks

For example:

```text
hello\sworld
```

can match:

```text
hello world
```

---

## Uppercase versions

There is a useful convention:

```text
\d    digit
\D    not a digit

\w    word character
\W    not a word character

\s    whitespace
\S    not whitespace
```

The uppercase version generally means "the opposite."

---

# 7. Quantifiers: repetition

Now we reach one of the most important parts of regex.

Quantifiers tell regex **how many times something should occur**.

The most important ones are:

```text
*       zero or more
+       one or more
?       zero or one
{n}     exactly n
{n,m}   between n and m
```

Let's examine them.

---

# 8. The `*` quantifier

The star means:

> Zero or more occurrences.

For example:

```text
ab*
```

means:

> Match `a`, followed by zero or more `b`s.

Therefore it can match:

```text
a
ab
abb
abbb
abbbb
```

Notice that it can match just:

```text
a
```

because zero `b`s are allowed.

---

# 9. The `+` quantifier

The plus means:

> One or more occurrences.

For example:

```text
ab+
```

can match:

```text
ab
abb
abbb
abbbb
```

But it cannot match:

```text
a
```

because at least one `b` is required.

Compare:

```text
ab*
```

with:

```text
ab+
```

The difference is:

```text
* = zero or more
+ = one or more
```

This is one of the most important distinctions in regex.

---

# 10. The `?` quantifier

The question mark means:

> Zero or one occurrence.

For example:

```text
colou?r
```

matches both:

```text
color
colour
```

The `u` is optional.

This is useful when a character may or may not exist.

---

# 11. Exact repetition with `{}`

You can specify an exact number of repetitions.

For example:

```text
\d{4}
```

means:

> Exactly four digits.

It can match:

```text
2026
1234
9876
```

but not:

```text
123
12345
```

You can also specify a range:

```text
\d{2,4}
```

means:

> Between two and four digits.

It can match:

```text
12
123
1234
```

Depending on the surrounding pattern and matching mode, it may match part of a longer sequence unless you constrain the boundaries.

---

# 12. Anchors: beginning and end

Sometimes finding a pattern somewhere inside a string isn't enough.

Suppose you want to check whether a string contains **only digits**.

You might write:

```text
\d+
```

But this could match the digits inside:

```text
abc123xyz
```

If you want the **entire string** to consist of digits, you need boundaries.

Use:

```text
^
```

for the beginning and:

```text
$
```

for the end.

Therefore:

```text
^\d+$
```

means:

> Start of string → one or more digits → end of string.

So:

```text
12345
```

matches.

But:

```text
abc123
```

does not.

---

# 13. Why anchors are so important

Consider:

```text
\d{10}
```

It means:

> Find ten digits.

But:

```text
^\d{10}$
```

means:

> The entire string must contain exactly ten digits.

This distinction is extremely important when validating user input.

For example, if a form asks for a ten-digit number, you probably don't want this:

```text
hello 9841234567 world
```

to be considered valid.

Anchors help you say:

> The whole input must follow this pattern.

---

# 14. Alternation: OR

Sometimes you want one pattern **or** another.

Regex uses:

```text
|
```

for OR.

For example:

```text
cat|dog
```

matches either:

```text
cat
```

or:

```text
dog
```

You can make more complicated alternatives:

```text
apple|banana|orange
```

means:

> Match apple, banana, or orange.

---

# 15. Groups with parentheses

Parentheses create groups.

For example:

```text
(cat|dog)
```

means:

> Either `cat` or `dog`.

Groups become particularly useful when combined with quantifiers.

Consider:

```text
(ab)+
```

This means:

> Repeat the group `ab` one or more times.

It can match:

```text
ab
abab
ababab
```

Without the parentheses:

```text
ab+
```

means:

> `a` followed by one or more `b`s.

So:

```text
ab+
```

matches:

```text
ab
abb
abbb
```

while:

```text
(ab)+
```

matches:

```text
ab
abab
ababab
```

Parentheses allow you to control **what gets repeated**.

---

# 16. Capturing groups

Parentheses do something else important: they can **capture** the text they matched.

Suppose you have:

```text
2026-08-09
```

and want to extract the year, month, and day.

You could write:

```text
(\d{4})-(\d{2})-(\d{2})
```

The three groups capture:

```text
2026
08
09
```

This is extremely useful in programming.

For example, a programming language can use the groups to retrieve specific pieces of the matched text.

So regex isn't only useful for answering:

> "Does this text match?"

It can also answer:

> "What pieces of information did I find?"

---

# 17. Non-capturing groups

Sometimes you want parentheses for grouping but don't need to capture the result.

You can use:

```text
(?:...)
```

For example:

```text
(?:cat|dog)
```

This groups the alternatives without creating a capturing group.

You don't need to learn this immediately, but it becomes useful when writing larger regular expressions.

---

# 18. Escaping special characters

We have seen characters that have special meanings:

```text
.
*
+
?
(
)
[
]
{
}
^
$
|
```

But what if you actually want to search for one of those characters?

For example, suppose you want to match:

```text
3.14
```

If you write:

```text
3.14
```

the `.` means "any character."

To match a literal period, escape it:

```text
3\.14
```

The backslash tells regex:

> Treat the next character literally.

Therefore:

```text
\.
```

means a literal period.

Similarly:

```text
\+
```

means a literal plus sign.

---

# 19. A complete example

Let's build a regex step by step.

Suppose we want to find a simple username.

Our rules are:

* It must contain letters, digits, or underscores.
* It must contain between 3 and 15 characters.
* Nothing else is allowed.

First, describe the allowed characters:

```text
[A-Za-z0-9_]
```

Now we need 3–15 of them:

```text
[A-Za-z0-9_]{3,15}
```

Finally, we want the entire string to follow the rule:

```text
^[A-Za-z0-9_]{3,15}$
```

Read it from left to right:

```text
^
```

Start of the string.

```text
[A-Za-z0-9_]
```

One letter, digit, or underscore.

```text
{3,15}
```

Repeat that 3 to 15 times.

```text
$
```

End of the string.

So the whole expression means:

> The entire string must contain 3–15 letters, digits, or underscores.

---

# 20. Another example: dates

Suppose dates are written like:

```text
2026-08-09
```

We can describe the structure:

```text
\d{4}-\d{2}-\d{2}
```

Break it down:

```text
\d{4}
```

Four digits.

```text
-
```

A literal hyphen.

```text
\d{2}
```

Two digits.

Another hyphen.

```text
\d{2}
```

Two more digits.

If we want the entire string to follow that format:

```text
^\d{4}-\d{2}-\d{2}$
```

Notice an important limitation:

This checks the **format**, not necessarily whether the date is real.

For example:

```text
9999-99-99
```

has the correct shape but is not a sensible date.

This illustrates an important lesson:

**Regex is good at recognizing text patterns, but it isn't always the right tool for validating meaning.**

---

# 21. Matching whitespace

Suppose you want to match:

```text
John Smith
```

You could write:

```text
John Smith
```

But if the amount of whitespace can vary, you could use:

```text
John\s+Smith
```

Here:

```text
\s+
```

means:

> One or more whitespace characters.

So it can match:

```text
John Smith
John  Smith
John    Smith
```

It may also match a tab or other whitespace, depending on the regex engine.

---

# 22. Greedy matching

One of the concepts that confuses beginners is **greediness**.

Consider:

```text
<.*>
```

and this text:

```text
<p>Hello</p>
```

You might expect it to match:

```text
<p>
```

But `.*` is normally **greedy**.

It tries to consume as much as possible while still allowing the rest of the expression to match.

So it may match:

```text
<p>Hello</p>
```

as one large match.

This can be surprising.

---

# 23. Lazy matching

You can make many quantifiers lazy by adding `?`.

For example:

```text
<.*?>
```

Now `.*?` tries to match as little as possible while still allowing the rest of the expression to succeed.

For:

```text
<p>Hello</p>
```

it can find:

```text
<p>
```

first.

This gives us an important pair:

```text
.*     greedy
.*?    lazy
```

You don't need to master greediness on day one, but you should learn it once you're comfortable with the basics.

---

# 24. Lookahead and lookbehind

These are more advanced features.

A **lookahead** lets you check what comes next without consuming it.

For example:

```text
\d+(?= dollars)
```

can find digits that are immediately followed by:

```text
 dollars
```

So in:

```text
I paid 50 dollars.
```

the digits `50` can be matched.

The `(?= dollars)` part checks what comes after the number.

Lookbehind does the opposite: it checks what comes before.

For example:

```text
(?<=\$)\d+
```

can find digits preceded by a dollar sign.

These features are powerful, but don't start your regex journey with them.

---

# 25. Common regex symbols to remember

Here is a useful cheat sheet.

| Regex     | Meaning                 |
| --------- | ----------------------- |
| `.`       | Any character           |
| `\d`      | Digit                   |
| `\D`      | Not a digit             |
| `\w`      | Word character          |
| `\W`      | Not a word character    |
| `\s`      | Whitespace              |
| `\S`      | Not whitespace          |
| `[abc]`   | `a`, `b`, or `c`        |
| `[a-z]`   | Lowercase letter        |
| `[0-9]`   | Digit                   |
| `[^0-9]`  | Anything except a digit |
| `*`       | Zero or more            |
| `+`       | One or more             |
| `?`       | Zero or one             |
| `{3}`     | Exactly 3               |
| `{3,}`    | 3 or more               |
| `{3,5}`   | 3 to 5                  |
| `^`       | Beginning               |
| `$`       | End                     |
| `\|`      | Literal pipe            |
| `\.`      | Literal period          |
| `(...)`   | Capturing group         |
| `(?:...)` | Non-capturing group     |
| `a\|b`    | `a` or `b`              |

---

# 26. How to read a regex

Don't try to understand a complicated regex all at once.

Read it from left to right.

Consider:

```text
^[A-Za-z]+\d{2}$
```

Break it into pieces:

```text
^
```

Start.

```text
[A-Za-z]+
```

One or more letters.

```text
\d{2}
```

Exactly two digits.

```text
$
```

End.

Now translate the whole thing into English:

> The entire string must contain one or more letters followed by exactly two digits.

Examples that match:

```text
abc12
Hello99
test42
```

Examples that don't:

```text
12345
abc
abc123
hello!
```

This method—**breaking regex into small pieces and translating each piece into English**—is one of the best ways to learn.

---

# 27. Regex is a language

A useful way to think about regex is as a small programming language.

These symbols are like its vocabulary:

```text
\d
.
[]
()
|
```

Quantifiers are like instructions about repetition:

```text
*
+
?
{n}
```

Anchors describe positions:

```text
^
$
```

And groups allow you to combine pieces.

For example:

```text
^\d{3}-\d{3}-\d{4}$
```

is essentially a little program that says:

> Start at the beginning, find three digits, then a hyphen, then three digits, another hyphen, four digits, and finish at the end.

Thinking this way makes regex much less mysterious.

---

# 28. Don't memorize complicated regexes

A common beginner mistake is trying to memorize expressions such as:

```text
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

Instead, learn the building blocks.

You should be comfortable with:

```text
\d
\w
\s
.
[]
()
|
*
+
?
{}
^
$
\
```

Once you understand those, you can construct larger expressions when you need them.

---

# 29. A practical learning sequence

If you're learning regex from scratch, I recommend this order.

### Stage 1 — Basic matching

Learn:

```text
abc
.
```

Understand how regex finds text.

### Stage 2 — Character classes

Learn:

```text
[abc]
[a-z]
[A-Z]
[0-9]
[^0-9]
```

### Stage 3 — Shortcuts

Learn:

```text
\d
\D
\w
\W
\s
\S
```

### Stage 4 — Repetition

Learn:

```text
*
+
?
{n}
{n,m}
```

### Stage 5 — Boundaries

Learn:

```text
^
$
```

### Stage 6 — Groups and alternatives

Learn:

```text
(...)
(?:...)
|
```

### Stage 7 — Escaping

Learn why these need special treatment:

```text
\.
\+
\?
\(
\[
\\
```

### Stage 8 — Capturing

Learn how to extract pieces of a match:

```text
(\d{4})-(\d{2})-(\d{2})
```

### Stage 9 — Greedy and lazy matching

Learn:

```text
.*
.*?
```

### Stage 10 — Advanced features

Finally learn:

```text
(?=...)
(?!...)
(?<=...)
(?<!...)
```

These are called lookarounds.

---

# 30. Practice is more important than memorization

The best way to learn regex is to solve small problems.

Try writing expressions for these:

### Exercise 1

Find a sequence of digits.

Expected idea:

```text
\d+
```

### Exercise 2

Find exactly five digits.

```text
\d{5}
```

### Exercise 3

Find a word beginning with `a`.

Think about:

```text
a...
```

### Exercise 4

Find a string containing only digits.

Think about:

```text
^ ... $
```

### Exercise 5

Find either `cat` or `dog`.

Think about:

```text
cat|dog
```

### Exercise 6

Find a word containing only letters and between 3 and 10 characters.

Think about:

```text
^ ... $
```

and combine:

```text
[A-Za-z]
```

with:

```text
{3,10}
```

Don't immediately look up the answer. Try constructing it from the pieces you've learned.

---

# 31. One important warning: regex engines differ

Regex is not completely identical everywhere.

You may encounter regex in:

* Python
* JavaScript
* Java
* C#
* PHP
* SQL
* command-line tools
* text editors
* IDEs

Most share the fundamentals, but some features and details differ.

For example, the meaning of certain Unicode characters, flags, escape sequences, and advanced constructs can vary.

Therefore, when learning a particular programming language, learn the regex flavor used by that language.

The good news is that the fundamentals you've learned here transfer very well.

---

# 32. Regex is powerful, but don't overuse it

Regex is excellent for tasks such as:

* finding patterns in text
* extracting information
* replacing text
* checking simple input formats
* searching logs
* processing files
* cleaning data

But regex isn't always the best tool.

For example, trying to parse a complicated programming language, HTML structure, or deeply nested data using one enormous regex can become difficult and fragile.

A good programmer asks:

> Is this actually a pattern-matching problem?

If yes, regex may be appropriate.

If the problem involves complex structure or meaning, another tool may be better.

---

# 33. The most important lesson

You don't need to become a regex expert before you can use regex.

Start with these:

```text
.       any character
[]      character class
\d      digit
\w      word character
\s      whitespace
*       zero or more
+       one or more
?       optional
{n,m}   repetition range
^       beginning
$       end
()      group
|       OR
\       escape
```

Then practice combining them.

For example:

```text
^[A-Za-z]+\d{2}$
```

looks complicated at first.

But after learning the building blocks, it becomes:

```text
^              start
[A-Za-z]+      one or more letters
\d{2}          exactly two digits
$              end
```

That's all regex really is: **small pieces combined to describe a pattern.**

---

# Final advice

When learning regular expressions, don't begin by memorizing giant expressions from the internet.

Instead, learn to ask three questions:

1. **What characters am I looking for?**
2. **How many times can they occur?**
3. **Where must the match begin and end?**

Then add groups, alternatives, and advanced features as your needs grow.

Once you can look at a regex and translate it into plain English, you've crossed the biggest hurdle.

Regex stops looking like a strange collection of symbols and starts looking like what it really is:

**a compact language for describing patterns in text.**
