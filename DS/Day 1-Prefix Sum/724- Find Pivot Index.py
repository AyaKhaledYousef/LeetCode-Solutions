
nums = [1,7,3,6,5,6]

sum_right=sum(nums)
sum_left = 0 

for i in range(len(nums)):
    print(i)
    sum_right -= nums[i]
    print(sum_right)
    
    if sum_right == sum_left :
        print ("i=",i) 
        
    sum_left += nums[i]
    print("sum_left = ",sum_left)