#include <iostream>
#include <climits>

using namespace std;

int max(int x, int y) { return (x > y)? x:y; }

void print_max_sum_subarray(int arr[], int n)
{
    int ending = 0,start = 0,save_start = 0;

    int sum = 0, max_sum = INT_MIN;

    for (int i=0; i < n; i++)
    {
        sum = arr[i] + sum;

        if ( sum < arr[i]){ 
            sum = arr[i];
            start = i;
            ending = i;
        } 
        
        if (sum > max_sum){
            max_sum = sum;
            save_start = start;
            ending = i;
        }
    } 
    cout<<"Max Sum: "<<max_sum<<endl;

    for (int i=save_start; i<=ending; i++){ cout<< arr[i]<<"  "; }
    cout<<endl;

}

int main() 
{
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    print_max_sum_subarray(arr, n);

    return 0;
}