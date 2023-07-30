# Give an integer array, move all zeros present in it 
# to the end. The solution should maintain the relative order of the items
# in the array.

# Keet track of the zeros, and swap it with the next non zero element in the array
# Time: O(N)
# Space: O(1)

def MoveZeros(arr):

    zero_pos = 0

    for i in range(len(arr)):
        if arr[i]!=0:
            arr[zero_pos], arr[i] = arr[i], arr[zero_pos]
            zero_pos += 1
    return arr

if __name__ == "__main__":
    MoveZeros([6, 0, 8, 2, 3, 0, 4, 0, 1])

