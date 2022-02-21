'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
----------
Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
----------
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


class Solution:
    
  def longestCommonPrefix(self, strs: list[str]) -> str:
    common_prefix = strs[0]
      
    for index in range(0, len(strs)):
      if len(common_prefix) != 0:
        while len(common_prefix) > 0:
          if strs[index].startswith(common_prefix):
            break
          else:
            common_prefix = common_prefix[:-1]
      else:
        break
    
    return common_prefix

