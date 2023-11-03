#include <iostream>
#include <utility>

//Time: O(N)
//Space: O(1)
std::pair<int, int> find_pairs_given_target_in_circular_sorted_array(int arr[], int n, int target)
{
    int max_position = 0, min_position = 0;

    for (int i =1; i < n; i++)
    {
        if (arr[i] > arr[max_position])
        {
            max_position = i;
        }
        if (arr[i] < arr[min_position])
        {
            min_position = i;
        }

    }
    int left
     = min_position, right = max_position;

    while( (left < n - max_position + 1) && (right >= 0) && (left != right))
    {
        if (arr[left] + arr[right] > target){
            right--;
        }
        else if (arr[left] + arr[right] < target){
            left++;
        }
        else {
            return std::make_pair(arr[left], arr[right]);
            
        }

    }
    return std::make_pair(-1, -1);
}

int main()
{
    int arr[] = {15, 3, 6, 8, 9, 10, 12};
    //int arr[] = {3, 6, 8, 9, 10, 12, 15};
    int n = sizeof(arr)/sizeof(arr[0]);

    int target = 18;
    
    std::pair<int, int> pair_with_target_sum = find_pairs_given_target_in_circular_sorted_array(arr, n,target);

    if (pair_with_target_sum.first != -1 && pair_with_target_sum.first != -1){
        std::cout<<pair_with_target_sum.first<<", "<<pair_with_target_sum.second<<"\n";
    }
    else
    {
        std::cout<<"There no pair that can for the target"<<"\n";
    }

    return 0;
}