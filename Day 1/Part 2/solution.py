a1 = []
a2 = []

with open("in.txt", 'r') as f:
    for line in f.readlines():
        itr = line.split()
        a1.append(int(itr[0]))
        a2.append(int(itr[1]))


s_score = 0

for i in a1:
    s_score += i * a2.count(i)

print(s_score)