#include <iostream>

using namespace std;
//Time: O(N^2)
//Space: O(1)

int max(int x, int y){ return (x > y)? x:y;}
int min(int x, int y){return (y < y)? x:y;}

int find_longest_consequtive_subarray(int arr[], int n){

    int longest_sub = 0;
    int max_value = 0, min_value = 0;

    for (int i = 0; i < n-1; i++)
    {
        max_value = arr[i];
        min_value = arr[i];
        
        for (int j=i+1; j < n; j++){
            
            max_value = max(arr[j], max_value);
            min_value = min(arr[j], min_value);

            if (max_value - min_value == j - i){
                longest_sub = max(longest_sub, max_value - min_value + 1);
            }
        }

    }
    return longest_sub;
}

int main()
{
    int arr[] = {2, 0, 2, 1, 4, 3, 1, 0};

    //int arr[] = {0, 1, 3, 2, 5, 4, 7, 8};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout<<find_longest_consequtive_subarray(arr, n)<<endl;

    return 0;
}