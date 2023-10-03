#include <iostream>

using namespace std;


void print_array(int arr[], int n)
{
    for(int i=0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void inplace_array(int X[],  int Y[], int n, int m)
{   
    int tmp;

    for (int i=0; i < n; i++){

        if (X[i] > Y[0]){ 

            tmp = X[i];
            X[i] = Y[0];
            Y[0] = tmp;

            int first = Y[0];
            int j = 1;
            while ((j < m )&&(Y[j] < first))
            {   Y[j-1] = Y[j];
                
                j++;
            }
            Y[j-1] = first;

        }

    }

}



int main()
{
    int X[] = {1, 4, 7, 8, 10};
    int Y[] = {2, 3, 9};

    int n = sizeof(X)/sizeof(X[0]);
    int m = sizeof(Y)/sizeof(Y[0]);

    inplace_array(X, Y, n, m);

    print_array(X, n);
    print_array(Y, m);

    return 0;
}