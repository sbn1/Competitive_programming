#include <iostream>
#include <unordered_map>

using namespace std;

void print_array_from_i_to_j(int arr[], int start, int end, int n)
{
    for (int i=start; i<= end; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

//Time: O(N)
//Space: O(N)
void find_distinct_subarrays(int arr[], int n)
{
    unordered_map <int, bool> map;

    int left = 0, right = 0;

    while (right < n)
    {

        while( (right < n) && (! map[arr[right]]) )
        {
            map[arr[right]] = true;

            right++;
        }

        print_array_from_i_to_j(arr, left, right-1, n);

        while ((right < n) && (map[arr[right]]))
        {
            map[arr[left]] = false;

            left++;
        }
    }
}

int main()
{
    int arr[] = {5, 2, 3, 5, 4, 3};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_distinct_subarrays(arr, n);

    return 0;
}