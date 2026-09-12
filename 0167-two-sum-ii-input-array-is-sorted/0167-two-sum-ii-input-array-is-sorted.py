class Solution:  
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # def twoSum(self, numbers, target):
        first = 0
        last = len(numbers) - 1
        while (first < last):
            if (numbers[first] + numbers[last] < target):
                first += 1
            
            elif ((numbers[first] + numbers[last]) > target):
                last -= 1
            
            else:
                break

        List = [first + 1, last + 1]
        return List
