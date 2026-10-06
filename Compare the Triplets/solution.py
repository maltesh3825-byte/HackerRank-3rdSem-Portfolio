def compareTriplets(a, b):
    """Return Alice's and Bob's comparison scores."""
    alice_score = sum(left > right for left, right in zip(a, b))
    bob_score = sum(left < right for left, right in zip(a, b))
    return [alice_score, bob_score]


if __name__ == "__main__":
    print(compareTriplets([5, 6, 7], [3, 6, 10]))
