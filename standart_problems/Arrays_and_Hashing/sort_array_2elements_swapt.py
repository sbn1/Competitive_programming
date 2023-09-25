# Given an array where all its elements are sorted in incresing order except 
#two swaped elements, sort it in linear time. Assume there are no duplicates
# in the array

# traverse the array using Two Pointers, start from the begging, 
# once the mismatch is found start to traverse the array from the bottom
# until you find the other one and swap them
# Time: O(N)
# Space: O(1)

def sortArray(a):
    if len(a)<1:
        return 
    
    l, r = 1, len(a)-1
    while l<r:
        if (a[l] < a[l-1]):
            while l <= r:
                if (a[r] < a[r-1]):
                    a[l-1], a[r] = a[r], a[l-1]
                r -= 1
        l += 1
    
    return a

if __name__ == "__main__":

    sortArray([3, 8, 6, 7, 5, 9])
    sortArray([3, 5, 6, 9, 8, 7])
    sortArray([3, 5, 7, 6, 8, 9])