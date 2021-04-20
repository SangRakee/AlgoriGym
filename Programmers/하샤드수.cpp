#include <bits/stdc++.h>


using namespace std;

bool solution(int x) {
	int t = x;
	int y = 0;
	while (t)
	{
		y += t % 10;
		t /= 10;
	}
	return (x%y == 0) ? true : false;
}
