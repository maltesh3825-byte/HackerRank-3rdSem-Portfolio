def dynamicArray(n, queries):
    """Process type-1 append and type-2 lookup queries."""
    sequences = [[] for _ in range(n)]
    last_answer = 0
    answers = []

    for query_type, value in queries:
        sequence_index = (value ^ last_answer) % n
        if query_type == 1:
            sequences[sequence_index].append(value)
        else:
            sequence = sequences[sequence_index]
            last_answer = sequence[value % len(sequence)]
            answers.append(last_answer)

    return answers


if __name__ == "__main__":
    sample_queries = [[1, 0], [1, 1], [1, 2], [2, 1], [2, 1]]
    print(dynamicArray(2, sample_queries))
