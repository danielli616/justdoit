class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
    
        list_re = []
        
        for i in range(numRows):
            li = [1]* (i+1)
            
            for j in range(1, i):
                li[j] = list_re[i-1][j-1] + list_re[i-1][j]
                      
            list_re.append(li)
            
        return list_re
            