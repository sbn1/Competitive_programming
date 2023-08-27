# Segregate an array of positive numbers and negative integers, segregate them
# without changing the relative order of the elements. The output should contain all
# positive numbers follow the negative numbers while maintaining the same relative ordering.

# Solution: Using a similar approach to Merge Sort
#Time: O(N*LOG(N))
#Space: O(N)

def segregate_neg_and_positive(a):

    if len(a)>1:

        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        segregate_neg_and_positive(left)
        segregate_neg_and_positive(right)

        k = 0
        i = j = 0
        # Select the negative elements from the left side
        while (i < len(left)):
            if left[i] < 0:
                a[k] = left[i]
                k += 1
            i += 1
        # select negative numbers from the right side
        while (j < len(right)):
            if (right[j] < 0):
                a[k] = right[j]
                k += 1
            j += 1

        i = j = 0
        #select positive numbers from the left side
        while (i < len(left)):
            if (left[i] >= 0):
                a[k] = left[i]
                k += 1
            i += 1
        
        # select positive numbers from the right side
        while ( j < len(right)):
            if (right[j] >= 0):
                a[k] = right[j]
                k += 1
            j += 1    
            
if __name__ == "__main__":
    a = [9, -3, 5, -2, -8, -6, 1,3]
    segregate_neg_and_positive(a)

    print(a)

            
