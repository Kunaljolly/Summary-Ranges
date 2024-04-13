class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = []
        l, r = 0, 0
        for x in range(len(nums)):
            if x == len(nums) - 1 or nums[x + 1] - nums[x] != 1:
                if r == l:
                    n.append(str(nums[l]))
                else:
                    n.append(str(nums[l]) + "->" + str(nums[r]))
                l = r = x + 1
            else:
                r = x + 1
        return n
