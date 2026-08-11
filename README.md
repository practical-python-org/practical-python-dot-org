# practical-python.org

The website and documentation space for the Practical Python Discord community.

Built with [Zensical](https://zensical.org/)

## Quick start

**Prerequisites:** [uv](https://docs.astral.sh/uv/getting-started/installation/). It fetches the
right Python for you, so that's the only thing to install.

```bash
uv sync
uv run zensical serve
```

That serves the site at `http://127.0.0.1:8000` and rebuilds when you save a file.

## Checking your work before you push

```bash
uv run zensical build --strict
```

Broken internal links and dead anchors are build failures, not warnings. CI runs the same command,
so if it passes here it passes there.

Install the git hooks once and you'll get that check automatically on every commit:

```bash
uv run --dev pre-commit install
```

To run every check by hand:

```bash
uv run --dev pre-commit run --all-files
```

## Layout

```text
docs/
├── index.md               landing page
├── CNAME                  custom domain, copied to the site root on build
├── stylesheets/           colour, font and hero overrides
├── getting-started/       the entry point for new members
├── rules/                 server rules, code of conduct, moderation
├── resources/             learning material and setup guides
└── projects/
    ├── our-projects/      software the community maintains
    └── build-something/   project challenges for members
scripts/
└── refresh_member_count.py  updates the Discord member count before a deploy build
zensical.toml              all site configuration, including the nav
```

## Adding a page

1. Create the Markdown file under the right folder in `docs/`.
2. Add it to the `nav` list in `zensical.toml`.

Step 2 isn't optional. Zensical can derive navigation from the folder structure, but that sorts
alphabetically and would put Projects ahead of Rules, so the nav is written out.

[CONTRIBUTING.md](CONTRIBUTING.md) covers the writing conventions, which matter more than the
mechanics.

## Deployment

Merging to `main` triggers `.github/workflows/deploy.yml`, which builds with `--strict` and
publishes to GitHub Pages.

Pull requests run `.github/workflows/ci.yml` — the same pre-commit checks you get locally.

## Dependencies

One direct dependency, `zensical`, pinned through `uv.lock`. `requirements.txt` is generated from
the lockfile for anyone who wants to read the tree without uv:

```bash
uv export --no-dev --no-hashes --no-emit-project -o requirements.txt
```

CI installs from the lockfile, not from `requirements.txt`.
