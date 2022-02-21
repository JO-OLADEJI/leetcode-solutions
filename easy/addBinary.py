'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

 
Example 1:
----------
Input: a = "11", b = "1"
Output: "100"


Example 2:
----------
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:
------------
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''


class Solution:

  def getCharacter(self, index: int, string: str) -> list:
    try:
      value = string[index]
      return [value, int(value)]
    except:
      return [None, 0]

  def addBinary(self, a: str, b: str) -> str:
    result = ''
    overflow = 0
    position = -1
    
    done = False
    while not done:
      num1 = self.getCharacter(position, a)
      num2 = self.getCharacter(position, b)

      if num1[0] == None and num2[0] == None and overflow == 0:
        done = True
      
      else:
        currentSum = num1[1] + num2[1] + overflow
        actualDigit = currentSum % 2
        overflow = currentSum // 2
        result = str(actualDigit) + result
      
      position -= 1
    
    return result