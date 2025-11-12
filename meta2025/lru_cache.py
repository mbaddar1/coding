from typing import Union


class UsageNode:
    def __init__(self, value: int, prevNode: Union["UsageNode", None], nextNode: Union["UsageNode", None]) -> None:
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode


class LRUCache:
    def __print_usage_list(self):
        curr = self.usage_list_head
        s = []
        while curr is not None:
            s.append(str(curr.value))
            curr = curr.nextNode
        print("-".join(s))
    def __add_recent_node(self, key: int):
        assert key in self.data.keys()  # I assume key is already added to data
        v = self.data[key]
        if v[1] is None:  # insert new node
            node = UsageNode(key, None, None)
            self.data[key]= (v[0],node)
            if self.usage_list_head is None and self.usage_list_tail is None:  # empty list
                self.usage_list_head = node
                self.usage_list_tail = node

            elif self.usage_list_head is not None and self.usage_list_tail is not None:
                node.prevNode = self.usage_list_tail
                self.usage_list_tail.nextNode = node
                self.usage_list_tail = node
                self.usage_list_tail.nextNode = None
            else:
                raise ValueError(f"Impossible case : head {self.usage_list_head} tail {self.usage_list_tail}")
        else:  # move node to tail
            node = v[1]

            if node != self.usage_list_tail:
                if node == self.usage_list_head:
                    self.usage_list_head = node.nextNode
                    self.usage_list_head.prevNode = None
                    self.usage_list_tail.nextNode = node
                    node.prevNode = self.usage_list_tail
                    self.usage_list_tail = node
                    self.usage_list_tail.nextNode = None
                else:
                    node.prevNode.nextNode = node.nextNode
                    node.nextNode.prevNode = node.prevNode
                    self.usage_list_tail.nextNode = node
                    node.prevNode = self.usage_list_tail
                    node.nextNode = None

    def __remove_lru(self):
        if self.usage_list_head is None and self.usage_list_tail is None:
            raise ValueError("Impossible case . Trying to remove lru key with no usage tracking")
        assert self.usage_list_head is not None and self.usage_list_tail is not None # at least one element in usage_list
        lru_k = self.usage_list_head.value
        # delete head
        if self.usage_list_head == self.usage_list_tail and self.usage_list_head is not None:
            self.usage_list_head = None
            self.usage_list_tail = None
        else:
            self.usage_list_head = self.usage_list_head.nextNode
            self.usage_list_head.prevNode = None
        # delete entry from dict
        del self.data[lru_k]

    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.usage_list_head = None
        self.usage_list_tail = None

    def get(self, key: int) -> int:
        if len(self.data) == 0:
            raise ValueError("Cache is empty")
        v = self.data.get(key, None)
        if v:
            self.__add_recent_node(key)
            # debug
            self.__print_usage_list()
            return v[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.data) == self.capacity and key not in self.data.keys():
            self.__remove_lru()
        self.data.update({key: (value,None)})
        self.__add_recent_node(key)
        # debug
        self.__print_usage_list()


if __name__ == "__main__":

    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1 = 1}
    lRUCache.put(2, 2) # cache is {1 = 1, 2 = 2}
    lRUCache.get(1) # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    lRUCache.get(2) #  returns - 1(not found)
    lRUCache.put(4, 4) #  LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    lRUCache.get(1) #  return -1(not found)
    lRUCache.get(3) #  return 3
    lRUCache.get(4) #  return 4

###################
# First coding attempt, logic is flawed
###################
# # https://leetcode.com/problems/lru-cache/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# from typing import Union
#
#
# class UsageNode:
#     def __init__(self, value: int,
#                  nextNode: Union[
#                      "UsageNode", None]):  # Postponed Evaluation of Annotation https://peps.python.org/pep-0563/
#         self.value = value
#         self.nextNode = nextNode
#
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.head_usage = None
#         self.tail_usage = None
#         self.capacity = capacity
#         self.data_dict = {}
#
#     def __add_usage_node(self, key: int):
#         if self.head_usage is None:
#             assert self.tail_usage is None, "head and tail both should be None or not None"
#             node = UsageNode(key, None)
#             self.head_usage = node
#             self.tail_usage = node
#         elif self.head_usage is not None and self.tail_usage is not None:
#             node = UsageNode(key, None)
#             self.tail_usage.nextNode = node
#             self.tail_usage = node
#         else:
#             raise RuntimeError("Head and Tail both be None or not None, check...")
#     def __get_lru_node(self):
#         if self.head_usage is None and self.tail_usage is None:
#             raise RuntimeError("No usage yet, tail is None")
#         elif self.head_usage == self.tail_usage and (self.head_usage is not None and self.tail_usage is not None):
#             to_return_node = self.head_usage
#             self.head_usage = None
#             self.tail_usage = None
#         elif self.head_usage != self.tail_usage and (self.head_usage is not None and self.tail_usage is not None):
#             to_return_node = self.head_usage
#             self.head_usage = self.head_usage.nextNode
#         else:
#             raise RuntimeError(f"Cannot happen case : head = {self.head_usage}, tail = {self.tail_usage}")
#         return to_return_node.value
#
#     def get(self, key: int) -> int:
#         self.__add_usage_node(key)
#         if len(self.data_dict) > 0:
#             self.capacity -= 1
#             return self.data_dict.get(key, -1)
#         else:
#             raise ValueError("Cache is empty")
#
#     def put(self, key: int, value: int) -> None:
#         self.__add_usage_node(key)
#         if len(self.data_dict) == self.capacity-1 and key not in self.data_dict.keys():
#             key = self.__get_lru_node()
#             del self.data_dict[key]
#         self.data_dict.update({key: value})


