#include <iostream>
#include <set>

//Time: O(N)
//Space: O(N)

bool find_if_array_has_sum_div_by_k(int arr[],int n,  int k)
{
    std::set<int> s;

    for (int i = 0; i < n; i++)
    {
        if (s.find(k - (arr[i] % k)) != s.end()){
            return true;
        }
        else {
            s.insert(arr[i] % k);
        }
    }
    return false;
}

int main()
{
    int arr[] = {5, 1, 13, 6, 9, 4};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = 8;

    std::cout<<find_if_array_has_sum_div_by_k(arr, n, k)<<"\n";

    return 0;
}