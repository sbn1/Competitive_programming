#include <iostream>
using namespace std;

void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void sort_array_1(int arr[], int n)
{
    int left = 0, right = n-1;

    while (left < right){

        if (arr[left] < arr[left - 1]) {
            while (left < right){
                if (arr[right+1] > arr[right]){
                    swap(arr, left - 1, right);
                }
                right --;
            }
        }
        left++;
    }
}

int main()
{
    //int arr[] = {3, 8, 6, 7, 5, 9};
    int arr[] = {3, 5, 6, 9, 8, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
    sort_array_1(arr, n);

    for (int i=0; i < n; i++)
    {
        cout<< arr[i]<<"  ";
    }
    cout<<endl;

    return 0;
}