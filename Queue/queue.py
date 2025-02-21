class Queue:
    def __init__(self):
        self.array=[]
        self.max=100
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        if self.front==self.rear==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.rear==self.max-1:
            return True
        else:
            return False
    def Enqueueq(self,data):
        if self.isFull():
            print("Queue Overflow")
        else:
            self.rear+=1
            self.front=0
            self.array.append(data)
            print(self.array)
    def Dequeueq(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            if self.array==[]:
                print("Queue Underflow")
            else:
                self.array.pop(0)
                print(self.array)
        if not self.array:
            self.front+=1
q=Queue()
print(q.isEmpty())
print(q.isFull())
q.Enqueueq(10)
q.Enqueueq(12)
q.Enqueueq(20)
q.Enqueueq(8)
q.Dequeueq()
q.Dequeueq()
q.Dequeueq()
q.Dequeueq()
q.Dequeueq()
q.Enqueueq(8)
q.Enqueueq(20)
