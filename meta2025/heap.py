class MAX_HEAP:
    def __init__(self, size: int):
        self.arr = [None] * size
        self.size = size
        self.count = 0

    def insert(self, v: int):
        if self.count == self.size:
            raise ValueError("heap overflow")
        self.arr[self.count] = v
        self.heapify_up(self.count)
        self.count += 1

    def heapify_up(self, i):
        if i == 0:
            return
        parent = i // 2
        if self.arr[i] > self.arr[parent]:
            tmp = self.arr[i]
            self.arr[i] = self.arr[parent]
            self.arr[parent] = tmp
        self.heapify_up(parent)
    def del_top(self):
        # swap
        self.arr[0] = self.arr[self.count-1]
        self.arr[self.count-1] = None
        #
        self.count -= 1
        self.heapify_down(0)

    def heapify_down(self, i):
        # def get index of bigger child
        if (2*i+1) > (self.size-1):
            return
        bigger_child_idx = None
        if self.arr[2*i+1] is not None and self.arr[2*i+2] is not None:
            if self.arr[2*i+1] > self.arr[2*i+2]:
                bigger_child_idx = 2*i+1
            else:
                bigger_child_idx = 2*i+2
        elif self.arr[2*i+1] is not None and self.arr[2*i+2] is None:
                bigger_child_idx = 2*i+1
        elif self.arr[2*i+1] is None and self.arr[2*i+2] is not None:
                bigger_child_idx = 2*i+2
        else: # both are none
            pass
        tmp = self.arr[i]
        self.arr[i] = self.arr[bigger_child_idx]
        self.arr[bigger_child_idx] = tmp
        self.heapify_down(bigger_child_idx)
    def check(self):
        self.check2(0)
    def check2(self,i):
        if i > (self.count-1):
            return
        if 2*i+1 > (self.count-1):
            return
        if self.arr[2*i+1] is not None and self.arr[2*i+2] is not None:
            assert(self.arr[i] >= self.arr[2*i+1] and self.arr[i] >= self.arr[2*i+2])
            self.check2(2*i+1)
            self.check2(2*i+2)
        elif self.arr[2*i+1] is not None and self.arr[2*i+2] is None:
            assert (self.arr[i] >= self.arr[2 * i + 1])
            self.check2(2*i+1)
        elif self.arr[2*i+1] is None and self.arr[2*i+2] is not None:
            assert (self.arr[i] >= self.arr[2 * i + 2])
            self.check2(2*i+2)
        else:
            pass



if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    heap_ = MAX_HEAP(len(a))
    for i in range(len(a)):
        heap_.insert(a[i])
    heap_.check()
    print(heap_.arr)
    heap_.del_top()
    heap_.check()
