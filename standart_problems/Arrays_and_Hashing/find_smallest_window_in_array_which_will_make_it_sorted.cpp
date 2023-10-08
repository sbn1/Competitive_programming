#include <iostream>
#include <climits>

using namespace std;

void find_window(int arr[], int n)
{
    int left_index = -1, right_index = -1;

    int max_so_far = INT_MIN;
    int min_so_far = INT_MAX;

    for (int i=0; i< n ; i++)
    {
        if (arr[i] > max_so_far){
            max_so_far = arr[i];
        }
        if(arr[i] < max_so_far)
        {
            right_index = i;
        }
    }

    for (int i = n-1; i>=0; i--){
        if (arr[i] < min_so_far){
            min_so_far = arr[i];

        }

        if (arr[i] > min_so_far){
            left_index = i;
        }
    }
    if(left_index == -1){
        cout<<"Array is already sorted"<<endl;
        return;
    }

    cout<<"Sort the array from: "<<left_index<<" to "<<right_index<<endl;
    

}

int main()
{ 
    int arr[] = {1, 2, 3, 7, 5, 6, 4, 8};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_window(arr, n);

    return 0;
}