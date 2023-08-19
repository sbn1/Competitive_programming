# Given an array return the ways to calculate the specified target from array
#using only addition and substraction operator.

# The problem can be reduced to a simple backtracking problem,
# using two recursive function, one for addition and one for substraction.

#Time: Exponential
#Space:Exponential, the solution will include the elements in it

def find_ways_to_calculate_target(nums,target, index, sol=[], tmp=""):
    if (target == 0):
        sol.append(tmp[:])
        return

    for i in range(index, len(nums)):
        # the sign is + becuse we decrease it from the target, threfore adding it to the reminder will give the target
        find_ways_to_calculate_target(nums, target - nums[i], i+1, sol, tmp+"+"+str(nums[i]))
        find_ways_to_calculate_target(nums, target + nums[i],i+1, sol, tmp +"-"+str(nums[i]))

    return sol

if __name__ == "__main__":

    find_ways_to_calculate_target([5, 3, -6, 2], 6, 0) 
    find_ways_to_calculate_target([5, 3, -6, 2], 4, 0) 