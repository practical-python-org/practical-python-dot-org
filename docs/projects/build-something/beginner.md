---
description: Three project challenges for people who know the basics and haven't built anything yet.
---

# Beginner challenges

You know loops, functions, lists and dictionaries. Nothing here needs a dependency.

## Unit converter

**Goal.** A command-line tool that converts between units — temperature, length, mass, pick two or
more categories.

**Done when:**

- [ ] It runs from the terminal and asks what you want to convert.
- [ ] It handles at least two categories with three units each.
- [ ] Typing nonsense produces a helpful message, not a traceback.
- [ ] Converting a value and converting it back gives you the original number.

**Stretch.** Accept arguments so `convert 100 c f` works without prompting. Add `argparse`. Support
unit aliases, so `celsius`, `c` and `C` all work.

**Time.** An evening.

!!! tip "The interesting part"

    The conversions are arithmetic. The design question is how you store the units so adding a new one
    doesn't mean writing another `if`. Try a dictionary before you try a class.

## Todo list that survives restarting

**Goal.** Add, list, complete and delete tasks, with the list still there after you close the
program.

**Done when:**

- [ ] Tasks persist to a file between runs.
- [ ] You can add, list, complete and delete.
- [ ] Deleting task 3 doesn't renumber the others in a way that surprises you.
- [ ] Starting with no data file works instead of crashing.

**Stretch.** Due dates. Priorities and sorting. Swap your file format for `sqlite3` from the
standard library.

**Time.** A weekend.

=== "Storing it as JSON"

    ```python
    import json
    from pathlib import Path

    TASKS = Path("tasks.json")

    def load():
        if not TASKS.exists():
            return []
        return json.loads(TASKS.read_text())
    ```

    Readable, editable by hand, and fine up to a few thousand tasks.

=== "Storing it as CSV"

    Simpler to append to, worse at nested data. Use `csv.DictReader` rather than splitting on commas
    yourself — quoting will bite you otherwise.

## Guess-the-number, properly

**Goal.** The classic, done well. The program picks a number and you guess it.

Everyone writes this in ten minutes and then discovers the interesting version takes longer.

**Done when:**

- [ ] It tells you higher or lower, and counts your guesses.
- [ ] Difficulty levels change the range.
- [ ] Non-numeric input doesn't crash it.
- [ ] It offers a rematch without restarting the program.
- [ ] High scores persist between runs.

**Stretch.** Reverse it — you pick, the computer guesses, and it plays optimally. Then explain to
yourself why binary search never needs more than seven guesses for 1 to 100.

**Time.** An evening, then another one for the reverse mode.

## Next

When one of these stops feeling difficult, move to the [intermediate challenges](intermediate.md).
