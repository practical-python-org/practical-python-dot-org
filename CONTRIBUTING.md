# Contributing

This site is written by members. Corrections, new resources and new project challenges are all
welcome.

- Collaborators branch directly and open a pull request from it.
- All changes reach `main` through a pull request, which needs two approvals.
- Branch names follow `feature/`, `bugfix/` or `chore/`, same as our other repos.

Local setup is in the [README](README.md). Run `uv run zensical build --strict` before you push — a
broken link fails the build, and it's faster to find out on your machine.

## Adding a page

1. Create the Markdown file under the right folder in `docs/`.
2. Add it to the `nav` list in `zensical.toml`.

Forgetting step 2 means your page builds but nobody can find it.

### Nav conventions

The nav is written out rather than derived from the folder structure. Zensical can derive it, but it
sorts alphabetically, which puts Projects ahead of Rules.

- Every section's `index.md` comes first in its list.
- Everything after that goes in reading order — the page a newcomer needs first goes first, not the
  one that's alphabetically luckiest.
- Nest a sub-group only when a section has two clear halves. `projects/` does. Nothing else needs
  to.

### Front matter

```yaml
---
description: One sentence. Used by search engines and link previews.
---
```

`description` is expected on every page. The landing page also uses `hide: [navigation, toc]`; you
probably don't need that anywhere else.

### Cross-links

Link to other pages by relative path to the `.md` file, not by URL:

```markdown
See [asking good questions](../resources/asking-good-questions.md).
Link to a specific heading with [rule 6](../rules/index.md#6-post-code-as-code).
```

Both the path and the anchor are checked at build time. A typo in either one fails the build, which
is the point.

### Admonitions

```markdown
!!! warning "Optional title"

    Indented four spaces.
```

`note`, `tip`, `warning`, `danger`, `info`, `example`, `question` and `failure` all work. Use `???`
instead of `!!!` to make it collapsible.

Don't stack three admonitions in a row. If everything is highlighted, nothing is.

### Content tabs

Good for per-platform instructions or two ways of doing one thing:

```markdown
=== "Windows"

    Indented four spaces.

=== "macOS"

    Same.
```

Tabs with matching labels switch together across the whole page, so keep the labels consistent.

### Tables

Tables beat bullet lists whenever each item has the same two or three properties. Most of the pages
here use them heavily; follow suit.

### Variables

Values that appear on more than one page live in `[project.extra]` in `zensical.toml`:

```markdown
Join us at {{ discord_invite }}.
```

Available: `discord_invite`, `eos_repo`, `site_repo`. Add more there rather than pasting a URL into
six pages.

### What not to add

- No custom JavaScript.
- No CSS beyond `docs/stylesheets/extra.css`, and only for colour, font or the landing page hero.
- No images over a few hundred KB. Nobody's phone wants your 4 MB screenshot.

## Writing voice

This is the part reviewers actually comment on. Read a couple of existing pages before you start and
you'll pick it up faster than from any list.

## Reviewing

If you're reviewing, say which of these a comment is about: correctness, voice, or preference.
Preference comments are fine as long as they're labelled, so the author knows they can decline.
