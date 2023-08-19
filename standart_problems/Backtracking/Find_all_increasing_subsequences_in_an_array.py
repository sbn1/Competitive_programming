# Given an int array , find all distinct increasing subsequences of length two or more

# Use backtracking to iterate through all the possible solutions
# and select only those that fit the criteria. 

# Time: Exponential 
# Space: Exponential
from typing import List

def find_increasing_subsequences(nums:List[int], sol:List[int], tmp:List[int], index:int)->List[List[int]]:

    #Base Case
    if len(tmp)>1:
        #select only the disting sequences
        if tmp not in sol:
            sol.append(tmp[:])
    
    for i in range(index, len(nums)):

        if not tmp or tmp[-1] < nums[i]:
            tmp += [nums[i]]
            find_increasing_subsequences(nums, sol, tmp, i + 1)
            tmp.pop()
    return sol

if __name__ =="__main__":

    find_increasing_subsequences([2, 4, 5, 4], [],[],0)

