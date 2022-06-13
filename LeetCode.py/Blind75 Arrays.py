# BLIND 75
# QUESTION 1-10  ARRAYS
from typing import List
nums = [2,5,8,14,22,21]
target = 22

class Solution:
    def twoSum (self,nums: List[int],target: int) -> List[int]:
        """
        : type nums: List[int]
        : type target: int
        : rtype: List[int]
        """
        preMap = {} # we are mapping vlaue to index
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i] #returns index of the difference and i
            preMap[n] = i # if the solution doesn't exist then it stores index of n as i, and continues to loop
        return
    

print (Solution().twoSum(nums,target))


#Question 2= Sliding Window (Best time to buy and sell Stock)

prices = [2,3,5,7,8,12,4] 

class Solution:
    def maxProfit(self,prices: List[int]) -> int:
        '''
        :type prices: List[int]
        rtype maxProfit: int
        '''
        # self.prices = prices
        l,r = 0,1 # left is buying and right is selling
        maxProfit = 0
        
        while r < len(prices): # iterates given that the selling prices has not passed the end of prices
            if prices[l] < prices[r]: # to check if profitable
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
    
    
print(Solution().maxProfit(prices))

# Question 3 : Constains Duplicates return Boolean
nums = [1,27,77,88,3,3,3,1]

class Solution:
    def containDuplicate(self, nums: List[int]) -> bool :
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    
print(Solution().containDuplicate(nums))

# Question 4 : Product of arrays of nums except itself.

nums =[1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums)) # giving an initial value to the result array
        
        prefix = 1 # initializing at 1 because if initialized at zero, all resulting numbers after * will be 0
        for i in range(len(nums)):
           result[i] = prefix
           prefix = prefix * nums[i]
        
        postfix = 1 # also initializing the post fix
        for i in range(len(nums) - 1, -1, -1): # to start iterating from the back to the front
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
            
        return result
    
    
print(Solution().productExceptSelf(nums))
        
# Question 5, - Maximum Sub Array
nums = [-2,1] 
     
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentsum = 0
        
        for i in nums:
            if currentsum < 0:
                currentsum = 0
            
            
            currentsum += i
            maxSub = max(maxSub, currentsum)
        
        return maxSub
    
print(Solution().maxSubArray(nums))      
 
# Question 6
  
nums = [-4,-3, -2] 
     
class Solution:
    def productSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1
        
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1,1
                continue
            
            temp = curMax * n
            curMax = max(temp, n*curMin, n)
            curMin = min(temp, n*curMin, n)
            res = max(res, curMax, curMin)
            
        return res
               
print(Solution().productSubArray(nums)) 

       
# Question 7 from Leet code: Find min value in a sorted array using Binary search to achive  O(nlogn)time complexity
nums = [2,3,4,5,6]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[1]
        l,r =0, len(nums)-1 # start at the first index and end a the last index
        # through a sorted array where left < right side
        while l < r:
            if nums[l] < nums[r] :
                res = min(res,nums[l])
                break
            
            # if the array is not sorted
            # do the Binary search
            
            m =(l+r) // 2    # integer division to return the middle index
            res = min(res, nums[m])
            if nums[m] >= nums[l] :
                l = m + 1
            else:
                r = m - 1
                
        return res
    
print(Solution().findMin(nums))

# Question 8 - Search in rortated Sorted Array

nums = [4,5,6,7,0,1,2]
target = 0

class Solution:
    def search(self, nums:List[int], target:int) -> int :
        l,r = 0, len(nums) - 1
   # for binary search we use, l,r, and m.
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            # left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l] :# then search right
                    l = m + 1 # shift the starting point of the left
                else:
                   r = m - 1 # searches the left portion, update right pointer
            
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # move the pointer for the right side
                else:
                    l = m + 1 # move the pointer for the left side
                    
        return -1
    
print(Solution().search(nums, target))
                
                    
nums = [-3,3,4,-3,1,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:                
            res =[]
            nums.sort()
            
            for i,a in enumerate(nums):
                # if i starts after the first value
                if i > 0 and a == nums[i - 1]: # that is if i and a are the same value
                    continue # continue to the next iteration of the loop
                
                l,r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = a + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([a,nums[l],nums[r]])
                        l += 1
                        # if the number on the left and even after shifting is the same number, keeping l<r
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
            return res

print(Solution().threeSum(nums))

#Bonus Leetcode Question: Two Sum2 in a sorted array
nums = [1,3,4,5,7,10,11]
target = 9


class Solution:
    def twoSum2(self, nums:List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l < r :
            curSum = nums[l] + nums[r]
            
            if curSum > target:
                r -=1
            elif curSum < target :
                l += 1
            else:
                return [l +1, r + 1]
        return []

print(Solution().twoSum2(nums,target))

# Bling 75 Questions-- Container with Most water
height =[1,8,6,2,5,4,8,3,7]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l]< height[r]:
                l += 1
            elif height[l]> height[r]:
                r -= 1
            else : # if equal you can decrement r or incerement l
                r -= 1
        
        return res
    
print(Solution().maxArea(height))


