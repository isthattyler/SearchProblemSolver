from bfsQueue import *
class PriorityQueue(Queue):
    def dequeue(self):
        try:
            largest=0
            for i in range(len(self.items)):
                if self.items[i] > self.items[largest]:
                    largest=i
            item=self.items.pop(largest)
            return item
        except IndexError:
            return None