#include <iostream>
#include <algorithm>

using namespace std;

//Time: O(M + N)
//Space: O(1)

void merge_arrays(int x[], int y[], int n, int m)
{
    int j = 0, k = 0;

    for (int i = 0; i < n; i++)
    {
        if (x[i] != 0){
            while(y[j] < x[i] && j < m){
                swap(x[k], y[j]);
                k++; 
                j++;
            }
            swap(x[k], x[i]);
            k++;

        }
    }

    while (j < m)
    {
        x[k] = y[j];
        j++;
        k++;
    }

    for (int i = 0; i < n; i++){
        cout<<x[i]<<"  ";

    }
    cout<<endl;


}

int main()
{
    //int x[] = {0, 2, 0, 3, 0, 5, 6, 0, 0};
    //int y[] = {1, 8, 9, 10, 15};

    // int x[] = {0,0,3, 0, 6, 7};
    // int y[] = {1,2,4};

    int x[] = {0, 2, 0, 3, 0, 5, 6, 0, 0};
    int y[] = {1, 8, 9, 10, 15};

    int n = sizeof(x)/sizeof(x[0]);
    int m = sizeof(y)/sizeof(y[0]);

    merge_arrays(x, y, n, m);

    return 0;
}