#include <iostream>
using namespace std;

void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

}
void move_zeros(int arr[], int n)
{

    int k = n-1;
    
    for (int i=n-1; i >=0; i--)
    {
        if (arr[i] == 0){
            swap(arr, k, i);
            k --;

        }
    }
}

int main()
{
    int arr[] = {6, 0, 8, 2, 3, 0, 4, 0, 1};
    int n = sizeof(arr)/sizeof(arr[0]);

    move_zeros(arr, n);

    for (int i=0; i<n; i++){
        cout<<arr[i]<< "  ";

    }
    cout<<endl;
}