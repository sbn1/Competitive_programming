# Given an unsorted int array, print all pairs with a given difference k in it.

# Set a set that will store the differences, (without duplicates)
# Check the element -k and element + k
# Time : O(N)
# Space: O(N)

def findPair(a, k):
    set_to_store_array = set()
    pairs = set()
    for i in a:
        if i - k in set_to_store_array:
            pairs.add((i-k, i))
        if i + k in set_to_store_array:
            pairs.add((i, i+k))
        set_to_store_array.add(i)

    return pairs

if __name__ == "__main__":
    
    findPair(a =[1,5,2,2,2,5,5,4],k=3)