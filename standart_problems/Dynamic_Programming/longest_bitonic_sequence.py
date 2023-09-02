# Find the longest bitonic subsequence, where the elements 
# of the subsequence are first sorted in increasing order, 
# then in decreasing order. Then find the subsequence that has the 
# maximum length and has bitonic proprietie.

# The solution combines the same approach as in longest increasing and longest 
#decresing subsequence, two classical dynamic programming problems.

#Time: O(N**2)
#Space: O(N)

def longest_bitonic_subsequence(a):
    if not a:
        return 0
    
    #First find the longest increasing subsequence

    I=[0]*len(a)
    I[0] = 1

    for i in range(1, len(a)):
        for j in range(i):

            if a[j] < a[i] and I[j] > I[i]:
                I[i] = I[j]

        I[i] = I[i] + 1

    # Find the longest decreasing subsequence, but starting from the end of the list
    D=[0]*len(a)
    D[-1] = 1

    for i in range(len(a)-2, -1, -1):
        for j in range(i, len(a)):
            if a[j] < a[i] and D[j] > D[i]:
                D[i] = D[j]
        D[i] = D[i] + 1
    
    # Find the position in both mnemonics that yields maximum value -1, since
    # both have already ccouted for a[i] 
    maximum_bitonic_seq = 1
    for i in range(len(a)):
        maximum_bitonic_seq = max(maximum_bitonic_seq, I[i] + D[i] -1)

    return maximum_bitonic_seq

if __name__ =="__main__":

    longest_bitonic_subsequence([4, 2, 5, 9, 7,6, 10, 3, 1])
    longest_bitonic_subsequence([1, 2, 3, 4, 5, 6, 7, 8])


