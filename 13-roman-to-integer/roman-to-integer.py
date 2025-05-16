class Solution(object):
    def romanToInt(self, s):
        R_To_I = {
            'I' : 1, 'V': 5, 'X' : 10 , 'L' : 50, 'C': 100, 'D': 500, 'M' : 1000
        }

        res = 0

        for i in range (len(s)):
            if i + 1 < len(s) and R_To_I[s[i]] < R_To_I[s[i + 1]] : 
                res -=  R_To_I[s[i]]
            else :
                res +=  R_To_I[s[i]]
        return res