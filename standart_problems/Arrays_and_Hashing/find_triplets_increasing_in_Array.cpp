#include <iostream>

// Condition: Find Triplets A[i] < A[j] < A[k],   0<=i<j<k<n

//Time: O(N)
//Space: O(1)
void find_tripplets(int arr[], int n)
{
    int min_index = 0;
    int low = 0, mid =-1;

    for (int i = 1; i < n; i++)
    {
        //find the minimum so far
        if(arr[i] < arr[min_index])
        {
            min_index = i;
        }

        else if (mid == -1)
        {
            low = min_index;
            mid = i;
        }
        else if (arr[i] < arr[mid])
        {
            low = min_index;
            mid = i;
        }
        else {
            std::cout<<arr[low]<<","<<arr[mid]<<","<<arr[i]<<"\n";
            return; 
        }
    }

}
int main()
{
    int arr[] = {5, 4, 3, 7, 6, 1, 9};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_tripplets(arr, n);

    return 0;

}