with open("in.txt", "r") as f:
    reports = [tuple(map(int, report.split())) for report in f.readlines()]

safe = 0
unsafe_reports = []
for report in reports:
    # Changed the way I was determining whther the sequence 
    # is asec or desc since the part 1 way wasn't working anywmore
    n, p = 0, 0
    for i in range(len(report)-1):
        if report[i] - report[i+1] > 0:
            p += 1
        elif report[i] - report[i+1] < 0:
            n += 1

    if p < n:
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
            unsafe_reports.append((report, order))
            break
    else:
        safe += 1

# Gave up on optimal approach and settled for this

for report, order in unsafe_reports:
    for k in range(0, len(report)):     
        prev = report[0] if k != 0 else report[1]
        for i in range(1, len(report)):
            if i == k:
                continue

            diff = prev - report[i]
            if diff >= order[0] and diff <= order[1]:
                prev = report[i]
                continue
            else:
                break
        else:
            safe += 1

print(safe)