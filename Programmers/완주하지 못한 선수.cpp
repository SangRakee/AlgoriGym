#include <bits/stdc++.h>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    map<string, int> mp;
    for(int i=0 ; i<participant.size() ; i++){
        string s = participant[i];
        mp[s]++;
    }

    for(int i=0 ; i<completion.size() ; i++){
        string s = completion[i];
        mp[s]--;
    }

    for(auto &it : mp) if(it.second == 1) { answer = it.first; break; }

    return answer;
}
