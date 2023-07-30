# Given an int array find the equillibrium indes in it.
# 
#Find the sum, then check the right side the sum and check where is the 
# equillibrium.
#Time: O(N)
#Space: O(N) 

def findEquillibrium(arr):
    suma = sum(arr)
    right_sum = 0
    indices=[]
    for i in range(len(arr)-1, -1, -1):
        if (right_sum == suma - arr[i] - right_sum):
            indices.append(i)
        right_sum += arr[i]

    return indices

if __name__ == "__main__":
    findEquillibrium([ 0, -3, 5, -4, -2, 3, 1, 0])