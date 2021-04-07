#include <bits/stdc++.h>
using namespace std;


string solution(int a, int b) {
    string weekend[7]={ "THU","FRI", "SAT","SUN", "MON", "TUE", "WED"};
    int day[13]={0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    string answer = "";

    int sum=0;

    for(int i=0;i<a;i++){
        sum+=day[i];
    }

    sum+=b;

    return weekend[sum%7];
}
