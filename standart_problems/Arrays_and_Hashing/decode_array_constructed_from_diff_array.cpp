#include <iostream>
#include <cmath>

using namespace std;

void find_original_array(int arr[], int n)
{

    if(n == 0 || n == 2){
        return;
    }

    //solve a simple quadratic equation
    int m = (sqrt(1 + 8*n) + 1)/2;

    //Create auxiliar array
    int AUX[m];

    if (m ==1 || n == 1){
        AUX[0] = arr[0];
    }
    else if ( m == 2){
        AUX[0] = arr[0] - arr[1];
    }
    else{ 
        AUX[0] = ( arr[0] + arr[1] - arr[m-1]) / 2;
    }


    for (int i =1; i < m; i++){
        AUX[i] = arr[i-1] - AUX[0];

    }

    for (int i=0; i < m; i++)
    {
        cout<<AUX[i]<<" ";
    }
    cout<<endl;

}
int main()
{
    int arr[] = {3, 4, 5, 6, 7};

    //int arr[] = {3, 4, 5, 6, 5, 6, 7, 7, 8, 9};
    int n = sizeof(arr)/sizeof(arr[0]);
    find_original_array(arr, n);

    return 0;
}