# Selection Sort
# Does only N swaps. insertion does O(N*N) swaps.
# find the minimum in each sub-array left
#Time: O(N*N)
#Space:O(N)
from typing import List

def selection_sort(a:List[int])->List[int]:

    for i in range(len(a)-1):
        min = i
        for j in range(i+1,len(a)):

            if (a[j] < a[min]):
                min = j

        a[i],a[min] = a[min],a[i]

    return a
if __name__ == "__main__":
    selection_sort([3,5,8,4,1,-2])
