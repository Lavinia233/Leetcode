class Solution:
    # brute Force
    # Time Complexity:O(n^2)
    # Space Complexity:O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    result.append(i)
                    result.append(j)
                    return result
