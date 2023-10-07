#include <iostream>
#include <utility>

using namespace std;

int max(int x, int y){ return (x > y)?x:y;}

int find_pairs(int arr[], int n){

    int max_difference = 0;

    int min_element = arr[0];


    for (int i = 1; i < n; i++) 
    {
        if (arr[i] < min_element){
            min_element = arr[i];
        }

        else {
            max_difference = max(max_difference, arr[i] - min_element); 
        }
    }arr[i] - min_element


return max_difference;


}


int main()
{
    int arr[] = {2, 7, 9, 5, 1, 3, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<find_pairs(arr, n) <<endl;

    return 0;

}