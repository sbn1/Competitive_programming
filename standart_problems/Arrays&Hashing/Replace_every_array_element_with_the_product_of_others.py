# Replace every array element with the product of every other 
# element without using a division operator

# create two menoizaton array, one that starts from left and other that starts form right that
# will represent the product of the previous elements

# Time: O(N)
#Space : O(N)
from typing import List

def replace_with_product(nums:List[int])->List[int]:

    left = [1]*(len(nums))
    right = [1]* (len(nums))

    for i in range(1,len(nums)):
        left[i] = left[i - 1]*nums[i-1]
        right[len(nums)-i-1] = right[len(nums)-i]*nums[len(nums)-i]

    for i in range(len(nums)):
        nums[i] = left[i]*right[i]
    
    return nums

def replace_recursive(nums:List[int], n, left = 1, index = 0):
    #Base Case
    if index == n:
        return 1
    
    current_element = nums[index]
    

if __name__ == "__main__":

    replace_with_product([1, 2,3, 4, 5])
    replace_with_product([5, 3, 4, 2, 6, 8])