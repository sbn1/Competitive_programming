#include <iostream>
#include <unordered_map>
#include <vector>
#include <iterator>

//Time: O(N ^ 2)
//Space: O(N)

void print_subarray(int arr[], int i, std::vector<int>& end)
{
    for (int j:end){
        std::cout<<"["<<(j + 1)<<","<<i<<"]"<<std::endl;
    }

}

void find_subarray_given_sum(int arr[], int n, int target){

    std::unordered_map<int, std::vector<int>> map;

    //base case arr[0] = target 
    map[0].push_back(-1);

    int sum_so_far = 0;

    for (int i = 0; i < n; i++)
    {
        sum_so_far += arr[i];

        auto itr = map.find(sum_so_far - target);
        if (itr != map.end())
        {
            print_subarray(arr, i, map[itr->first]);
        }
        map[sum_so_far].push_back(i);
    }

}
int main()
{
    int arr[] = {3, 4, -7, 1, 3, 3, 1, -4};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 7;
    find_subarray_given_sum(arr, n, target);

    return 0;
}