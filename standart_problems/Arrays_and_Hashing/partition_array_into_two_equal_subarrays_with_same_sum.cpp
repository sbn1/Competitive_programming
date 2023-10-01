#include <iostream>

using namespace std;

//Time: O(N)
//Space: O(1)
int find_position(int arr[], int n)
{
    int total_sum = 0, so_far_sum = 0;

    for (int i=0; i<n; i++){ total_sum +=arr[i]; }

    for (int i=0; i < n; i++)
    {
        if (so_far_sum == total_sum - so_far_sum){
            return i;
        }
        so_far_sum += arr[i];
    }

    return -1;

}

int main()
{
    int arr[] = {6, -4, -3, 2, 3};
    int n = sizeof(arr)/sizeof(arr[0]);

    int position = find_position(arr, n);

    if (position != -1){
        for (int i=0; i<position; i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
        for (int i=position; i < n; i++ ){
            cout<<arr[i]<<" ";

        }
        cout<<endl;
    }
    else {
        cout<<"the array can not be partitioned";
    }

    return 0;

}