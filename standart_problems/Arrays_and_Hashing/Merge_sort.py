# Merge Sort: Divide and Conquer Algorithm, split the array in left and right
# sort each part and then traverse one by one and fill in the array = left+right
# traverse the case when both left and right have the same length
# if there is something left, either in the left side or the right side, then that is the 
# maximum value att hat particular level, so just simply add it at the end of the array.

# Time: O(N*Log N)
#Space: O(N)

from typing import List

def merge_sort(array:List[int]):

# the base case
    if len(array) > 1:

        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        # two indexes that will track the left and right sides
        i = j = 0
        # one index that will track the full array = left + right
        k = 0

        while (i < len(left)) and (j < len(right)):
            if (left[i] <= right[j]):
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # Check if there is remeinder in theleft side
        while (i < len(left)):
            array[k] = left[i]
            i += 1
            k += 1
        
        #Check if there is reminder in the right side

        while (j < len(right)):
            array[k] = right[j]
            j += 1
            k += 1
    #print(array)
    return array

if __name__ == "__main__":

    array = [83, 20, 9, 50, 115, 61, 17]
    merge_sort(array)


