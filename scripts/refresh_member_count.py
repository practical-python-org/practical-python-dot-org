"""Refresh the Discord member count in the zensical.toml.

Runs before `zensical build` at deploy time. The count is referenced in
`[project.extra] member_count` and reaches pages as the `{{ member_count }}`
macro, so no nasty JavaScript runs in the reader's browser and the number is present
in the HTML when it loads up.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

CONFIG = Path(__file__).resolve().parent.parent / "zensical.toml"

API = "https://discord.com/api/v10/invites/{code}?with_counts=true"
TIMEOUT = 10

USER_AGENT = (
    "practical-python-dot-org/1.0 (+https://practical-python.org; deploy script)"
)
MEMBER_COUNT_LINE = re.compile(r'^(member_count\s*=\s*)"[^"]*"', re.MULTILINE)


def invite_code(config: dict) -> str:
    """Pull the invite code off the end of the configured invite URL."""
    url = config["project"]["extra"]["discord_invite"]
    code = url.rstrip("/").rsplit("/", 1)[-1]
    if not code or "REPLACE" in code.upper():
        raise ValueError(f"discord_invite is not a usable invite URL: {url!r}")
    return code


def fetch_member_count(code: str) -> int:
    request = urllib.request.Request(
        API.format(code=code), headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        payload = json.load(response)

    count = payload.get("approximate_member_count")
    if not isinstance(count, int) or count <= 0:
        raise ValueError(f"no usable member count in response: {payload!r}")
    return count


def render(count: int) -> str:
    """Round down to a hundred, so 4307 members reads as '4,300+'."""
    if count < 200:
        return f"{count:,}"
    return f"{count - count % 100:,}+"


def main() -> int:
    raw = CONFIG.read_text(encoding="utf-8")
    config = tomllib.loads(raw)

    try:
        count = fetch_member_count(invite_code(config))
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError) as error:
        # The committed fallback is a real number, just an older one, so a
        # Protects us when Discord yolos something into their endpoint and breaks it.
        print(f"member count unchanged: {error}", file=sys.stderr)
        return 1

    rendered = render(count)
    updated, substitutions = MEMBER_COUNT_LINE.subn(rf'\1"{rendered}"', raw)
    if substitutions != 1:
        print(
            f"expected one member_count line in {CONFIG.name}, found "
            f"{substitutions}",
            file=sys.stderr,
        )
        return 1

    if updated != raw:
        CONFIG.write_text(updated, encoding="utf-8")

    print(f"member_count = {rendered!r} (from {count:,} reported)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
