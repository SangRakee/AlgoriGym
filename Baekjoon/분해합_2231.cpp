#include <bits/stdc++.h>
using namespace std;

void numfind(int N)
{
    int tmp = N;
    int start,i,sum,tmp2 = 0;
    for(i = -1; tmp; i++)
        tmp /= 10;
    start = round(pow(10,i)) - 9*i;
    tmp = start;
    while(1)
    {
        sum = tmp;
        tmp2 = tmp;
        while(tmp2)
        {
            sum += tmp2 % 10;
            tmp2 /= 10;
        }
        if(sum == N)
        {
            cout << tmp;
            return;
        }
        if(tmp == N)
        {
            cout << '0';
            return;
        }
        tmp++;
    }
}
int main() {
    int N;
    cin >> N;
    numfind(N);
}
