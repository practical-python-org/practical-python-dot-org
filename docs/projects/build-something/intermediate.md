---
description: challenges for people who can finish a project and want structure, tests and interfaces.
---

# Intermediate challenges

You've built something that works. These are about structure, error handling and code someone else
can read.

Each of these needs more than one module. If yours is one long file, that's the first thing the
brief is teaching you.

## HTTP API client with a cache

**Goal.** A small library that wraps a public API and caches responses so you don't re-request the
same thing.

Pick an API with no authentication — there are plenty of open ones.

**Done when:**

- [ ] Repeat calls with the same arguments hit the cache, not the network.
- [ ] The cache expires after a configurable interval.
- [ ] Network failures raise something your caller can catch and understand.
- [ ] Tests pass with no network access at all.
- [ ] The public interface is documented well enough for someone to use without reading the source.

**Stretch.** Cache to disk instead of memory. Add retries with backoff. Rewrite it with `httpx` and
`async`, and measure whether it actually got faster.

**Time.** A week of evenings.

!!! warning "The test requirement is the hard part"

    Testing without network access forces you to separate "fetch" from "decide whether to fetch". If you
    can't test it offline, the design needs changing — which is the lesson.

## Log file analyser

**Goal.** Read a large log file, extract structure, and report on it.

**Done when:**

- [ ] It handles a file too large to fit in memory.
- [ ] Malformed lines are counted and skipped, not fatal.
- [ ] Output includes counts, a time range, and the most frequent entries.
- [ ] It has a `--json` mode for machine-readable output.
- [ ] Running it on an empty file produces an empty report, not a crash.

**Stretch.** Multiple log formats via a plugin structure. Streaming from stdin so it works in a
pipe. Charts, if you can do it without making the tool worse.

**Time.** A week of evenings.

=== "Iterating lazily"

    ```python
    def parse(path):
        with open(path) as handle:
            for line in handle:
                entry = parse_line(line)
                if entry is not None:
                    yield entry
    ```

    A generator keeps memory flat regardless of file size, and composes with `itertools` and
    `collections.Counter`.

=== "Reading it all in"

    ```python
    lines = open(path).read().splitlines()
    ```

    Fine for a 2 MB file, a problem at 2 GB. Try it on something large once so the failure mode is
    familiar rather than theoretical.

## Discord bot cog

**Goal.** Add a feature to [Eos](../our-projects/eos.md) — or your own bot, if you'd rather not open
a pull request yet.

This is the brief most likely to end with your code running in the server.

**Done when:**

- [ ] The cog loads without touching any other cog.
- [ ] Commands validate their input and fail with a message, not a traceback.
- [ ] Anything needing the database goes through the API, not direct SQL.
- [ ] No blocking calls in an async function. No `time.sleep`.
- [ ] Permissions are checked where they matter.

**Stretch.** Add persistence via a new API route. Write tests for the helper functions. Handle
Discord's rate limits properly under load.

**Time.** A weekend, plus review time if you open a pull request.

!!! tip "Read one first"

    Pick an existing cog in `src/bot/cogs/features/` and follow it end to end before writing yours. The
    patterns are consistent, and matching them is most of passing review.

## Where next

There isn't an advanced page yet. At this point the useful next step is maintaining something real —
pick an issue on [one of our projects](../our-projects/index.md) and work with a reviewer.
