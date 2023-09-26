#include <iostream>
#include <algorithm>

#include <unordered_map>

using namespace std;

// using sort: Time: O(N lngN), Space: O(1)

void find_pairs_with_sorting(int arr[], int n, int target)
{
    int left = 0, right = n-1;

    sort(arr, arr + n);

    while (left < right)
    {
        if (arr[left] + arr[right] == target){
            cout<<arr[left]<<" + "<<arr[right]<<" = "<<target<<endl;

            return;
        }
        (arr[left] + arr[right] < target) ? left++ : right++;

    }
    cout<<"Pair not found";
}

// Using Hashing
// Time: O(N)
// Space: O(N)

void find_pairs_with_hashing(int arr[], int n, int target)
{
    unordered_map <int, int> un_map;

    for (int i=0; i < n; i++)
    {
        if (un_map.find(target - arr[i]) != un_map.end())
        {
            cout<<arr[un_map[target - arr[i]]]<<"  "<<arr[i]<<endl;
            return;
        }
        else {
            un_map[arr[i]] = i;

        }
    }
    cout<<"Pair not found";
}

int main()
{
    int arr[]={8, 7, 2, 5,3, 1};
    int target = 10;
    int n = sizeof(arr)/sizeof(arr[0]);

    find_pairs_with_sorting(arr, n, target);
    find_pairs_with_hashing(arr, n, target);


return 0;
}