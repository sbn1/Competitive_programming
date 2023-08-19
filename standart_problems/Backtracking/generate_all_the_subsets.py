# Given an array , generate all the subsets

# There are several approaches, in this case these will be used 2 recursive calls
# one will select the last element in the array, and another one will select thre rest of the element.

#Time: O(2^N-1)
#Space: O(2^N-1)

from typing import List
def subsets(nums:List[int], n:int, sol=[], tmp=[])->List[List[int]]:
    if n == 0:
        sol.append(tmp[:])
        return
    
    tmp += [nums[n-1]]
    subsets(nums, n - 1, sol, tmp)
    tmp.pop()
    subsets(nums, n - 1,sol,  tmp)

    return sol

if __name__ == "__main__":

    subsets([1,2,3], 3)
    subsets(["A", "B", "C"], 3)
    