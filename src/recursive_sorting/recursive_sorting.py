# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    longest = len(arrA) if len(arrA) >= len(arrB) else len(arrB)
    while len(arrA) != 0 and len(arrB) != 0:
        for i in range(0, longest-1):
            print(i)
            # if arrA[i] < arrB[i]:
                # merged_arr.append(arrA[i])
                # print(merged_arr)
                # arrA.remove(f'{arrA[i]}')
            # elif arrB[i] < arrA[i]:
                # merged_arr.append(arrB[i])
                # arrB.remove(f'{arrB[i]}')
    return merged_arr

print(merge([6,8,9,10],[1,2,3]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
