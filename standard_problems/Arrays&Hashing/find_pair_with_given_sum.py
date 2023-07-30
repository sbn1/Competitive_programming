# Given an unsorted array, find pair with the given sum in it.

# Store the element in an hash(dictionary), and check if the difference
# has been stored before

# Time: O(N)
# Space: O(N) for the dictionary

def findPairs(arr, target):
    dct = {}
    for i, element in enumerate(arr):
        if target-element in dct:
            return [target-element,element ]
        dct[element] = i
    
    return -1
if __name__ == "__main__":

    findPairs([8,7, 2, 5, 3, 1], target=10)