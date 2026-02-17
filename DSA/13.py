class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RI = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s) -1):
            if RI[s[i]] < RI[s[i + 1]]:
                result = result - RI[s[i]]
            else:
                result = result + RI[s[i]]
        return result + RI[s[-1]]