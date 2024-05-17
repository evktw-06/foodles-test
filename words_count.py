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

def test_get_words_occurrences_number_example():
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = 3

    result = get_words_occurrences_number(sentence, n)

    assert result == [('zblah', 3), ('bar', 2), ('baz', 2)]


def test_get_words_occurrences_number_empty_sentence():
    sentence = ""
    n = 4

    result = get_words_occurrences_number(sentence, n)

    assert result == []


def test_get_words_occurrences_number_invalid_n():
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = -3

    # Testing libraries like pytest provide useful tools for handling exceptions, such as pytest.raises(Exception).
    # Using try/except blocks in tests is considered a bad practice.
    try:
        get_words_occurrences_number(sentence, n)
    except ValueError:
        exception_raised = True
    else:
        exception_raised = False

    assert exception_raised


# Execution
test_get_words_occurrences_number_example()
test_get_words_occurrences_number_empty_sentence()
test_get_words_occurrences_number_invalid_n()
print(get_words_occurrences_number("baz bar foo foo zblah zblah zblah baz toto bar", 3))
