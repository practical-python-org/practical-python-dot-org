---
date: 2026-10-10
authors:
  - xarlos
description: Python 3.15 is out. Lazy imports, frozendict, unpacking in comprehensions, UTF-8 by default and a new profiler.
categories:
  - Python releases
---

# Python 3.15 is out

Python 3.15.0 was released on 9 October 2026. It adds a `lazy` keyword for imports, a built-in
`frozendict`, `*` unpacking inside comprehensions, and a new sampling profiler. It also makes UTF-8
the default text encoding on every platform, which is the change most likely to affect code you have
already written.

<!-- more -->

Everything below comes from the official
[What's new in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html), which is the full
list. This is the short one.

## The parts you will notice

### Lazy imports

Put `lazy` in front of an import and the module is not loaded until you first use the name
([PEP 810](https://peps.python.org/pep-0810/)).

```python
lazy import json
lazy from pathlib import Path

print("Starting up...")  # json and pathlib are not fully imported yet

data = json.loads('{"key": "value"}')  # json gets fully imported here
p = Path(".")  # pathlib gets fully imported here
```

This is for programs with slow startup, mostly command-line tools that import a lot and use a little
of it on any one run. The catch: if the module is missing, the error turns up at first use, not on
the import line. A typo in a lazy import can sit there until that code path runs.

### `frozendict`

A dictionary you can't change, and can therefore hash
([PEP 814](https://peps.python.org/pep-0814/)). It is a built-in, so there is nothing to import.

```pycon
>>> a = frozendict(x=1, y=2)
>>> a
frozendict({'x': 1, 'y': 2})
>>> a['z'] = 3
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    a['z'] = 3
    ~^^^^^
TypeError: 'frozendict' object does not support item assignment
>>> b = frozendict(y=2, x=1)
>>> hash(a) == hash(b)
True
>>> a == b
True
```

Being hashable means it can be a dictionary key or a member of a set, which a `dict` can't. It keeps
insertion order but ignores it when comparing, same as `dict`. It is not a subclass of `dict`, so
`isinstance(a, dict)` is `False`.

### Unpacking in comprehensions

`*` and `**` now work inside comprehensions and generator expressions
([PEP 798](https://peps.python.org/pep-0798/)).

```pycon
>>> lists = [[1, 2], [3, 4], [5]]
>>> [*L for L in lists]  # equivalent to [x for L in lists for x in L]
[1, 2, 3, 4, 5]

>>> dicts = [{'a': 1}, {'b': 2}, {'a': 3}]
>>> {**d for d in dicts}  # equivalent to {k: v for d in dicts for k,v in d.items()}
{'a': 3, 'b': 2}
```

Flattening a list of lists is one of the most-asked questions in the server. The old answer was a
comprehension with two `for` clauses in an order nobody remembers. This one reads the way you would
say it.

### Error messages

`AttributeError` now recognises method names from other languages and tells you the Python one:

```pycon
>>> [1, 2, 3].push(4)
AttributeError: 'list' object has no attribute 'push'. Did you mean '.append'?

>>> 'hello'.toUpperCase()
AttributeError: 'str' object has no attribute 'toUpperCase'. Did you mean '.upper'?

>>> {}.put("a", 1)
AttributeError: 'dict' object has no attribute 'put'. Use d[k] = v.

>>> (1, 2, 3).append(4)
AttributeError: 'tuple' object has no attribute 'append'. Did you mean to use a 'list' object?
```

If you came to Python from JavaScript or Java, this one is for you.

## The part that can break things

Python now uses UTF-8 whenever you don't pass `encoding`
([PEP 686](https://peps.python.org/pep-0686/)). So `open("notes.txt")` reads UTF-8 on every
platform.

On Linux and macOS that was almost always the case already. On Windows the default used to be the
system code page, so a script that reads a file written by an older Windows program may now raise
`UnicodeDecodeError`, or quietly read the wrong characters.

| Situation                              | What to do                                         |
|----------------------------------------|----------------------------------------------------|
| New code                               | Pass `encoding="utf-8"` anyway. It works on every version |
| Old file in a legacy encoding          | Name it: `open(path, encoding="cp1252")`           |
| Need the old behaviour for a whole run | Set `PYTHONUTF8=0` or run with `-X utf8=0`         |

## For people who measure things

There is a new `profiling` package ([PEP 799](https://peps.python.org/pep-0799/)).
`profiling.tracing` is the deterministic profiler you know as `cProfile`, which stays as an alias.
`profiling.sampling` is new. It is a sampling profiler called Tachyon that can attach to a process
that is already running, by PID, and write flame graphs. The pure-Python `profile` module is
deprecated and goes away in 3.17.

The experimental JIT compiler got a significant upgrade as well. It is still experimental.

## Smaller things

- A `sentinel` built-in for making unique marker values, the job `object()` has been doing
  ([PEP 661](https://peps.python.org/pep-0661/)).
- `re.prefixmatch()` is the new name for what `re.match()` does. `re.match()` still works and is
  soft deprecated, meaning no removal is planned.
- The `__cached__` module attribute is gone. Use `__spec__.cached`.
- Typing gained `TypedDict` with typed extra items ([PEP 728](https://peps.python.org/pep-0728/))
  and `TypeForm` ([PEP 747](https://peps.python.org/pep-0747/)).
- The official macOS installer now includes the free-threaded build by default.

## Should you upgrade?

| You are                               | Suggestion                                                      |
|---------------------------------------|-----------------------------------------------------------------|
| Learning, on your own machine         | Yes. The error messages alone are worth it                      |
| Working on a project with dependencies | Try it in a fresh virtual environment first. Packages with compiled parts can take a few weeks to publish 3.15 builds |
| Running something in production       | Wait for 3.15.1 unless you need a feature now                   |

Python 3.14 is supported until October 2030, so nobody has to hurry.

## Trying it

Installers are on [python.org](https://www.python.org/downloads/). With
[uv](https://docs.astral.sh/uv/), which keeps versions side by side without touching the one you
already have:

```console
$ uv self update
$ uv python install 3.15
$ uv run --python 3.15 python
```

Update uv first. A copy from before the release only knows about the release candidates.

Then type `[1, 2, 3].push(4)` and see what it says.
