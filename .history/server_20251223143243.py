x = { '1' : 4, '3' : 6 , '6' : 9 , '2' : 3 }
for i in x:
    if int(i) % 3 == 0:
        print(x[i])