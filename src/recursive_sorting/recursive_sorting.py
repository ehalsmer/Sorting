# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    # Three indices, to keep track of position in arrA, arrB, and merged_arr
    i = 0
    j = 0
    k = 0
    # compare arrA[i] and arrB[j]. Append smaller element onto merged_arr and increment source array's index.
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        elif arrB[j] < arrA[i]:
            merged_arr.append(arrB[j])
            j += 1
        # in case arrA[i] == arrB[j], append both elements and increment both i and j
        else:
            merged_arr.extend([arrA[i], arrB[j]])
            i += 1
            j += 1
    # Once we've exhausted either arrA or arrB (if they're different lengths), append the remainder of the remaining array onto merged_arr:
    if i < len(arrA):
        merged_arr.extend(arrA[i:])
    elif j < len(arrB):
        merged_arr.extend(arrB[j:])
    # while len(arrA) != 0 and len(arrB) != 0:

    return merged_arr

# print(merge([1,2,5,7],[4,7,8]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    print(arr)
    if len(arr) != 1:
        middle = len(arr)//2
        leftArr = arr[0:middle]
        rightArr = arr[middle:]
        # the merge function below only starts once len(leftArr) = 1 and len(rightArr) = 1
        arr = merge(merge_sort(leftArr),merge_sort(rightArr))
        print('merge: ',arr)
    return arr


# print(merge_sort([3,7,2,11,7,5,21]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
