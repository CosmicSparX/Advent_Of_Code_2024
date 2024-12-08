inp = open("in.txt", 'r').read()

ot = 0

start = 0
stop = inp.find("don't()")

while start != -1:
    stop = inp.find("don't()", start)

    while (idx := inp.find("mul(", start, stop)) != -1:        
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
    start = inp.find("do()", stop)

print(ot)