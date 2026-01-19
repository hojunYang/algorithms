/*
2026.01.19
title: Valid Palindrome
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/
*/
#include <algorithm>
#include <string>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        string filtered = "";
        for_each(s.begin(), s.end(), [&](char c){
            if (isalnum(c)) filtered += tolower(c);
        });
        s = filtered;
        if(s == "") {
            return true;
        }
        for(int i = 0; i < s.size() / 2; i ++) {
            if(s[i] != s[s.size() - 1 - i]) {
                return false;
            }
        }
        return true;
        }
};
/*
python 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]
*/