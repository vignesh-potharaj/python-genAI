class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        seperator = ""
        sdigits = seperator.join(map(str, digits))
        udigits = int(sdigits) + 1
        result = list(map(int, str(udigits)))
        
        return result