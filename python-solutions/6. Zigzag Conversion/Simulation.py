
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge case if number of rows is 1
        if numRows == 1: 
            return s
        
        # create buckets list where each bucket holds characters in its respective row
        buckets = [[] for _ in range(numRows)]
        # elevation and down maintain boudaries and order
        elevation = 0
        down = True
        
        # iterate string
        for i in range(len(s)):
            # add character
            buckets[elevation].append(s[i])
            # update down and elevator if need be
            if down and elevation == numRows - 1: down = False
            elif not down and elevation == 0: down = True
                
            elevation += (1 if down else -1)
        # convert buckets to string and return it
        return "".join(["".join(bucket) for bucket in buckets])
