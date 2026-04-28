#再帰

#今度こそ再帰処理で作成する。
import random

total=0
data_1=0
data_2=0
result_list=[]
line=[]
count=0

def eight_stairs(data_1,data_2,line,result_list,count):
    if(len(result_list)==19):
        return result_list
    data_1=random.randrange(1,3,1)
    if(sum(line)==8):
        result_list.append(line)
        print(line)
        #print(result_list)
        count+=1
        print(count)
        return -1
        
    
    if(data_1==1):
        line.append(data_1)
        #print(line)
        return  eight_stairs(data_1,data_2,line,result_list,count)
    
    elif(data_1==2):
        if(data_1==2 and data_2==2):
            data_1=1
        line.append(data_1)
        print(line)
        return  eight_stairs(data_1,data_2,line,result_list,count)
    
eight_stairs(data_1,data_2,line,result_list,count)
    