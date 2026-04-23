class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums)- k +1):
            maxi = nums[i]
            for j in range(i,i+k):
                maxi =max(maxi,nums[j])
            output.append(maxi)

        return output
             
        