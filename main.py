from functools import cmp_to_key

ROW = 5
COL = 5


def mycmp(a, b):
    if (a.distance == b.distance):
        if (a.x != b.x):
            return (a.x - b.x)
        else:
            return (a.y - b.y)
    return (a.distance - b.distance)

class cell:

    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

def isInsideGrid(i, j):
    return (i >= 0 and i < ROW and j >= 0 and j < COL)

def shortest(grid, row, col):
    dis = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            dis[i][j] = 1000000000

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    st = []

    st.append(cell(0, 0, 0))

    dis[0][0] = grid[0][0]

    while (len(st) != 0):

        k = st[0]
        st = st[1:]

        for i in range(4):

            x = k.x + dx[i]
            y = k.y + dy[i]

            if (isInsideGrid(x, y) == 0):
                continue

            if (dis[x][y] > dis[k.x][k.y] + grid[x][y]):
                dis[x][y] = dis[k.x][k.y] + grid[x][y]
                st.append(cell(x, y, dis[x][y]))

                st.sort(key=cmp_to_key(mycmp))

    return dis[row - 1][col - 1]


grid = [[29, 99, 70, 15, 20], [9, 10, 50, 159, 5], [100, 110, 185, 11, 33], [88, 124, 41, 20, 140],[99, 32, 111, 41, 20]]
print(shortest(grid, ROW, COL))