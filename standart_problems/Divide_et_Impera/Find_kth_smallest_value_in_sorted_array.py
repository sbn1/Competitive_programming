# Given a row-wise and column-wise sorted square matrix and a positive integer k, 
# find the kth smallest number in the matrix.


# The solution will use binary search and divide et impera. First will traverse the matrix using binary search 
# and on every step will count the elements up to mid. The taversa will focus on the interval [min, max] and will
# loop thourgh the mid in this interval.



def count_elements_less_or_equal(matrix, mid_value):

    top, bottom = len(matrix)-1, 0
    counter = 0

    while (top >= 0) and (bottom < len(matrix)):
        if matrix[top][bottom] > mid_value:
            top -= 1
        else:
            counter += (top + 1)
            bottom += 1

    return counter


def find_k_smalles_element(matrix, k):

    if (len(matrix) == 0 or k<=0):
        return
    
    low, high = matrix[0][0], matrix[len(matrix)-1][len(matrix)-1]

    while low <= high:
        mid = (low + high)//2

        count = count_elements_less_or_equal(matrix, mid)

        if count < k:
            low = mid + 1
        else:
            high = mid - 1

    return low

if __name__ == "__main__":

    matrix = [[-3, 1, 3], [-2, 2, 4], [1, 3, 5]]

    find_k_smalles_element(matrix, k=6)
    find_k_smalles_element(matrix, k=5)