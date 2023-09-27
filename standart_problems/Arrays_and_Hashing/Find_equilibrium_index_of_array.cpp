#include <iostream>
using namespace std;

void find_equilibrium_index(int arr[], int n)
{
    int total_sum = 0, incremental_sum=0;
    for (int i=0; i < n; i++)
    {
        total_sum += arr[i];
    }

    for (int i=0; i<n; i++)
    {
        if (incremental_sum == total_sum - incremental_sum - arr[i]){
            cout<<i<<"  ";
        }
        incremental_sum += arr[i];
    }
    cout<<endl;
}

int main()
{
    int arr[] = {0, -3, 5, -4, -2, 3, 1,0};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_equilibrium_index(arr, n);
}