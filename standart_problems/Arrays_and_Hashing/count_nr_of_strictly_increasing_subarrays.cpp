#include <iostream>

//Time:O(N)
//Space: O(1)

int count_strictly_increasing_subarrays(int arr[], int n)
{
    int length = 1, count_inc_subarrays = 0;

    for (int i=1; i < n; i++)
    {
        if (arr[i] > arr[i-1]){
            count_inc_subarrays += length;
            length ++;
        }
        else {
            length = 1;
        }
    }

    return count_inc_subarrays;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 4, 5};
    int n = sizeof(arr)/sizeof(arr[0]);

    std::cout<<count_strictly_increasing_subarrays(arr, n)<<'\n';

    return 0;
}