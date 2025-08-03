from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in lookup:
                return[lookup[rest],i]
            lookup[num] = i

solution = Solution()

print(solution.twoSum([3,2,4], 6))