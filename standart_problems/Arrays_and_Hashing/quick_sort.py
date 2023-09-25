# Quick Sort: Classic Algorithm

#Time: O(N*Log N)

from typing import List

def partition(a:List[int], start:int,end:int)->int:

    pivot = a[end]
    p_index = start

    for i in range(start, end):
        if a[i]<=pivot:
            a[i],a[p_index] = a[p_index], a[i]
            p_index += 1
    a[p_index], a[end] = a[end], a[p_index]

    return p_index

def quicksort(a:List[int], start, end)->None:

    if start >= end:
        return 
    
    pivot = partition(a, start, end)
    
    quicksort(a, start, pivot - 1)
    quicksort(a, pivot + 1, end)

if __name__ == "__main__":
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quicksort(a, 0, len(a)-1)