---
description: Part 1 of Built-in Functions
---

# Built-in Functions Part 01

## What are built-in functions?

A function is a reusable block of code that performs a specific task. You give it some input
(sometimes), it does something with it, and it gives you back a result. Python has many built-in
functions which you can use to make your life easier. In this section, we will take a look at
`print`, `input` and some type-casting functions in detail for this chapter.

## `print()` function

The `print` function is used to show text on the screen (also known as the terminal or standard
output). With this, you can write your first program that every programmer writes when they learn a
new language:

```python
print("Hello World!")
```

When you run this program, it should show `Hello World!` in your terminal. We are not limited to
only strings, we can even print out other kinds of data types!

```python
print("My name is Alex")
print(56)
print(3.14)
print(False)
```

We can also use print variables, which will print out the data present within them!

```python
age = 43
print(age)

language = "python"
print(language)
```

The output of the code above will be:

```text
43
python
```

Each `print` statement prints on a new line. You can print multiple things using a single `print`
statement by separating them using commas (`,`), which will result in all the values being printed
on the same line separated by spaces.

```python
print("Value of pi is", 3.14)
```

This allows us to also print out variables in the same line too.

```python
name = "Radagon"
money = 30
print(name, "has", money, "dollars to his name.")
```

This will print out `Radagon has 30 dollars to his name.`

!!! note

    Keep in mind that the comma separation of values only work in the `print` function.

## `input()` function

The `input` function is used to take input from the user through the terminal. It returns everything
the user types until the user hits the ++enter++ key. You can also pass in a string to the function
which will appear as a prompt before asking for input, like so:

```python
input("Enter your name: ")
```

The above code will print `Enter your name: ` followed by a blinking cursor where you can type the
actual input. Now, to actually use the value entered by the user, you need to assign the value
returned by the `input` function to a variable.

```python
name = input("Enter your name: ")
print("Hello", name, "! Hope you have a wonderful day.")
```

The output of this will be:

```text
Enter your name: Krish
Hello Krish ! Hope you have a wonderful day.
```

!!! note

    You must keep in mind that the `input` function will _always_ return the user input as a string.

## Type Casting

Type casting is the process of converting one data type to another. Remember the note from above?
> You must keep in mind that the `input` function will _always_ return the user input as a string.

There will be scenarios where you need the input function to return a data type other than a string.
One such place could be when you want to make a calculator that adds two numbers. Let's take a look
at how we would do it without any type casting.

```python
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = num1 + num2

print("The sum of", num1, "and", num2, "is", result)
```

If we run this program and enter two numbers, this is the result we would get:

```text
Enter the first number: 23
Enter the second number: 12
The sum of 23 and 12 is 2312
```

As we can see, `23 + 12` is clearly _not_ supposed to be 2312. So what's happening here?

The variables `num1` and `num2` hold a string data type of the user input. When you perform an
addition operation on two strings (`result = num1 + num2`) you are simply joining two strings
together, side-by-side. This is also called string concatenation which we will learn more about in
the next chapter.

This is where type casting comes to fix this problem. We need to convert the string data type to
integer so the computer can follow regular arithmetic for our use case.

```python
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

int_num1 = int(num1)
int_num2 = int(num2)

result = int_num1 + int_num2

print("The sum of", num1, "and", num2, "is", result)
```

Running it now gives the correct result:

```text
Enter the first number: 23
Enter the second number: 12
The sum of 23 and 12 is 35
```

`int_num1 = int(num1)` and `int_num2 = int(num2)` is what we call type casting. We're casting the
input string to an integer, then assigning it to a variable.

Another common way to write the code above is:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2

print("The sum of", num1, "and", num2, "is", result)
```

Both the programs perform the same way, with the only difference being that we aren't creating an
extra variable in the latter. Whenever you see functions being executed within another function:

```python
num1 = int(input("Enter the first number: "))
```

Remember that the innermost function is the one that always executes first. In this case, the
`input` function is the one that fires first. Once the user gives an input, the string input
automatically goes to the `int` function, which then converts the input string to an integer and
assigns it to the `num1` variable.

The example above shows you how to convert user input to an integer. In case you want to use
decimals instead of integers, you can type cast it to `float`.

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 + num2

print("The sum of", num1, "and", num2, "is", result)
```
