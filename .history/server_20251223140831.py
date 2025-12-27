class Sample():
    def __init__(self):
        self.a = 1
        self._b = 2 
        self.__c = 3 
 
x = Sample()
print(x.a, x._b, x.__c)