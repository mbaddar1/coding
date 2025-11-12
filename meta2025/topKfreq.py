class TopKfreq:
    def __init__(self):
        self.freq = dict()  # freq(any_number) ranges from n = num of elements

    def findTopKfreq(self, arr: list, k: int, num_buckets=10) -> list:
        # find freq
        n = len(arr)
        for i in range(n):
            self.freq[arr[i]] = self.freq.get(arr[i], 0) + 1

        # keep in mind that frequency can be repeated, i.e. two element have same frequency q
        freq_buckets = [[] for i in range(n)]  # freq range from 1 to n
        for key, val in self.freq.items():
            freq_buckets[val].append(key)

        top_k = []
        for j in range(n - 1, -1, -1):
            for u in freq_buckets[j]:
                top_k.append(u)
                if len(top_k) == k:
                    break
            if len(top_k) == k:
                break
        return top_k


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 3]
    topKfinder = TopKfreq()
    r = topKfinder.findTopKfreq(nums, 2)
    print(r)
