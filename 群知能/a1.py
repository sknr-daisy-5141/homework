#課題２ 19の独列した数列のパターンの作成

import random

#精算して８になる関数

data_1=0
data_2=0
list=[]
result_list=[]
def eight_stairs(data_1,data_2,list):
    total=0
    list=[]
    while(total<8):
        data_1=random.randrange(1,3,1)
        total+=data_1
        list.append(data_1)
        if(data_1==2 and data_2==2):
            print("2が連続 終了")
            #連続で2が来たとき値をリセットしてもう一度関数を呼び出す。
            return eight_stairs(0,0,list.clear())
        elif(total==8):
            print("合計が8 終了")
            return list
        elif(total>8):
            print("合計が8より大きい 終了")
            #合計が8を超えたとき値をリセットしてもう一度関数を呼び出す。
            return eight_stairs(0,0,list.clear())
        data_2=data_1

    #print(list)

#何回実行するか入力する。
n=int(input("繰り返し回数"))

#関数の実行
for i in range(n):
    result_list.append(eight_stairs(data_1,data_2,list))
    #print(result_list)
    count_d=0
    #リストから重複しているものを削除する。
    for k in range(len(result_list)):
        if(result_list.count(result_list[k-count_d])==2):#リストの中の同じ内容を数えて2つあるならば、条件を実行する。
            result_list.remove(result_list[k-count_d])
            count_d+=1 #リストから削除するので列がずれるのを防ぐために実行された回数を数える。

#出力する
for j in range(len(result_list)):
    print(result_list[j])
print(str("列の数は")+str(len(result_list))+str("です。"))

#AIに聞くと再帰処理の形にはなっているけれど厳密には再帰処理ではなく、繰り返しになっている。
#次の課題は今のコードをうまく再帰処理を利用する形にすればよい。