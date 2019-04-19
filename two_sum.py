"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Solved by Eddy Ruhana
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans1 = -1
        ans2 = -2
        
        that_index = 0
        the_index = 0
        index_limit = len(nums)
        
        enums = enumerate(nums, 0)
        
        for a, b in enums:
            the_index = a + 1
            
            while the_index < index_limit:
                if b + nums[the_index] == target:
                    ans1 = a
                    ans2 = nums[the_index]
                    that_index = the_index
                    
                the_index += 1
                
        return(ans1, that_index)