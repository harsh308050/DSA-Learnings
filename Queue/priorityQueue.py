class PriorityQueue:
    def __init__(self):
        self.array = []
    def isEmpty(self):
        if len(self.array)==0:
            return True
    def Enqueue(self,data,priority):
        self.index=0
        while self.index < len(self.array) and self.array[self.index][1] <= priority:
            self.index+=1
        self.array.insert(self.index,(data,priority))
    def Dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            element = self.array.pop(0)
            print(self.array)
q = PriorityQueue()
print(q.isEmpty())  # True
q.Enqueue(10, 2)
q.Enqueue(12, 1)
q.Enqueue(20, 3)
q.Enqueue(8, 1)
q.Dequeue()
q.Dequeue()
