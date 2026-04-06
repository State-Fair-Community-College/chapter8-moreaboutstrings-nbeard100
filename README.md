[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9BSZIVV5)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23436665)
# 📘 Chapter 8: More About Strings
### *Starting Out with Python — Textbook Companion & Practice Guide*

---

## 📚 Table of Contents

1. [Basic String Operations](#1-basic-string-operations)
2. [Accessing Individual Characters](#2-accessing-individual-characters)
3. [String Concatenation](#3-string-concatenation)
4. [Strings Are Immutable](#4-strings-are-immutable)
5. [String Slicing](#5-string-slicing)
6. [The `in` Operator with Strings](#6-the-in-operator-with-strings)
7. [String Testing Methods](#7-string-testing-methods)
8. [String Modification Methods](#8-string-modification-methods)
9. [Searching Strings](#9-searching-strings)
10. [The Repetition Operator](#10-the-repetition-operator)
11. [Splitting Strings and Tokens](#11-splitting-strings-and-tokens)

---

## 1. Basic String Operations

Strings are one of the most commonly used data types in Python. Because strings are **sequences** — just like lists — many of the same tools that work on lists also work on strings: indexing, slicing, the `in` operator, `len()`, and `for` loops.

> 💡 Think of a string as a list of individual characters, each sitting at a numbered position starting at `0`.

---

## 2. Accessing Individual Characters

Every character in a string has an **index** — a number that identifies its position, starting at `0`.

### Using Indexing

```python
my_string = 'Roses are red'
#            0123456789...

print(my_string[0])   # Output: R
print(my_string[6])   # Output: a
print(my_string[-1])  # Output: d  (last character)
```

### Using a `for` Loop

Use a `for` loop when you need to visit every character in a string:

```python
word = 'Hello'
for character in word:
    print(character)
# Output:
# H
# e
# l
# l
# o
```

### Using `len()` with Strings

`len()` returns the total number of characters in a string — including spaces and punctuation:

```python
message = 'Hello, World!'
print(len(message))   # Output: 13
```

> ⚠️ An `IndexError` will occur if you try to access an index that is out of range. Use `len()` to avoid going past the end of the string.

**Quick Check:**

<details>
<summary>How do you access the first and last character of a string?</summary>

Use index `0` for the first character and `-1` for the last:

```python
name = 'Python'

print(name[0])    # Output: P  (first character)
print(name[-1])   # Output: n  (last character)
print(name[-3])   # Output: h  (third from the end)
```

Negative indexes are especially useful when you don't know how long the string is.

</details>

<details>
<summary>How do you loop through every character in a string?</summary>

Use a `for` loop — Python will automatically move through each character one at a time:

```python
greeting = 'Hi!'
for ch in greeting:
    print(ch)
# Output:
# H
# i
# !
```

You can also use `range(len(string))` if you need the index number as well:

```python
word = 'cat'
for i in range(len(word)):
    print(i, word[i])
# Output:
# 0 c
# 1 a
# 2 t
```

</details>

---

## 3. String Concatenation

**Concatenation** means joining two strings together end-to-end using the `+` operator:

```python
first = 'Hello'
second = ' World'
result = first + second
print(result)   # Output: Hello World
```

The `+=` augmented assignment operator works too:

```python
message = 'Good'
message += ' morning!'
print(message)   # Output: Good morning!
```

> ⚠️ The variable on the left of `+=` must already exist, or Python will raise an exception.

**Quick Check:**

<details>
<summary>How does string concatenation work in Python?</summary>

The `+` operator joins two strings into one new string:

```python
greeting = 'Hello, ' + 'Alice!'
print(greeting)   # Output: Hello, Alice!
```

You can concatenate as many strings as you like in a single expression:

```python
full = 'first' + ' ' + 'middle' + ' ' + 'last'
print(full)   # Output: first middle last
```

Remember: you can only concatenate a string with another string. Trying `'Hello' + 5` will raise a `TypeError` — you'd need `'Hello' + str(5)` instead.

</details>

---

## 4. Strings Are Immutable

Strings in Python are **immutable** — once created, their characters cannot be changed. This is different from lists, which are mutable.

```python
name = 'Carmen'
name[0] = 'D'   # ❌ TypeError — strings don't support item assignment
```

Concatenation doesn't actually modify the existing string. Instead, it creates a **brand new string** and assigns it to the variable:

```python
name = 'Carmen'
name = name + ' Brown'
# 'Carmen' still exists in memory briefly; the variable now points to 'Carmen Brown'
print(name)   # Output: Carmen Brown
```

> 💡 Even though the variable `name` looks like it changed, what really happened is that a new string `'Carmen Brown'` was created and `name` was reassigned to point to it.

**Quick Check:**

<details>
<summary>Why can't you change a single character in a Python string?</summary>

Because strings are **immutable** — Python doesn't allow individual characters to be overwritten once the string is created. This is by design to keep strings safe and efficient.

```python
word = 'cat'
word[0] = 'b'   # ❌ TypeError: 'str' object does not support item assignment
```

The workaround is to build a new string using slicing and concatenation:

```python
word = 'cat'
word = 'b' + word[1:]   # ✅ Creates a new string 'bat'
print(word)              # Output: bat
```

</details>

---

## 5. String Slicing

Just like lists, you can extract a **substring** (a portion of a string) using slicing.

### Syntax

```python
string[start : end]
```

- `start` — index to begin at (inclusive)
- `end` — index to stop at (**exclusive** — not included)

### Examples

```python
name = 'Alexander'

print(name[0:4])    # Output: Alex   (indexes 0–3)
print(name[4:])     # Output: ander  (index 4 to the end)
print(name[:4])     # Output: Alex   (start to index 3)
print(name[-3:])    # Output: der    (last 3 characters)
```

### Step Values

```python
alphabet = 'abcdefghij'
print(alphabet[::2])   # Output: acegi  (every other character)
```

**Quick Check:**

<details>
<summary>How do you extract a substring from a string in Python?</summary>

Use slicing with the format `string[start:end]`. The character at `start` is included, but the character at `end` is not:

```python
phrase = 'Hello, World!'

print(phrase[0:5])    # Output: Hello
print(phrase[7:12])   # Output: World
print(phrase[7:])     # Output: World!
print(phrase[:5])     # Output: Hello
```

A practical use: if you know a full name is `'Jane Smith'` and the space is at index 4, you can slice the first and last name apart:

```python
full = 'Jane Smith'
first = full[:4]    # 'Jane'
last  = full[5:]    # 'Smith'
```

</details>

---

## 6. The `in` Operator with Strings

You can use the `in` operator to check whether one string is contained inside another. It returns `True` or `False`.

```python
sentence = 'The quick brown fox'

print('fox' in sentence)      # Output: True
print('cat' in sentence)      # Output: False
print('cat' not in sentence)  # Output: True
```

This works with single characters too:

```python
print('q' in sentence)   # Output: True
```

**Quick Check:**

<details>
<summary>How do you check if a word or character exists inside a string?</summary>

Use the `in` operator — it searches the entire string and returns `True` or `False`:

```python
email = 'student@school.edu'

print('@' in email)         # Output: True
print('.com' in email)      # Output: False
print('.edu' in email)      # Output: True
```

You can use it in an `if` statement:

```python
if '@' in email:
    print('Looks like a valid email format')
```

</details>

---

## 7. String Testing Methods

Python provides several **Boolean methods** that test a string for specific characteristics. Each one returns `True` or `False`.

### Testing Methods Reference

| Method | Returns `True` if... |
|--------|----------------------|
| `isalpha()` | String contains only letters (no spaces, digits, or symbols) |
| `isdigit()` | String contains only numeric digits |
| `isalnum()` | String contains only letters or digits (no spaces or symbols) |
| `islower()` | All alphabetic characters are lowercase |
| `isupper()` | All alphabetic characters are uppercase |
| `isspace()` | String contains only whitespace (spaces, tabs, newlines) |

### Examples

```python
print('Hello'.isalpha())    # Output: True
print('Hello1'.isalpha())   # Output: False  (contains a digit)

print('12345'.isdigit())    # Output: True
print('12.5'.isdigit())     # Output: False  (contains a period)

print('hello'.islower())    # Output: True
print('Hello'.islower())    # Output: False  (H is uppercase)

print('PYTHON'.isupper())   # Output: True
print('Python'.isupper())   # Output: False
```

> 💡 These methods are commonly used to **validate user input** — for example, checking that a password contains only letters and numbers.

**Quick Check:**

<details>
<summary>What is the difference between isalpha() and isalnum()?</summary>

- **`isalpha()`** returns `True` only if every character is a **letter** (A–Z or a–z). Digits and spaces make it return `False`.
- **`isalnum()`** returns `True` if every character is a **letter OR a digit**. Spaces and symbols still make it return `False`.

```python
print('Hello'.isalpha())     # True  — only letters
print('Hello2'.isalpha())    # False — contains a digit
print('Hello2'.isalnum())    # True  — letters and digits are both OK
print('Hello 2'.isalnum())   # False — space is not a letter or digit
```

Use `isalpha()` when you need letters only (like a name), and `isalnum()` when you need letters or digits (like a username).

</details>

<details>
<summary>How do you use these methods to validate user input?</summary>

Combine them with `input()` and an `if` statement:

```python
user_input = input('Enter your age: ')

if user_input.isdigit():
    age = int(user_input)
    print('Your age is', age)
else:
    print('Please enter numbers only.')
```

Another example — checking that a name contains only letters:

```python
name = input('Enter your name: ')

if name.isalpha():
    print('Valid name!')
else:
    print('Names should contain only letters.')
```

</details>

---

## 8. String Modification Methods

These methods return a **new copy** of the string with some modification applied. Because strings are immutable, the original string is never changed — you work with the returned copy.

### Case Methods

| Method | Description |
|--------|-------------|
| `lower()` | Returns the string with all letters converted to lowercase |
| `upper()` | Returns the string with all letters converted to uppercase |

```python
name = 'Marie Curie'
print(name.lower())   # Output: marie curie
print(name.upper())   # Output: MARIE CURIE
print(name)           # Output: Marie Curie  (original unchanged)
```

### Whitespace Stripping Methods

| Method | Description |
|--------|-------------|
| `strip()` | Removes leading AND trailing whitespace |
| `lstrip()` | Removes leading (left-side) whitespace |
| `rstrip()` | Removes trailing (right-side) whitespace |
| `strip(char)` | Removes a specific character from both ends |

```python
messy = '   hello world   '
print(messy.strip())    # Output: 'hello world'
print(messy.lstrip())   # Output: 'hello world   '
print(messy.rstrip())   # Output: '   hello world'
```

> 💡 `lower()` and `upper()` are very useful for **case-insensitive comparisons**. For example, `user_input.lower() == 'yes'` will match `'Yes'`, `'YES'`, and `'yes'` equally.

**Quick Check:**

<details>
<summary>How do you make a case-insensitive comparison in Python?</summary>

Convert both strings to the same case before comparing using `lower()` or `upper()`:

```python
response = input('Do you want to continue? (yes/no): ')

if response.lower() == 'yes':
    print('Continuing...')
else:
    print('Stopping.')
```

This way, whether the user types `YES`, `Yes`, or `yes`, the condition still works correctly.

</details>

<details>
<summary>What does strip() do and when would you use it?</summary>

`strip()` removes any **spaces, tabs, or newlines** from the beginning and end of a string. It does not remove spaces in the middle.

```python
raw = '   hello world   '
clean = raw.strip()
print(clean)           # Output: hello world
print(len(raw))        # Output: 17
print(len(clean))      # Output: 11
```

This is especially useful when processing **user input** or **file data**, where extra whitespace often sneaks in accidentally:

```python
name = input('Enter your name: ').strip()
# Now leading/trailing spaces won't cause comparison issues
```

</details>

---

## 9. Searching Strings

Python provides several methods to **search inside** a string.

### Search Methods Reference

| Method | Description |
|--------|-------------|
| `find(substring)` | Returns the **lowest index** where the substring is found, or `-1` if not found |
| `startswith(substring)` | Returns `True` if the string begins with the given substring |
| `endswith(substring)` | Returns `True` if the string ends with the given substring |
| `replace(old, new)` | Returns a copy of the string with every occurrence of `old` replaced by `new` |

### Examples

```python
sentence = 'The quick brown fox jumps over the lazy dog'

print(sentence.find('fox'))         # Output: 16
print(sentence.find('cat'))         # Output: -1  (not found)

print(sentence.startswith('The'))   # Output: True
print(sentence.endswith('dog'))     # Output: True

print(sentence.replace('fox', 'cat'))
# Output: The quick brown cat jumps over the lazy dog
```

> 💡 `find()` returns `-1` when the substring isn't found — **not** an error. You can use this in an `if` statement: `if sentence.find('fox') != -1`.

**Quick Check:**

<details>
<summary>What does find() return and how is it different from the in operator?</summary>

- The `in` operator returns `True` or `False` — it just tells you whether the substring exists.
- `find()` returns the **index** (position) where the substring starts, or `-1` if it's not found.

```python
text = 'Hello, World!'

# in operator — True/False only
print('World' in text)       # Output: True

# find() — tells you WHERE it is
print(text.find('World'))    # Output: 7
print(text.find('Python'))   # Output: -1
```

Use `in` when you just need to know if something is there. Use `find()` when you also need to know *where* it is.

</details>

<details>
<summary>How does replace() work — does it change the original string?</summary>

No — `replace()` returns a **new string** with the substitutions made. The original string is unchanged because strings are immutable.

```python
message = 'I like cats. Cats are great.'
new_message = message.replace('cat', 'dog')

print(new_message)   # Output: I like dogs. Dogs are great.
print(message)       # Output: I like cats. Cats are great.  (unchanged)
```

Note: `replace()` is **case-sensitive** — `'cat'` and `'Cat'` are treated as different substrings.

</details>

---

## 10. The Repetition Operator

The `*` operator can make multiple copies of a string and join them together:

```python
print('ha' * 3)      # Output: hahaha
print('-' * 20)      # Output: --------------------
```

The string goes on the left, and the number of copies goes on the right:

```python
separator = '=' * 30
print(separator)     # Output: ==============================
```

> 💡 This is handy for creating formatted output — like printing a line of dashes as a divider between sections.

---

## 11. Splitting Strings and Tokens

The `split()` method breaks a string into a **list of substrings** by dividing it at a separator character.

### Default — Split on Spaces

```python
sentence = 'One two three four'
words = sentence.split()
print(words)   # Output: ['One', 'two', 'three', 'four']
```

### Split on a Custom Delimiter

Pass a character as an argument to split at that character instead:

```python
data = '1/2/3/4/5'
numbers = data.split('/')
print(numbers)   # Output: ['1', '2', '3', '4', '5']
```

### Tokens and Delimiters

When a string contains substrings separated by a special character, those substrings are called **tokens** and the separator is called a **delimiter**.

```python
flavors = 'peach raspberry strawberry vanilla'
tokens = flavors.split()
print(tokens)
# Output: ['peach', 'raspberry', 'strawberry', 'vanilla']

address = 'www.example.com'
parts = address.split('.')
print(parts)
# Output: ['www', 'example', 'com']
```

Once split, you can loop through the tokens just like any list:

```python
for flavor in tokens:
    print(flavor)
```

**Quick Check:**

<details>
<summary>How does split() work and what does it return?</summary>

`split()` divides a string into pieces wherever it finds the delimiter and returns those pieces as a **list**:

```python
csv = 'Alice,85,92,78'
parts = csv.split(',')
print(parts)        # Output: ['Alice', '85', '92', '78']
print(parts[0])     # Output: Alice
print(parts[1])     # Output: 85
```

By default (no argument), it splits on any whitespace and removes extra spaces automatically:

```python
messy = '  hello   world  '
words = messy.split()
print(words)   # Output: ['hello', 'world']
```

</details>

<details>
<summary>What is a token and what is a delimiter?</summary>

A **token** is a meaningful chunk of data inside a string. A **delimiter** is the character that separates the tokens.

```python
# Delimiter is ';'  — tokens are the numbers
data = '17;92;81;12;46;5'
tokens = data.split(';')
print(tokens)   # Output: ['17', '92', '81', '12', '46', '5']

# Delimiter is '.'  — tokens are the URL parts
url = 'www.example.com'
tokens = url.split('.')
print(tokens)   # Output: ['www', 'example', 'com']
```

Tokenizing is used constantly in real programs — reading CSV files, parsing URLs, processing user input, and more.

</details>

---

## 📝 Key Terms Summary

| Term | Definition |
|------|------------|
| **Index** | A number identifying a character's position in a string (starts at 0) |
| **Substring** | A portion of a string |
| **Concatenation** | Joining two strings together using `+` |
| **Immutable** | Cannot be changed after creation — strings are immutable |
| **Slice** | A portion of a string extracted using `[start:end]` |
| **Token** | A meaningful chunk of data within a string |
| **Delimiter** | The character used to separate tokens in a string |
| **`split()`** | Method that breaks a string into a list of substrings |
| **`find()`** | Returns the index of a substring, or `-1` if not found |
| **`replace()`** | Returns a new string with occurrences of a substring swapped out |
| **`strip()`** | Removes leading and trailing whitespace from a string |
| **Boolean method** | A method that returns `True` or `False` (e.g., `isalpha()`, `isupper()`) |

---

*Chapter 8 — Starting Out with Python, Fifth Edition by Tony Gaddis*
