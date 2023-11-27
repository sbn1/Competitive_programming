#include <iostream>
#include <limits.h>
#include <vector>

//Time: O(N^2)
//Space: O(1)
void replace_with_least_greater(int arr[], int n)
{
    for (int i=0; i < n; i++)
    {
        int replace_value =-1;
        int diff = INT_MAX;

        for (int j=i+1; j < n;j++)
        {
            if ((arr[j] > arr[i]) && (arr[j] - arr[i] < diff)){
                replace_value = arr[j];
                diff = arr[j] - arr[i];

            }

        }

        arr[i] = replace_value;

    }

}
int main()
{
    int arr[] = {10, 100, 93, 32, 35, 65, 80, 90, 94, 6};
    int n = sizeof(arr)/sizeof(arr[0]);
    replace_with_least_greater(arr, n);

    for (int i:arr){
        std::cout<<i<<" ";
    }
    std::cout<<"\n";

    return 0;
}
