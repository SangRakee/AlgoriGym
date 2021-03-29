#include <bits/stdc++.h>


using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> result;
    int num;
    vector<vector<int>> student={{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};

    for(int i=0;i<student.size();i++){
        int cnt=0;
        for(int j=0;j<answers.size();j++){
            if(student[i][j%student[i].size()]==answers[j]){
                cnt++;
            }
        }        answer.push_back(cnt);

    }

    num=*max_element(answer.begin(),answer.end());

    for(int i=0;i<answer.size();i++){
        if(num==answer[i]){
            result.push_back(i+1);
        }
    }


    return result;
}
