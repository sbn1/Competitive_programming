#include <iostream>

using namespace std;

// Time: O(N); 
// Space: O(1)

int max(int x, int y)
{
    return (x > y)? x: y;
}
int min(int x, int y)
{
    return (x < y) ? x:y;
}
int find_max_product(int arr[], int n)
{
    if (n < 1){
        return 0;
    }
    if (n == 1){
        return arr[n-1];
    }

    int max_product = arr[0], min_product = arr[0];


    for (int i=1; i < n; i++) {
    max_product = max(max_product, max(max_product*arr[i], min_product*arr[i]));
    min_product = min(min_product, min_product*arr[i]);


    }
    return max_product;
}

int main()
{
    int arr[] = {-6, 4, -5, 8, -10, 0, 8};
    int arr1[] = {4, -8, 0, 8};
    int n = sizeof(arr)/sizeof(arr[0]);
    int n1 = sizeof(arr1)/sizeof(arr1[0]);

    cout<<find_max_product(arr, n)<<endl;
    cout<<find_max_product(arr1, n1)<<endl;

    return 0;
}