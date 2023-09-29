#include <iostream>
#include <unordered_set>

using namespace std;

//Time: O(N)
// Space: O(N)

void find_pairs(int arr[], int n, int k)
{
    unordered_set<int> set;
    unordered_multiset<int, int> multi_set;

    for (int i=0; i < n; i++){
        if (set.find(arr[i] - k)!= set.end()){
        cout<<"("<<arr[i]<<","<<arr[i] - k<<")"<<endl;
        }

        if (set.find(arr[i] + k) != set.end()){
            cout<<"("<<arr[i]<<", "<<arr[i] - k<<")"<<endl;
        }

        set.insert(arr[i]);
    }

}
int main()
{
    int arr[] = {1, 5, 2, 2, 2, 5, 5, 4};
    int k = 3;
    int n = sizeof(arr)/sizeof(arr[0]);

    find_pairs(arr, n, k);

    return 0;
}