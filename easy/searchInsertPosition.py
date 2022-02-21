'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
-----------
Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:
-----------
Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:
-----------
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''


class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    lowerBoundaryIndex = 0
    upperBoundaryIndex = len(nums) - 1
    
    if nums[0] > target or nums[0] == target:
      return 0
    elif nums[len(nums) - 1] < target:
      return len(nums)
    
    while lowerBoundaryIndex < upperBoundaryIndex:
      midpointIndex = (lowerBoundaryIndex + upperBoundaryIndex) // 2
      
      if nums[midpointIndex] == target:
        return midpointIndex
      
      elif upperBoundaryIndex - lowerBoundaryIndex == 1 and lowerBoundaryIndex == midpointIndex:
        return midpointIndex + 1
      
      elif nums[midpointIndex] < target:
        lowerBoundaryIndex = midpointIndex
        
      elif nums[midpointIndex] > target:
        upperBoundaryIndex = midpointIndex
    
    