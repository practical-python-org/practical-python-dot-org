---
description: Conditional Statements and Control Flow in Python.
---

# Conditional Statements

When developing programs, we often need our code to execute certain instructions _conditionally_.
Let's take a simple banking program as an example.

Our task is to ask the user how much money they have so they can open a bank account. If they have
less than `$25`, we print a message declining the request. If they have `$25` or more, we accept the
money and deposit it into their new account.

One way of doing this problem is like so:

```python
bank_amount = 0

print("Welcome to Practical Python Bank!")
print("Let's open you an account for you!")

current_amount = int(input("How much money do you have (in dollars)? "))
# Don't forget to convert user input to an integer
# so we can compare it with another integer.

if current_amount >= 25:
    bank_amount += current_amount
    current_amount = 0

    print("You have successfully opened a bank account!")
    print("All your money has been deposited.")
    print(f"You have ${bank_amount} in your account.")

else:
    print("Sorry, you cannot open an account.")
    print("You need at least $25 dollars to open a bank account.")
```

Running the program and entering a number below 25 gives us:

```
Welcome to Practical Python Bank!
Let's open you an account!
How much money do you have (in dollars)? 10
Sorry, you cannot open an account.
You need at least $25 dollars to open a bank account.
```

Now let's enter a value of 25 or more:

```
Welcome to Practical Python Bank!
Let's open you an account!
How much money do you have (in dollars)? 25
You have successfully opened a bank account!
All your money has been deposited.
You have $25 in your account.
```

!!! warning

    When entering input, type only the number itself, with no `$` symbol or other characters. The
    `int()` function can only convert strings that look like whole numbers (such as `"25"`), so text or
    symbols (such as `"$25"` or `"twenty"`) will make it fail with an error. The same applies to
    `float()`, which accepts numbers like `"12.5"`.

The code almost reads like plain English! If you don't understand what's going on immediately, it's
alright. We'll take it apart and see what each piece is doing. First, the `if` statement.

## `if` Condition Statement

This is the starting block of any conditional statement. Its general syntax is:

```
if <bool>:
    <code>
```

!!! note

    In programming, syntax refers to the grammar of a language. Just as grammar lets us form coherent
    sentences in human languages, syntax tells the computer how to read our code.

The `if` condition statement only runs the `<code>` within it when the `<bool>` is `True`. Here's an
example:

```python
if True:
    print("Hi")
    print("Running from the True statement")
    print("Good bye!")

if False:
    print("Hello")
    print("Running from the False statement")
    print("See you later!")
```

Upon running this code, we get the following output:

```text
Hi
Running from the True statement
Good bye!
```

The code within the `if False:` statement never ran.

One important thing you may have noticed so far is the indentation (the four spaces in front of each
`print` calls). In Python, indentation is what tells the computer that "this block of code belongs
to this statement".

<figure markdown="span">

![Image title](/static/python-tutorial/07-conditional-statements-01.png){ width="640" }

</figure>

A quick way to remember when you need to apply indentation is to look out for colons (`:`). If a
statement ends with a colon, it means that the next line must be indented one level further. Python
recommends 1 indent to consist of 4 spaces.

!!! warning

    You can press the ++tab++ key to place indents in your code. Depending on the code editor you use,
    it can either place spaces or a single `Tab` character. If your editor places a `Tab` character,
    make sure to change it to spaces.

From the previous chapter we have learned about how Comparison Operators return a bool. The same
concept is being used here. Let's take a look at an example and an animation that explains how it
works.

```python
print("Program start")

age = 15

if age >= 13:
    print("Is teenager")

if age >= 18:
    print("Is an adult")

print("Program end")
```

When you run your code, this is how Python would interpret it:

<figure markdown="span">

![Image title](/static/python-tutorial/07-conditional-statements-02.gif){ width="640" }

</figure>
