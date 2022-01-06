import numpy as np


class MaxHeap():
    arr = None

    insert_idx = None

    @staticmethod
    def get_left_child(idx, a):
        n = len(a)
        left_idx = 2 * idx + 1
        left = a[left_idx] if left_idx <= n - 1 else None
        return left

    @staticmethod
    def get_right_child(idx, a):
        n = len(a)
        right_idx = 2 * idx + 2
        right = a[right_idx] if right_idx <= n - 1 else None
        return right

    @staticmethod
    def getParent(idx, a):
        if idx == 0:
            return None
        parent_idx = int((idx - 1) / 2)
        return a[parent_idx]

    def insert(self, element):
        assert self.insert_idx < len(self.arr), "insert index >=len(self.arr) , max-heap is full"
        self.arr[self.insert_idx] = element
        j = self.insert_idx
        while MaxHeap.getParent(j, self.arr) is not None and MaxHeap.getParent(j, self.arr) < self.arr[j]:
            parent_idx = int((j - 1) / 2)
            tmp = self.arr[j]
            self.arr[j] = self.arr[parent_idx]
            self.arr[parent_idx] = tmp
            j = parent_idx
        self.insert_idx += 1

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


if __name__ == '__main__':
    input_arr = [2, 1, 2, 1, 2]
    n = len(input_arr)
    mh = MaxHeap(n)
    for i in range(n):
        mh.insert(input_arr[i])
    validate_ = mh.validate()
    print(mh.arr)
    print(validate_)

