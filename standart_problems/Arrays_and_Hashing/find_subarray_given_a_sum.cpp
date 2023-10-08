#include <iostream>
#include <unordered_map>
using namespace std;

//Movind Window
//Time: O(N)
//Space: O(1)
void find_subarray_given_sum(int arr[], int n, int target)
{
    int start = 0, end=0;
    int moving_sum = 0;

    for (start = 0; start < n; start++)
    {
        while( moving_sum < target && end < n)
        {
            moving_sum += arr[end];
            end++;
        }

        if (moving_sum == target){
            cout<<" ("<<start<<" , "<<end - 1<<")"<<endl;
        }
        moving_sum -= arr[start];
    }

}
//Hashing Method
//Time :O(N)
//Space: O(N)

void find_subarray_hashing(int arr[], int n, int target)
{
    unordered_map<int, int> map;
    int sum_so_far = 0;

    for (int i=0; i < n; i++)
    {
        sum_so_far += arr[i];

        if (map.find(sum_so_far - target) != map.end()){
            cout<<"( "<<map[sum_so_far -target]+1 <<" , "<<i<<" )"<<endl;
        }

        //the positions needs to be updated even if that element already exists
        map[sum_so_far] = i;

    }

}

int main()
{
    int arr[] = {2, 6, 0, 9, 7, 3, 1, 4, 1, 10};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 15;

    cout<<"Moving Window"<<endl;
    find_subarray_given_sum(arr, n, target);
    cout<<"Hashing"<<endl;
    find_subarray_hashing(arr, n, target);

    return 0;
}