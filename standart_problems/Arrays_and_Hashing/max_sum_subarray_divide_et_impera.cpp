#include <iostream>
#include <limits.h>
#include <vector>

//Time: O(N*LogN)
//Space: O(N) due to recursion
int max(int x, int y){
    return (x > y) ? x:y;
}

int find_maxim_sum_subarray(int arr[], int left, int right)
{
    if ( left >= right){
        return arr[left];
    }

    int mid = (left + right)/2;

    //left subarray

    int max_to_left = INT_MIN;
    int sum_left = 0;
    for (int i=mid; i >=left; i--){
        sum_left += arr[i];
        
        if (sum_left > max_to_left){
            max_to_left = sum_left;
        }

    }

    // right subarray

    int max_to_right = INT_MIN;
    int sum_right = 0;
    for (int i=mid + 1; i <= right; i++)
    {
        sum_right += arr[i];

        if (sum_right > max_to_right)
        {
            max_to_right = sum_right;
        }
    }

    //max between the left and the right side recursive
    int max_left_or_right = max(find_maxim_sum_subarray(arr, left, mid), 
                                find_maxim_sum_subarray(arr, mid+1, right));

    //compare the max between left and right with maximum combined
    return max(max_left_or_right, max_to_left + max_to_right);
    
}

int main()
{

    int arr[] = {2, -4, 1, 9, -6, 7, -3};
    int n = sizeof(arr)/sizeof(arr[0]);

    std::cout<<find_maxim_sum_subarray(arr, 0, n-1)<<"\n";

    return 0;
}