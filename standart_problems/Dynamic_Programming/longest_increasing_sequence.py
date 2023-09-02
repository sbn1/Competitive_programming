#Given an array, to be found the longest subsequence of a given sequence in which 
# the subsequence's elements are i sorted order. 

# Recoursive approach

def longest_increasing_subsequence(a, index=0, prev=float("-inf")):
     
    if index == len(a):
        return 0
    maxim_lenght = 0
    for i in range(index, len(a)):
        if a[i] > prev:
            increasing_subsequence = longest_increasing_subsequence(a, i, a[i]) + 1
            maxim_lenght = max(maxim_lenght, increasing_subsequence)

    return maxim_lenght

#Recursive approach 

def longest_increasing_subsequence_alt(a, index=0, prev=float("-inf")):

    if index == len(a):
        return 0
    
    from_next_position = longest_increasing_subsequence_alt(a, index + 1, prev)

    # initiation required, otherwise will not be allowed to use it
    from_current_position = 0
    if a[index] > prev:
        from_current_position = longest_increasing_subsequence_alt(a, index+1, a[index])+1

    return max(from_current_position, from_next_position)



# Divide et Impera aproach - Fails for very long arrays. 
# Fails to find the longest increasing sequence, but still passes some test
# Display the longest increasing sequence
def divide_et_impera(a, mid):
    left_prev = right_prev = a[mid]

    left_sum = []
    for i in range(mid-1, -1, -1):
        if a[i] < left_prev:
            left_sum += [a[i]]
            left_prev = a[i]

    right_sum =[]
    for j in range(mid+1, len(a)):
        if a[j] > a[mid]:
            right_sum += [a[j]]
            right_prev = a[j]

    if not left_sum and not right_sum:
        return []
    else:
        return left_sum[::-1] + [a[mid]] + right_sum
    
def main(a):
    if len(a) == 1:
        return []
    
    mid = len(a)//2

    left = main(a[:mid])
    right = main(a[mid:])
    combined = divide_et_impera(a, mid)

    return max([left, right, combined], key=len)

#Dynamic Programming Approach
#Time: O(N**2)
#Space: O(N)
def longest_increasing_dynamic(a):
    if not a:
        return []
    
    DP = [0]*(len(a))

    DP[0] = 1
    # will start from the second element and compare all the elements up to it
    for i in range(1,len(a)):
        #checks all the numbers up to a[i]
        for j in range(i):

            if a[j] < a[i] and DP[j] > DP[i]:
                # updates the longest sequences up to a[i]
                DP[i] = DP[j]
        # Once the highest value up to a[i] has been found, it will take +1 to consider the a[i]        
        DP[i] = DP[i] + 1

    return max(DP)

# Dynamic Programing Approach to display the longest increasing sequence
# Time: O(N**2)
#Space: O(N**2)
def longest_increasing_seq_display(a):
    if not a:
        return []
    # A matrix that will store the longest increasing sequences
    DP =[[] for _ in range(len(a))]

    DP[0].append(a[0])

    for i in range(1, len(a)):
        for j in range(i):
             if a[j] < a[i] and len(DP[j]) > len(DP[i]):
                 #Store the copy
                 DP[i] = DP[j].copy()
        DP[i].append(a[i])

    return max(DP, key=len)



if __name__ == "__main__":
    
    a_1 = [4, 2, 5, 9, 7, 10]
    a_2 = [1,2,3,4,5,6,7]
    longest_increasing_subsequence(a_1)
    longest_increasing_subsequence(a_2)

    longest_increasing_subsequence_alt(a_1)
    longest_increasing_subsequence_alt(a_2)

    main(a_1)
    main(a_2)

    longest_increasing_dynamic(a_1)
    longest_increasing_dynamic(a_2)

    longest_increasing_seq_display(a_1)
    longest_increasing_seq_display(a_2)