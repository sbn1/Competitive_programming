# Given that there are two sorted arrays X and Y, mearge elements of X and Y
# so that the sorted order is maintained, where X will contains the smallest 
# and Y will contains the remainding elements (greatest).

# Traverse the array and compare each elements of X with the first elements of Y
# if the elemtns of Y is lower, replace them than then traverse again the Y 
# to find the position on the newly swaped element.
# The conversion has to be inplace without using any other data structures

# Time: O(N*M)
# Space: O(1)

from typing import List
def merge_sorted_inplace(x:List[int], y:List[int]) -> List[int]:

    for i in range(len(x)):
         if (x[i] > y[0]):
              x[i], y[0] = y[0], x[i]
              j = 1
              while (j < len(y)) and (y[j - 1] > y[j]):
                   y[j-1], y[j] = y[j], y[j-1]
                   j += 1
    return x, y

if __name__ == "__main__":
     merge_sorted_inplace(x = [1,4,7,8,10], y = [2, 3, 9])