def is_anagram(a_word, b_word):
    """
    >>> is_anagram("abc", "acb")
    True
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("one", "two")
    False
    >>> is_anagram("anagram", "nag a ram")
    True
    """
    return sorted(a_word) == sorted(b_word)

# lines 9: there are spaces in "nag a ram"
# fix: remove spaces