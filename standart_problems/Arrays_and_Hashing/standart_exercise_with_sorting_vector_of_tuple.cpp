#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>

//standart exercise from geekforgeek

bool sort_desc(const std::tuple<int, int, int> & a, 
                const std::tuple<int, int, int> & b)
                {
                    return std::get<0>(a) > std::get<0>(b);

                }
int main()
{
    std::vector<std::tuple<int, int, int>> v;

    v.push_back(std::make_tuple(10, 20, 30));
    v.push_back(std::make_tuple(15, 5, 25));
    v.push_back(std::make_tuple(3, 2, 1));

    for (int i=0; i < v.size(); i++)
    {
        std::cout<<std::get<0>(v[i])<<"  "
        <<std::get<1>(v[i])<<" "
        << std::get<2>(v[i])<<" \n";

    }
    sort(v.begin(), v.end(), sort_desc);

    std::cout<<" After Sorting \n";

    for (int i=0; i < v.size(); i++)
    {
        std::cout<<std::get<0>(v[i])<<" "
                 <<std::get<1>(v[i])<<" "
                 <<std::get<2>(v[i])<<" \n";
    }


    return 0;

}
