#include <iostream>
#include <climits>
using namespace std;

//Time: O(N)
//Space: O(1)

void find_min_subarray(int arr[], int n, int k)
{
    int window_sum = 0;
    int min_window = INT_MAX;
    int last = 0;

    for (int i = 0; i < n; i++) {

        window_sum += arr[i];

        if (i + 1 >= k) {
            
            if (window_sum < min_window) {
                min_window = window_sum;
                last = i;
            }
            //remove last element from the movind window
            window_sum -= arr[i + 1 -k];
        }
    }
    cout<<"Min subarray: ("<<last - k  + 1<<","<<last<<")"<<endl;

}

int main()
{
    int arr[] = {10, 4, 2 , 5, 6, 3, 8, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = 3;

    find_min_subarray(arr, n, k);

    return 0;

}