# Time Complexity: O(1)- technically constant time
# Space Complexity: O(1) - technically constant time

class Solution:
    def intToRoman(self, num: int) -> str:
        
        i2r = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
              4 : "IV", 9 : "IX", 40 :"XL", 90:"XC", 400 : "CD", 900 : "CM"}
        
        parts = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        string = []
        for i in range(len(parts)):
            while num >= parts[i]:
                num -=  parts[i]
                string.append(i2r[parts[i]])
        return "".join(string)
