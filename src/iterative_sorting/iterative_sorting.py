# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find min of unsorted subarray
        '''
        Could also find min without min function:
        smallest_index = 0
        for g in range(1,len(arr)):
            if arr[g] < arr[smallest_index]:
                smallest_index = g
        '''
        current_min = min(arr[i:])
        # Do the swap
        min_index = arr.index(current_min)
        arr[i],arr[min_index] = arr[min_index],arr[i]
        # print(arr)
    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                # swap:
                arr[j],arr[j-1] = arr[j-1],arr[j]
        # print(arr)
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr