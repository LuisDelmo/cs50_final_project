import random

class Node:
    def __init__(self,coords,parent=None):
        #TODO maybe remove complty the node class doesnt seem that useful
        self.coords = coords
        self.parent = parent
        #initialize list and shuffle self
        self.nums = list(range(1, 10))
        random.shuffle(self.nums)
        self.index = 0
        self.value = self.nums[self.index]


