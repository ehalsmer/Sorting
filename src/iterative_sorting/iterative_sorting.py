# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find min of unsorted subarray
        current_min = min(arr[i:])
        # Do the swap
        min_index = arr.index(current_min)
        temp = arr[i]
        arr[i] = current_min
        arr[min_index] = temp
        # print(arr)
    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        # swaps = 0
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                # swap:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                # swaps +=1
    return arr

# print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr