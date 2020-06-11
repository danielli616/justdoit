class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return
    
        list_re = [None] * numRows
        
        for i in range(numRows):
            li = [None]* (i+1)
            li[0] = 1
            
            for j in range(1, i):
                li[j] = list_re[i-1][j-1] + list_re[i-1][j]
                
            li[i] = 1        
            list_re[i] = li
            
        return list_re
            