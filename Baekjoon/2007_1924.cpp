#include <bits/stdc++.h>
using namespace std;

int main() {
    int month[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    string week[7]={"SUN","MON","TUE","WED","THU", "FRI", "SAT"};


    int x,y;
    cin >> x >> y;
    int day=0;

    for(int i=0;i<x;i++){
        day+=month[i];
    }
    day+=y;
    cout<<week[day%7];
}
