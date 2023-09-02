# Find the longest decreasing subsequence (LDS) of a given array 
# in which the elements of the subsequence are in decreasing order.
#The subsequence does not have to be continuous or unique.

#Recoursive Approach

def LDS_recoursive(a, index=0, prev = float("inf")):
    if index == len(a):
        return 0
    
    longest_subsequence = 0

    for i in range(index, len(a)):
        if a[i] < prev:
            subsequence = LDS_recoursive(a, i, a[i]) + 1
            longest_subsequence = max(longest_subsequence, subsequence)

    return longest_subsequence

def LDS_recoursive_alt(a, index=0, prev=float("inf")):
    if index ==len(a):
        return 0
    
    from_next_element = LDS_recoursive_alt(a, index+1, prev)
    from_current_element = 0
    if a[index] < prev:
        from_current_element = LDS_recoursive_alt(a, index+1, a[index])+1

    return max(from_next_element, from_current_element) 


def LDS_dynamic_programming(a):
    if not a:
        return 
    
    DP = [0]*len(a)
    DP[0] = 1
    #starts from the second element
    for i in range(1, len(a)):
        #compare all the elements up to a[i]
        for j in range(i):
            #Update DP[i] with the higest length out of the elements that are lower
            if a[j] > a[i] and DP[j] > DP[i]:

                DP[i] = DP[j]
        # Add 1 to the length of the lonest sequence to account for a[i]
        DP[i] = DP[i] + 1

    return max(DP)

if __name__ == "__main__":
    a = [0, 8, 4,12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    LDS_recoursive(a)
    LDS_recoursive_alt(a)
    LDS_dynamic_programming(a)
    a = [1,2,3,4,5,6,7]
    LDS_recoursive(a)
    LDS_recoursive_alt(a)
    LDS_dynamic_programming(a)


