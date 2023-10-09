#include <iostream>

using namespace std;

int max(int x, int y) { return (x > y)? x:y; }

int find_max_sum_path(int X[], int Y[], int n, int m)
{   
    int sum_of_x = 0, sum_of_y = 0;
    int max_sum = 0;

    //indexes of the arrays
    int i = 0, j = 0;

    // combined traversal 
    while ((i < n) && (j < m))
    {
        //check repeating elements in X[]

        while ((i+1 < n) && (X[i] == X[i + 1]))
        {
            sum_of_x += X[i];
            i++;
        }
        //check repeating elements in Y[]

        while( (j+1 < m) && (Y[j] == Y[j + 1]))
        {
            sum_of_y += Y[j];
            j++;
        }

        if( X[i] > Y[j]){
            sum_of_y += Y[j];
            j++;
        }
        else if (Y[j] > X[i]){

            sum_of_x += X[i];
            i++;
        }
        //The case when X[i] == Y[j] and the swithc can take place
        else 
        {
            max_sum += max(sum_of_x, sum_of_y) + X[i];
            i++;
            j++;
            
            //resetting the sum_of_x and sum_of_y
            sum_of_x = 0;
            sum_of_y = 0;

        }
    }
    //checking the instances when one array is fully traversed and the other one not

    //Case: when X[] is not fully traversed
    while(i < n){
        sum_of_x += X[i];
        i++;
    }
    //Case: when Y[] is not fully traversed
    while(j < m){
        sum_of_y += Y[j];
        j++;
    }

    max_sum += max(sum_of_x, sum_of_y);

    return max_sum;
}

int main()
{
    int X[] = {3, 6, 7, 8, 10, 12, 15, 18, 100};
    int Y[] = {1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50};

    int n = sizeof(X)/sizeof(X[0]);
    int m = sizeof(Y)/sizeof(Y[0]);

    cout<<find_max_sum_path(X, Y, n, m)<<endl;

    return 0;
}