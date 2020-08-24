class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mark = [[False] *len(board[0]) for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0, mark):
                     return True
        return False
    
    def dfs(self, board, i, j , word, m, mark):
        
        if (m == len(word)):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or mark[i][j]:
            return False
        
        mark[i][j] = True
        
        if (board[i][j] == word[m]):
            # right
            if self.dfs(board, i, j + 1, word, m + 1, mark):
                return True
            # left
            if self.dfs(board, i, j - 1, word, m + 1, mark):
                return True
            # up
            if self.dfs(board, i + 1, j, word, m + 1, mark):
                return True
            # down
            if self.dfs(board, i - 1, j, word, m + 1, mark):
                return True
        
        mark[i][j] = False
        return False