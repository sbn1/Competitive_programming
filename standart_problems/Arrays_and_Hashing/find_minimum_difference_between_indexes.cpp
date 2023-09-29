#include <iostream>
#include <climits>
#include <math.h>
using namespace std;

int min(int x, int y)
{
    return (x < y)? x:y;
}
int find_min_differences(int arr[], int n, int x, int y){

    int x_i = -1, y_i = -1;
    int min_difference = INT_MAX;

    for (int i=0; i < n; i++){
        if (arr[i] == x)
        {   x_i = i;
            if (y_i != -1){
                min_difference = min(min_difference, abs(x_i - y_i));
            }
        }
        if (arr[i] == y) 
        {
            y_i = i;
            if (x_i != -1)
            {
                min_difference = min(min_difference, abs(x_i - y_i));
            }
        }
    }
    return min_difference;

}

int main()
{
    int arr[] = {1, 3, 5, 4, 8, 2, 4, 3, 6, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 3, y = 2;

    cout<<find_min_differences(arr, n, x, y)<<endl;

    return 0;
}