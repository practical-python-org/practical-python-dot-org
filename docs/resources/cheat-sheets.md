---
description: Quick references and small tools worth keeping in a browser tab.
---

# Cheat sheets and tools

Things you look at for thirty seconds and then close. None of this teaches you
Python — it saves you from re-learning the same syntax every few weeks.

## Quick reference

| Reference | Covers |
|-----------|--------|
| [Python module index](https://docs.python.org/3/py-modindex.html) | Every module in the standard library, alphabetically. The official answer to "is there something built in for this?" |
| [OverAPI Python](https://overapi.com/python) | One dense page of syntax, built-ins and common methods |
| [W3Schools Python](https://www.w3schools.com/python/default.asp) | One short page per topic, each with an example you can run |
| [fstring.help](https://fstring.help/cheat/) | Formatting inside f-strings — padding, alignment, decimal places, dates |
| [pyreadiness.org](https://pyreadiness.org/) | Which popular packages support which Python version. Check before upgrading |
| [Selenium quick reference](https://github.com/Red-xcv420/Selenium_Docs) | Community-written Selenium notes, from someone here |

!!! warning "Check the Python version"

    Cheat sheets rot quietly. If something on one of these contradicts
    [the official docs](https://docs.python.org/3/), the docs win.

## Small tools

| Tool | Use it when |
|------|-------------|
| [JSON Formatter](https://jsonformatter.curiousconcept.com/) | An API handed you one unreadable line of JSON and you need to see its shape |
| [Regex Tester](https://www.regextester.com/) | You're writing a pattern. Paste a real string, watch the matches highlight, adjust |
| [pyreadiness.org](https://pyreadiness.org/) | A package won't install and you suspect your Python version is too new |
| [Visual TK](https://visualtk.com/) | Laying out a `tkinter` window by dragging, then taking the generated code as a starting point |

Treat generated GUI code as a first draft. It gets a window on screen; it won't
be organised the way you'd organise it.

## Learning git

Git isn't Python, and it will still take up a week of your life eventually.

[Learn Git Branching](https://learngitbranching.js.org/) is the best free
introduction we know of. It draws the commit graph as you type real commands,
which turns `rebase` and `merge` from incantations into something you can see.

Do the "Introduction Sequence" before your first pull request and most of the
scary parts of git stop being scary.

## Where to go next

The [learning path](learning-path.md) has material sorted by level, and the
[project briefs](../projects/build-something/index.md) give you something to
point all this at.
