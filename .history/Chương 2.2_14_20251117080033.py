import math

perimeter = 0

first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

prev_x = first_x
prev_y = first_y

while True:
    x_str = input("Enter the next x-coordinate (blank to quit): ")

    if x_str == " ":
        distance = math.sqrt((first_x - prev_x)**2 + (first_y - prev_y)**2)
        perimeter += distance
        break
    
    current_x = float(x_str)
    current_y = float(input("Enter the next y-coordinate: "))
    
    distance = math.sqrt((current_x - prev_x)**2 + (current_y - prev_y)**2)
    
    perimeter += distance
    
    prev_x = current_x
    prev_y = current_y

print(f"The perimeter of that polygon is {perimeter}")