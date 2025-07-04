import re
from collections import Counter


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter[str] = Counter(words)
    return word_counts.most_common(n=5)  # n=5 gives the 5 most commonly used words only


def main() -> None:
    text: str = input("Enter your text: ")
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
