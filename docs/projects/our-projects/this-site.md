---
description: How this documentation site is built, checked and deployed.
---

# This site

The site you're reading. Markdown in, static HTML out, deployed by CI when
something lands on `main`. Source at [{{ site_repo }}]({{ site_repo }}).

## Stack

| Piece | What it does |
|-------|--------------|
| [Zensical](https://zensical.org/) | Static site generator, by the Material for MkDocs team. Search, navigation and macros are built in |
| [uv](https://docs.astral.sh/uv/) | Dependency management. Versions are pinned in `uv.lock` |
| pre-commit | Formatting, typo and build checks before a commit lands |
| GitHub Actions | Builds on every pull request, deploys on merge to `main` |
| GitHub Pages | Hosting, with a custom domain |

There is one dependency, `zensical`, and it brings eight transitive packages with
it. That's deliberate — the plugin list this site would have needed under MkDocs
is all built in.

## Running it locally

```console
$ uv sync
$ uv run zensical serve
```

That serves on `http://127.0.0.1:8000` and rebuilds when you save. To check what
CI will check:

```console
$ uv run zensical build --strict
```

!!! warning "--strict is the gate"

    Broken internal links and dead anchors are build failures, not warnings. If
    a link to `resources/getting-started.md` has a typo, the build fails and the
    deploy never happens. Run it before you push.

## Adding a page

Two steps, and the second one is easy to forget:

1. Create the Markdown file in the right folder under `docs/`.
2. Add it to the `nav` list in `zensical.toml`.

[CONTRIBUTING.md](https://github.com/practical-python-org/practical-python-dot-org/blob/main/CONTRIBUTING.md)
covers the writing conventions, which matter more than the mechanics.

## Deployment

Merging to `main` triggers a workflow that builds the site and publishes it to
GitHub Pages. There's no manual step.
PRs to main require at least 2 approving reviews from verified contributors.

Pull requests run with `--strict`, plus the pre-commit checks.


## Related

- [Eos](eos.md) — the other project, and considerably more moving parts.
