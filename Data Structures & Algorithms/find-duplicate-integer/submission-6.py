class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]== nums[j]:
                    return nums[i]
        
        