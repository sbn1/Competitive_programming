# Given a string, find all combinations of non-overlapping substrigs of it.

# Take the prefix of the string s up to i+1, s[:i+1] and backtrack the remainging 
#sting s[i+1:] until the whole stirng is processed. One it is empty save the 
#solution

def find_all_combinations_of_substrings(s:str, sol=[], tmp=[]):
    #Base Case: we check if the string s is empty
    if not s:
        sol.append(tmp[:])
        return

    for i in range(len(s)):
        tmp += [s[:i+1]]
        find_all_combinations_of_substrings(s[i+1:], sol, tmp)
        tmp.pop()
    return sol

if __name__== "__main__":

    find_all_combinations_of_substrings("ABC")
    find_all_combinations_of_substrings("ABCD")