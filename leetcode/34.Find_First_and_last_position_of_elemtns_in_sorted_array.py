from typing import List



class Solution:
    def first_occurence_position(self, nums:List[int], target:int)->List[int]:
        left, right = 0, len(nums)-1
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] < target):
                left = mid+1
            else:
                right = mid-1
        return left
    
    def last_occurence_position(self, nums:List[int], target:int)->List[int]:
        left, right = 0, len(nums)-1

        while (left <= right):
            mid = (left + right)//2

            if (nums[mid] <= target):
                left = mid+1
            else:
                right = mid - 1
        return right

    def searchRange(self, nums:List[int], target:int)->List[int]:
        first, last = self.first_occurence_position(nums, target), self.last_occurence_position(nums, target)
        
        return [first,last] if first <= last else [-1,-1]


Solution().searchRange( nums = [5,7, 7, 8, 8, 10], target=8) 
Solution().searchRange(nums=[5, 7, 7, 8, 8, 10],target=6)
Solution().searchRange([],0)