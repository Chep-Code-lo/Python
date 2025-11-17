x = float(input("Nhập số x: "))

guess = x / 2
epsilon = 1e-12 

while abs(guess * guess - x) > epsilon:
    guess = (guess + (x / guess)) / 2

print(f"Thuật toán Newton tìm được căn bậc hai của {x} là: {guess}")