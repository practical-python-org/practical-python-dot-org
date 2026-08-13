---
description: The Discord bot that runs the server — architecture, setup, and how to contribute.
---

# Eos

Eos is the bot that handles verification, moderation, logging and points on the server. Source lives
at [{{ eos_repo }}]({{ eos_repo }}).

## Architecture

Three services, talking in one direction:

```text
discord.py bot  <->  Flask API  <->  Postgres
```

The bot never touches the database. It calls the API, which owns all the SQL. That split means you
can work on bot behaviour without knowing the schema, and change the schema without touching the
bot.

| Component | Location   | Notes                                                                                            |
|-----------|------------|--------------------------------------------------------------------------------------------------|
| Bot       | `src/bot/` | Cogs grouped by purpose: `admin/`, `features/`, `logging/`, `moderation/`, `verification/`       |
| API       | `src/api/` | Flask. Routes in `src/api/routes/`, database access wrapped in `src/api/core/db_helper.py`       |
| Database  | `src/db/`  | `init.sql` runs on first start; `migrations.sql` is applied by a migration service on every boot |

The bot's HTTP calls are wrapped in `src/bot/core/api_helper.py`, so individual cogs don't build
requests by hand.

## Running it

=== "Docker (recommended)"

    You need Docker with Compose, and a Discord bot token.

    ```console
    $ cd src/
    $ cp .env.EXAMPLE .env
    ```

    Set your token and `MASTER_GUILD` — the ID of the guild the bot treats as home — then:

    ```console
    $ docker compose up -d
    ```

    The bot should come online. Run `>hc` in the server to healthcheck the API and database.

    !!! warning "Port 5432 is often taken"

        If you already run Postgres locally, change `POSTGRES_PORT_HOST` in `.env` to something free,
        usually `5433`, and rebuild with `docker compose up -d --build`. `POSTGRES_PORT` is the in-container
        port and shouldn't change.

=== "Locally with uv"

    Faster for iterating on one service. The repo is a [uv](https://docs.astral.sh/uv/) workspace with
    two members, `eos-api` and `eos-bot`:

    ```console
    $ uv sync
    $ source .venv/bin/activate
    ```

    Add a dependency to one workspace, not the whole repo:

    ```console
    $ uv add --package eos-bot some-library
    ```

    The bot still needs the API reachable and a populated `src/.env`. The usual arrangement is Postgres
    and the API in Docker while you run the service you're editing on the host.

## Points

Points are awarded automatically. Sending a message earns points based on its word count; deleting
one takes them back off. Joining adds you to the table, leaving removes you.

| Command                         | Does                                    | Who can run it         |
|---------------------------------|-----------------------------------------|------------------------|
| `>top_10`                       | Shows the leaderboard                   | Anyone                 |
| `>get_points @user`             | Shows one member's points               | Anyone                 |
| `>update_points @user <amount>` | Adds or subtracts. Negative to subtract | Admin, home guild only |

The full command reference — moderation, settings, verification, healthchecks — is in the repository
README rather than duplicated here, because it changes with the code.

## Contributing

Read `CONTRIBUTING.md` in the repo first. The essentials:

- Collaborators branch directly. Everyone else forks.
- Branch names follow `feature/`, `bugfix/` or `chore/` prefixes.
- All changes reach `master` through a pull request with one approval.
- Install the hooks once with `uv run --dev pre-commit install`. The same checks run in CI, so this
  only saves you a round trip.

!!! tip "Where to start reading"

    Pick a cog in `src/bot/cogs/` and follow one command end to end — cog to `api_helper`, to a route,
    to `db_helper`. It's a small trip and it explains the whole codebase.

## Related

- [Moderation](../../rules/moderation.md) — what the automatic enforcement does, from a member's
  point of view.
- [This site](this-site.md) — the other thing we maintain.
