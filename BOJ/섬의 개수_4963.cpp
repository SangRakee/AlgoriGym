#include <bits/stdc++.h>

using namespace std;

int dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

int graph[201][201], visited[201][201];

int w, h;

void bfs(int x, int y){
    queue<pair<int,int>> q;
    pair<int,int> cur;
    q.push({x,y});

    while(!q.empty()){
        cur = q.front();
        q.pop();
        int c = cur.first;
        int r = cur.second;
        for(int i=0 ; i<8 ; i++){
            int nx = c + dx[i];
            int ny = r + dy[i];
            if(nx>=0 && nx<h && ny>=0 && ny<w){
                if(visited[nx][ny] == 0 && graph[nx][ny] == 1){
                    q.push({nx,ny});
                    visited[nx][ny] = 1;
                }
            }
        }
    }
}

int main(){



    cin >> w >> h;

    for(int i=0 ; i<h ; i++){
        for(int j=0 ; j<w ; j++){
            cin >> graph[i][j];
        }
    }

    int cnt = 0;
    for(int i=0 ; i<h ; i++){
        for(int j=0 ; j<w ; j++){
            if(graph[i][j] == 1 && visited[i][j] == 0){
                bfs(i,j);
                cnt += 1;
            }
        }
    }
    cout << cnt << '\n';

    return 0;
}
