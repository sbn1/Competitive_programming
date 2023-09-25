# Given an int array find the maximum product of two integers in it.

# Check the maximum product between the max and element and min and element at each step, 
# since there can be negtive elements.
# Time: O(N)
# Space: O(1)


def findMaxProduct(arr):
    product = float("-inf")
    minimum = maximum = arr[0]
    for i in range(1, len(arr)):
        product = max(product, maximum*arr[i], minimum*arr[i])
        maximum = max(maximum, arr[i])
        minimum  = min(minimum, arr[i])

    return product

if __name__ == "__main__":

    findMaxProduct([-10, -3, 5, 6, -2])
    findMaxProduct([-3, 4, 5, -7, 2, 0, 1])