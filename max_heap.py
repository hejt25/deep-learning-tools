# 最大堆的实现
import sys


class MaxHeap:
    def __init__(self, heapSize):
        # 定义存储锥的大小
        self.heapSize = heapSize
        # 使用数组存储完全二叉树
        self.maxheap = [0] * (heapSize + 1)
        # realSize用于记录堆元素的个数
        self.realSize = 0

    # 添加元素
    def add(self, element):
        self.realSize += 1
        # 如果堆的元素的个数大于一开始设定的数组的个数，则返回：Add too many elements
        if self.realSize > self.heapSize:
            print("Add too many elements")
            self.realSize -= 1
            return
        # 将元素添加到数组中
        self.maxheap[self.realSize] = element
        # 新增元素的索引位置
        index = self.realSize
        # 父节点的索引位置
        parent =  index // 2
        # 判断父节点的值是否大于当前孩子节点的值
        while self.maxheap[parent] < self.maxheap[index] and  index  > 1:
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2

    # 删除元素
    def pop(self):
        # 如果当前元素的个数问0，则返回：Don't have any element
        if self.heapSize < 1:
            print("Don't have any element")
            return sys.maxsize
        else:
            remove_element = self.maxheap[1]
            # 将堆中的最后一个元素赋值给第一个元素
            self.maxheap[1] = self.maxheap[self.realSize]
            self.realSize -= 1
            index = 1
            # 当前节点不是孩子节点
            while index < self.realSize and index < self.realSize // 2:
                # 当前节点的左右两孩子节点
                left = index * 2
                right = index * 2 + 1
                # 当删除节点的元素小于左孩子或右孩子节点时，代表该元素的值小，此时需要将该元素与左右孩子节点中的最大节点进行交换
                if self.maxheap[index] < self.maxheap[left] or self.maxheap[index] < self.maxheap[right]:
                    if self.maxheap[left] < self.maxheap[right]:
                        self.maxheap[index], self.maxheap[right] = self.maxheap[right], self.maxheap[index]
                        index = right
                    else:
                        self.maxheap[index], self.maxheap[left] = self.maxheap[left], self.maxheap[index]
                        index = left
                else:
                    break
        return remove_element

    # 取出堆顶元素
    def peek(self):
        return self.maxheap[1]

    # 返回堆的元素的个数
    def size(self):
        return self.realSize

    def toString(self):
        print(self.maxheap[1: self.realSize])


if __name__ == "__main__":
    # 测试用例
    maxHeap = MaxHeap(5)
    maxHeap.add(1)
    maxHeap.add(2)
    maxHeap.add(3)
    # [3,1,2]
    maxHeap.toString()
    # 3
    print(maxHeap.peek())
    # 3
    print(maxHeap.pop)
    # 2
    print(maxHeap.pop)
    # 1
    print(maxHeap.pop)
    maxHeap.add(4)
    maxHeap.add(5)
    # [5,4]
    maxHeap.toString()

