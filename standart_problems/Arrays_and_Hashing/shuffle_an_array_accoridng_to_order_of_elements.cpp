#include <iostream>

//Time: O(N)
//Space: O(1)
void swap(int arr[], int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
// The idea is to rearange pos[] in increasing order
//this algorithms works as long as all the elements are distinct 
void shuffle_array(int nums[], int pos[], int n)
{
    for (int i=0; i < n; i++)
    {
        while (pos[i] != i){
            swap(nums, pos[i], i);
            swap(pos, pos[i], i);
            
        }
    }

}

int main()
{
    int nums[] = {1, 2, 3, 4, 5};
    int pos[]={3, 2, 4, 1, 0};
    int n = sizeof(nums)/sizeof(nums[0]);
    
    shuffle_array(nums, pos, n);

    for (int i:nums){
        std::cout<<i<<" ";
    }
    std::cout<<"\n";

    return 0;
}