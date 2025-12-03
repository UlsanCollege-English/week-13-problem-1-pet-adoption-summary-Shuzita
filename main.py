def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.

    Example:
    summarize_adoptions(["cat", "dog", "cat"]) -> {"cat": 2, "dog": 1}
    """

    counts = {}

    for animal in adoptions:
        if animal not in counts:
            counts[animal] = 0
        counts[animal] += 1

    return counts


if __name__ == "__main__":
    # Optional manual test (not used by pytest)
    sample = ["cat", "dog", "cat", "rabbit", "dog", "cat"]
    print(summarize_adoptions(sample))
