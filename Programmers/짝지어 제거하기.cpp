#include <bits/stdc++.h>

using namespace std;

stack<char> st;
int solution(string s)
{
    int answer = 0;
    for(int i=0; i<s.size(); i++){
        if(st.size() > 0 && st.top() == s[i]) st.pop();
        else st.push(s[i]);
    }
    answer = !st.size();

    return answer;
}
