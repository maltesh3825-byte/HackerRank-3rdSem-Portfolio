def diagonalDifference(arr):
    """Return the absolute difference between the matrix diagonals."""
    size = len(arr)
    primary = sum(arr[index][index] for index in range(size))
    secondary = sum(arr[index][size - 1 - index] for index in range(size))
    return abs(primary - secondary)


if __name__ == "__main__":
    matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(matrix))
