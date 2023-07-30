# Given an array and a positive number k, check whether the array
# contains any duplicate elements within the range k. If k is more 
# than the array’s size, the solution should check for duplicates in the complete array.

# Create a dictionary and store the positions, the difference will be negative
#Time: O(N)
#Space: O(N) for the dictionary

from typing import List

def findDuplicate(arr:List[int],k)->bool:

    dct = {}
    for i in range(len(arr)):
        if arr[i] in dct:
            if dct[arr[i]] - i<=k:
                return True
        else:
            dct[arr[i]] = i

    return False
if __name__ == "__main__":
    findDuplicate([5, 6, 8, 2, 4, 6, 9], k=4)
