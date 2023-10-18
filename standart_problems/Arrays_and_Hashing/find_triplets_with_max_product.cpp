#include <iostream>
#include <climits>
#include <algorithm>


//Time: O(N log N)
//Space: O(1)
void find_triplets_max_product(int arr[], int n)
{
    if (n < 3){
        return;
    }

    std::sort(arr, arr + n);

    if (arr[0] * arr[1]*arr[n-1] > arr[n-1]*arr[n-2]*arr[n-3])
    {
        std::cout<<arr[0]<<" "<<arr[1]<<" "<<arr[n-1]<<std::endl;
    }
    else {
        std::cout<<arr[n-1]<<" "<<arr[n-2]<<" "<<arr[n-3]<<std::endl;
    }
    
}

void find_tripleats_max_product_optimal(int arr[], int n)
{
    int max_1 = -1, max_2 = -1, max_3 = -1;

    for (int i=1; i < n; i++)
    {
        if (arr[i] > arr[max_1])
        {
            max_3 = max_2;
            max_2 = max_1;
            max_1 = i;
        }

        else if ( max_2== -1 || arr[i] > arr[max_2])
        {
            max_3 = max_2;
            max_2 = i;
        }

        else if (max_3 == -1 || arr[i] > arr[max_3])
        {
            max_3 = i;
        }
    }

    int min_1 = 0, min_2 = -1;
    

    for (int i =1; i < n; i++)
    {
        if (arr[i] < arr[min_1])
        {
            min_2 = min_1;
            min_1 = i;
        }

        else if (min_2 == -1 || arr[i] < arr[min_2]){
            min_2 = i;
        }
    }

    std::cout<<arr[min_1]<<"  "<<arr[min_2]<<std::endl;
    // if (arr[max_1]*arr[max_2]*arr[max_3] > arr[min_1]*arr[min_2]*arr[max_1]){

    //     std::cout<<arr[max_1]<<" "<<arr[max_2]<<" "<<arr[max_3]<<std::endl;
    // }
    // else {
    //     std::cout<<arr[min_1]<<" "<<arr[min_2]<<" "<<arr[max_1]<<std::endl;
    // }

    

}

int main()
{
    int arr[] = {-4, 1, -8, 9, 6};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_triplets_max_product(arr, n);
    find_tripleats_max_product_optimal(arr, n);

    return 0;
}