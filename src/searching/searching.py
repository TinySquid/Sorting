import math


def linear_search(arr, target):
    """
    Iterates through a list and compares each element with target. Returns index of target if found.
    
    Arguments:
        arr [list] -- [List to be searched]
        target [int] -- [Item to be found]
    
    Returns:
        [int] -- [index of target, or -1 if not found]
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print("| Linear Search |")
print(f"Index of target: {linear_search(arr1, -6)}")
print("")


def binary_search(arr, target):
    """
    Searches a list for the provided target argument in O(log n) time.
    
    Arguments:
        arr [list] -- [Pre-sorted list to search]
        target [int] -- [Item to be found]
    
    Returns:
        [int] -- [Index of item in list, or -1 if not found]
    """

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:

        # Guess midpoint between low and high (rounded down)
        guess = math.ceil((low + (high - 1)) / 2)

        if arr[guess] == target:
            return guess
        elif arr[guess] < target:
            # Go to the right side
            low = guess + 1
        else:
            # Go to the left side
            high = guess - 1

    return -1  # not found


arr2 = [-9, -8, -6, -4]
print("| Binary Search |")
print(f"Index of target: {binary_search(arr2, -4)}")
print("")


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if low > high:
        return -1  # not found

    if len(arr) == 0:
        return -1  # array empty

    guess = math.ceil((low + (high - 1)) / 2)

    if arr[guess] == target:
        return guess
    elif arr[guess] < target:
        # Go to the right side
        return binary_search_recursive(arr, target, guess + 1, high)
    else:
        # Go to the left
        return binary_search_recursive(arr, target, low, guess - 1)


arr3 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print("| Binary Search Recursive |")
print(f"Index of target: {binary_search_recursive(arr3, 3, 0, len(arr3) - 1)}")
print("")
