#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;
//Time: O(N)
//Space: O(N)

bool find_duplicates(int arr[], int n, int k){
    unordered_map<int, int> hash_table;

    for (int i=0; i < n; i++) {
        if (hash_table.find(arr[i]) != hash_table.end()){
            if (i - hash_table[arr[i]] <= k){
                return true;
            }
        }
        
        hash_table[arr[i]] = i;
        

    }
return false;
}

//Moving window using unorered set
//Time: O(N)
//Space: O(k)
bool find_duplicates_set(int arr[], int n, int k)
{
    unordered_set<int> set;

    for (int i=0; i < n; i++){
        if (set.find(arr[i]) != set.end()){
            return true;
    }
    set.insert(arr[i]);


    if (i >=k) { 
        set.erase(arr[i-k]);
    }
    }

    return false; 
}

int main()
{
    int arr[] = {5, 6, 8, 2, 4, 6, 9};
    int k = 4;
    int n = sizeof(arr)/sizeof(arr[0]);

    cout<<find_duplicates(arr, n, k)<<endl;
    cout<<find_duplicates_set(arr, n, k)<<endl;

    return 0;
}