#include <iostream>

//Find min number of removals form the original array
//to obtain the subarray that meets the condiion 2 x min > max

//Time:O(N**2)
//Space:O(1)

int max(int x, int y) { return (x > y)? x:y;}
int min(int x, int y) { return (x < y)? x:y; }

int find_min_number_of_removals(int arr[], int n)
{
    int max_len_subarray = 0;

    for (int i=0; i<n; i++)
    {
        int max_subarray = arr[i], min_subarray = arr[i];

        for (int j = i; j < n; j++)
        {
            max_subarray = max(max_subarray, arr[j]);
            min_subarray = min(min_subarray, arr[j]);

            if (min_subarray * 2 <= max_subarray){
                break;
            }
            max_len_subarray = max(max_len_subarray, j - i + 1);
        }
    }

    return n - max_len_subarray;

}

int main()
{
    int arr[] = {4, 6, 1, 7, 5, 9, 2};
    //int arr[] = {4, 2, 6, 4, 9};
    int n = sizeof(arr)/sizeof(arr[0]);

    std::cout<<find_min_number_of_removals(arr, n)<<'\n';

    return 0;
}