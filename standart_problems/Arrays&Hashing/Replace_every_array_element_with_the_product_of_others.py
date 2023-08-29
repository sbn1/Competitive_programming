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

def recursive_replace_product(a):

    def replace_recursive(a, index=0, left=1, right=1):
        #Base Case
        if index == len(a):
            return 1
        
        right = replace_recursive(a, index + 1, left*a[index], right*left)
        tmp = a[index]
        a[index] = left*right

        return right*tmp
    replace_recursive(a)
    
    return a

    

if __name__ == "__main__":

    replace_with_product([1, 2,3, 4, 5])
    replace_with_product([5, 3, 4, 2, 6, 8])
    recursive_replace_product([1, 2, 3,4,5])
    recursive_replace_product([5, 3, 4, 2, 6, 8])