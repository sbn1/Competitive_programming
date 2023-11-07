#include <iostream>

void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

}

int partition(int arr[], int start, int end)
{
    int pivot = arr[end];

    int index_position = start;

    for (int i = start; i < end; i++){
        if ( arr[i] <= pivot)
        {
            swap(arr, index_position, i);
            index_position++;
        }
    }

    swap(arr, index_position, end);

    return index_position;

}
void quick_sort(int arr[], int start, int end)
{
    //Base Case
    if (start >= end)
    {
        return;
    }

    int index = partition(arr, start, end);

    quick_sort(arr, start, index - 1);
    quick_sort(arr, index + 1, end);

}

int main()
{
    int arr[] = {4, 6, 1, 7, 9, 2};
    int n = sizeof(arr)/sizeof(arr[0]);

    quick_sort(arr, 0, n-1);

    for (int i=0; i<n; i++)
    {
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";

    return 0;

}

