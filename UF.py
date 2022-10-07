#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：UF.py
@IDE     ：PyCharm 
@Author  ：hejintao
@Date    ：2022/10/7 10:47 
"""
from typing import *


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n
        self.node_cnt = n
        self.set_cnt = n

    def find(self, x):
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return False
        if self.size[root1] >= self.size[root2]:
            big, small = root1, root2
        else:
            big, small = root2, root1
        self.root[small] = big
        self.size[big] += self.size[small]
        self.set_cnt -= 1
        return True

    def is_connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.set_cnt



