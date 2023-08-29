# Given a sequence of n numbers such that the difference between the 
#consecutive terms is constant, find the the missing term in log time. 
# To be assumed that the first and last terms are always part of the 
# sequence, the missing element is located on position 1 and n-1

# Solution involves a Binary Search that will compare the 
#difference between the medium value and the first value and the position of the 
# mid times the step(diff).

# Time: O(LogN)

# Space: O(1)

from typing import List

def find_missing_term(a:List[int])->int:

    left, right = 0, len(a)-1
    diff = (a[-1] - a[0])//len(a)

    while left <= right:

        mid = (left+right)//2

        if (mid-1 >= 0) and (a[mid] - a[mid-1] != diff):
            return a[mid-1] + diff
        
        if (mid+1 <len(a)) and (a[mid+1] - a[mid] != diff):
            return a[mid] + diff
        
        if (a[mid] - a[0]) != (mid)*diff:
            right = mid -1
        else:
            left = mid + 1
    
    return -1

if __name__ == "__main__":

    find_missing_term([5, 7, 9, 11, 15])
    find_missing_term([1, 4, 7, 13, 16])
    find_missing_term([1, 5, 7, 9, 11])


