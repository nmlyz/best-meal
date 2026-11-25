#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt.

The sentence is a single sentence of at most 200 characters: curry from a
truck stop, rice scooped from a dented pot, a spoon bending slightly, and the
driver beside me eating in silence like a man saying grace without words.
Running it twice produces byte-identical output.
"""

import os

SENTENCE = (
    "The curry from a truck stop, the rice scooped from a dented pot, "
    "the spoon bending slightly, and the driver beside me eating his "
    "in silence like a man saying grace without words."
)


def output_directory():
    """The directory the entry is written to, /output unless overridden."""
    return os.environ.get("OUTPUT_DIR", "/output")


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    verify(path, text)


def verify(path, expected):
    """Read the file back and confirm it holds exactly the entry sentence."""
    with open(path, encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == expected + "\n", "entry.txt does not match the sentence"
    print(path)
    print(expected)


if __name__ == "__main__":
    os.umask(0o022)
    main()
