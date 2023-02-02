

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sum = 0
    l = []
    for n in nums:
        sum +=n
        l.append(sum)

    return l 


nums = [1,1,1,1,1]
print(runningSum(nums)) # [1, 2, 3, 4, 5]