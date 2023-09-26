# include<iostream>

using namespace std;

// Time: O(N)
//Space: O(1)
void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}


void sort_binary(int arr[], int n)
{
    int k=0;

    for (int i=0; i < n; i++)
    {
        if (arr[i] == 0)
        {
            swap(arr, k, i);
            k++;
        }
    }
}

int main()
{
    int arr[] = {0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0};

    int n = sizeof(arr)/sizeof(arr[0]);

    sort_binary(arr, n);

    for (int i=0; i < n; i++){
        cout<<arr[i]<<" ";
    }
    
    cout<<endl;

    return 0;
}