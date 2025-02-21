class Stack:
    #you must declare self in each method for better implementation
    def __init__(self):
        self.top=-1 #initially top is -1 due to stack is empty
        self.max=100 #max length of stack
        self.array=[] #defined stack or list
    def isEmpty(self):
        if self.top==-1: 
            return True
        else:
            return False
    def isFull(self):
        if self.top==len(self.array):
            return True
        else:
            return False
    def Push(self,data): #for pushing the element you must need the data so also passing the data (value)
        if self.isFull():
            print("Stack is Overflow")
        else:
            self.top+=1 #increase the top value by one if Pushing the element
            self.array.append(data) #appending the element in stack list 
            print(self.array) #printing the stack
    def Pop(self):
        if self.isEmpty():
            print("Stack is Underflow")
        else:
            self.top-=1 #decrease the top value by one if Poping the element
            self.array.pop() #poping or deleting the element
            print(self.array) #printing the stack
    def Max(self):
        if self.isEmpty():
            print("Stack is Underflow")
        else:
           print(max(self.array)) #using default max method of python for max element #remember the syntax of max method
    def Min(self):
        if self.isEmpty():
            print("Stack is Underflow")
        else:
           print(min(self.array)) #using default min method of python for min element #remember the syntax of min method
s=Stack()
print(s.isEmpty())
print(s.isFull())
s.Push(5) #you can also pass the string in stack not just int but remember it won't return max or min value of stack 
s.Push(15)
s.Push(52)
s.Push(4)
s.Pop()
s.Max()
s.Min()