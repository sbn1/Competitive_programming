#include <iostream>
#include <vector>
#include <string>

using namespace std;

int order(int x)
{
    int suma = 0;

    while (x)
    {
        suma += x%10;
        x /= 10;

    }
    return suma;
}

int main()
{
    int n = 1234567;
    cout<< order(n)<<endl;
    

}
