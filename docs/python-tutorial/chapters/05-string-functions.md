---
description: String concatenation and interpolation in Python
---

# String Interpolation and Concatenation

We learned what the string data type was from our [third chapter](03-data-types-pt01.md). A quick
recap: Strings are used to represent any textual data.

We also saw how adding two inputs resulted in a different output than we expected.

```py
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = num1 + num2

print("The sum of", num1, "and", num2, "is", result)
```

After running the program:

```text
Enter the first number: 23
Enter the second number: 12
The sum of 23 and 12 is 2312
```

We briefly touched on the fact that this was caused by _string concatenation_. In this chapter, we
will look at what concatenation is, and at a more powerful way of combining text and variables
called _string interpolation_.

## Why do we need this?

Most programs need to build sentences out of a mix of fixed text and changing data. For example,
greeting a user by name, or showing a player's score. So far, the only way we've done this is by
passing multiple values to `print`:

```python
name = "Alan"
age = 34

print("My name is", name, "and I am", age, "years old.")
```

This works, but it only works with `print`. What if we want to, for example, store the full sentence
in a variable instead? This is where concatenation and interpolation come in.

## String Concatenation

Concatenation simply means joining two or more strings together, one after the other. In Python, we
can do this with the `+` operator.

```python
first_name = "Alan"
last_name = "Turing"

full_name = first_name + " " + last_name
print(full_name)
```

```text
Alan Turing
```

Notice that we added `" "` (a string containing a single space) in the middle. Concatenation joins
strings _exactly_ as they are, so Python will not add any spaces for us. Without it, we would get
`AlanTuring` as the output.

### Concatenating with other data types

Concatenation only works between strings. This means that if we try to join a string with a number,
Python will raise an error:

```python
name = "Alan"
age = 34

print("My name is " + name + " and I am " + age + " years old.")
```

```text
TypeError: can only concatenate str (not "int") to str
```

Python doesn't know whether `"I am " + 34` should mean "add" or "join", so instead of guessing, it
stops with an error. To fix it, we need to convert the number to a string first. Remember type
casting from the previous chapter? We can use the `str` function for this:

```python
name = "Alan"
age = 34

print("My name is " + name + " and I am " + str(age) + " years old.")
```

```text
My name is Alan and I am 34 years old.
```

## String Interpolation

Interpolation is the process of inserting values directly into a string. Instead of breaking the
string apart and gluing the pieces back together, we write the whole sentence at once and mark the
places where the values should go. Python gives us two ways of doing this.

### f-strings

An f-string (short for _formatted string literal_) is a string with an `f` placed right before the
opening quote. Inside it, anything wrapped in curly braces `{}` is replaced with its value.

```python
name = "Alan"
age = 34

print(f"My name is {name} and I am {age} years old.")
```

```text
My name is Alan and I am 34 years old.
```

That's the same output as before, but much easier to read and write! Also notice that we didn't need
to use `str(age)`. This is because f-strings convert the values for us automatically.

!!! warning

    Don't forget the `f` before the quote! Without it, Python treats the string as normal text and
    prints the curly braces as-is: `My name is {name} and I am {age} years old.`

#### Expressions inside f-strings

You can put any valid Python expression (not just variable names) inside the curly braces, and
Python will work out the result:

```python
price = 20
quantity = 3

print(f"Total cost: {price * quantity}")
```

```text
Total cost: 60
```

#### Formatting values

You can also control how a value is displayed by adding a colon `:` followed by a format
specification inside the braces. One of the most common uses of this is limiting the number of
decimal places of a float:

```python
pi = 3.14159265

print(f"Pi is roughly {pi:.2f}")
```

```text
Pi is roughly 3.14
```

Here, `.2f` means "show this as a float with 2 digits after the decimal point".

### The `str.format()` method

Before f-strings were introduced in Python 3.6, the most common way to interpolate was the `format`
method of strings. You will still see this in a lot of older code, so it is worth knowing.

Instead of placing the variables inside the string, you leave empty curly braces `{}` as
placeholders, and pass the values to `.format()` afterwards. The values are filled in order like so:

```python
name = "Alan"
age = 34

print("My name is {} and I am {} years old.".format(name, age))
```

```text
My name is Alan and I am 34 years old.
```

You can also number the placeholders to control which value goes where, or give them names:

```python
# Using positions
print("{1} is {0} years old.".format(age, name))

# Using names
print("{n} is {a} years old.".format(n=name, a=age))
```

!!! note

    Anything after a `#` on a line is a comment. Comments are notes for humans reading the code, so
    Python ignores them completely.

It's output:

```text
Alan is 34 years old.
Alan is 34 years old.
```

## Which one should I use?

All three approaches produce the same kind of result: a new string. Here's a quick comparison using
the same example.

```python
name = "Alan"
age = 34

print("My name is " + name + " and I am " + str(age) + " years old.") # concatenation
print("My name is {} and I am {} years old.".format(name, age))       # str.format()
print(f"My name is {name} and I am {age} years old.")                 # f-string
```

Here are some general rules for their usage.

- Use **f-string** interpolation for most situations. They are the shortest, the most readable, and
  the most common way to write modern Python.
- Use **concatenation (+)** for simple cases where you want to join two strings only.
- **`str.format()`** when you are reading older code.
