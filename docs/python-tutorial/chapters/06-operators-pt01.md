---
description: Comparison and Arithmetic Operations in Python.
---

# Comparison and Arithmetic Operations

A quick revision on what all concepts we have learned so far:

- Brief on Python history
- Variables
- Data types (strings, integers, floats, booleans)
- String concatenation & interpolation

In this chapter we will be looking at what comparison and arithmetic operations are.

## Comparison Operators

Comparison Operators (also known as Relational Operators), are used to compare values. They're very
similar to how they're in mathematics.

There are six types of comparison operators as follows:

| Operator Symbol  | Name                          |
| ---------------- | ----------------------------- |
| `>`              | Greater Than                  |
| `<`              | Lesser Than                   |
| `==`             | Equal To                      |
| `!=`             | Not Equal To                  |
| `>=`             | Greater Than Or Equal To      |
| `<=`             | Lesser Than Or Equal To       |

Comparison operators always return a boolean values (`True` or `False`) when used.

<figure markdown="span">

![Image title](/static/python-tutorial/06-operators.png){ width="640" }

<figcaption>
    The either side of the operator is what we call an operand.
</figcaption>

</figure>

### Greater Than Operator (`>`)

Checks if the left hand side operand is larger than the right hand side operand.

```py
print(1 > 2)
print(20 > 1)
print(3.2 > 9)
```

Running this will give us the following output: ```text False True False ```

This reads almost like plain English! 1 is not greater than 2, hence it returns and prints out
`False`. 20 is larger than 1, which results the output being `True`, and so on.

### Lesser Than Operator (`<`)

Checks if the right hand side operand is larger than the left hand side operand.

```py
print(3 < 9)
print(200 < 100)
print(23.12 < 9)
```

Output:

```text
True
False
False
```

### Equal To Operator (`==`)

Checks if both left and right hand side operands are exactly equal.

```py
print(123 == 321)
print(909 == 909)
print(812 == 22)
```

Output:

```text
False
True
False
```

!!! warning

    Do not confuse between the Equivalence Operator (`==`) and the Assignment Operator (`=`). The
    Equivalence Operator is used to check if both the operands are equal, whereas the Assignment
    Operator is used to assign data to a variable.

### Not Equal To Operator (`!=`)

Checks if both the operands are _not_ equal.

```py

print(10 != 10)
print(3 != 4)
print(3 != 8)
```

Output:

```text
False
True
True
```

### Greater Than Or Equal To Operator (`>=`)

Checks if the left hand side operand is either greater than or equal to the right hand side operand.

```py
print(90 >= 18)
print(23 >= 32)
print(1 >= 0)
```

Output:

```text
True
True
False
```

Here, 90 is greater than 18 which gives us `True` as the output. 23 is not greater but it is equal
to 23 which also gives us `True` as the output.

### Lesser Than Or Equal To Operator (`<=`)

Checks if the right hand side operand is either greater than or equal to the left hand side operand.

```py
print(4 <= 18)
print(9 <= 3)
print(10 <= 10)
```

Output:

```text
True
False
True
```
