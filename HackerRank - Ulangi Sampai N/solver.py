# Ulangi Sampai N

n = int(input())

for x in range(1, n+1):
    if x % 5 == 0:
        continue
    elif(x % 10 == 3):
        print("Nice")
    elif(x >= 113):
        print("Error")
        break
    else:
        print(x)