#include <iostream>
#include <unordered_set>

using namespace std;

bool zero_sum_subarray(int arr[], int n)
{
    unordered_set<int> set;

    set.insert(0);

    int sum=0;

    for (int i=0; i < n; i++)
    {
        sum += arr[i];

        if (set.find(sum) != set.end()) { 
            return true;
        }
        else { 
            set.insert(sum);
             }
    }

    return false;

}

int main()
{
    int arr[] = {3, 4, -7, 3, 1, 3, 1, -4, -2, -2};
    int n = sizeof(arr)/sizeof(arr[0]);

    zero_sum_subarray(arr, n) ? cout<<"Zero Subarray exists"<<endl: 
                                cout<<"Zero Subarray does not exist"<<endl;

    return 0;
}