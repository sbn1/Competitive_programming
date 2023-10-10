#include <iostream>
using namespace std;

int max(int x, int y) { return (x > y)?x:y; }

//Time: O(N)
//Space: O(1)

int find_max_profit(int arr[], int n)
{
    int local_min = 0, max_profit = 0, total_profit = 0;

    int i=0;

    while (i + 1 < n)
    {
        local_min = arr[i];
        max_profit = 0;
        while ((arr[i+1] > arr[i]) &&( i + 1 < n))
        {   
            max_profit = max(max_profit, arr[i+1] - local_min);
            i++;
        }

        total_profit += max_profit;

        i++;
    }

    return total_profit;

}

int find_max_profit_alt(int arr[], int n){

    int local_min_pozition = 0, profit=0;
    
    for (int i=1; i < n; i++)
    {
        if (arr[i] < arr[i-1]) {
            local_min_pozition = i;
        }

        if ((arr[i] >= arr[i-1]) &&((i + 1 == n) || (arr[i + 1] < arr[i]))){
            
            profit += arr[i] - arr[local_min_pozition];
        }
    }

    return profit;
}

int main()
{
    int arr[] = {1, 5, 2, 3, 7, 6, 4, 5};

    //int arr[] = {10, 8, 6, 5, 4, 2};

    int n = sizeof(arr)/sizeof(arr[0]);

    cout<< "Max Profit: "<< find_max_profit(arr, n)<<endl;
    cout<< "Max Profit: "<< find_max_profit_alt(arr, n)<<endl;
    return 0;
}