class Solution:
    def findMin(self, nums: List[int]) -> int:
        # res = nums[0]
        # if len(nums)
        # for i in range(1,len(nums)-1,1):
        #     l = i-1
        #     r = i+1
        #     if nums[i] < nums[l] and nums[i] < nums[r]:
        #         res= nums[i]
        # if res > nums[0]:
        #     return nums[0]
        # return res
        if not nums:
            return None
        minimum = nums[0]
        for i in range(len(nums)):
            minimum = min(minimum, nums[i])
        return minimum