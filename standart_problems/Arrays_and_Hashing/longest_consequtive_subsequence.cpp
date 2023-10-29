#include <iostream>
#include <unordered_set>
#include <set>
#include <vector>

//Time: O(N) with we search in the set the worst time it is O(N longN), 
//assumming that all the elements in the original array are different
//Space: O(N)

int max(int x, int y) { return (x > y)? x : y; }

int longest_consequtive_subsequence(std::vector<int> & vec)
{
    std::set<int> set(vec.begin(), vec.end());

    int max_lenght = 0;

    for (int i=0; i<vec.size(); i++)
    {
        if (set.find(vec[i] - 1) == set.end())
        {
            int length = 1;

            while ( set.find(vec[i] + length) !=set.end())
            {
                length++;
            }
            max_lenght = max(max_lenght, length);
        }
    }

    return max_lenght;
}

int main()
{
    std::vector<int> vec = {2, 0, 6, 1, 5, 3, 7};

    std::cout<<longest_consequtive_subsequence(vec)<<"\n";

    return 0;
}