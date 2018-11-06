'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


class Solution:
    def twoSum(self, nums, target):
        temp = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            index = self.binary_search(target-nums[i], nums, 0, len(nums)-1, (len(nums)-1)/2 )
            print(index)
            print()
            if nums[i] + nums[index] == target:
                find = [i, index]
                break
        res = []
        for j in range(len(temp)):
            if temp[j] == nums[find[0]] or temp[j] == nums[find[1]]:
                res.append(j)
                
        res.sort()
        return res

    def binary_search(self, target, nums, lw, hi, mid):

        if nums[hi] == target:
            return hi
        elif nums[lw] == target:
            return lw

        if hi == mid or lw == mid: return 0

        if target > mid:
            argmid = int((mid + hi)/2)
            return self.binary_search(target, nums, int(mid), hi, argmid)
        else:
            argmid = int((lw + mid)/2)
            return self.binary_search(target, nums, lw, int(mid), argmid)

        
