"""
    https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=226517205173943&c=282010630480533&ppid=454615229006519&practice_plan=1
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
"""

# Add any extra import statements you may need here


# Add any helper functions you may need here
import numpy as np


def count_subarrays(arr):
    n = len(arr)
    fw_stack = [0]
    cnt = np.zeros(n)
    cnt[0]=1
    for i in range(1, n):
        curr_count=0
        if arr[i] > arr[i - 1]:
            while len(fw_stack) > 0:
                pop_idx = fw_stack.pop()
                cand = arr[pop_idx]
                if arr[i] < cand:

                    fw_stack.append(pop_idx)
                    fw_stack.append(i)
                    cnt[i] = i-pop_idx
                    break
            if len(fw_stack) == 0:
                fw_stack.append(i)
                cnt[i] = i+1

        else:
            cnt[i]=1

    print(cnt)


def max_forward(arr):
    n = len(arr)
    if n == 0:
        return []
    max_vals = list()
    max_vals.append((arr[0], 0))
    max_entry = (arr[0], 0)
    for i in range(1, n):
        if arr[i] > max_entry[0]:
            max_entry = arr[i], i
        max_vals.append(max_entry)
    return max_vals


def max_backward(arr):
    n = len(arr)
    if n == 0:
        return []
    max_vals = list()
    max_vals.append((arr[n - 1], n - 1))
    max_entry = (arr[n - 1], n - 1)
    for i in range(n - 2, -1, -1):
        if arr[i] > max_entry[0]:
            max_entry = arr[i], i
        max_vals.insert(0, max_entry)
    return max_vals


def count_subarrays_false_solution(arr):
    n = len(arr)
    if n == 0:
        return np.array([])
    max_fw = max_forward(arr)
    max_bw = max_backward(arr)
    counts = np.ones(n)
    # fw pass
    for i in range(1, n):
        x0 = max_fw[i - 1][0]
        x1 = max_fw[i - 1][1]
        if arr[i] >= x0:
            cnt_delta = i

        else:
            cnt_delta = i - (x1 + 1)
        counts[i] += cnt_delta
    # bw pass
    for i in range(n - 2, -1, -1):
        arr_i = arr[i]
        x0 = max_bw[i + 1][0]
        x1 = max_bw[i + 1][1]
        if arr[i] >= x0:
            cnt_delta = n - 1 - i
        else:
            cnt_delta = (x1 - 1) - i
        counts[i] += cnt_delta
    return counts[i]


# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # test_1 = [3, 4, 1, 6, 2]
    #test_1 = [3, 4, 6, 1, 2, 3, 7]
    #test_1 = [1, 2, 3, 4, 5, 6, 7]
    test_1 = [7, 6, 5, 4, 3, 2, 1]
    count_subarrays(test_1)
    # expected_1 = [1, 3, 1, 5, 1]
    # output_1 = count_subarrays(test_1)
    # check(expected_1, output_1)
    #
    # test_2 = [2, 4, 7, 1, 5, 3]
    # expected_2 = [1, 2, 6, 1, 3, 1]
    # output_2 = count_subarrays(test_2)
    # check(expected_2, output_2)

    # Add your own test cases here
