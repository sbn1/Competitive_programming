#include <iostream>

//Time: O(N * Log (max elemnts in a))
//Space: O(1)

int find_min_nr_of_moves(int arr[], int n)
{
    int min_nr_moves = 0;

    while(true)
    {
         int nr_of_zeros = 0;

        //convert odd elements into even
        for (int i=0; i < n; i++)
        {
            if (arr[i] % 2 == 1){
                arr[i] = arr[i] - 1;
                min_nr_moves++;
            }
            if (arr[i] == 0){

                nr_of_zeros++;
            }

        }

        //while loop breaker

        if (nr_of_zeros == n)
        {
            break;
        }

        //Division of all even elements
        for (int i = 0; i < n; i++)
        {
            arr[i] = arr[i]/2;
        }
        min_nr_moves++;
    }

    return min_nr_moves;
}

int main()
{
    int arr[] = {8, 9, 8};
    int n = sizeof(arr)/sizeof(arr[0]);

    std::cout<<find_min_nr_of_moves(arr, n)<<"\n"<<"\n";

    return 0;
}