#include <iostream>

using namespace std;

int max(int x, int y) { return (x > y)? x:y;}

//Time : O(N)
//Space: O(N)
int find_max_bitonic_seq(int arr[], int n)
{
    int inc_arr[n], dec_arr[n];
    int longest_bitonic_subarr = 1;

    for (int i=0; i < n; i++){
        inc_arr[i]= 1;
        dec_arr[i] = 1;
    }
    
    for (int i=1; i < n; i++){

        if (arr[i] > arr[i-1]){
            inc_arr[i] = inc_arr[i-1] + 1;

        }
    }

    for (int i=n-2; i>=0; i--) {
        if (arr[i] > arr[i+1]){
            dec_arr[i] = dec_arr[i+1]+1;
        }
    }

    for (int i=0; i < n; i++) {
        longest_bitonic_subarr = max(longest_bitonic_subarr, inc_arr[i] + dec_arr[i] - 1);
    }


    //for (int i=0; i < n; i++){ cout<<dec_arr[i]<<" "; }

    //cout<<endl;

    return longest_bitonic_subarr;

}
//Time :O(N)
//Space: O(1)
int optimal_max_bitonic_subarr(int arr[], int n)
{
    int max_bitonic=1, ending=0;
    
    int i = 0;

    while ( i+1 < n){

        int bitonic_length = 1;

        while((i+1 < n) && (arr[i+1] > arr[i])){
            bitonic_length++;
            i++;
        }

        while ((i+1 < n) && (arr[i+1] < arr[i])){
            bitonic_length++;
            i++;
        }


        while((i+1<n) && (arr[i+1] == arr[i])){
            i++;
        }

        if ( bitonic_length > max_bitonic) {
            max_bitonic = bitonic_length;
            ending = i;

        }


    }


    for (int i=ending - max_bitonic+1; i <= ending; i++){ cout<<arr[i]<<" ";}
    cout<<endl;

    return max_bitonic;

}   

int main ()
{
    int arr[] = {3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout<< find_max_bitonic_seq(arr, n)<<endl;

    cout<<optimal_max_bitonic_subarr(arr, n)<<endl;

    return 0;
}