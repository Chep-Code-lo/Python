class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
if __name__ == "__main__":
    points = [ Point(1, 2), Point(3, 4), Point(-1, 5) ]
    result = Point(0, 0)
    for p in points:
        result = result + p   
    print("Danh sách các điểm:")
    for p in points:
        print(p)             
    print("Tổng các điểm:", result)
