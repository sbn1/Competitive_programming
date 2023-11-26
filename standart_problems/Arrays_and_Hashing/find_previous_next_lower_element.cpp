#include <iostream>
#include <stack>
#include <vector>

std::vector<int> find_previous_lower_element(std::vector<int> const &arr)
{
    std::vector<int> solution (arr.size(), -1);
    std::stack<int> s;

    for (int i = arr.size()-1; i >=0; i--)
    {
        while(!s.empty() && arr[s.top()] > arr[i])
        {
            solution[s.top()] = arr[i];
            s.pop();
        }
        
        s.push(i);
        
    }

    return solution;
}
int main()
{
    //std::vector<int> arr = {2, 5, 3, 7, 8, 1, 9};
    //std::vector<int> arr = {2, 3, 4, 5, 6,7};
    std::vector<int> arr = {7,6,5,4,3,2,1};
    std::vector<int> solution = find_previous_lower_element(arr);

    for (int i=0; i<solution.size(); i++ )
    {
        std::cout<<solution[i]<<" ";
    }

    std::cout<<"\n";

    return 0;
}