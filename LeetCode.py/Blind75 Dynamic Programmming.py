from typing import List
# Question from Dynamic programming
# n = 5

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1,1 # bottom up strategy
        
#         for i in range (n - 1):
#             temp = one
#             one = one + two
#             two = temp
            
#         return one
# print(Solution().climbStairs(n))

# Question Coin change

# coins= [1,2,5]
# amount = 11

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount + 1] * (amount + 1) # going from 0 to max value in amount
#         dp[0] = 0 # we know to get the solution for 0 is 0
        
#         for a in range(1, amount + 1): # starting for Bottom up
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a-c])
#         return dp[amount] if dp[amount] != amount + 1 else -1

# Question Long Increasin Subsequence

# nums = [10,9,2,5,3,7,101,18]

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         LIS = [1] * len(nums)
        
#         for i in range(len(nums)-1, -1,-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] > nums[j]:
#                     LIS[i] = max(LIS[i], 1+LIS[j])
                    
#         return max(LIS)
# print(Solution().lengthOfLIS(nums))  # this is O(n^2)
 
 
 # Dynamic Programming Longest Common Subsequence
# text1 , text2= "abcde","ace" 

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2)+ 1) ] for i in range(len(text1)+1)]
#         # creates and extra row and column of zero asides the len of text 1 and2, hence + 1
        
#         for i in range(len(text1)-1,-1,-1): # reverse iterate through the rows
#             for j in range(len(text2)-1, -1,-1): # revers iterater through columns
#                 # if the letters in i and j don't match
#                 if text1[i] == text2[j]:
#                     # move diagonally
#                     # to create a diagonal
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                 # if they do not match, we have to look left or down
#                 else:
#                     dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
#                 # we know the answer will be in the first position of the 2 grid matrix
#         return dp[0][0]
    

 # Question WordBreak.
# s = "leetcode"
# wordDict= {"leet", "code"}

# def wordBreak(s,wordDict):
#     wordDict = set(wordDict)
#     isBreakable = False
#     index= [len(s)]
    
#     for i in range(len(s)-1, -1, -1): # reverse iterate through len(s)
#         isBreakable = False
#         for j in index:
#             if (s[i: j] in wordDict):
#                 isBreakable = True
#                 index += [i]
#                 break   
#     return isBreakable

# print(wordBreak(s,wordDict))


# Question Combinaton Sum

# nums = [1,2,3]
# target = 4

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [0] * (target+1)
#         dp[0] = 1
        
#         for i in range(1,len(dp)):
#             for j in nums:
#                 if i-j >= 0:
#                     dp[i]= dp[i] + dp[i-j]
                    
#         return dp[-1]
        
       
# print(Solution().combinationSum4(nums,target))

# Question House robbery
# nums= [2,7,9,3,1]


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0, 0
        
#         # [rob1, rob2, n, n+1]
#         for n in nums:
#             temp = max(rob1 + n, rob2)
#             rob1 = rob2
#             rob2 = temp
        
#         return rob2
    
# print(Solution().rob(nums))


# 
# 


nums = [2,3,1,1,4]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)- 1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i # recall we are working backwards
                
        return True if goal == 0 else False # returns true if the goal was managed to be shifted ti the first index[0]
    
print(Solution().canJump(nums))