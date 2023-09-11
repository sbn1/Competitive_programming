# Given sequence, find the longest subsequence in which 
# the elements are in alternating order and in which the sequence is 
# as long as possible. 

# Example: Input: [8, 9, 6, 4, 5, 7, 3, 2, 4]
        #  Output: 8 < 9 > 6 < 7 > 3 < 4

# Recursive Approach 


def longest_subsequence_recursive(arr,index,end, Flag):

    solution = 0
    for i in range(index, end):
        # if the Flag is True the next element should be greater
        # If the flag is set to False the next element should be smaller
        if (arr[i] > arr[i-1]) and Flag:

            # arr[i] is included in the sequence
            solution = max(solution,longest_subsequence_recursive(arr, i + 1, end, not Flag) + 1)
         # in a sense if the Flag variable changes the " >" with "<"
        elif (arr[i] < arr[i -1]) and not Flag:
            # arr[i] is included in the sequence
            solution = max(solution, longest_subsequence_recursive(arr, i + 1, end, not Flag) + 1)
        
        else:
            # the arr[i] is skipped
            solution = max(solution, longest_subsequence_recursive(arr, i + 1, end, Flag))
    
    return solution


def longest_alternating_rec(arr, n, Flag):
    
    # BASE CASE
    if n < 0 :
        return 0
    
    solution = 0
    exclude = longest_alternating_rec(arr, n -1, Flag)

    if arr[n] > arr[n-1] and Flag:
        solution = max(solution, 1 + longest_alternating_rec(arr, n -1, not Flag))

    elif arr[n] < arr[n -1] and not Flag:
        solution = max(solution, 1 + longest_alternating_rec(arr, n - 1, not Flag))

    else:
        solution = max(solution,exclude)

    return solution

def find_longest_subsequence(arr):

    if not arr:
        return 0
    
    # The longest_subsequence_recursive function does not account the first element, 
    # it compares the arr[i] with arr[i-1], and the arr[i-1] is not included in the length. 
    # However, it should be aways part of the longest subsequence since the other 
    # elements are either lower or higher than the firsr element

    # the returns check cases when the sequence starts with "<" or ">" plus 1 for the first element
    return 1 + max(longest_subsequence_recursive(arr, 1, len(arr), True), 
                   longest_subsequence_recursive(arr, 1, len(arr), False))

def find_longest_alternating(arr):
    if not arr:
        return 0
    
    return 1 + max(longest_alternating_rec(arr, len(arr)-1, True), 
                   longest_alternating_rec(arr, len(arr)-1, False))


# Dynamic Programming Approach

#The solution can be optimized if instead of the dict saved_paths a 2 X len(arr) 
# matrix is taken since there are 2 dimensions for True and False 

# Time: O(N**2)
# Space: O(N)
def longest_subsequence_dynamic(arr,index,end, Flag, saved_paths={}):

    if index >=end:
        return 0
    
    key = (index, Flag)
    if key not in saved_paths:

        solution = 0
        for i in range(index, end):

            if (arr[i] > arr[i-1]) and Flag:

                solution = max(solution,longest_subsequence_dynamic(arr, i + 1, end, not Flag, saved_paths) + 1)
            # in a sense if the Flag variable changes the " >" with "<"
            elif (arr[i] < arr[i -1]) and not Flag:
                # arr[i] is included in the sequence
                solution = max(solution, longest_subsequence_dynamic(arr, i + 1, end, not Flag, saved_paths) + 1)
            
            else:
                solution = max(solution, longest_subsequence_dynamic(arr, i + 1, end, Flag, saved_paths))

        saved_paths[key] = solution

    return saved_paths[key]

def find_longest_alternating_dynamic(arr):

    if not arr:
        return 0
    
    return 1 + max(longest_subsequence_dynamic(arr, 1, len(arr), True),
                    longest_subsequence_dynamic(arr, 1, len(arr), False))


# Dynamic Programming Approach  - Classic

# Time: O(N**2)
# Space: O(N)

def find_Longest_subsequence_dynamic(arr):

    if not arr or len(arr) <= 1:
        return len(arr)
    
    DP = [[0 for _ in range(2)] for _ in range(len(arr)+1)]
    
    solution = 1

    # First element is always part of the longest alternating subsequence
    DP[0][0] = DP[0][1] = 1

    for i in range(1,len(arr)):

        for j in range(i):

            if arr[i] > arr[j]:

                DP[i][0] = max(DP[i][0], DP[j][1] + 1)

            if arr[i] < arr[j]:

                DP[i][1] = max(DP[i][1], DP[j][0] + 1)

        if solution < max(DP[i][0], DP[i][1]):
            solution = max(DP[i][0], DP[i][1])

    return solution



if __name__ == "__main__":

    arr = [8, 9, 6, 4, 5, 7, 3, 2, 4]
    find_longest_subsequence(arr)
    find_longest_alternating(arr)

    find_longest_alternating_dynamic(arr)

    find_Longest_subsequence_dynamic(arr)

        