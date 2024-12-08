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
"""

inp = open("in.txt", "r").readlines()

count = 0

def get_directions(x, y):
    cardinal = [
        [(x+1, y), (x+2, y), (x+3, y)], 
        [(x-1, y), (x-2, y), (x-3, y)], 
        [(x, y+1), (x, y+2), (x, y+3)],
        [(x, y-1), (x, y-2), (x, y-3)]
    ]

    diagonal = [
        [(x+1, y+1), (x+2, y+2), (x+3, y+3)],
        [(x+1, y-1), (x+2, y-2), (x+3, y-3)],
        [(x-1, y+1), (x-2, y+2), (x-3, y+3)],
        [(x-1, y-1), (x-2, y-2), (x-3, y-3)] 
    ]

    return cardinal + diagonal

st = "MAS"
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 'X':
            for direction in get_directions(i, j):
                for k, coords in enumerate(direction):
                    x, y = coords
                    if x < 0 or x >= len(inp) or y < 0 or y >= len(inp[0]) or inp[x][y] != st[k]:
                        break
                else:
                    count += 1

print(count)
    