# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:34:05 2022

@author: MMEENAK4
"""
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.flatten(nestedList)

    def flatten(self, lst):
        for el in lst:
            if el.isInteger(): self.data.append(el.getInteger())
            else: self.flatten(el.getList())

    def hasNext(self) -> bool: return len(self.data)

    def next(self) -> int: return self.data.pop(0)
"""   
class NestedIterator:
    actual = []
    idx = 0
    n = 0
    def __init__(self, nestedList):
        self.actual = []
        self.rec(nestedList)
        self.n = len(self.actual)
        self.idx = 0
    def rec(self, nestedList):
        for i in range(len(nestedList)):
            x = nestedList[i]
            if(x.isInteger()):
                self.actual.append(x.getInteger())
            else:
                self.rec(x.getList())
    def next(self):
        self.idx += 1
        return self.actual[self.idx-1]
    def hasNext(self):
        if(self.idx < self.n):
            return True
        return False

