#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

//using object as comp

struct my_comparisor
{
    bool operator()(const int &a, const int &b){ 
        std::string value_1 = std::to_string(a) + std::to_string(b);
        std::string value_2  =std::to_string(b) + std::to_string(a);

        return value_1 > value_2;

    }
} my_comp_struct;
// using function as comp
bool sorting_instruction(const int &a, const int &b)
{
    std::string value_1 = std::to_string(a) + std::to_string(b);
    std::string value_2  =std::to_string(b) + std::to_string(a);

    return value_1 > value_2;

}


int main()
{
    std::vector<int> v = {10, 68, 75, 7, 21, 12};
    
    //std::sort(v.begin(), v.end(), sorting_instruction);

    std::sort(v.begin(), v.end(), my_comp_struct);

    
    std::string number;

    for (auto i:v){
        number += std::to_string(i);
    }

    std::cout<<number<< "\n";

    return 0;

}
