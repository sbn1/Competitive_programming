# Given an array , find the peak element in it. A peak element is an element that
# is greater than its neighbour. There might be multiple peak elements in the array, the solution
# should include any peak element

#Time:O(LogN)
#Space: O(1)

def find_peak_element(a, left=None, right=None):

    if left is None and right is None:
        left, right = 0, len(a)-1
        
    mid = (left + right)//2

    if (mid ==0 or a[mid-1] <= a[mid]) and (mid == len(a)-1 or a[mid+1] <= a[mid]):
        return mid
    
    if (mid - 1 >= 0) and (a[mid - 1] > a[mid]):
        return find_peak_element(a, left, mid - 1)
    
    return find_peak_element(a, mid + 1, right)

def print_peak(a):
    if not a:
        return 
    index_of_peak = find_peak_element(a)
    return a[index_of_peak]

if __name__ == "__main__":


    print_peak([8, 9, 10, 2, 5, 6])
    print_peak([10, 8, 6, 5, 3,2])