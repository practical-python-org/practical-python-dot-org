---
description: Which channel your message belongs in.
---

# Channels

Post in the right place and you'll get an answer faster. Post in the wrong place
and maybe someone will move you, or your question won't get seen.


## Getting help

| You want | Channel type | Notes |
|----------|--------------|-------|
| Help with code that won't run | [#python](https://discord.com/channels/900302240559018015/903542455675260928) | Include the traceback. See [asking good questions](../resources/asking-good-questions.md) or the [Python help forums](https://discord.com/channels/900302240559018015/1047117243349221396) |
| A review of code that works | [#projects](https://discord.com/channels/900302240559018015/1271849700634525769) | Say what you want reviewed — style, structure, performance |
| Career or study advice | [#professional-life](https://discord.com/channels/900302240559018015/962414521664815144) | Not a job board unless staff say otherwise |

One question per channel. Don't be that guy. Asking the same thing in three places gets you three
half-answers and an irritated moderator.

## Everything else

| Channel type | For |
|--------------|-----|
| General chat | Anything not a support request |
| Off-topic | Not Python. Still covered by [the rules](index.md) |
| Voice | Pair programming, study sessions, quiet co-working |

## Threads

Use a thread when a conversation outlives its usefulness to the channel — a long
debugging session, a tangent, a design argument. Start one, don't apologise for
it.

Threads inherit the rules of their parent channel.

## Bot commands

Commands work in most channels, but check before filling a help channel with bot
output.

=== "Slash commands"

    Newer commands are registered with Discord and autocomplete as you type:

    ```text
    /hc
    /top_10
    /ticket
    ```

!!! tip "It's a long list..."

    The full list, with permissions and arguments, is in the
    [Eos documentation](../projects/our-projects/eos.md).


=== "Run code in the chat!"

    `>run` executes a Python code-block and replies with the output.

    The format is:

    ````text
    >run
    ```py
    print("oh wow!")
    ```
    ````
