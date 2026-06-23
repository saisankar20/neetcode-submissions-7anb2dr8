import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        

    def findMedian(self) -> float:
        length = len(self.nums)
        if length % 2 == 0:
            left = int((length/2)-1)
            right = int((length/2))
            median = (self.nums[left] + self.nums[right]) / 2
            return median
        else:
            index = int((length - 1) / 2)
            return self.nums[index]

        return 0.0
        
        