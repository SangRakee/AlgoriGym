#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());

    int i=0;
    int j=people.size()-1;

    while(i<=j){
        answer++;
        if(people[i]+people[j])<=limit{
            i++;
        }
        j--;
    }

    return answer;
}
