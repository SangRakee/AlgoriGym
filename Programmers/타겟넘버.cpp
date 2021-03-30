#include <bits/stdc++.h>

using namespace std;

int answer=0;

void dfs(vector<int> numbers, int target, int v, int count){
    if(count==numbers.size()){
        if(v==target){
            answer+=1;
        }
        return;
    }
    dfs(numbers,target,v+numbers[count],count+1);
    dfs(numbers,target,v-numbers[count],count+1);
}

int solution(vector<int> numbers, int target) {

    dfs(numbers,target,numbers[0],1);
    dfs(numbers,target,-numbers[0],1);

    return answer;
}
