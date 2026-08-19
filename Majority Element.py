class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_frequency = Counter(nums)
        return nums_frequency.most_common()[0][0]
         