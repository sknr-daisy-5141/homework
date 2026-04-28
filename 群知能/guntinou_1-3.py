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