/*
2026.01.15
title: Reverse Integer
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/
*/
#include <iostream>
using namespace std;

// first try
// 0ms. 97%
class Solution {
public:
    int reverse(int x) {
        int result = 0;
        while(x != 0) {
            if (INT_MAX / 10 < result || INT_MIN / 10 > result) {
                return 0;
            }
            result = result * 10 + x % 10;
            x /= 10;
        }
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.reverse(1534236461) << endl;
    return 0;
}

/*
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = sign * int(str(abs(x))[::-1])
        return result if -2**31 <= result <= 2**31 - 1 else 0
*/
