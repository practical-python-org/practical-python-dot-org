---
description: Install Python, pick an editor, and understand virtual environments.
---

# Getting started

Get a working Python and an editor that helps you. Half the questions in the help
channels are environment problems wearing a costume.

## Install Python

Get 3.12 or newer. I'd avoid any version of python that isn't in the [latest stable release](https://devguide.python.org/versions/). 

=== "Windows"

    Install from [python.org](https://www.python.org/downloads/). Tick **Add
    python.exe to PATH** in the installer — it's off by default and it's the
    single most common cause of "python is not recognized".

    Verify it, using the `py` launcher that ships with the Windows installer:

    ```console
    > py --version
    Python 3.12.7
    ```

    !!! warning "Skip the Microsoft Store version"

        It works, mostly, until it doesn't. Its sandboxing breaks tools that
        expect to write next to the interpreter.

=== "macOS"

    The system Python is there for macOS, not for you. Install your own with
    [Homebrew](https://brew.sh/):

    ```console
    $ brew install python@3.13
    $ python3 --version
    Python 3.13.14
    ```

    Or download the installer from
    [python.org](https://www.python.org/downloads/) if you'd rather not add a
    package manager.

=== "Linux"

    Your distribution has a Python, and it's probably fine for scripts. For
    anything you plan to keep, install a version you control:

    ```console
    $ sudo apt install python3.13 python3.13-venv   # Debian, Ubuntu
    $ sudo dnf install python3.13                   # Fedora
    ```

    The `-venv` package is separate on Debian and Ubuntu, and leaving it out
    breaks virtual environments with a genuinely baffling error.

## Pick an editor

No editor here is better than the others — more features is not the same as more
suitable. Pick one that fits what you're doing now and change later if it starts
getting in the way.

=== "Barely any setup"

    Opens, runs your file, gets out of the way.

    | Editor | Notes |
    |--------|-------|
    | [IDLE](https://docs.python.org/3/library/idle.html) | Ships with Python, so it's already installed. Fine for a first week |
    | [Thonny](https://thonny.org/) | Built for learners. Its variable and step debugger is the best reason to use it |
    | [Zed](https://zed.dev/) | Fast, modern, very little to configure |
    | [Notepad++](https://notepad-plus-plus.org/downloads/) | Windows only. A text editor with syntax highlighting, not an IDE |
    | [PyScripter](https://sourceforge.net/projects/pyscripter/) | Windows only. Lightweight, Python-specific |

=== "General purpose"

    A real editor you'll grow into, without a full IDE's weight.

    | Editor | Notes |
    |--------|-------|
    | [VS Code](https://code.visualstudio.com/) | What most people here use. Install the Python extension first |
    | [VSCodium](https://vscodium.com/) | VS Code without Microsoft's branding and telemetry |
    | [Sublime Text](https://www.sublimetext.com/) | Very fast. Free to evaluate indefinitely, licence requested |
    | [Pulsar](https://github.com/pulsar-edit/pulsar) | Community continuation of Atom |
    | [Neovim](https://neovim.io/) | People who already use Neovim |

=== "Full IDE"

    Refactoring, debugging and project tooling built in. Heavier to start, worth
    it on anything large.

    | Editor | Notes |
    |--------|-------|
    | [PyCharm](https://www.jetbrains.com/pycharm/) | The most capable Python IDE. Free community edition |
    | [Wing](https://wingware.com/) | Python-only IDE with a strong debugger. Free personal edition |
    | [Spyder](https://github.com/spyder-ide/spyder) | Aimed at data and scientific work, MATLAB-ish layout |

!!! tip "Don't shop for long"

    An hour comparing editors is an hour not spent writing Python. Take VS Code
    if you have no opinion yet.

## Virtual environments

A virtual environment is a per-project copy of Python's package directory.
Without one, every project shares one set of packages, and two projects that need
different versions of the same library can't both work.

=== "venv (built in)"

    ```console
    $ python3 -m venv .venv
    $ source .venv/bin/activate      # macOS, Linux
    $ .venv\Scripts\activate         # Windows
    (.venv) $ pip install requests
    ```

    The `(.venv)` prefix means it's active. If it isn't there, `pip install` is
    installing somewhere you didn't intend.

=== "uv (faster)"

    [uv](https://docs.astral.sh/uv/) replaces `pip` and `venv` with one much
    faster tool, and it manages Python versions too:

    ```console
    $ uv init myproject
    $ cd myproject
    $ uv add requests
    $ uv run main.py
    ```

    `uv run` activates the environment for you, so there's nothing to forget.
    Our own projects use it — see [Eos](../projects/our-projects/eos.md).

!!! tip "Add .venv to .gitignore"

    A virtual environment is build output. It's large, it's platform-specific,
    and committing it will earn you comments on your first pull request.

## Where to go next

The [learning path](learning-path.md) has material sorted by level, and the
[cheat sheets and tools](cheat-sheets.md) page has the things worth keeping in a
browser tab. If you're already stuck on something,
[ask well](asking-good-questions.md) and you'll get an answer.
