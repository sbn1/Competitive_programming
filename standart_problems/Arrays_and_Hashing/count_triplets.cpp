#include <iostream>
using namespace std;

//Time: O(N^2)
//Space: O(1)
int find_triplets(int arr[], int n)
{
    int count = 0;
    for (int j=1; j < n-1; j++){

        int left = 0; 
        for (int i = 0; i < j; i++){
            if (arr[i] > arr[j]){
                left ++;
            }
        }

        int right = 0;
        for (int k = j+1; k < n; k++){
            if (arr[k] < arr[j]){
                right++;
            }
        }
        count += (left * right);
    }

    return count;
}
int main()
{
    //int arr[] = {1, 9, 6, 4, 5};
    int arr[]={9, 4, 3, 5, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<find_triplets(arr, n)<<endl;

    return 0;
}