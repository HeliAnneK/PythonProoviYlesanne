"""EX02."""


def find_amount_of_smaller_numbers(nums):
    """
    You are given a list of numbers. Your task is to return a new list where each element represents the count of
    numbers in the original list that are smaller than the corresponding number.

    Consider the list [0, 3, 5, 2]:
    For 0, there are no smaller numbers in the list -> 0
    For 3, there are two smaller numbers in the list (0, 2) -> 2
    For 5, there are three smaller numbers in the list (0, 2, 3) -> 3
    For 2, there is one smaller number in the list (0) -> 1
    Thus, the result should be [0, 2, 3, 1].
    Examples:
        [1, 2, 3] -> [0, 1, 2] - there are no smaller numbers than 1, there is one smaller number than 2(1),
        there is 2 smaller numbers than 3(1, 2).
        [5, 2, 4, 5, 1] -> [3, 1, 2, 3, 0]
        [3, 3, 3] -> [0, 0, 0]
    """
    answer = []
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        answer.append(sorted_nums.index(nums[i]))
    return answer
