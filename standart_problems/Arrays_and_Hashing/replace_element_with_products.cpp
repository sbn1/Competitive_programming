#include <iostream> 
using namespace std;

//Time : O(N)
//Space: O(N)

void replace_n_space(int arr[], int n)
{
    int aux[n];
    int forward = 1, backward = 1;
    aux[0] = 1;
    for (int i=1; i < n; i++){
        aux[i] = forward;
        forward *= arr[i];

    }
    for (int i=n-1; i>=0; i-- ){
        aux[i] = aux[i]* backward;
        backward *= arr[i];

    }
    for (int i=0; i < n; i++){
        cout<<aux[i]<<"  ";

    }
    cout<<endl;

}

//Time: O(N)
//Space: O(1)
int replace_recursvie(int arr[], int i, int n, int prod_from_left){
    if (i == n){
     return 1;
        }

    int current = arr[i];

    int prod_from_right = replace_recursvie(arr, i + 1, n, prod_from_left * arr[i]);

    arr[i] = prod_from_left * prod_from_right;

    return current * prod_from_right;

}

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    //replace_n_space(arr, n);

    replace_recursvie(arr, 0, n, 1);

    for (int i=0; i < n; i++) {
        cout<<arr[i]<<" ";

    }
    cout<<endl;


    return 0;
}