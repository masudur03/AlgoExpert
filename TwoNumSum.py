#solution 1
#O(n^2) time | O(n)^2 space
def twoNumberSum(array, targetSum):
    # Write your code here.
    output = []
    for i in range(len(array) - 1):
        num1 = array[i]
        for j in range(i+1, len(array)):
            num2 = array[j]
            if(num1+num2 == targetSum):
                output.append(num1)
                output.append(num2)
                
    return output;




#solution 2
#O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}

    #go through the numbers in array
    for num in array:
        num2 = targetSum - num
        if num2 in nums:
           return [num2, num]
        else:
            nums[num] = True
    
    return []
