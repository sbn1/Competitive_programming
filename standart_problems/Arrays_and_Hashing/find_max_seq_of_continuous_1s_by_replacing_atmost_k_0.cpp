#include <iostream>

using namespace std;

//Time :O(N)
//Space: O(1)

void find_max_subarray(int arr[], int n, int k)
{
    int left = 0;
    int left_index=0;
    int count = 0;
    int window = 0;

    for (int right = 0; right < n; right++)
    {
        if (arr[right] == 0) {
            count++;
        }
        while (count > k)
        {
            if (arr[left] == 0){
                count--;
            }
            
            left++;
        }

    
        
        if ((right - left + 1) > window ){
            window = right - left + 1;
            left_index = left;
        }

    }
    

    if (window == 0){
        return;
    }
    

    cout<<"Max subarray: "<<window<<endl;
    cout<<"("<<left_index<<", "<<left_index + window - 1<<")"<<endl;

    
}

int main()
{
    int arr[] = {1,1,0,1,1,0,1,1,1,1,0,0};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = 2;
    find_max_subarray(arr, n, k);

    return 0;
}