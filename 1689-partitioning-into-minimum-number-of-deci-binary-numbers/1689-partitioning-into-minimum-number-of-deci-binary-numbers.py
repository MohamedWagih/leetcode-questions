'''
for example: '32'
we need at least three ones to sum up to '3'
and two ones to sum up the '2'

1 1
1 1
1 0
---_
3 2

for example '135'
we need 5 ones to sum up the '5'
and three ones to sum up the '3'
and just one to sum up the '1'

1 1 1
0 1 1
0 1 1
0 0 1
0 0 1
------
1 3 5

so the minimum number of positive deci-binary numbers needed
will always be the max digit in n.


'''
class Solution:
    def minPartitions(self, n: str) -> int:
        # we just need to return the max digit in n
        return max(n)