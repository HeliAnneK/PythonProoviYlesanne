"""EX01."""


def string_score(s):
    """
    You are given a list with strings in it. The score of a string is defined as the
    arithmetic average of the unicode values for each character.

    Return the string with the biggest score.

    Example:
        string_score("ABC", "abc") -> (65 + 66 + 67) / 3 -> 66
        string_score("Hello") -> (72 + 101 + 108 + 108 + 111) / 5 -> 100
        string_score("Python") -> 80 + 121 + 116 + 104 + 111 + 110 -> 107

    Hint:
    For this exercise using ord(char) is encouraged. Method ord(char) returns
    the unicode value of the character.
    For example: ord('A') -> 65
    """
    if not s.strip():
        return 0
    answer = 0
    for c in s:
        answer += ord(c)
    return answer / len(s)


def string_with_best_score(string_list):
    """
    You are given a list with strings in it. The score of a string is defined as the
    arithmetic average of the unicode values for each character.

    Return the string with the biggest score.

    Example:
        string_score("ABC", "abc") -> (65 + 66 + 67) / 3 -> 66
        string_score("Hello") -> (72 + 101 + 108 + 108 + 111) / 5 -> 100
        string_score("Python") -> 80 + 121 + 116 + 104 + 111 + 110 -> 107

    Hint:
    For this exercise using ord(char) is encouraged. Method ord(char) returns
    the unicode value of the character.
    For example: ord('A') -> 65
    """
    biggest_value = 0
    biggest_string = ""
    for s in string_list:
        if string_score(s) > biggest_value:
            biggest_value = string_score(s)
            biggest_string = s
    return biggest_string
