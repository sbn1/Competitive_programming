# Given an array sort it using insertion.

# It shifts the elements in the array until it finds the right position of the element

# Time: O(N*N)

from typing import List

def insertion(a:List[int])->List[int]:

    for i in range(1,len(a)):

        value = a[i]
        j = i

        while (j > 0) and (a[j-1] > value):
            a[j] = a[j-1]
            j -= 1

        a[j] = value

    return a

if __name__ == "__main__":
    insertion([5,4,6,2,1,8,7])