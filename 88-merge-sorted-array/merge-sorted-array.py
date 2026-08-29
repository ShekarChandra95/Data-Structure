class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for l in range(n):
            nums1[m+l] = nums2[l]

        nums1.sort()