#include <bits/stdc++.h>
using namespace std;


int load[100001];
int city[100001];


int main(){

    int n=0;
    int money=0;

	for (int i = 1; i <= n - 1; i++)
		cin >> load[i];

	for (int i = 1; i <= n; i++)
		cin >> city[i];

    int dic=0;
    int mincity=city[0];

    for (int i=0; i<n-1; i++){
        if(mincity>=city[i+1]){
            dic+=load[i];
            money+=dic*mincity;
            mincity=city[i+1];
            dic=0;
        }else{
            dic+=load[i];
        }
    }


    cout<<money;

}
