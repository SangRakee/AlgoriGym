#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> result;

    for(int x=0;x<commands.size();x++){
        int i=commands[x][0]-1;
        int j=commands[x][1]-1;
        int k=commands[x][2]-1;

        for(int y=0;y<array.size();y++){
            if(y>=i && y<=j){
                answer.push_back(array[y]);
            }
        }
        sort(answer.begin(),answer.end());
        result.push_back(answer[k]);
        answer.clear();

    }

    return result;
}
