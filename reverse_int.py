"""
This block of code is credited to Eddy Ruhana (Software Engineer)
From www.leetcode.com 
Algorithms Problem
Level: Easy
Title: Reverse Integer

Notes:
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

Example: 
- Input: 123
- Output: 321
"""

class Solution:
    def reverse(self, x: int) -> int:
        int_to_transform = x
        
        if(x < 0):
            int_to_transform = x * (-1)
            
        x_to_string = str(int_to_transform)
        
        a_list = []
        
        str_index = len(x_to_string) - 1
        
        while(str_index >= 0):
            a_list.append(x_to_string[str_index])
            str_index -= 1
            
        reverse_str = ''.join(a_list)
        reverse_int = int(reverse_str)
        
        if(x < 0):
            reverse_int = reverse_int * (-1)
            
        if(reverse_int < (-2**31) or reverse_int > ((2**31) - 1)):
            print(0)
            return 0
        else:
            print(reverse_int)
            return reverse_int