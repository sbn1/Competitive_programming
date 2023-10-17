#include <iostream>
#include <utility>
#include <math.h>

using namespace std;

//Time: O(N)
//Space: O(1)

pair<int, int> find_pair(int A[],int B[],  int n,int m, int target)
{
    //The position will track the last pair that is clossest to the target
    int position_a = 0, position_b = m-1;

    for (int i = 0, j=n-1; (i < n)&&(j >=0);)
    {
        if ( abs(A[i] + B[j] - target) < abs(A[position_a] - B[position_b]- target)){
            position_a = i;
            position_b = j;
        }

        if (A[i] +B[j] < target){
            i++;
        }
        else if ( A[i] + B[j] > target){
            j--;
        }
        else  {
            i++;
            j--;
        }
    }
    return make_pair(A[position_a], B[position_b]);

}

int main()
{
    int A[] = {1, 8, 10, 12};
    int B[] = {2, 4, 9, 15};
    int target = 11;

    int n = sizeof(A)/sizeof(A[0]);
    int m = sizeof(B)/sizeof(B[0]);

    //pair<int, int> p = find_pair(A, B, n, m, target);
    //cout<<"("<<p.first<<","<<p.second<<")"<<endl;

    cout<<"["<<find_pair(A, B, n, m, target).first<<","<<find_pair(A, B, n, m, target).second<<"]"<<endl;


    return 0;
}
























