#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int max(int x, int y) { return (x > y)? x:y;}

int find_min_platform(vector<double> arrivals, vector<double> departures)
{
    int count = 0;

    int min_platform = 0;

    int i=0, j=0;

    sort(arrivals.begin(), arrivals.end());

    sort(departures.begin(), departures.end());

    while(i < arrivals.size()){
        
        if (arrivals[i] < departures[j]){

            count++;

            min_platform = max(min_platform, count);

            i++;

        }
        else 
        {
            count--;
            j++;
        }
    }


    return min_platform;
}

int main()
{
    vector<double> arrivals = {2.00, 2.10, 3.00, 3.20, 3.50, 5.00 };
    vector <double> departures = {2.30, 3.40, 3.20, 4.30, 4.00, 5.20};

    cout<<" Min platforms needes:"<<find_min_platform(arrivals, departures)<<endl; 

    return 0;
}