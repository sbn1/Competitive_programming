#include <iostream>
#include <climits>
using namespace std;

int find_smallest_subarray_sum_greater(int arr[], int n, int k)
{
    int left = 0, left_index = 0;
    int moving_sum = 0;
    int min_lenght = INT_MAX;

    for (int i=0; i < n; i++)
    {
        moving_sum += arr[i];

        while (moving_sum > k && left <= i){
            if ((i - left + 1) < min_lenght ){
                min_lenght = i - left + 1;
            }

            moving_sum -= arr[left];

            left++;
        }
        

    }

    
    return (min_lenght == INT_MAX)? 0:min_lenght;
 

}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6,7, 8};
    int n =sizeof(arr)/sizeof(arr[0]);
    int k = 21;

    if (find_smallest_subarray_sum_greater(arr, n,k ) != INT_MAX){
        cout<<"Smallest subarray greater than "<<k<<" : "<<find_smallest_subarray_sum_greater(arr, n,k )<<endl;
    }
    else {
        cout<<"There is no subarray smaller than k"<<endl;
    }

    return 0; 
}