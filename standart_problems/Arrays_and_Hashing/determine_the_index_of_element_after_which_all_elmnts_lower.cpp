#include <iostream>
#include <climits>

using namespace std;

//Time: O(N)
//Space: O(N)

int min(int x, int y){ return (x < y) ? x:y; }
int max(int x, int y){ return (x > y) ? x:y; }

int find_index(int arr[], int n){
    int index = 0;
    int right[n];
    int minimum = INT_MAX;
    for (int i=n-1; i >= 0; i--){
        minimum = min(minimum, arr[i]);
        right[i] = minimum;
    }

    int maximum = arr[0];
    for (int i=1; i < n-1; i++){

        if (arr[i] > maximum && arr[i] < right[i+1]){
            return i;
        }
        maximum = max(maximum, arr[i]);

    }

    return -1;
}

int main()
{
    int arr[] = {4, 2, 3, 5, 1, 6, 9, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
    int index = find_index(arr, n);
    cout<<"Index:"<<index<<"  Element:"<<arr[index]<<endl;

    return 0;
}