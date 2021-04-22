#include <bits/stdc++.h>


using namespace std;

int solution(int n) {
    int answer = 0;

    string str;

    while(true){
        str += to_string(n%3);

        if(n<3)
            break;

        n = n/3;

    }

    for(int i=0; i<str.size(); i++){
        answer += pow(3,str.size()-i-1) * (str[i]-'0');
    }

    return answer;
}
