class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums = sorted(nums)

        if not nums:
            return 0

        current_count = 1
        longest = 0

        for i in range(len(nums)-1):
            if (nums[i+1] == nums[i] + 1):
                current_count += 1
            elif (nums[i+1] == nums[i]):
                continue
            else:
                longest = max(longest, current_count)
                current_count = 1

        longest = max(longest, current_count)
        return longest