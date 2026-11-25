"""The Excuse That Almost Works — make.fun bounty entry.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt. Deterministic: same bytes every run.
"""

import os

# The excuse, assembled from three beats so each part reads like one
# hurried text: the boring household failure, the specific detail that
# makes it believable, and the consequence that proves it.
# The "12 degrees" is the believability anchor: a tired manager has heard
# a dead boiler every winter, and numb fingers explain why the texter
# cannot simply work from home — the excuse proves itself.
PARTS = [
    "Boiler died overnight,",
    "house is 12 degrees and I can't feel my fingers to type,",
    "engineer comes tomorrow.",
]


def entry_line():
    """Return the entry: one line, 18 words, 104 characters."""
    return " ".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 140, "gate: entry must be 1-140 characters"
    assert len(line.split()) <= 20, "judge brief: at most 20 words"
    assert "\n" not in line, "judge brief: one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
