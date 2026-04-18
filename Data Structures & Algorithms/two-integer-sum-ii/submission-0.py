class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(numbers)
        for i in range(len(numbers)):
            compliment = target -  numbers[i]
            if compliment in numbers[i+1 :]:
                return [i+1, numbers.index(compliment)+ 1]



        