#include <bits/stdc++.h>


using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int weight=brown+yellow;

    for(int i=brown;i>2;i--){
        for(int j=brown;j>2;j--){
            if (yellow==(i-2)*(j-2)){
                if(weight==i*j){
                    answer.push_back(i);
                    answer.push_back(j);
                    return answer;
                }
            }
        }
    }

}
