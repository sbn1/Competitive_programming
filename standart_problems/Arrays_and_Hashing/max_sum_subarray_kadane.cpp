#include <iostream>
#include <climits>
using namespace std;

int max_sum_subarray(int arr[], int n)
{
    int total_max_sum=INT_MIN, max_sum = 0;

    for (int i=0; i < n; i++)
    {
        if (max_sum + arr[i] > arr[i])
        {
            max_sum = max_sum + arr[i];
        }
        else { max_sum = arr[i]; }

        if (max_sum > total_max_sum) {
            total_max_sum = max_sum;
        }
    }
    return total_max_sum;
}

int main()
{
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<< max_sum_subarray(arr, n)<<endl;

return 0;
}