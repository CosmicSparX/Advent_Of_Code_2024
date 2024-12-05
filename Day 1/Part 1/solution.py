a1 = []
a2 = []

with open("in.txt", 'r') as f:
    for line in f.readlines():
        itr = line.split()
        a1.append(int(itr[0]))
        a2.append(int(itr[1]))


a1.sort()
a2.sort()

ot = 0
for i, j in zip(a1, a2):
    ot += abs(i - j)

print(ot)