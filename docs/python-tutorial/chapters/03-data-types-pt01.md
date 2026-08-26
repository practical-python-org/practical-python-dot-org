---
description: Part 1 of Python Data Types
---

# Data Types Part 01

From our previous chapter, we learned about variables with a small primer on data types. In this
chapter we will understand what they are and how we use them.

## What are data types?

In Python, we can define a data type to be a concrete representation of any value. A value could be
someone's name, money, age, or even a game boss's HP.

## String Data Type

Let's take the example from our previous chapter:

```python
name = "Alan"
```

From here, `"Alan"` is what we call the string data type. It is used to represent textual data
within its quotes (`"`). Python strings can use both double and single quotes, but the opening and
closing quote must match.

Examples of **valid** strings:

```python
country = "New Zealand"
capital = 'Wellington'
```

Examples of **invalid** strings:

```python
language = 'English"
favourite_colour = "Purple'
```

## Integer Data Type

Just like in mathematics, we have an integer data type in Python. An integer is a number that can be
written without a fractional or decimal component.

Example:

```python
age = 34
player_hp = 90
player_hp_max = 100
```

## Floating Point Data Type

Floating Point data type, more commonly called Float, is a data type representing decimal numbers.

Example:

```python
wallet_money_amount = 124.43
bank_money_amount = 33.2
```

## Boolean Data Type

Boolean (or bool) is a special data type in Python. A boolean can only be one of two values: `True`
or `False`.

Example:

```python
is_running = True
is_flying = False
```

!!! warning

    `True` and `False` are case sensitive. `true` is **not** the same as `True`.

Booleans are more commonly used in conditional statements, loops and comparison operators which we
will learn in later chapters as a continuation.
