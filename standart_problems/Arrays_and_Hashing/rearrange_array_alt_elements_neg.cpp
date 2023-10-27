#include <iostream>

//group the negative and the positive elements
int rearrange_array_find_nr_neg(int arr[], int n)
{
    int j = 0; //stores nr of negative elements, how many times it swaps

    for (int i=0; i < n; i++)
    {
        if (arr[i] < 0)
        {
            int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                
                j++;
        }
    }

    return j;
}

void alter_the_array(int arr[], int n)
{
    int neg_elements = rearrange_array_find_nr_neg(arr, n);

    for (int i = 0; (neg_elements < n && i < neg_elements); neg_elements++, i+=2)
    {
        int tmp = arr[i];
            arr[i] = arr[neg_elements];
            arr[neg_elements] = tmp;
        
    }
}

int main()
{
    //int arr[] = {9, -3, 5, -2, -8, -6, 1, 3};
    int arr[] = {9, -3, 5, -2, 8, 6, 1, 3};
    int n = sizeof(arr)/sizeof(arr[0]);

    alter_the_array(arr, n);

    for (int i = 0; i < n; i++)
    {
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";

    return 0;
}