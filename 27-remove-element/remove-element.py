class Solution:
    def removeElement(self, nums: list[int], val = int):
        self.nums = nums
        self.val = val
        k = 0

        for i in nums:
            if i != val:
                nums[k] = i
                k+=1

        return k
