import random


def merge(lhs, rhs):
    """Merge Sort helper function
        iteratively sorts two lists and merges them together
    Returns:
        list -- A sorted list
    """

    # Keep track of left / right index and array lengths
    left_len, right_len = len(lhs), len(rhs)
    left_index, right_index = 0, 0

    # Sorted array
    merged_arr = []

    # Taking into account uneven array pairs, compare left and right side and append to sorted array
    while left_index < left_len and right_index < right_len:
        if lhs[left_index] < rhs[right_index]:
            merged_arr.append(lhs[left_index])
            left_index += 1
        else:
            merged_arr.append(rhs[right_index])
            right_index += 1

    # Leftover elements get appended now
    merged_arr += lhs[left_index:]
    merged_arr += rhs[right_index:]

    return merged_arr


def merge_sort(arr):
    """Merge Sort (recursive)
    A divide and conquer algorithm that recursively divides the given list
    and merges it together, resulting in a sorted list
    
    Arguments:
        arr {list} -- An unsorted list
    
    Returns:
        list -- A sorted list
    """

    # Does array need to be halved?
    if len(arr) > 1:
        # divide and merge
        lhs = merge_sort(arr[: len(arr) // 2])  # Left side
        rhs = merge_sort(arr[len(arr) // 2 :])  # Right side
        return merge(lhs, rhs)

    # Base case - list length is 1, no work needs to be done
    return arr


# Test - Should print list with 0 - 15 ascending
arr1 = random.sample(range(15), 15)
print("| Merge Sort |")
print(f"Original: {arr1}")
print(f"Sorted: {merge_sort(arr1)}")
print("")

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
