from collections import Counter


# Function
def get_words_occurrences_number(sentence: str, n: int) -> list[tuple[str, int]]:
    """
    Count the occurrences of words in a sentence and return the top 'n' words with their counts.

    I didn't verify the type because I assumed we were using a static type checker like mypy.

    Args:
        sentence (str): The input sentence.
        n (int): The number of top words to return.

    Returns:
        list: A list of tuples containing the top 'n' words along with their counts, sorted by count and then alphabetically.

    Example:
        get_words_occurrences_number("baz bar foo foo zblah zblah zblah baz toto bar", 3)
        [('zblah', 3), ('bar', 2), ('baz', 2)]
    """
    if not sentence:
        return []

    if n < 1:
        # It's usable with 0 and negative numbers because we only slice with 'n', but it's an edge case.
        raise ValueError("Function should be used with a number greater or equal to 1")

    word_count = Counter(sentence.split())

    return sorted(word_count.items(), key=lambda x: (-x[1], x[0]))[:n]

# Execution
print(get_words_occurrences_number("baz bar foo foo zblah zblah zblah baz toto bar", 3))
