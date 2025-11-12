import heapq


class MedianHeapFinder:
    def __init__(self):
        # the init state : size of max heap (track lower) half
        self.min_heap = []
        self.max_heap = []

    def addNumber(self, val: int):
        # add element to max heap to keep to track the largest value of the lower end
        heapq.heappush(self.max_heap, -val)
        lower_half_max_val = -heapq.heappop(self.max_heap)
        # now add the largest element of lower half to min-heap to keep track
        heapq.heappush(self.min_heap, lower_half_max_val)
        if len(self.min_heap) > len(self.max_heap):  # len(min_heap) must be <= len(max_heap)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def getMedian(self):
        if len(self.max_heap) == (len(self.min_heap) + 1):
            return -heapq.heappop(self.max_heap)
        elif len(self.max_heap) == len(self.min_heap):
            return (-heapq.heappop(self.max_heap) + heapq.heappop(self.min_heap)) / 2.0
        else:
            raise ValueError("something went wrong")


if __name__ == '__main__':
    mf = MedianHeapFinder()
    nums = [5, 2, 10, 1]
    for num in nums:
        mf.addNumber(num)
    r = mf.getMedian()
    print(r)
