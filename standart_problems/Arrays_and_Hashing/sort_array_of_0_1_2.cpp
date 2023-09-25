#include <iostream>

using namespace std;

void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

}

void sort_array(int arr[], int end)
{
    int pivot=1, start=0, mid=0;

    while (mid <= end)
    {

        if (arr[mid] < pivot)
        {
            swap(arr, start, mid);

            mid++;
            start++;

        }
        else if (arr[mid] > pivot)
        {
            swap(arr, mid, end);
            
            end--;
        }
        else { mid++;}
    }

  

}

int main()
{

int arr[] = {1, 0, 0, 2, 1, 2, 0};
int n = sizeof(arr)/sizeof(arr[0]);

sort_array(arr, n-1);

for(int i=0; i < n; i++){
    cout<<arr[i]<<"  ";
}
cout<<endl;
return 0;

}