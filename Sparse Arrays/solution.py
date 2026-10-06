from collections import Counter


def matchingStrings(strings, queries):
    """Return the frequency of each query in strings."""
    frequencies = Counter(strings)
    return [frequencies[query] for query in queries]


if __name__ == "__main__":
    print(matchingStrings(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"]))
