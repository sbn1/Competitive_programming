#include <iostream>
#include <vector>
#include <utility>
#include <unordered_set>

using namespace std;

//Time: O(N)
//Space: O(N)

void find_symetric_pairs(vector<pair<int, int>> & arr)
{
    unordered_set<string> set;

    for (int i=0; i<arr.size(); i++)
    {
        string p = "{" + to_string(arr[i].first) + "," + to_string(arr[i].second) + "}";
        
        set.insert(p);

        string swaped_pair = "{" + to_string(arr[i].second) + "," + to_string(arr[i].first) + "}";

        if (set.find(swaped_pair) != set.end()) {
            cout<<p<< " | "<<swaped_pair<<endl;
        }
    }
}

int main()
{
    vector<pair<int, int>> arr = {{3, 4}, {1,2}, {5,2}, {7, 10},{4,3}, {2,5} };
    find_symetric_pairs(arr);

    return 0;
}