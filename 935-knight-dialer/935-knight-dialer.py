def possibleCells(num):
    dic = {
        0:[4,6],
        1:[6,8],
        2:[7,9],
        3:[4,8],
        4:[3,9,0],
        5:[],
        6:[1,7,0],
        7:[2,6],
        8:[3,1],
        9:[4,2]
    }
    
    return dic[num]

def getCount(curr_num, n, cash):
    if len(curr_num) == n:
        return 1
    
    cells = possibleCells(int(curr_num[-1]))
    count = 0
    for next_cell in cells:
        if (next_cell, n-len(curr_num)+1) not in cash:
            cash[(next_cell, n-len(curr_num)+1)] = getCount(curr_num+str(next_cell), n, cash) % (10**9 + 7)
            
        count += cash[(next_cell, n-len(curr_num)+1)] 
    
    return count

class Solution:
    def knightDialer(self, n: int) -> int:
        numbers_count = 0
        cash = {}
        for i in range(10):
            numbers_count += getCount(str(i), n, cash)

        return numbers_count % (10**9 + 7)