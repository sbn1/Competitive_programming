#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

pair<int, int> find_pairs(int arr[], int n)
{
    if (n <=1){
        return make_pair(-1, -1);
    }

    sort(arr, arr+n, greater<int>());
    
    int first = 0;
    for (int i=0; i < n; i=i+2){
        first = first*10 + arr[i];
    }
    
    int second = 0;

    for (int i=1; i < n; i=i+2){
        second = second *10 + arr[i];
    }

    return make_pair(first, second);
}

int main()
{
    int arr[] = {4, 6, 2, 7, 9, 8};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    pair<int, int> max_numbers = find_pairs(arr, n);

    cout<< max_numbers.first<< "  "<<max_numbers.second<<endl;

    return 0;

}