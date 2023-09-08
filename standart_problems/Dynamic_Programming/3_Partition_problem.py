# 3 -partition problem: Given a set S of positive integers, determine if it 
# can be partiitoned into three disjoint subsets that all have the same sum, sum(S)//3

# create 3 distinct targets : a, b, c. Where each is sum(arr)//3. If 
# 


# Recursive Approach 

def three_partition_recursive(arr, n, a, b, c):

    # return True when all three sets have been found
    if (a == 0) and (b == 0) and (c == 0):
        return True
    # BAse Case: when the limit of the array is reached
    if (n < 0):
        return False
    
    A = False
    if (a - arr[n] >=0):
        A = three_partition_recursive(arr, n -1, a - arr[n], b, c)
    
    B = False
    if (not A) and (b - arr[n] >= 0):
        B = three_partition_recursive(arr, n - 1, a, b - arr[n], c)

    C = False
    if (not A) and (not B) and (c - arr[n] >=0):
        C = three_partition_recursive(arr, n - 1, a, b, c - arr[n])
    
    return A or B or C

# Time: O(N x sum(S)**3)
# Space: O(N x sum(S)**3)

def three_partition_dynamic(arr, n, a, b, c, saved_paths={}):

    # return True when all three sets have been found
    if (a == 0) and (b == 0) and (c == 0):
        return True
    
    # BAse Case: when the limit of the array is reached
    if (n < 0):
        return False
    
    key = (n, a, b, c)

    if key not in saved_paths:

        A = False
        if (a - arr[n] >=0):
            A = three_partition_dynamic(arr, n -1, a - arr[n], b, c,saved_paths)
        
        B = False
        if (not A) and (b - arr[n] >= 0):
            B = three_partition_dynamic(arr, n - 1, a, b - arr[n], c, saved_paths)
            
        C = False
        if (not A) and (not B) and (c - arr[n] >=0):
            C = three_partition_dynamic(arr, n - 1, a, b, c - arr[n],saved_paths)
    
        saved_paths[key] = A or B or C

    return saved_paths[key]

if __name__ == "__main__":

    arr = [7, 3, 2, 1, 5, 4, 8]
    three_partition_recursive(arr, len(arr)-1, sum(arr)//3, sum(arr)//3, sum(arr)//3)
    three_partition_dynamic(arr, len(arr)-1, sum(arr)//3, sum(arr)//3, sum(arr)//3)

    