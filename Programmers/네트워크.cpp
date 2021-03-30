#include <bits/stdc++.h>

using namespace std;

int visited[201];

void dfs(vector<vector<int>> computers,int v){
    visited[v]=1;
    for(int i=0;i<computers.size();i++){
        if(visited[i]==0 and computers[v][i]==1){
            dfs(computers,i);
        }
    }

}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;

    for(int i=0; i<n;i++){
        if(visited[i]==0){
            dfs(computers,i);
            answer++;
        }
    }

    return answer;
}
