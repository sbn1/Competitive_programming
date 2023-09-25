# Given an array, count the total number of triplets that satisfy the 
# relationship  (i < j < k) and (A[i] > A[j] >A[k])

#Find the elements lower than A[j] and those higher than it, then sum them

#Time: O(N*N)
#Space: O(1)

from typing import List

def count_triplets(arr:List[int])->int: 

    count_triplets = 0

    for j in range(1, len(arr)-1):

        i = 0
        k = len(arr)-1
        greater = 0

        while(i < j):
            if (arr[i] > arr[j]):
                greater += 1
            i += 1

        smaller = 0
        
        while (j < k):
            if (arr[k] < arr[j]):
                smaller += 1
            k -= 1
        count_triplets += (smaller * greater)

    return count_triplets

if __name__ == "__main__":

    count_triplets([1,9,6,4,5])
    count_triplets([9,4,3,5,1])