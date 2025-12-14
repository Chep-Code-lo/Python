class stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def isFull(self):
        return len(self.data) == self.capacity
    def push(self, value):
        if self.isFull():
            print("Stack đầy ròi!!!")
        else:
            self.data.append(value)
    def pop(self):
        if self.isEmpty():
            print("Stack rỗng ròi!!!")
            return None
        else:
            return self.data.pop()
    def top(self):
        if self.isEmpty():
            print("Stack rỗng nên ko có phần tử đầu !!!")
            return None
        else:
            return self.data[-1]