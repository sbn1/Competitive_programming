#include <iostream>
#include <set>
#include <vector>
#include <experimental/iterator>
using namespace std;

void find_combination(vector<int> const &arr, int i, int k, set<vector<int>> &sol, vector<int> &tmp )
{
    if (arr.size() == 0 || k > arr.size()) {
        return;
    }

    if (k == 0) {
        sol.insert(tmp);
        return;
    }

    for (int j = i; j < arr.size(); j++) {
        tmp.push_back(arr[j]);
        find_combination(arr, j + 1, k-1, sol, tmp);
        tmp.pop_back();

    }

}
template <typename T> 
void print_vector(vector<T> const &input)
{
    cout<<"[ ";
    copy(begin(input), end(input), experimental::make_ostream_joiner(cout,", "));
    cout<<"]"<<endl;
}

int main()
{
    vector<int> arr = {1, 2,3};
    int k = 2;
    //sol will store all unique solution
    set<vector<int>> sol;

    //temporary vector that will add k elements
    vector<int> tmp;

    find_combination(arr, 0, k, sol, tmp);

    for (auto const &vect:sol) {
        print_vector(vect);
    }

    return 0;

}
