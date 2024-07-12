
def product(nums):
    retValue = 1
    for each in nums:
        retValue = retValue * each
    return retValue

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    retList = []
    for index in range(len(nums)):
        retList.append(product(nums[0:index:1] + nums[index+1::1]))
    return retList

        
#Example 1:
#Input: 
nums = [1,2,3,4]
print(productExceptSelf(nums))
#Output: [24,12,8,6]

#Example 2:
#Input: 
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
#Output: [0,0,9,0,0]
 