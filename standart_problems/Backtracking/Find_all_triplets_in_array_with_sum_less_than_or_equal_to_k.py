# Given an unsorted array, print all the triplets in it with sum
# less than or equal to a given number

# First sort the array and backtrack through all the solutions with the constraint
# that the sum is less than sum
#The idea is not to find the most optimal solution, but rather to solve this problem through Backtracking.
# A more optimal solution would be to solve this problem through binary search, with Time:O(N*)

#Time: Exponential
#Space: Exponential

def find_triplets_less_or_equal(nums, suma,  sol=[], tmp=[], index=0):
    if len(tmp) == 3:
        sol.append(tmp[:])
        return
    
    i = index
    while i < len(nums) and nums[i] <= suma:
        tmp += [nums[i]]
        find_triplets_less_or_equal(nums,suma-nums[i],sol, tmp,i+1)
        tmp.pop()
        i += 1
    
    return sol


if __name__ == "__main__":
    
    nums = [2, 7, 4, 9, 5, 1, 3]
    nums.sort()
find_triplets_less_or_equal(nums, suma =10)


