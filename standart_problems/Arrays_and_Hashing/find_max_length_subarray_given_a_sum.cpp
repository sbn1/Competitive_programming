#include <iostream>
#include <unordered_map>
using namespace std;

void find_max_len_subarray(int arr[], int n, int target)
{
    unordered_map<int, int> map;

    int length = 0, suma = 0;
    int ending = -1;

    //case when the array starts with target
    map[0] = -1;

    for (int i=0; i < n; i++)
    {
        suma += arr[i];

        if (map.find(suma) == map.end()){
            map[suma] = i;
        }

        if ((map.find(suma - target) != map.end()) && (length < i - map[suma - target])){
            length = i - map[suma - target];
            ending = i;

        }
    }

    cout<<"Max length:"<<length<<endl;
    cout<<"["<<ending - length + 1<<", "<<ending<<"]"<<endl;


}

int main()
{
    int arr[] = {5, 6, -5, 5, 3, 5, 3, -2, 0};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 8;

    find_max_len_subarray(arr, n, target);

    return 0;

}