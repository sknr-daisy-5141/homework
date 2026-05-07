#課題3　経路を確かめるプログラム　再帰は無理だったのでランダムでやってみる。
import random
 
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
 

def road(cu_point,new_graph,process):
    process+=" "+str(cu_point+1)
    #print(process)
    pass_line=[]
    #進める個所を調べる。
    for i in range(len(new_graph[cu_point])):
        if(new_graph[cu_point][i]==1):
            pass_line.append(i)
    if(len(pass_line)==0):
       #print("道がないので終了")
       #print(new_graph)
        #すべての道を使用したかチェックする。
        for j in range(len(new_graph)):
            if(1 in new_graph[j]):
                print(" 道が残っている。",process)
                return 0
        print("すべての道を使用済み",process)
        return 0
    #進む道をランダムに決める。
    div_road=pass_line[int(len(pass_line)*random.random())]
    new_graph[cu_point][div_road]=0#通った道を塞ぐ
    new_graph[div_road][cu_point]=0
    road(div_road,new_graph,process)

#スタート地点をランダムにすると時間がかかるので固定にする。
times=10
for k in range(times):
    start=5
    result="start"
    new_graph = [row[:] for row in rinsetu]
    road(start-1,new_graph,result)



    
        
        

    
