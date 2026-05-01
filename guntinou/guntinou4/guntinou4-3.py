#課題3　経路を確かめるプログラム
 
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
 
def road(cu_point,pre_point,rinsetu_line,pre_line,count,process):
    pre_line=rinsetu_line
    if(rinsetu_line[cu_point][count]==1):#列に通過可能な道がある場合　つまり列に１があるとき
        rinsetu_line[cu_point][count]=0#通った道を塞ぐ
        rinsetu_line[count][cu_point]=0
        process+=" "+str(cu_point+1)#道を記録する
        print(process)
        road(count,cu_point,rinsetu_line,pre_line,0,process)#次のポイントへ移動
    if((rinsetu_line[cu_point]).count(1)>1):
        road(cu_point,13,pre_line,0,count+1,process)#ほかの道に分岐したい

    
    if(count==11):#12列まで来たときに候補に
        print(rinsetu_line[cu_point],"逃げ場なし？")
        return 0
    (road(cu_point,pre_point,rinsetu_line,pre_line,count+1,process))
            
        
        #print(process, "逃げ場なし")
        #return 0

result="start"
road(0,0,rinsetu,0,0,result)