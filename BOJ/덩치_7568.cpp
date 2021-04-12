#include <bits/stdc++.h>
using namespace std;


int main() {

    int n,x,y;
    cin >> n;

    int cnt = 1;
    pair<int,int> people[50];

    for(int i=0 ; i<n ; i++){
        cin >> people[i].first >> people[i].second;
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
            if(people[i].first < people[j].first && people[i].second < people[j].second)
                cnt++;
        cout << cnt << ' ';
        cnt = 1;
    }

    return 0;
}
