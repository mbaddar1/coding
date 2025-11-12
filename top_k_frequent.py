"""
Problem Statement

Given an integer array nums and an integer k, return the k most frequent elements.
Return the answer in any order.

Example

makefile
Copy
Edit
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
makefile
Copy
Edit
Input: nums = [1], k = 1
Output: [1]
Constraints

1 <= nums.length <= 10^5

-10^4 <= nums[i] <= 10^4

k is in the range [1, the number of unique elements in nums]

Follow-up: Can you solve it in O(n) time complexity?


"""


def top_k_frequent(arr, k):
    n = len(arr)
    freq = dict()
    aux = [[] for _ in range(n)]
    for i in range(n):  # O(n)
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    for item in freq.items():
        num = item[0]
        freq = item[1]
        aux[freq - 1].append(num)  # freq ranges from 1 to n
    count = k
    i = n - 1
    top_K = []
    while i >= 0 and count > 0:
        for u in aux[i]:
            top_K.append(u)
            count -= 1
            if count == 0:
                break
        if count == 0:
            break
        i -= 1
    return top_K


if __name__ == "__main__":
    a = [3, 3, 2, 2, 2, 1, 1]
    r = top_k_frequent(a, 3)
    print(r)
