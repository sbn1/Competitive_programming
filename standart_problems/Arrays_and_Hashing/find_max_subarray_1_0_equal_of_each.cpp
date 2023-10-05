#include <iostream>
#include <unordered_map>
using namespace std;

//Time: O(N)
// Space: O(N)

void find_max_subarray(int arr[], int n)
{
    int suma = 0;
    int ending = -1, max_len = 0;
    unordered_map<int, int> map;

    // base case 
    map[0] = -1;

    for (int i=0; i < n; i++)
    {
        suma += (arr[i] == 0) ? -1: 1;
        cout<<suma;
        if (map.find(suma) != map.end()) {

            if (max_len < i - map[suma]) {
                max_len = i - map[suma];
                ending = i;

                }

        }
        else {
            map[suma] = i;
        }
    }
    cout<<" ["<<ending - max_len + 1<<" , "<<ending<<"]"<<endl;

}

int main()
{
    int arr[] = {0, 0, 1, 0, 1, 0, 0};
    int n = sizeof(arr)/sizeof(arr[0]);

    find_max_subarray(arr, n);

    return 0;
}