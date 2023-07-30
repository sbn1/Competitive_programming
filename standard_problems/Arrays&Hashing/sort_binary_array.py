# Given a binarry array, sort it in linear time and constant space. The 
# output should print all zeros, followed by ones.

# Method 1:using Two Pinters
# Method 2:Loop thourgh it and keep track of the position for zeros, 
# when encounter and non-zero, swap their places

# Time: O(N)
# Space: O(1)

def sortBinary(arr):
    l, r = 0, len(arr)-1

    while l<r:

        if (arr[l] == 1 and arr[r] == 0):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif (arr[l] ==1 and arr[r]==1):
            r -= 1
        else:
            l+=1
    return arr

def sortBinary_loop(arr):

    zero_position = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i], arr[zero_position] = arr[zero_position], arr[i]
            zero_position += 1

    return arr

if __name__ == "__main__":

    sortBinary([1,0,0,0,1,0,1,1,0,0,1,1])
    sortBinary_loop([1,0,0,0,1,0,1,1,0,0,1,1])