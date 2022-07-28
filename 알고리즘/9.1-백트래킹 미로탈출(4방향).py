global v, m, ex, ey 

def find_way_from_maze(r, c):
    if r == ex and c == ey:
        return True
    v[r][c] = True

    if m[r][c+1] == '0' and v[r][c+1] == False:
        if find_way_from_maze(r, c+1):
            m[r][c+1] = trace
            return True
    if m[r+1][c] == '0' and v[r+1][c] == False:
        if find_way_from_maze(r+1, c):
            m[r+1][c] = trace
            return True
    if m[r][c-1] == '0' and v[r][c-1] == False:
        if find_way_from_maze(r,c-1):
            m[r][c-1] = trace
            return True
    if m[r-1][c] == '0' and v[r-1][c] == False:
        if find_way_from_maze(r-1, c):
            m[r-1][c] = trace
            return True
    return False

trace = '\u00B7'
n = int(input())
sx, sy, ex, ey = (int(x) for x in input().split())
m = []

for i in range(n):
    m.append([c for c in input()])

v = [[False for _ in range(n)] for _ in range(n)]
m[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
m[ex][ey] = 'e'

if success:
    for row in m:
        for c in row:
            if c == '1':
                print('#', end="")
            elif c== '0':
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")
