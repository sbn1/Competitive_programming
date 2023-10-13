#include <iostream>
#include <unordered_map>
#include <utility>

using namespace std;

//Time : O(N^3)
//Space: O(N^2)
void find_4_elements_given_a_sum(int arr[], int n, int target)
{
    for (int i=1; i < n-3; i++)
    {
        unordered_map <int, pair<int, int>> map;

        for (int left = 0; left < i; left++)
        {
            map[target - arr[i] - arr[left]] = make_pair(left, i);
        }

        for (int j = i+1; j < n-1; j++)
        {
            for (int k = j+1; k < n; k++)
            {
                if (map.find(arr[j] + arr[k]) != map.end()){
                    cout<<"["<<arr[map[arr[j] + arr[k]].first]<<", "<<arr[map[arr[j] + arr[k]].second]<<", "<<arr[j]<<", "<<arr[k]<<"]"<<endl;
                } 
            }
        }
    }

}

int main()
{
    int arr[] = {2, 7, 4, 0, 9, 5, 1, 3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 20;

    find_4_elements_given_a_sum(arr, n, target);

    return 0;
}