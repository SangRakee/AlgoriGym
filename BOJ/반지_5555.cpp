#include <bits/stdc++.h>

using namespace std;

int main(void) {
	string str;
	string input;
	cin >> str;
	int size = str.size();
	int partCnt = 0;
	int partTmp = 0;
	int idx = 0;

	int n;
	cin >> n;

	int cnt = 0;
	for (int i = 0; i < n; i++) {
		cin >> input;
		partCnt = 0;
		idx = 0;
		for (int j = 0; j < size; j++) {
			if (input.find(str[j], idx) == -1) break;
			else {
				partCnt++;
				idx = input.find(str[j], idx) + 1;
				if (idx >= input.size()) idx = 0;
				if (partCnt == size) cnt++;
			}
		}

	}

	cout << cnt;
}
