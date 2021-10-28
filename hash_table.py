import array as arr

"""
Simple TranspositionTable

if you want to store, call
store(the point in board, value)

if you want to lookup, 
lookup(the point in board)
return the value or -9 (which means its empty)
"""


class TranspositionTable(object):
    table = arr.array('i', [])

    def __init__(self):
        for i in range(70):
            self.table.insert(i, -9)

    def store(self, point, score):
        self.table.insert(point, score)

    def lookup(self, point):
        return self.table[point]
