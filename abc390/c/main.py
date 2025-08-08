import sys

def possible_rectangle(grid):
    H = len(grid)
    W = len(grid[0])
    # find bounding rectangle of all known black cells '#'
    rows = []
    cols = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                rows.append(i)
                cols.append(j)
    r_min, r_max = min(rows), max(rows)
    c_min, c_max = min(cols), max(cols)
    # check cells inside rectangle: must not be '.'
    for i in range(r_min, r_max + 1):
        for j in range(c_min, c_max + 1):
            if grid[i][j] == '.':
                return False
    # cells outside rectangle: must not be '#'
    for i in range(H):
        for j in range(W):
            if not (r_min <= i <= r_max and c_min <= j <= c_max):
                if grid[i][j] == '#':
                    return False
    return True

def main():
    data = sys.stdin.read().split()
    H, W = map(int, data[:2])
    rows = data[2:]
    grid = [list(row) for row in rows]
    print('Yes' if possible_rectangle(grid) else 'No')

if __name__ == '__main__':
    main()
