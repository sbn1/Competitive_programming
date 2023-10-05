#include <iostream>
using namespace std;

void swap(int arr[], int i, int j){
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

}

void alter_array(int arr[], int n)
{
    for (int i=1; i < n; i=i+2){
        if (arr[i] < arr[i-1]){
            swap(arr, i, i-1);
        }
        if ((i+1 < n) && (arr[i+1] > arr[i])){
            swap(arr, i, i+1);

        }
    }
} 
int main()
{
    //int arr[] = {1, 2, 3, 4, 5, 6, 7};

    int arr[] = {9, 6, 8, 3, 7};
    int n = sizeof(arr)/sizeof(arr[0]);

    alter_array(arr, n);

    for (int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}