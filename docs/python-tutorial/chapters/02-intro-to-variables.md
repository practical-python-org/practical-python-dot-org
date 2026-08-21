---
description: Introduction to Python variables.
---

# Introduction to Variables

??? note "Brief on Computer RAM"

    In this chapter, we will also be talking about Random Access Memory (RAM) to better understand
    variables, but first, let's quickly cover what it is. RAM is where your computer stores data while a
    program is running. It is fast, but volatile (wiped when power is lost, unlike disk storage).
    Whenever you run your Python program, it loads it into the RAM and the instructions are then fed to
    the CPU by your operating system.

Variables give programmers an easy way to work with the computer's memory - they act as a bridge
that lets us use and manipulate memory without dealing with it directly. That is all variables do.
Different languages have different syntax, rules, types of variables, etc., but in the end, they are
all doing the same task. As far as we are concerned, Python does not have multiple types of
variables.

Let's take a look at how we can define a variable in python:

```python
name = "Alan"
```

Let's break this down. Over here, `name` is what we call a variable. `"Alan"` is the data we're
assigning to that variable through the assignment operator (`=`).

!!! note

    We will learn more about data types and operators in later chapters. We will be focusing mostly on
    variables for now.

So, where does the memory that we discussed before come into play here? When we create a variable in
Python, it automatically reserves some space in memory and places the data there, which the variable
then points to.

<figure markdown="span">

![Image title](/static/python-tutorial/02-memory.png){ width="600" }

<figcaption>
    The numbers indicate memory addresses and `~` indicate some random data from other programs,
    irrelevant to us. You can imagine memory addresses in a similar concept to your house address.
    They both are used to locate the whereabouts.
</figcaption>

</figure>

!!! note

    The above image is only an example of how variables point to memory addresses. Note that it is not a
    complete representation of how computer memory looks like. Only meant for understanding purposes.

From the diagram above, the variable `name` points to the memory addresses `3` - `6`, but in our
previous example code, we never had to specify it! That's because python keeps track of what
variables point to which memory addresses, hence the whole point of it! Instead of manually keeping
track of which data point to what memory locations, we can use variables which provide a clear way
for us to label certain parts of the memory for specific uses.

Now that we understand why we use variables, we must also know the rules for declaring variables in
Python. There are 4 simple rules which follow:

1. Variables cannot contain any special characters other than underscore (`_`).
1. Variables cannot have spaces in them, use underscores instead.
1. Variables cannot start with a number but can contain numbers inside or at the end of them.
1. Variables cannot share the same names as Python keywords (keywords are reserved words with
   special functionality in Python).

!!! note "Case Sensitivity"

    Python is a case sensitive language, meaning, in this piece of code:

    ```python
    name = "Zeed"
    Name = "Stun"
    ```

    There now exists two variables, `name` and `Name` instead of one. A good rule of thumb is to always
    use `snake_casing` convention for your variables which is to keep your variables in all lower cases
    and use underscores for word separation.

## Examples

Here is a list of **invalid** python variables:

```python
full name = "James Bond"  # Contains a space
age! = 90  # Contains a special character
finally = "yes"  # Conflicts with the Python keyword "finally"
20money = 900  # Starts with a number
```

Below is a list of **valid** python variables:

```python
full_name = "Bonding Jameful"
age = 90
answer_1 = "yes"
answer_2 = "no"
```
