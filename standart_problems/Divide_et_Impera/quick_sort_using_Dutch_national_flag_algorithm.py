# Implement quicksort efficiently for inputs with many repeated values

# the efficient sorting will categorize the values into three groups, less than the pivot, higher than the pivot
# and equal to the pivot. The values equal to the pivot are already sorted , so the algorithms will focus on 
# the other two groups. 
#
# Time: O(N*Log(N))
# Space: O(N)

from typing import List
def partition(a:List[int], start:int, end:int):
    pivot = a[end]
    mid_index = start

    while mid_index <= end:

        if (a[mid_index] < pivot):
            a[mid_index], a[start] = a[start], a[mid_index]
            mid_index += 1
            start += 1
        elif (a[mid_index] > pivot):
            a[mid_index], a[end] = a[end], a[mid_index]
            end -= 1
        else:
            mid_index += 1
    
    return start - 1, mid_index

def quicksort(a:List[int], start, end):
    if start >= end:
        return
    
    less_than_index,higher_than_index = partition(a, start, end)

    quicksort(a, start, less_than_index)

    quicksort(a, higher_than_index, end)


if __name__ == "__main__":

    a = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    quicksort(a, 0, len(a)-1)
    print(a)
