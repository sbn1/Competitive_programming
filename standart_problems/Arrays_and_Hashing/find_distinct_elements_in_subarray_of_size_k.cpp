#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

//Time: O(N * K)
//Space: O(K)
void find_distinct_elements(vector<int> const & arr, int k)
{
    for (int i = 0; i < arr.size() - k + 1; i++)
    {
        unordered_set<int> set(arr.begin() + i, arr.begin() + i + k);

        cout<<"Subarray: ["<<i<<","<<i + k-1<<"] distinct elements: "<<set.size()<<endl;
    }
}

//Time: O(N)
//Space: O(N)
void find_distinct_moving_window(vector<int> const & arr, int k){
    
    unordered_map<int, int> map;

    int distinct_elements = 0;

    for (int i=0; i < arr.size(); i++)
    {
        if ( i >= k){

            map[arr[i - k]] --; 

            if (map[arr[i - k]] == 0){
                distinct_elements --;
            }
        }

        map[arr[i]] ++; 

        if (map[arr[i]] == 1){
            distinct_elements ++;
        }

        if (i >= k - 1){
            cout<<"Subarray: ["<<i - k +1<<","<<i<<"], distinct elements: "<<distinct_elements<<endl;
        }
    }


}

int main()
{
    vector<int> arr = {2, 1, 2, 3, 2, 1, 4, 5};
    int k = 5;

    find_distinct_elements(arr, k);
    find_distinct_moving_window(arr, k);

    return 0;
}