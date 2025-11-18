n = int(input())

listso = []
for i in range(n + 1):   
    listso.append(i)
listbinhphuong = []
for i in range(n):       
    listbinhphuong.append(i * i)

print("List các số từ 0 đến n:", listso)
print("List bình phương các số < n:", listbinhphuong)