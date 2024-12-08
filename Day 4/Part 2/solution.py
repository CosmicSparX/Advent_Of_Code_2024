inp = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".splitlines()

inp = open("in.txt", "r").readlines()

count = 0

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 'A':
            if i+1 >= len(inp) or i-1 < 0 or j+1 >= len(inp[0]) or j < 0:
                continue
            if ((inp[i-1][j-1] == 'M' and inp[i+1][j+1] == 'S') or (inp[i-1][j-1] == 'S' and inp[i+1][j+1] == 'M')) \
                and ((inp[i-1][j+1] == 'M' and inp[i+1][j-1] == 'S') or (inp[i-1][j+1] == 'S' and inp[i+1][j-1] == 'M')):
                count += 1
                
print(count)