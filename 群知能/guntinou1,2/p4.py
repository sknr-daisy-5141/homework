#今度こそ再帰処理で作成する。 今やってるのは4
import random

total=0
data_1=0
data_2=0
result_list=[]
line=[]
count=0

def eight_stairs(data_1,data_2,total,line,result_list,count):
    if(len(result_list)==19):
        return result_list
    data_1=random.randrange(1,3,1)
    
    
    if(data_1==2 and data_2==2):
            data_1=1
    line.append(data_1)
    data_2=data_1
    total+=data_1
    count_d=0
    for k in range(len(result_list)):
        if(result_list.count(result_list[k-count_d])==2):
            result_list.remove(result_list[k-count_d])
            count_d+=1

    if(total<8):
        return eight_stairs(data_1,data_2,total,line,result_list,count)
    
    elif(total==8):
        #print(line)
        result_list.append(line)
        total=0
        line=[]
        return eight_stairs(data_1,data_2,total,line,result_list,count)
    
    elif(total>8):
        total=0
        line.clear()
        return eight_stairs(data_1,data_2,total,line,result_list,count)
   

    
eight_stairs(data_1,data_2,total,line,result_list,count)

#print(result_list)
for j in range(len(result_list)):
    print(result_list[j])