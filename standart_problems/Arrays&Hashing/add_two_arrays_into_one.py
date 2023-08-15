# Given two arrays of positive integers, add their elements into a new 
# array. The solution should add both arrays, one by one starting from the 0th index,
# and split the sum into individual digits if it is a 2–digit number.

def split(combined, solution):
    # recoursive function
    if combined > 0:
        split(combined//10, solution)
        solution.append(combined%10)
    return solution

def addArray(arr1, arr2,solution):
    
    i = 0
    while i<len(arr1) and i < len(arr2):
        split(arr1[i] + arr2[i],solution)
        i += 1
    while i < len(arr1):
        split(arr1[i],solution)
        i += 1
    while i < len(arr2):
        split(arr2[i], solution)
        i += 1
    
    return solution

if __name__ =="__main__":
    addArray(arr1 =[ 23, 5, 2, 7, 87], arr2 = [4, 67, 2, 8],solution=[])
     
    