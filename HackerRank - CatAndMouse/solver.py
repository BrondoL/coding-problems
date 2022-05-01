def catAndMouse(x, y, z):
    catA = abs(x - z)
    catB = abs(y - z)
    if catA < catB:
        return "Cat A"
    elif catA > catB:
        return "Cat B"
    else:
        return "Mouse C"

n = int(input())
x = []
y = []
z = []
for i in range(n):
    position = [x for x in map(int, input().split())]
    x.append(position[0])
    y.append(position[1])
    z.append(position[2])

for i in range(n):
    print(catAndMouse(x[i], y[i], z[i]))

