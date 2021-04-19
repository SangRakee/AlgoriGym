#include <bits/stdc++.h>


using namespace std;

int solution(vector<int> nums) {
	set<int> s;
	for (int i = 0; i < nums.size(); i++) {
		s.insert(nums[i]);
	}
	if (s.size() <= nums.size() / 2) {
		return s.size();
	}
	else {
		return nums.size() / 2;
	}
}
