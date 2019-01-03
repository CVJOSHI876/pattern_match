# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:42:22 2019

@author: kj494
"""

class Solution(object):
    def isMatch(self, s, p):
        pattern_len = len(p)
        input_len = len(s)
        truth_table = [[False for j in range(input_len+1)] for i in range(pattern_len+1)]
        
        for i in range(pattern_len+1):
            for j in range(input_len+1):
                if(i==0 and j==0):
                    truth_table[i][j]=True
                elif(j==0):
                    truth_table[i][j]= (pattern_len>0 and i>0 and p[i-1]=='*' and (truth_table[i-1][j]));
                elif(i==0):
                    truth_table[i][j]= (pattern_len>0 and i>0 and p[i-1]=='*' and (truth_table[i][j-1]));
                else:
                    truth_table[i][j]=((truth_table[i-1][j-1] and (pattern_len>0 and input_len>0 and p[i-1]==s[j-1]))or
                              (pattern_len>0 and p[i-1]=='*' and (truth_table[i-1][j] or truth_table[i][j-1])) or 
                              (pattern_len>0 and p[i-1]=='?' and truth_table[i-1][j-1]))
        return truth_table[pattern_len][input_len]


# Test 
myobj = Solution()
s ='artificial'
p = 'a*if*a?'
output = myobj.isMatch(s, p) 