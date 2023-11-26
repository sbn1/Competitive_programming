#include <iostream>
#include <stack>
#include <vector>

std::vector<int> find_greater_next_element(std::vector<int> const &arr)
{
    int n  = arr.size();
    //saves the default values -1
    std::vector<int> result(n, -1);

    std::stack<int> s;

    for (int i=0; i < n; i++)
    {
        while(!s.empty() && arr[s.top()] < arr[i] )
        {
            result[s.top()] = arr[i];
            s.pop();
        }

        s.push(i);
    }

    return result;
}

int main()
{   
    //Basic Case
    std::vector<int> arr = {2, 8, 3, 5, 4, 6, 7};
    //strictly increasing 
    //std::vector<int> arr = {2, 3, 5, 6, 7}
    //Strictly decreasing
    //std::vector<int> arr = {5, 4, 3, 2, 1, 6};

    std::vector<int> result = find_greater_next_element(arr);

    for(int i:result)
    {
        std::cout<<i<<" ";
    }
    std::cout<<"\n";

    return 0;
}