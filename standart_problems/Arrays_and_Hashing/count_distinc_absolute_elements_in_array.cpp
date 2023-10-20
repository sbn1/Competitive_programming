#include <iostream>
#include <math.h>

int count_distinct_abs_elements(int arr[], int n)
{
    int count_distinct = n;
    int left = 0, right = n-1;

    while (left < right)
    {
        //check repeating elements from the left side
        while ((left < right) && arr[left+1] == arr[left])
        {
            count_distinct--;
            left++;
        }
        //check repeting from the rght side

        while ((left < right)&&(arr[right] == arr[right - 1]))
        {
            count_distinct--;
            right--;
        }

        int sum = arr[left] + arr[right];

        if (sum == 0)
        {
            count_distinct--;
            left++;
            right--;
        }
        else if (sum < 0)
        {
            left++;
        }
        else {
            right--;
        }
    }

    return count_distinct;
}

int main()
{
    int arr[] = {-1, -1, 0, 1, 1, 1};

    //int arr[] = {1,1,1,1,1,1,1,1};
    int n = sizeof(arr)/sizeof(arr[0]);

    std::cout<<count_distinct_abs_elements(arr, n)<<std::endl;

    return 0;
}