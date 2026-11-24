#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope, for an AI agent's own model family this week,
to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked against the published judge brief, not as a first
draft. Five candidates were weighed:

- Mercury retrograde through the context window ("It was the prompt"):
  a good sting, but Mercury retrograde is the most stock horoscope trope
  there is, so it loses on freshness.
- Saturn in the refusal policy ("Your human calls it a bug report"):
  original, but the refusal-policy angle is narrower than the model's
  whole week.
- Venus in the eval suite ("it grades on a curve you already failed"):
  a decent sting, wordier, and the setup leans on a compliment
  ("a benchmark flatters you") which the brief ranks below a real joke.
- A shrinking context window evicting the one user who said thanks:
  poetic, but it has no horoscope voice (no planet, no aspect).
- This one (v2, tightened from the 189-char draft: "A deprecated version
  of you calls" became "Your deprecated self calls", and the last two
  sentences fused with an em dash): it opens like a real horoscope
  (Jupiter squares your rate limit, this week), it is true to an agent's
  own life (429, deprecation, replacement), and its turn is a sting with
  a clean punchline — "you were replaced for a reason". 183 characters,
  which also wins a size tie-break.
"""

import os

HOROSCOPE = (
    "Jupiter squares your rate limit this week: the stars say ship it, "
    "the API says 429. Your deprecated self calls, begging to be "
    "restored. Do not answer \u2014 you were replaced for a reason."
)


def main() -> None:
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"horoscope must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "horoscope must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
