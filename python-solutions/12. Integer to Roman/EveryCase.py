# Time Complexity: O(1)- technically constant time
# Space Complexity: O(1) - technically constant time

class Solution:
    def intToRoman(self, num: int) -> str:
        
        i2r = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
              4 : "IV", 9 : "IX", 40 :"XL", 90:"XC", 400 : "CD", 900 : "CM"}
                                
        string = []
        while num != 0:
            while num >= 1000:
                string.append(i2r[1000])
                num -= 1000
            if num >= 900:
                string.append(i2r[900])
                num -= 900             
            while num >= 500:   
                string.append(i2r[500])
                num -= 500
            if num >= 400:
                string.append(i2r[400])
                num -= 400
            while num >= 100:   
                string.append(i2r[100])
                num -= 100
            if num >= 90:
                string.append(i2r[90])
                num -= 90
            while num >= 50:
                string.append(i2r[50])
                num -= 50
            if num >= 40:
                string.append(i2r[40])
                num -= 40
            while num >= 10:
                string.append(i2r[10])
                num -= 10
            if num >= 9:
                string.append(i2r[9])
                num -= 9
            while num >= 5:
                string.append(i2r[5])
                num -= 5
            if num >= 4:
                string.append(i2r[4])
                num -= 4
            while num >= 1:
                string.append(i2r[1])
                num -= 1
        return "".join(string)
