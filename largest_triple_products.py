"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=510655302929581&c=282010630480533&ppid=454615229006519&practice_plan=0
"""
import numpy as np


class MaxHeap():
    arr = None

    insert_idx = None

    @staticmethod
    def get_left_child(idx, a):
        n = len(a)
        left_idx = 2 * idx + 1
        left_idx = left_idx if left_idx <= n - 1 and a[left_idx] is not None else None
        return left_idx

    @staticmethod
    def get_right_child(idx, a):
        n = len(a)
        right_idx = 2 * idx + 2
        right_idx = right_idx if right_idx <= n - 1 and a[right_idx] is not None else None
        return right_idx

    @staticmethod
    def getParent(idx):
        if idx == 0:
            return None
        parent_idx = int((idx - 1) / 2)
        return parent_idx

    def insert(self, element):
        assert self.insert_idx < len(self.arr), "insert index >=len(self.arr) , max-heap is full"
        self.arr[self.insert_idx] = element
        j = self.insert_idx
        while MaxHeap.getParent(j) is not None and self.arr[MaxHeap.getParent(j)] < self.arr[j]:
            parent_idx = int((j - 1) / 2)
            tmp = self.arr[j]
            self.arr[j] = self.arr[parent_idx]
            self.arr[parent_idx] = tmp
            j = parent_idx
        self.insert_idx += 1

    def getMaxChild(self, idx):
        left_child_idx = MaxHeap.get_left_child(idx, self.arr)
        right_child_idx = MaxHeap.get_right_child(idx, self.arr)
        if left_child_idx is not None and right_child_idx is not None:
            if self.arr[left_child_idx] > self.arr[right_child_idx]:
                return left_child_idx
            else:
                return right_child_idx
        elif left_child_idx is not None:
            return left_child_idx
        elif right_child_idx is not None:
            return right_child_idx
        else:
            return None

    def extractMax(self):
        root_val = self.arr[0]
        parent_idx = 0
        max_child_idx = self.getMaxChild(parent_idx)
        while max_child_idx is not None:
            self.arr[parent_idx] = self.arr[max_child_idx]
            parent_idx = max_child_idx
            max_child_idx = self.getMaxChild(parent_idx)
        self.arr[parent_idx] = None
        self.insert_idx -= 1
        return root_val

    def __init__(self, max_size):
        self.arr = np.array([None] * max_size)
        self.insert_idx = 0

    def inorder_print(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        n = len(self.arr)
        if left_idx <= n - 1 and self.arr[left_idx] is not None:
            self.inorder_print(left_idx)
        print(self.arr[idx])

        if right_idx <= n - 1 and self.arr[right_idx] is not None:
            self.inorder_print(right_idx)

    def validate(self):
        n = len(self.arr)
        for i in range(n):
            left_child = MaxHeap.get_left_child(i, self.arr)
            right_child = MaxHeap.get_right_child(i, self.arr)
            if left_child is not None and left_child > self.arr[i] or \
                    right_child is not None and right_child > self.arr[i]:
                return False
        return True


# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMaxProduct(arr):
    if len(arr) == 0:
        return np.array([])
    n = len(arr)
    max_heap_ = MaxHeap(n)
    result_arr_ = np.array([-1] * n)
    for i in range(n):
        max_heap_.insert(arr[i])
        if i >= 2:
            x1 = max_heap_.extractMax()
            x2 = max_heap_.extractMax()
            x3 = max_heap_.extractMax()
            product_ = x1 * x2 * x3
            max_heap_.insert(x1)
            max_heap_.insert(x2)
            max_heap_.insert(x3)
            result_arr_[i] = product_
    return result_arr_


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
    arr_1 = [1, 2, 3, 4, 5]
    expected_1 = [-1, -1, 6, 24, 60]
    output_1 = findMaxProduct(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [-1, -1, 56, 56, 140, 140]
    output_2 = findMaxProduct(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
