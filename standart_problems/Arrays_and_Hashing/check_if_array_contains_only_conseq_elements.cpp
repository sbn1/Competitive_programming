#include <iostream>
#include <unordered_set>

//Time: O(N)
//Space: O(N)

bool check_if_array_constains_only_consequtives(int arr[], int n)
{
    //Base Case:
    if (n < 2 ){
        return true;
    }
    int min_element = arr[0], max_element = arr[0];

    for (int i = 1; i < n; i++)
    {
        if (arr[i] > max_element)
        {
            max_element = arr[i];
        }
        if (arr[i] < min_element)
        {
            min_element = arr[i];
        }
    }
    if (max_element - min_element != n-1){
        return false;
    }

    //max-min == n-1 may fail, ex: [1, 2, 2, 4]-> 4 - 1 == 4 - 1 True, 
    //however it is not consequtive

    std::unordered_set <int> set;

    for (int i=0; i < n; i++)
    {
        if (set.find(arr[i]) != set.end()){
            return false;
        }

        set.insert(arr[i]);
    }

    return true;
}

int main()
{
    int arr[] = {-1, 5, 4, 2, 0, 3, 1};
    //int arr[] = {1, 2, 2, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    check_if_array_constains_only_consequtives(arr, n)? std::cout<<"Array contains only consequtives"<<std::endl:
                                                        std::cout<<"Array does not contain only consequtives"<<std::endl;

    return 0;
}