inp = open("in.txt", 'r').read()

ot = 0
start = 0
while (idx := inp.find("mul(", start)) != -1:
    idx += 4
    start = idx
    digit1 = ""
    while inp[idx].isdigit() and len(digit1) < 3:
        digit1 += inp[idx]
        idx += 1
    
    if inp[idx] != "," or len(digit1) == 0:
        continue

    idx += 1
    digit2 = ""
    while inp[idx].isdigit() and len(digit2) < 3:
        digit2 += inp[idx]
        idx += 1
    
    if inp[idx] != ")" or len(digit2) == 0:
        continue

    ot += int(digit1) * int(digit2)

print(ot)