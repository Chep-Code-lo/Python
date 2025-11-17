n = int(input("Nhập vào số N"))

primes_list = [] 
num_to_check = 2 
while len(primes_list) < n:
    is_prime = True        
    for i in range(2, int(num_to_check**0.5) + 1):
        if num_to_check % i == 0:
            is_prime = False
            break 
    if is_prime:
        primes_list.append(num_to_check)
            
    num_to_check += 1
print(f"{n} số nguyên tố đầu tiên là: {primes_list}")