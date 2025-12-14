class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def isFull(self):
        return len(self.data) == self.capacity
    def enqueue(self, value):
        if self.isFull():
            print("queue đầy ròi!!!")
        else:
            self.data.append(value)
    def dequeue(self):
        if self.isEmpty():
            print("queue rỗng ròi!!!")
            return None
        else:
            return self.data.pop()
    def front(self):
        if self.isEmpty():
            print("queue rỗng nên ko có phần tử đầu !!!")
            return None
        else:
            return self.data[0]