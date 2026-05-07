import heapq

inf = float('INF')

G = [
    [0,2,3,1,0,0,0,0,0],
    [2,0,2,0,3,5,0,0,0],
    [3,2,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,3,0,0],
    [0,3,0,0,0,4,0,3,0],
    [0,5,1,0,4,0,2,0,0],
    [0,0,0,3,0,2,0,0,2],
    [0,0,0,0,3,0,0,0,5],
    [0,0,0,0,0,0,2,5,0],
]

def dijkstra(s, G):

    n = len(G)

    dist = [inf] * n
    dist[s] = 0

    seen = [False] * n

    prev = [-1] * n

    hq = [(0, s)]

    while hq:

        d, v = heapq.heappop(hq)

        # すでに確定済みなら飛ばす
        if seen[v]:
            continue

        seen[v] = True

        # 隣接頂点を調べる
        for to in range(n):

            cost = G[v][to]

            # 辺が存在しない
            if cost == 0:
                continue

            # より短い経路を発見した場合
            if dist[v] + cost < dist[to]:

                dist[to] = dist[v] + cost

                prev[to] = v

                heapq.heappush(hq, (dist[to], to))

    return dist, prev


# 経路復元
def get_path(t, prev):

    path = []

    while t != -1:
        path.append(t)
        t = prev[t]

    return path[::-1]


dist, prev = dijkstra(0, G)

print("最短距離:", dist)

goal = 8

print("最短経路:", get_path(goal, prev))