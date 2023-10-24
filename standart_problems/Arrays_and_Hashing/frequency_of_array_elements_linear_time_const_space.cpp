#include <iostream>

//Time: O(N)
//Space: O(1)
void find_frequency(int arr[], int n)
{

    for (int i=0; i < n; i++)
    {
        arr[arr[i] % n] += n;
    }

    for (int i=0; i< n; i++)
    {
        if (arr[i]/n )
        {
            std::cout<<"Freq of "<<i<<" is "<<arr[i]/n<<"\n";
        }
    }

    //Transform back ot the original Matrix
    for (int i=0; i < n; i++)
    {
        arr[i] = arr[i] % n;
    
    }
}

int main()
{
    int arr[] = {2, 3, 3, 2, 1};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_frequency(arr, n);

    return 0;

}