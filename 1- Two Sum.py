class Solution(object):
    def twoSum(self, nums, target):
 
        look_for={}
        for n,x in enumerate(nums):
            try:
                return look_for[x], n    
            except KeyError:
                look_for.setdefault(target - x,n)
        
Solution()       

