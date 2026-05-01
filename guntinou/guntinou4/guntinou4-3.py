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
 
def road(cu_point,pre_point,rinsetu_line,count):
    process  += " " + str(pre_point)
    count+=1
    if(rinsetu_line[cu_point] in 1):
        road(count,cu_point,rinsetu_line,0)
    if(rinsetu_line[cu_point].count>1):
        road(cu_point,13,rinsetu_line,count+1)
        
            
            
        
        #print(process, "逃げ場なし")
        #return 0
    