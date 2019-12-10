# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find min of unsorted subarray
        current_min = min(arr[i:])
        # Do the swap
        minFound = arr.index(current_min)
        temp = arr[i]
        arr[i] = current_min
        arr[minFound] = temp
        print(arr)
        # cur_index = i
        # print('cur_index', cur_index)
        # smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 




        # TO-DO: swap




    return arr

selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr