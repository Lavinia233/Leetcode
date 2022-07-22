class Solution:
    # Hash Table
    # Time Complexity:0(N)
    # Space Complexity:0(N)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        mapping = {}
        for i in range(0, len(nums)):
            mapping[nums[i]] = i
        for j in range(0, len(nums)):
            diff = target - nums[j]
            if diff in mapping and mapping[diff] != j:
                result.append(j)
                result.append(mapping[diff])
                return result
