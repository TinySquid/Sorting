import random


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i

        # Find smallest element
        for cur_index in range(smallest_index + 1, len(arr)):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index

        # Swap
        arr.insert(i, arr.pop(smallest_index))

    return arr


# Test - Should print list with 0 - 9 ascending
print(selection_sort(random.sample(range(10), 10)))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
