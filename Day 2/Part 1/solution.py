with open("in.txt", "r") as f:
    reports = [tuple(map(int, report.split())) for report in f.readlines()]

safe = 0
for report in reports:
    if report[0] < report[1]:
        order = (-3, -1)
    else:
        order = (1, 3)
    
    prev = report[0]
    for i in range(1, len(report)):
        diff = prev - report[i]
        if diff >= order[0] and diff <= order[1]:
            prev = report[i]
            continue
        else:
            break
    else:
        safe += 1

print(safe)