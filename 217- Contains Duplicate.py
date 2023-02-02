def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
       
print(containsDuplicate([1,2,3,1])) # True