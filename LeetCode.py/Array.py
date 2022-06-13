# from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
                

#     print(twoSum([2,3,4,5,9], 9))

# numbers = list(range(20))
# print(numbers[::-2])

class Solution:

    def countDown(self, n):
        if n == 0 :
            return
        
        return self.countDown(n - 1)

print(Solution().countDown(5))

