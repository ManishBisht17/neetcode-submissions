class Solution:
    def findDuplicate(self, nums):
        counts = {}

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    count += 1

            counts[nums[i]] = count

        return max(counts, key=counts.get)