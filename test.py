from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 3:
            res = []
            n = len(nums)
            nums.sort()
            for i in range(n):
                x = -nums[i]
                j = i + 1
                k = n - 1
                while j < k:
                    if nums[j] + nums[k] == x:
                        entry = sorted([nums[i], nums[j], nums[k]])
                        if entry not in res:
                            res.append(entry)
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] > x:
                        k -= 1
                    else:
                        j += 1
            return res
        elif sum(nums) == 0:
            return [nums]
        else:
            return []

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))