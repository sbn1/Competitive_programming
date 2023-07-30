# Given an int array containintg duplicates, return the majority 
# element that appears more than n/2 times, where n is the size of the array

# Use Boyer-Moore Algorithms: keep an counter and store the elements in
# in a candidate variable. If a similar element is encountered , the counter will increase.
# The algorithm work as long as there are more than n/2 similar elements.

# Time: O(N)
# Space: O(1)

def findMajorityElement(arr):

    counter = 0
    candidate = -1

    for i in range(len(arr)):
        if counter ==0:
            candidate = arr[i]
            counter = 1
        elif arr[i] == candidate:
            counter += 1
        else:
            counter -= 1
    return candidate

if __name__ == "__main__":
    findMajorityElement([1,8,7,4,1,2,2,2,2,2,2])