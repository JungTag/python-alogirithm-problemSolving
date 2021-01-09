import sys
sys.setrecursionlimit(10**6)

# DFS -> 88ms
while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    g, lands, visited = [], [], [[0 for _ in range(w)] for _ in range(h)]
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [1,1,1,0,0,-1,-1,-1]
    cnt =  0 
     
    for i in range(h):
        raw = [int(x) for x in sys.stdin.readline().split()]
        for j in range(w):
            if raw[j] == 1:
                lands.append([i, j]) # y, x
        g.append(raw)

    def dfs(y, x):
        visited[y][x] = 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if g[ny][nx] == 1 and visited[ny][nx] == 0:
                dfs(ny, nx) 

    for land in lands:

        if visited[land[0]][land[1]] == 0:
            dfs(land[0], land[1])
            cnt += 1
    
    print(cnt)