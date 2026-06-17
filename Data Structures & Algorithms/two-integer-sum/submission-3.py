class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {

        }
        for num, i in enumerate(nums):
            diff = target - i
            if diff in numbers:
                
                return [numbers[diff], num]
            else:
                numbers[i] = num
                
            

