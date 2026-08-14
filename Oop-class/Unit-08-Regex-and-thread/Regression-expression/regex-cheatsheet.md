# Regular Expressions (Regex) Cheat Sheet

## 1. Basic Matching

| Regex | Meaning              | Example              |
| ----- | -------------------- | -------------------- |
| `abc` | Literal text         | Matches `abc`        |
| `.`   | Any single character | `c.t` → `cat`, `cot` |

---

## 2. Character Classes

| Regex         | Meaning                 | Example       |
| ------------- | ----------------------- | ------------- |
| `[abc]`       | `a`, `b`, or `c`        | `[abc]` → `a` |
| `[a-z]`       | Any Lowercase letter        | `a`–`z`       |
| `[A-Z]`       | Any Uppercase letter        | `A`–`Z`       |
| `[0-9]`       | Any Digit                   | `0`–`9`       |
| `[A-Za-z]`    | Any English letter      | `A`, `b`, `Z` |
| `[A-Za-z0-9]` | Letter or digit         | `A`, `z`, `5` |
| `[^0-9]`      | Anything except a digit | `a`, `!`, ` ` |

### Important

`^` inside `[]` means **NOT**:

```regex
[^0-9]
```

means "anything except a digit."

>`^` outside [ ]  → beginning
>
> `^` inside [ ]   → NOT

---

# 3. Character Shortcuts

| Regex | Meaning | Example Regex | Matches |
|---|---|---|---|
| `\d` | Digit | `\d` | `0`, `1`, `5`, `9` |
| `\D` | Not a digit | `\D` | `a`, `Z`, `@`, `_` |
| `\w` | Word character | `\w` | `a`, `Z`, `5`, `_` |
| `\W` | Not a word character | `\W` | `@`, `!`, `#`, ` ` |
| `\s` | Whitespace | `\s` | space, tab, newline |
| `\S` | Not whitespace | `\S` | `a`, `5`, `_`, `@` |

---

# 4. Quantifiers

Quantifiers control **how many times** something can occur.

| Quantifier | Meaning | Example Regex | Matches |
|---|---|---|---|
| `*` | Zero or more | `ab*` | `a`, `ab`, `abb`, `abbb` |
| `+` | One or more | `ab+` | `ab`, `abb`, `abbb` |
| `?` | Zero or one | `colou?r` | `color`, `colour` |
| `{n}` | Exactly `n` | `\d{3}` | `123`, `456`, `987` |
| `{n,}` | `n` or more | `\d{2,}` | `12`, `123`, `1234`, `12345`, ... |
| `{n,m}` | Between `n` and `m` | `\d{2,4}` | `12`, `123`, `1234` |
---

# 5. Anchors

Anchors specify **where the match must occur**.

| Regex | Meaning | Example Regex | Matches |
|---|---|---|---|
| `^` | Beginning of string/line | `^hello` | `hello world` |
| `$` | End of string/line | `world$` | `hello world` |

Example:

```regex
^\d+$
```

Means:

> The entire string must contain one or more digits.

Matches:

```text
12345
987
```

Doesn't match:

```text
abc123
123abc
hello 123
```

### Important distinction

```regex
\d{10}
```

means:

> Find ten digits.

Whereas:

```regex
^\d{10}$
```

means:

> The entire string must be exactly ten digits.

---

# 6. Alternation — OR

Use:

```regex
|
```

to mean **OR**.

Example:

```regex
cat|dog
```

Matches:

```text
cat
dog
```

Another example:

```regex
red|green|blue
```

Matches any of:

```text
red
green
blue
```

---

# 7. Groups

Use parentheses:

```regex
(...)
```

to create a group.

Example:

```regex
(ab)+
```

Matches:

```text
ab
abab
ababab
```

Compare:

```regex
ab+
```

which matches:

```text
ab
abb
abbb
```

### Why?

```regex
ab+
```

means:

> `a` + one or more `b`s

But:

```regex
(ab)+
```

means:

> One or more repetitions of `ab`

---

# 8. Capturing Groups

Parentheses can capture part of a match.

Example:

```regex
(\d{4})-(\d{2})-(\d{2})
```

For:

```text
2026-08-09
```

you can capture:

```text
Group 1 → 2026
Group 2 → 08
Group 3 → 09
```

This is especially useful when extracting information in programs.

- Even without the parentheses, the match is the same.
- Both expressions match the same date: 2026-08-09.
- Parentheses () create groups within the regex.
- Groups let you capture individual parts of the match separately, such as year, month, and day.
- Parentheses can also make multiple characters act as one unit for quantifiers.
- Without () → match the pattern; with () → match and group/capture parts.
---

# 9. Non-Capturing Groups

Use:

```regex
(?:...)
```

when you want grouping without capturing.

Example:

```regex
(?:cat|dog)123
```

Means:

> Match `cat` or `dog`, but don't create a capture group. Because we want either `cat123` or `dog123`. Not them separately. However, the parentheses were important to capture the pattern.

---

# 10. Escaping

A backslash `\` gives special meaning to some characters or removes their special meaning.

For example:

```regex
\.
```

means:

> A literal period.

Because:

```regex
.
```

normally means:

> Any character.

### Common escaped characters

| Regex | Matches |
| ----- | ------- |
| `\.`  | `.`     |
| `\+`  | `+`     |
| `\?`  | `?`     |
| `\*`  | `*`     |
| `\(`  | `(`     |
| `\[`  | `[`     |
| `\\`  | `\`     |

---

# 11. Greedy vs Lazy

Most quantifiers are **greedy** by default.

```regex
.*
```

means:

> Match as much as possible.

Add `?` to make it **lazy**:

```regex
.*?
```

which means:

> Match as little as possible.

### Quick comparison

```text
.*     greedy
.*?    lazy
```

This becomes especially important when working with repeated structures such as HTML-like text.

---

# 12. Lookarounds

Advanced feature for checking nearby text without consuming it. It is like saying "Before I match this, let me check what comes next."

### 12.1. Lookahead

```regex
(?=...)
```

Checks what comes **after**.

Example:

```regex
\d+(?= dollars)
```

Can find:

```text
50
```

in:

```text
I paid 50 dollars.
```

In the example, it asked, "Is dollars immediately after me?"

### 12.2. Negative lookahead

```regex
(?!...)
```

Checks that something does **not** come after.

### 12.3. Lookbehind

```regex
(?<=...)
```

Checks what comes **before**.

Example:

```regex
(?<=\$)\d+
```

Can find:

```text
50
```

in:

```text
$50
```

### 12.4. Negative lookbehind

```regex
(?<!...)
```

Checks that something does **not** come before.

---

# 13. Common Patterns

## Only digits

```regex
^\d+$
```

---

## Exactly 10 digits

```regex
^\d{10}$
```

---

## Only letters

```regex
^[A-Za-z]+$
```

---

## Letters, 3–10 characters

```regex
^[A-Za-z]{3,10}$
```

---

## Username: 3–15 letters, digits, underscores

```regex
^[A-Za-z0-9_]{3,15}$
```

---

## Date format: `YYYY-MM-DD`

```regex
^\d{4}-\d{2}-\d{2}$
```

Remember: this checks the **format**, not whether the date is actually valid.

---

## Word beginning with `a`

```regex
\ba\w*
```

`\b` is a word boundary. It is another useful regex concept to learn.

---

## `cat` or `dog`

```regex
^(cat|dog)$
```

The anchors ensure that the entire string is either `cat` or `dog`.

---

# 14. The Most Important Symbols

If you're just starting, memorize these first:

```text
.       Any character

[]      Character class

\d      Digit
\w      Word character
\s      Whitespace

*       Zero or more
+       One or more
?       Zero or one

{n}     Exactly n
{n,m}   Between n and m

^       Beginning
$       End

()      Group
|       OR

\       Escape
```

---

# 15. How to Read a Regex

Take this:

```regex
^[A-Za-z]+\d{2}$
```

Read it piece by piece:

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

Therefore:

> The entire string must contain one or more letters followed by exactly two digits.

Examples:

```text
abc12       ✓
Hello99     ✓
test42      ✓

12345       ✗
abc         ✗
abc123      ✗
hello!      ✗
```

---

# 16. The Three Questions

When creating a regex, ask:

### 1. What characters do I want?

Examples:

```regex
\d
[A-Z]
[aeiou]
```

### 2. How many?

Examples:

```regex
*
+
?
{3}
{2,5}
```

### 3. Where?

Examples:

```regex
^
$
```

Then combine them.

For example:

> "I want exactly five digits, and nothing else."

Start with:

```regex
\d
```

How many?

```regex
\d{5}
```

Where?

```regex
^\d{5}$
```

Final answer:

```regex
^\d{5}$
```

---

# 17. Learning Order

Learn regex in this order:

```text
1. Literal characters
       ↓
2. .
       ↓
3. Character classes []
       ↓
4. \d, \w, \s
       ↓
5. *, +, ?
       ↓
6. {n}, {n,m}
       ↓
7. ^ and $
       ↓
8. Groups ()
       ↓
9. OR |
       ↓
10. Capturing groups
       ↓
11. Escaping \
       ↓
12. Greedy vs lazy
       ↓
13. Lookarounds
```

Don't start with lookarounds or complicated email regexes.

Master the basics first.

---

# 18. Golden Rule

Don't memorize huge regexes.

Instead, learn to **build them from small pieces**.

For example:

```regex
^[A-Za-z0-9_]{3,15}$
```

looks complicated initially.

Break it down:

```text
^
    Start

[A-Za-z0-9_]
    Letter, digit, or underscore

{3,15}
    Repeat 3–15 times

$
    End
```

Therefore:

> The entire string must contain 3–15 letters, digits, or underscores.

That's the key to becoming good at regex:

**Learn the pieces → understand what each piece does → combine them.**
