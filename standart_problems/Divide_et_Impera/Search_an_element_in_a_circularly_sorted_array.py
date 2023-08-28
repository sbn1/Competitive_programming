# Given a circularly sorted array, search for an element in it. Assume, there are no duplicates in the 
# array, and the rotation is in counter-clockwise direction.
#Time: O(LogN)
#Space : O(1)

from typing import List

def search_rotated(nums: List[int], target: int) -> int:
    
    if not nums:
        return -1

    left,right = 0, len(nums)-1
    while( left <= right):
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        if (nums[left]<=nums[mid]):

            if (nums[left]<=target<nums[mid]):
                right=mid-1
            else:
                left=mid+1
        else:
            if (nums[mid]<target<=nums[right]):
                left=mid+1
            else:
                right=mid-1
    return -1

if __name__ == "__main__":

    search_rotated([8, 9, 10, 2, 5, 6],target=2)