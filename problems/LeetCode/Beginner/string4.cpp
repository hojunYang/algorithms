/*
2026.01.19
title: Valid Anagram
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/
*/
#include "string"
using namespace std;

// 0ms. 73%
class Solution {
    public:
        bool isAnagram(string s, string t) {
            int countOriginalString[26] = {0};
            int countCheckString[26] = {0};

            for(auto word : s) {
                countOriginalString[word - 'a'] += 1;
            }
            for(auto word: t) {
                countCheckString[word - 'a'] += 1;
            }

            for(int i = 0; i < 26; i++) {
                if(countCheckString[i] != countOriginalString[i])
                    return false;
            }
            return true;
        }
    };