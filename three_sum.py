from typing import List

class Solution:

    # single pass O(N)
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums_map:
                return [nums_map[diff], index]
            nums_map[value] = index
        return

    # single pass O(N)
    def twoSumSorted(self, nums: List[int], target: int) -> List[List[int]]:
        left = 0
        right =  len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1
            if curr_sum == target:
                return [left, right]
                
                
    # O(N log N)
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]: # if index gt 0 and value is in list
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                three_sum = value + nums[left] + nums[right]
            
                if three_sum > target:
                    right -= 1
                if three_sum < target:
                    left += 1
                if three_sum == target:
                    sums.append([value, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right: # if left is equal to left - 1 and left is still lt right
                        left += 1
        return sums

                


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []

        def kSum(k: int, start: int, target: int) -> None:
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]: # if current num is equal to last
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base case two sum
            left = start
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                if curr_sum > target:
                    right -= 1
                if curr_sum == target:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        kSum(4, 0, target)
        return res



