---
description: Built-in Functions Part 1
---

# Built-in Funcitons Part 1

!!! note

    This chapter will only cover how to use some built-in functions so for now consider functions as
    helper code which does some specific task and is pre-written for you to use. You will learn about
    functions in great detail later in this tutorial so don't worry about that for now.

Python has many built-in functions which you can use to make your life easier. In this section we will
take a look at `print`, `input` and some type casting functions in detail.

## `print()`

`print` function is used to print / show something on the screen also known as the terminal or standard
output. With this you can write the first program that every programmer writes when they learn a new
language:

```python
print("Hello World!") # Output: Hello World!
```

This line of code will print `Hello World!` on your screen. You can also print any datatype (`int`,
`float`, `string`) using `print`.

```python
print("My name is Alex") # Output: My name is Alex
print(56) # Output: 56
print(3.14) # Output: 3.14
print(False) # Output: False
```

You can also print the data currently present in a variable using `print`.

```python
a = 5
print(a) # Output: 5
a = "python"
print(a) # Output: python
```

Each `print` statement prints on a new line. You can print multiple things using a single `print`
statement by separating them using `,`s which will result in all the values being printed on the
same line separated by spaces.

```python
print("Value of pi is", 3.14) # Output: Value of pi is 3.14
```

!!! note

    Keep in mind that this works only in `print` and can NOT be used to combine different strings
    or variables with strings otherwise.

## `input()`

`input` function is used to take input from the user through the terminal also known as the standard
input. It returns everything the user types until the user hits `Enter` on the keyboard. You can also
give a `string` to the `input` function which will be displayed on the screen while taking the input.
For example:

```python
input("Enter your name: ")
```

The above code will print `Enter your name: ` followed by a blinking cursor where you can type the
actual input. Now to actually use the value the user entered you need to assign the value returned
by the `input` function to a variable.

```python
name = input("Enter your name: ")
print(name)
```

The `input` function returns the input as a `string` so the variable `name` will be of type `string`.
The output of above code will be whatever the user entered.

## Type Casting

Now you know how to take input from the user, but, the `input` function returns a `string` no matter
what the user types. So for example if the user types `54`, it will return a `string` (`"54"`) not an
`int` (`54`). So if you want to use the number the user entered, you will need to convert the `string`
returned by `input` to an `int`. This process of converting one data type to another is called **type
casting**.

There are two types of type casting:

1. **Implicit Type Casting**: It is done automatically by `python` when it is needed.
2. **Explicit Type Casting**: It is done manually by the programmer.

### Explicit Type Casting

Python has many built-in functions for explicit type casting and they are often named the same as the
data type it casts to. Here is the list of type casting functions with the type it casts to:

| Function  | Type |
|-----------|------|
| `bool()`  | `bool` |
| `float()` | `float` |
| `int()`   | `int` |
| `str()`   | `string` |

For example to get a number from the user you can do:

```python
number_string = input("Enter a number: ")
number_int = int(number_string)
```

Similarly you can use other functions according to the data type you need.
