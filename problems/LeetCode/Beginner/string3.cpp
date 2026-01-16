/*
2026.01.16
title: First Unique Character in a String
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/
*/
#include <string>
using namespace std;

// first try
// 19ms 25%. 87%.
// O(n^2). O(1)
// class Solution {
//     public:
//         int firstUniqChar(string s) {
//             int index = -1;
//             for(int i = 0; i < s.size(); i ++) {
//                 index = i;
//                 for(int j = 0; j < s.size(); j++) {
//                     if(s[i] == s[j] && i != j) {
//                         index = -1;
//                         break;
//                     }
//                 }
//                 if (index != -1)
//                     return index;
//             }
//             return index;
//         }
//     };


//second try
//2ms. 53%
// class Solution {
//     public:
//         int firstUniqChar(string s) {
//             int array[26] = {0};
//             for (auto x : s) {
//                 array[x - 'a'] += 1;
//             }
//             for (int i = 0; i < s.size(); i++) {
//                 if (array[s[i] - 'a'] == 1)
//                     return i;
//             }
//             return -1;
//         }
//     };

// third try made by LLM
// O(n + 26) = O(n), but faster for long strings
// 인덱스 힌트를 작성해서 second의 2n보다 더 빠르게 확인할 수 있음
class Solution {
public:
    int firstUniqChar(string s) {
        int count[26] = {0};
        int firstIdx[26];
        fill(firstIdx, firstIdx + 26, -1);
        
        for (int i = 0; i < s.size(); i++) {
            int c = s[i] - 'a';
            count[c]++;
            if (firstIdx[c] == -1) firstIdx[c] = i;
        }
        
        int result = s.size();
        for (int i = 0; i < 26; i++) {
            if (count[i] == 1 && firstIdx[i] < result)
                result = firstIdx[i];
        }
        return result == s.size() ? -1 : result;
    }
};