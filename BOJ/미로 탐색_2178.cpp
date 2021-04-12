#include <bits/stdc++.h>
using namespace std;


//»óÇÏÁÂ¿ì
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

int graph[101][101];

int n,m;

void bfs(int column, int row){
    queue<pair<int,int>> q;
    pair<int,int> cur;
    q.push({column,row});

    while(!q.empty()){
        cur = q.front();
        q.pop();
        int x = cur.first;
        int y = cur.second;
        for(int i=0 ; i<4 ; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>=0 && nx<n && ny>=0 && ny<m){
                if(graph[nx][ny] == 1){
                    q.push({nx,ny});
                    graph[nx][ny]=graph[x][y]+1;
                }
            }
        }
    }
}

int main() {


    cin >> n >> m;

    for(int i=0 ; i<n ; i++){
        for(int j=0 ; j<m ; j++){
            cin >> graph[i][j];
        }
    }

    bfs(0,0);

    cout<<graph[n-1][m-1]<<'\n';

    return 0;
}
