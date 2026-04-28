#課題3　19の独列した数列のパターンの作成　再帰処理を利用する形にする。
import random
result_list=[]
def eight_stairs(result_list):
    total=0
    data_1=0
    data_2=0
    count_d=0
    list=[]
    while(len(result_list)<19):
        
        data_1=random.randrange(1,3,1)
        total+=data_1
        #改良型：酒田先生の授業で言及してたやつ
        #2が連続できたとき2を1に置き換える。
        if(data_1==2 and data_2==2):
            data_1=1
            data_2=1
        list.append(data_1)
        data_2=data_1

        if(total==8):
            result_list.append(list)
        
        elif(total>8):
            return eight_stairs(result_list)
        
        for k in range(len(result_list)):
            if(result_list.count(result_list[k-count_d])==2):
                result_list.remove(result_list[k-count_d])
                count_d+=1

    for j in range(len(result_list)):
        print(result_list[j])
    print(str("列の数は")+str(len(result_list))+str("です。"))

eight_stairs(result_list)

#ループを用いているので再帰処理はできていない
#8列作るところを再帰処理でもう一度作成する。


"""
#■課題1-3
#再帰処理で解く方法を実装せよ

num_of_method = 0
target_step  = 20  #目的の階段の段数

def kaidan(total_step, before_step, process):
   
   process  += " " + str(before_step)  
   total_step += before_step

   if total_step == target_step:
        global num_of_method
        num_of_method += 1
        print(process, "end")
        return 0
 
   if total_step >= target_step+1:
        print(process, "16dan damedayo")
        return 0
    
   if before_step == 1:
        kaidan(total_step, 1, process)
        kaidan(total_step, 2, process)
        
   if before_step == 2:
        kaidan(total_step, 1, process)

    
result ="start"
result2 ="start"

kaidan(0,1, result)
kaidan(0,2, result2)
print(num_of_method)


"""