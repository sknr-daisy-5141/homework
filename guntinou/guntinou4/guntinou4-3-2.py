rinsetu=[ 
    [0,1,0,0,0,1,0,0,0,0,0,0], 
    [1,0,1,1,1,0,0,0,0,0,0,0], 
    [0,1,0,0,0,0,1,0,0,0,0,0], 
    [0,1,0,0,1,1,0,1,0,0,0,0], 
    [0,1,0,1,0,0,1,1,1,0,0,0], 
    [1,0,0,1,0,0,0,1,0,1,0,0], 
    [0,0,1,0,1,0,0,0,1,0,0,1], 
    [0,0,0,1,1,1,0,0,1,0,1,0], 
    [0,0,0,0,1,0,1,1,0,0,1,0], 
    [0,0,0,0,0,1,0,0,0,0,1,0], 
    [0,0,0,0,0,0,0,1,1,1,0,1], 
    [0,0,0,0,0,0,1,0,0,0,1,0], 
 
] 

def road(cu_point, goal, rinsetu_line, process, edge_count):
    process.append(cu_point + 1)

    #すべて使い切ったかどうか
    if edge_count == 0:
        if cu_point == goal:
            print("完全経路:", process)
        process.pop()
        return  

    for next_point in range(len(rinsetu_line)):
        if rinsetu_line[cu_point][next_point] == 1:
            new_graph = [row[:] for row in rinsetu_line]#コピーの作成
            new_graph[cu_point][next_point] = 0
            new_graph[next_point][cu_point] = 0

            
            road(next_point, goal, new_graph, process, edge_count - 1)


    process.pop()


# 初期設定
start = 4
goal = 7

# 辺の総数を数える
edge_count = 0
for i in range(len(rinsetu)):
    for j in range(i):
        if rinsetu[i][j] == 1:
            edge_count += 1

for start in range(len(rinsetu)):
    process = []
    road(start, goal, rinsetu, process, edge_count)
