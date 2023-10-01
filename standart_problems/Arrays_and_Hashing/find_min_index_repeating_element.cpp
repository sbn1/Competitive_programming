#include <iostream>
#include <unordered_set>

using namespace std;

//Time: O(N)
//Space: (N)
int find_min_index(int arr[], int n)
{
    unordered_set<int> set;
    int min_index = n;

    for (int i=n-1; i >= 0; i--)
    {
        if (set.find(arr[i]) != set.end()){
            min_index = i;
        }
        else {
            set.insert(arr[i]);
        }
    }

    return (min_index == n)? -1: min_index;

}
int main()
{
    int arr[] = {5, 6, 3, 4, 3, 6, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    int index = find_min_index(arr, n);

    if (index !=-1){
        cout<<index<<endl;
    }
    else { cout<<"Invalid input";}

    return 0;
}