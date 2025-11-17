import math

chu_vi = 0
x = float(input("Enter the first x-coordinate: "))
y = float(input("Enter the first y-coordinate: "))
temp_x = x
temp_y = y

while True:
    x_str = input("Enter the next x-coordinate (blank to quit): ")
    if x_str == " ":
        khoang_cach = math.sqrt((temp_x -x)**2 + (temp_y - y)**2)
        chu_vi += khoang_cach
        break
    
    current_x = float(x_str)
    current_y = float(input("Enter the next y-coordinate: "))
    
    khoang_cach = math.sqrt((current_x - temp_x)**2 + (current_y - temp_y)**2)
    chu_vi += khoang_cach
    temp_x = current_x
    temp_y = current_y
print(f"The perimeter of that polygon is {chu_vi}")