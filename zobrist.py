import random

class zobrist:
    def __init__(self,boardsize):
        self.range_hash = boardsize*boardsize
        for i in range (64):
            for j in range (boardsize):
                self.table[i][j] = random.getrandbits(64)
    
    def hash(self,board):
        code = self.table[0][board[0]]
        for i in range(1,self.range_hash):
            code = code ** self.table[i][board[i]]
        return code


