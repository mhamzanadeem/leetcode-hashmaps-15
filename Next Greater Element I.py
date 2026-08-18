class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {value:index for index , value in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur>stack[-1]:
                value = stack.pop()
                index = nums1_dict[value]
                res[index] = cur

            if cur in nums1_dict:
                stack.append(cur)
        
        return res