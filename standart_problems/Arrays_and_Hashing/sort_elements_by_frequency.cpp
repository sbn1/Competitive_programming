#include<iostream>
#include <algorithm>
#include <unordered_map>
#include <tuple>
#include <vector>
#include <utility>

//
bool waterfall_sort(const std::tuple<int, int, int> &a, 
                    const std::tuple<int, int, int>  &b)
                    {
                        if (std::get<1>(a) != std::get<1>(b))
                        {
                            return std::get<1>(a) > std::get<1>(b);
                        }
                        else
                        {
                            return std::get<2>(a) < std::get<2>(b);
                        }
                    }

void sort_by_frequency(int arr[], int n)
{
    std::unordered_map<int, std::pair<int, int>> map;

    for (int i=0; i < n; i++)
    {
        if(map.find(arr[i]) != map.end())
        {
            map[arr[i]].first++;
        }
        else {
            map[arr[i]] = std::make_pair(1, i);
        }
    }

    std::vector<std::tuple<int, int, int>> tuples;

    for (auto it: map)
    {
        std::pair<int, int> p = it.second;
        tuples.push_back(std::make_tuple(it.first, p.first, p.second));
        
    }

    sort(tuples.begin(), tuples.end(), waterfall_sort);

    int a, b, c, k=0;

    for (auto tuple:tuples){
        std::tie(a, b, c) = tuple;
        for (int i = 0; i < b; i++)
        {
            arr[k] = a;
            k++;
        }
    }

}

int main()
{
    int arr[] = {3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8};
    int n = sizeof(arr)/sizeof(arr[0]);

    sort_by_frequency(arr, n);

    for (int i = 0; i < n; i++)
    {
        std::cout<<arr[i]<<" ";

    }

    std::cout<<"\n";

    return 0; 
}