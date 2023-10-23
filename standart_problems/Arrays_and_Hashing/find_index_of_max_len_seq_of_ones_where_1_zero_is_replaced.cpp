#include <iostream>


//moving windows: [left..i]
//Time: O(N)
//Space: O(1)
int find_max_len_ones_replace_one_zero(int arr[], int n)
{
    int left = 0, count=0;
    int max_count = 0, max_index = -1, prev_zero_index = -1;

    for (int i=0; i < n; i++)
    {

        if (arr[i] == 0)
        {
            prev_zero_index = i;
            count++;
        }

        if (count ==2)
        {
            while(arr[left])
            {
                left++;
            }

            left++;
            count = 1;
        }

        if ((i - left  + 1) > max_count){
            max_count = i - left + 1;
            max_index = prev_zero_index;
        }
    }

    return max_index;
}

int main()
{
    int arr[] = {0, 0, 1, 0, 1, 1, 1, 0, 1, 1};
    int n = sizeof(arr)/sizeof(arr[0]);

    int index = find_max_len_ones_replace_one_zero(arr, n);
    std::cout<<index<<'\n';

    return 0;

}