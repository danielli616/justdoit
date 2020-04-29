class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
        int len_text1 = text1.length();
        int len_text2 = text2.length();
        
        int matrix[len_text1+1][len_text2+1];     
        memset(matrix,0,sizeof(matrix));
        
        for(int i = 1; i <= text1.length(); i++)
        {
            for(int j = 1; j <= text2.length(); j++)
            {
                if (text1.at(i-1) == text2.at(j-1))
                {
                     matrix[i][j] = matrix[i-1][j-1] + 1;
                }
                else
                {
                    matrix[i][j] = std::max(matrix[i-1][j],matrix[i][j-1]); 
                }                               
            }
        }
        
        return matrix[len_text1][len_text2];
    }
};