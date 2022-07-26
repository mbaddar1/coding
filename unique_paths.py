# https://leetcode.com/problems/unique-paths/
class Node:
    def __init__(self, val, path):
        self.val = val
        self.path = path


class Solution:
    def __init__(self):
        self.counter = 0

    def get_neighbors(self, i, j, m, n):

        neighbors = []
        # # left
        # if j > 0:
        #     neighbors.append((i, j - 1))
        # right
        if j < n - 1:
            neighbors.append((i, j + 1))
        # # up
        # if i > 0:
        #     neighbors.append((i - 1, j))
        # down
        if i < m - 1:
            neighbors.append((i + 1, j))
        return neighbors

    # def uniquePaths(self, m: int, n: int) -> int:
    #     stack_ = []
    #     init_node = Node((0, 0), set())
    #     stack_.append(init_node)
    #     while stack_:
    #         node = stack_.pop()
    #         if node.val == (m-1, n-1):
    #             self.counter += 1
    #             print(node.path)
    #             continue
    #         neighbors = self.get_neighbors(node.val, m, n)
    #         for neighbor in neighbors:
    #
    #             if neighbor not in node.path:
    #                 if neighbor == (1, 1):
    #                     print('----')
    #                 new_path = node.path
    #                 new_path.add(node.val)
    #                 new_node = Node(neighbor, new_path)
    #                 stack_.append(new_node)
    #
    #     return self.counter
    def __init__(self):
        self.mem = {}
        self.mem_hit_counter = 0

    def uniquePaths(self, m, n):
        r = self.__unique_paths(0, 0, m, n)
        return r

    def __unique_paths(self, i, j, m, n):
        if (i, j) in self.mem.keys():
            self.mem_hit_counter += 1
            return self.mem[(i, j)]
        neighbors = self.get_neighbors(i, j, m, n)
        if (m - 1, n - 1) in neighbors:
            return 1
        cntr = 0
        for i_, j_ in neighbors:
            r = self.__unique_paths(i_, j_, m, n)
            cntr += r
        self.mem[(i, j)] = cntr
        return cntr


if __name__ == '__main__':
    s = Solution()
    r = s.uniquePaths(3, 7)
    print(r)
    print(s.mem_hit_counter)
