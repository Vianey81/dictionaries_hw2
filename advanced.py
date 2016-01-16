
"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""
from collections import Counter

def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    most_common_dict = Counter()
    for char in input_string:
        if char != " ":
            most_common_dict[char] += 1

    max_counter = most_common_dict.most_common()[0]
    max_counter = max_counter[1]
    most_common_char = [char for char, value in most_common_dict.items() if value == max_counter]

    return most_common_char


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    len_word = 0
    dict_words = {}
    result_tuple = ()
    result_list = []
    for word in words:
        len_word = len(word)
        if len_word in dict_words:
            dict_words[len_word].append(word)
        else:
            dict_words[len_word] = [word]

    for key, value in dict_words.items():
        result_tuple = (key, sorted(value))
        result_list.append(result_tuple)
    return result_list


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
