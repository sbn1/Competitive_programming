#include <iostream>
#include <math.h>
#include <utility>
#include <climits>

using namespace std;

int min(int x, int y)
{
    return (x < y)? x:y;
}

pair<int, int> find_min_sum(int arr[], int n)
{
    if (n < 2){
        return make_pair(-1,-1);
    }

    int left = 0,right = n-1;
    int optimal_left = 0, optimal_right;
    int min_sum = INT_MAX;

    while (left < right){

        //update the minium found so far
        if (abs(arr[left] + arr[right]) < min_sum ) {
            min_sum = abs(arr[left] + arr[right]);
            optimal_left = left;
            optimal_right = right;
        }

        // the optimal solution when the min_sum is zero
        if (min_sum == 0){ 
            break; }

        ((arr[left] + arr[right]) < 0) ? left++ : right--;
    }

    return make_pair(optimal_left, optimal_right);

}

int main()
{
    int arr[] = {-6, -5, -3, 0, 2, 4, 9};
    int n = sizeof(arr)/sizeof(arr[0]);
    pair<int, int> solution = find_min_sum(arr, n);

    cout<<"The pair is: "<<arr[solution.first]<<" and "<<arr[solution.second]<<endl;

    return 0;
}
