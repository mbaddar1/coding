"""
https://leetcode.com/problems/design-hit-counter/description/
"""
from typing import List


# Sol1 - BinSearch
# Sol2 -

class HitCounter:
    NUM_BUCKETS = 100
    def __init__(self):
        self.timestamps = []
        self.counts = {}
        self.total_count = 0
    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.total_count += 1
        self.counts[timestamp] = self.total_count

    def getHits(self, timestamp: int) -> int:
        lower_bound = timestamp - 300
        if lower_bound < self.timestamps[0]:
            count1 = 0
        else:
            idx_actual_lower_bound = HitCounter.bin_search(arr=self.timestamps, target=lower_bound, low=0,
                                                           high=len(self.timestamps) - 1, mode="higher")
            assert idx_actual_lower_bound >= 0
            actual_lower_bound = self.timestamps[idx_actual_lower_bound]
            count1 = self.counts[actual_lower_bound]
        if timestamp < self.timestamps[0]:
            count2 = 0
        else:
            idx_actual_upper_bound = HitCounter.bin_search(arr=self.timestamps, target=timestamp, low=0,
                                                           high=len(self.timestamps) - 1, mode="lower")
            actual_upper_bound = self.timestamps[idx_actual_upper_bound]
            count2 = self.counts[actual_upper_bound]

        return count2-count1
    @staticmethod
    def bin_search(arr:List[int], target:int, low:int, high:int, mode: "str"):
        assert mode in ["higher","lower"]
        mid = (low + high) // 2
        if low > high:
            return -1
        elif  arr[0]>target and mode == "higher":
            return 0
        elif arr[0]>target and mode == "lower":
            raise ValueError
        elif arr[-1] < target and mode == "lower":
            return len(arr)-1
        elif arr[-1] < target and mode == "higher":
            raise ValueError
        elif arr[mid] == target:
            return mid
        if mid+1 < len(arr) and arr[mid] < target < arr[mid+1]:
                if mode == "lower":
                    return mid
                elif mode == "higher":
                    return mid+1
                else:
                    raise ValueError
        if target < arr[mid]:
            return HitCounter.bin_search(arr, target, low, mid - 1, mode)
        elif target > arr[mid]:
            return HitCounter.bin_search(arr, target, mid + 1, high, mode)
        else:
            raise ValueError



if __name__ == '__main__':
    hitCounter = HitCounter()
    hitCounter.hit(1)
    hitCounter.hit(2)
    hitCounter.hit(3)
    assert hitCounter.getHits(4) == 3
    hitCounter.hit(300)
    assert hitCounter.getHits(300) == 4
    assert hitCounter.getHits(301) ==3

    # a = [2,4,5,8,10]
    # r = HitCounter.bin_search(a,2,0,len(a),"lower")
    # assert r == 0

    # r = HitCounter.bin_search(a,3,0,len(a),"higher")
    # assert r == 1

    # r = HitCounter.bin_search(a, 6, 0, len(a), "higher")
    # assert r == 3

    # r = HitCounter.bin_search(a, 6, 0, len(a), "lower")
    # assert r == 2

    # r = HitCounter.bin_search(a, 3, 0, len(a), "lower")
    # assert r == 0

    #r = HitCounter.bin_search(a, 1, 0, len(a), "lower")
    # assert r == 0



