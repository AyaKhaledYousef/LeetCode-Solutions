def increasingTriplet(self, nums):
    small,big = 100000000000000000000,100000000000000000000
    for i in nums:
        
        if i <= small:
            small = i
        elif i<=big:
            big = i
        else :
            return True
    return False