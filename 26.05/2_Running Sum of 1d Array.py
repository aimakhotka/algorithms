# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []
        j = 0
        for i in nums:
            if j == 0:
                runSum.append(i)
                j += 1
            else:
                num1 = runSum[j-1]
                runSum.append(num1+i)
                j += 1
        return runSum