#下グラフの最短経路を求めるプログラムの作成
x=1000
rinsetu=[
    [x,2,3,1,x,x,x,x,x],
    [2,x,2,x,3,5,x,x,x],
    [3,2,x,x,x,1,x,x,x],
    [1,x,x,x,x,x,3,x,x],
    [x,3,x,x,x,4,x,3,x],
    [x,5,1,x,4,x,2,x,x],
    [x,x,x,3,x,2,x,x,2],
    [x,x,x,x,3,x,x,x,5],
    [x,x,x,x,x,x,2,5,x],

]
save_cost=[0,0,0,0,0,0,0,0,0]

#print(rinsetu)
def short_road(cu_point,cu_cost,new_graph,process):
    process+=" "+str(cu_point+1)
    print(process)
    pass_line=[]
    #進める個所を調べる。
    for i in range(len(new_graph[cu_point])):
        if(new_graph[cu_point][i]<x):
            pass_line.append(i)
    print(pass_line)

    #進める箇所で最も小さいところ
    save_line=[]
    save_min=new_graph[cu_point][pass_line[0]]
    for k in range(len(pass_line)):
        for j in range(len(new_graph[cu_point])):
            #save_min=min(pass_line)
            #print(save_min)
            if(save_min==new_graph[cu_point][j]):
                save_line.append(j+1)
                pass_line.remove(save_min)
                count+=1
                break
    for l in range(len(save_line)):
        save_cost[save_line[l]]+=new_graph[cu_point][save_line[l]]
    print(save_cost)
    #print(save_line)
    for m in range(len(save_line)):
        new_graph[cu_point][save_line[m]]=x
        new_graph[save_line[m]][cu_point]=x
        short_road(save_line[m],save_cost,new_graph,result)


  





start=0
result="start"
cu_cost=0
new_graph = [row[:] for row in rinsetu]
short_road(start,cu_cost,new_graph,result)
