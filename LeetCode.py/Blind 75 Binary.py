# Question 1 Number of Bits
from typing import List
# n = 1111111111111011111111111111

# class Solution:
#     def hammingWeight(self,n: int) -> int:
#         res = 0
        
#         while n:
#             n = n & (n - 1)
#             res += 1
        
#         return res
    
# print(Solution().hammingWeight(n))

# Question 2 Counting Bits

# n  = 2
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n +1)
#         offset = 1
        
#         for i in range(1,n + 1):
#             if offset * 2 == i:
#                 offset = i
#             dp[i] = 1+ dp[i - offset]
            
#         return dp
    
# print(Solution().countBits(n))

# Question 3 Missing Number
# nums = [3,0,1]

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
        
#         for i in range(len(nums)):
#              res = res + (i - nums[i]) # adding every value from 1- len(nums) but  then subtracting nums[i]
#         return res

# print(Solution().missingNumber(nums))

# Question 4
# n = 00000010100101000001111010011100

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
        
#         for i in range(32):
#            bit = (n >> i) & 1 # to get the ith bit. we shift the n by i, then we and & with 1, to access each bit
#            res = res | (bit << (31 - i)) #we are putting the bit from line 55 and putting it in the 31st spot, reversing it
#         return res
    