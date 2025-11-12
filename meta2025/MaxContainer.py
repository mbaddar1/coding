from typing import List


def find_max_container(heights: List[int]):
    n = len(heights)
    left_wall_index = 0
    right_wall_index = n - 1
    max_size = 0
    while left_wall_index < right_wall_index:
        left_unchanged = False
        right_unchanged = False
        # measure
        size = min(heights[left_wall_index], heights[right_wall_index]) * (right_wall_index - left_wall_index)
        max_size = max(size, max_size)
        # update indices
        k1 = left_wall_index + 1
        while k1 < right_wall_index:
            if heights[k1] - heights[left_wall_index] <= (k1 - left_wall_index):
                k1 += 1
            else:
                left_wall_index = k1

        k = right_wall_index - 1
        while k > left_wall_index:
            if heights[k] - heights[right_wall_index] <= (right_wall_index - k):
                k -= 1
            else:
                right_wall_index = k
                break


    return max_size


if __name__ == '__main__':
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    r = find_max_container(a)
