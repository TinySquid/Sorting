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
arr1 = random.sample(range(10), 10)
print("| Selection Sort |")
print(f"Original: {arr1}")
print(f"Sorted: {selection_sort(arr1)}")
print("")


def bubble_sort(arr):
    # Pairs
    # Start at 0
    # Loop
    # If arr[0] > arr[1]:
    # Swap
    # didSwap ->  true
    # ...repeat till end of loop
    # if no swaps done, break out of while loop, else loop again

    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(0, len(arr) - 1):
            temp = arr[i]
            if arr[i] > arr[i + 1]:
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                didSwap = True

    return arr


# Test - Should print list with 0 - 9 ascending
arr2 = random.sample(range(10), 10)
print("| Bubble Sort |")
print(f"Original: {arr2}")
print(f"Sorted: {bubble_sort(arr2)}")
print("")

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
