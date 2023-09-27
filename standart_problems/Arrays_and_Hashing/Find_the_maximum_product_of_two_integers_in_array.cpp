#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;
//Time : O(N)
//Space: O(1)
void find_max_product(int arr[], int n)
{
// ensure that there are more than 2 elements in the array
if (n < 2){
    return;
}
int max_1 = arr[0], max_2 = INT_MIN;
int min_1 = arr[0], min_2 = INT_MAX;

for (int i=1; i < n; i++)
{
    if (arr[i] > max_1)
    {   
        max_2 = max_1;
        max_1 = arr[i];
    }
    else if (arr[i] > max_2){
        max_2 = arr[i];
    }

    if (arr[i] < min_1)
    {
        min_2 = min_1;
        min_1 = arr[i];
    }
    else if (arr[i] < min_2)
    {
        min_2 = arr[i];
    }
}
if (max_1 * max_2 > min_1*min_2){
    cout<<max_1<<"  "<<max_2<<endl;}
    else {cout<<min_1<<"  "<< min_2<<endl;}
}

int main()
{
    int arr[] = {-10, -3, 5, 6, -2};
    int n = sizeof(arr)/sizeof(arr[0]);
    find_max_product(arr, n);


}