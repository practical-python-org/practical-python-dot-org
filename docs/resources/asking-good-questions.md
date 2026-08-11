---
description: How to ask so that someone can actually answer.
---

# Asking good questions

A good question gets answered in minutes. A bad one sits there while people read it, sigh, and
scroll past. Laziness is not a virtue.

## The short version

Post four things:

1. What you're trying to do.
2. What you did.
3. What happened, including the full error.
4. What you expected instead.

That's it. Most unanswered questions are missing number three.

## Post the whole traceback

Not the last line. The whole thing, from `Traceback (most recent call last)` down. The useful
information is usually in the middle.

```
Traceback (most recent call last):
  File "shopping.py", line 12, in <module>
    total = sum(prices)
            ^^^^^^^^^^^
  File "shopping.py", line 8, in sum
    return a + b
           ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

That tells a helper the bug is in your `sum`, that one of your prices is a string, and which line to
look at. "I get a TypeError" tells them nothing.

## Format your code

Use a fenced block with a language tag. In Discord, three backticks and the language:

````
```python
prices = ["4.99", 3.50]
print(sum(prices))
```
````

!!! failure "Not screenshots"

    [Rule 7](../rules/index.md#7-ask-effective-questions) asks for code as text because helpers need to
    run your code. Nobody is retyping your program from a photograph, and screen readers can't read it
    at all.

## Cut it down first

Post the smallest program that still shows the problem. Deleting code until the bug disappears tells
you where the bug is — you'll often solve it yourself before you finish, which is the best possible
outcome.

If your file is 400 lines and you don't know which part is broken, say so, and post the part you
suspect.

??? example "Before and after"

    **Before** — 200 lines of a Discord bot, one broken function.

    **After:**

    ```python
    def split_name(full):
        first, last = full.split(" ")
        return last

    print(split_name("Guido van Rossum"))   # ValueError, why?
    ```

    Six lines, reproduces the bug, answerable at a glance.

## Say what you already tried

It stops people suggesting it again, and it tells them how you think. "I checked the type with
`print(type(prices[0]))` and it's a string, but I don't see where it became one" is a question
someone will enjoy answering.

## Things that slow you down

| Don't                                    | Why                                                                                              |
|------------------------------------------|--------------------------------------------------------------------------------------------------|
| "Does anyone know Python?"               | Obviously not, this is a server about snakes after all. Ask the actual question. Get on with it. |
| "Can someone DM me?"                     | No, that's so much more effort than just asking the question.                                    |
| Pinging a specific person                | Are you in a conversation with that person? Do you know them? No? Don't ping.                    |
| Deleting your question after it's solved | The next person with your bug wanted to read it, and it makes the chat lame.                     |

## After you get an answer

Say whether it worked. Helpers are debugging blind, and "that fixed it" is the only signal they get.

If it didn't work, say what happened instead.
