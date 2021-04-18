#include <bits/stdc++.h>


using namespace std;

int N, M, X, Y, K;
vector<pair<int, int>> toy[101];
queue<int> num;
int indegree[101];
int cnt[101][101];

int main() {

    ios::sync_with_stdio(false);

    cin >> N >> M;

    for (int i = 1; i <= M; i++) {
        cin >> X >> Y >> K;
        toy[X].push_back({ Y,K });
        indegree[Y]++;
    }

    for (int i = 1; i <= N; i++) {
        if (indegree[i] == 0) {
            num.push(i);
            cnt[i][i] = 1;
        }
    }


    while (!num.empty()) {
        int i = num.front();
        num.pop();
        for (pair<int,int> temp : toy[i]) {
            for (int t = 1; t <= N; t++) {
                cnt[t][temp.first] += temp.second * cnt[t][i];
            }
            indegree[temp.first]--;
            if (indegree[temp.first] == 0) num.push(temp.first);
        }
    }

    for (int i = 1; i <= N; i++) {
        if (toy[i].size() == 0) {
            cout << i << " " << cnt[N][i] << "\n";
        }
    }

    return 0;
}


ÃâÃ³: https://gyutts.tistory.com/80 [Developer Q.bot]


