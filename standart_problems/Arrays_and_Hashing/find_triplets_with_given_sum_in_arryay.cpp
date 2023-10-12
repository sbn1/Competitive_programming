#include <iostream>
#include <unordered_set>
#include <algorithm>

using namespace std;

//Time: O(N)
//Space O(N)

void find_triplets_hash(int arr[], int n, int target)
{
   

    for (int i=1; i < n-1; i++)
    {
        unordered_set <int> set; 

        for (int j = 0; j < i; j++)
        {
            set.insert(target - arr[i] - arr[j]);
        }

        for (int k=i+1; k < n; k++)
        {
            if (set.find(arr[k]) != set.end()){
                cout<<"["<<target - arr[i] - arr[k] <<", " <<arr[i]<<", "<<arr[k]<<"]"<<endl;
            }
        }
    }


}

void find_triplets_sort(int arr[], int n, int target)
{
    sort(arr, arr + n);

    for (int i=1; i < n-1; i++)
    {
        int left = 0, right = n-1;

        while ((left < i)&&(right > i))
        {
            if ((arr[i] + arr[left] + arr[right]) > target){
                right--;
            }

            else if ((arr[i] + arr[left] + arr[right]) < target){
                left++;
            }
            else {
                cout<<"["<<arr[left]<<", "<<arr[i]<<", "<<arr[right]<<"]"<<endl;
                left++;
                right--;
            }
        }

    }
}

int main()
{
    int arr[] = {2, 7, 4, 0, 9, 5, 1, 3};
    int target = 6;
    int n = sizeof(arr)/sizeof(arr[0]);

    find_triplets_hash(arr, n, target);

    cout<<endl;

    find_triplets_sort(arr, n, target);

    return 0;

}