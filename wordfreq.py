"""Print the most frequent words of a text file."""

import argparse
import re
from collections import Counter

WORD = re.compile(r"[a-z']+")
STOPWORDS = {"the", "of", "and", "to", "in", "it", "was", "is"}


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most frequent words of text, most frequent first."""
    words = [w for w in WORD.findall(text.lower()) if w not in STOPWORDS]
    return Counter(words).most_common(n)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="text file to read")
    parser.add_argument("--top", type=int, default=10, help="how many words to print")
    args = parser.parse_args()
    with open(args.path, encoding="utf-8") as f:
        text = f.read()
    for word, count in top_words(text, args.top):
        print(f"{count:6} {word}")


if __name__ == "__main__":
    main()
