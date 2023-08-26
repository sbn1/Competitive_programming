# Given an array, generate all the possible permutaitons

# Time : O(N!)
# Space: O(N!)

def permuations(a, index=0, sol=[]):
    
    if index == len(a):
        sol.append(a[:])
        return

    for i in range(index, len(a)):
        a[i], a[index] = a[index], a[i]
        permuations(a, index + 1, sol)
        a[i], a[index] = a[index], a[i]

    return sol



def permutations_1(a, sol=[], tmp=[]):

    if not a:
        sol.append(tmp[:])
        return
    
    for i in range(len(a)):
        permutations_1(a[:i]+a[i+1:],sol, tmp+[a[i]])
    
    return sol



if __name__ == "__main__":
    
    permuations([1, 2, 3])
    permutations_1([1, 2, 3, 4])