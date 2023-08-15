# Activity selection problem: Given a  set of activities with their 
#start and end time, find the max number of activites performed, 
# assumming that the person can work only on a limited nr of activities at
# the time

# Sort by the end time, and check if the starting time of the next
#activity is more than the end time of the current

# Time: O(N*LOG N)
#Space: O(N)

from typing import List

def activities(arr:List[List[int]])->List[List[int]]:
    
    if len(arr)<1:
        return 
    
    previous = arr[0]
    solution = [arr[0]]
    # sort by the end time
    arr.sort(key=lambda x:x[1])

    for i in range(1,len(arr)):
        if arr[i][0] >= previous[1]:
            solution.append(arr[i])
            previous = arr[i]

    return solution

if __name__ == "__main__":
    activities([[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]])

