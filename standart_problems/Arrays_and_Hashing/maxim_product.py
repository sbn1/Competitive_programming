# Given an integer array, find the maximum product of its elements among 
# all its subsets
#Keep track of the maximum and minimum product and update them on each step
# during the iteraiton
# Time: O(N)
# Space: O(1)
def FindMaxProduct(a):
    max_product = min_product = a[0]

    for i in range(1, len(a)):
        max_product = max(max_product, max_product*a[i], min_product*a[i])
        min_product = min(min_product, min_product*a[i])
    return max_product, min_product

if __name__ == '__main__':
    
    a = [-6, 4, -5, 8, -10, 8]
    FindMaxProduct(a)

    a = [-6, 4, -5, 8, -10]
    FindMaxProduct(a)