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
        if(data_1==2 and data_2==2):#前回の列が2の場合
            #print("2が連続 終了")
            return eight_stairs(0,0,list.clear())
        elif(total==8):#列内の合計が8の時
            #print("合計が8 終了")
            return list
        elif(total>8):#列内の合計が8より大きいとき
            #print("合計が8より大きい 終了")
            return eight_stairs(0,0,list.clear())
        
        data_2=data_1
    #print(list)
#何回実行するか入力する。
n=int(input("繰り返し回数"))

#リスト内に同じ内容があればそれを削除する。
for i in range(n):
    result_list.append(eight_stairs(data_1,data_2,list))
    #print(result_list)
    m=0
    for k in range(len(result_list)):
        #リスト内の同じ内容をカウントする。
        #同じ内容が2個ある場合、その内容を一つ削除する。
        if(result_list.count(result_list[k-m])==2):
            result_list.remove(result_list[k-m])
            m+=1
    
#出力する
for j in range(len(result_list)):
    print(result_list[j])
    
print(str("列の数は")+str(len(result_list))+str("です。"))


"""
#■課題1-2
#課題1-1をもとにして、積算して８になる19の独立した数列のパターンを出力するプログラムを作れ。（何万回、実行してもOK）力する関数をつくり、積算して８になるまで計算させ続けるプログラムを作れ。ただし、２が二回連続でると停止するものとする。
import random

#max=到達する階段の数の設定 
def plus_until_max(max):
    total = 0
    pre_element = 0
    element = 0
    process=""
        
    for i in range(max):
        
        element = int( 2*random.random() ) + 1 ## 1 or 2を生成
        
        #if element == 2 and pre_element == 2:  ##2が連続、2段連続昇る場合はルール違反なので、elementを強制的に１に
        #      element = 1       　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　→1に置き換える方法のほうが簡単
        
        process  += " " + str(element)   ##途中経過を文字列として足して記録
        total += element                 ##階段を1段か2段のぼる
        pre_element = element #2段連続判定のために保存
        
        if total > max:    ##計算打ち切り処理 15段目が終了だとしても14+2の場合を弾く。失敗ということで0を返す
            return (0, process)

        if total == max:   ##目的の段数に到達。成功したことを伝える１と途中経過がはいったprocessを返す
            return (1, process)
        
###ここからメイン
result_list = list()
sikou_kaisuu = 300000
target_number = 8

for p in range( sikou_kaisuu ):
    tmp_data = ""
    result = plus_until_max(target_number)  #関数の戻り値を一旦受ける
    
    if result[0] == 1:                                #戻り値の１要素目が１のときは成功なので、結果を足す処理に移行
       #print(result[1])
       if "2 2" not in result[1]:  
           result_judge =result[1] in result_list         #result[1]がすでにresult_list内にあるかどうかの判定
           if result_judge == False:                      #result[1]がresult_listになかったので、result_listにresult[1]を追加
              result_list.append(result[1])


result_list.sort(key=lambda x: len(x))     #適当な順番で入ってるので、長さでソートし直し

for index, value in enumerate(result_list): #全要素を出力
    print(index, value)

print(target_number, "段の階段をのぼる方法は", index+1, "通り") #indexに１をたして(result_list[0]からなので)出力
    
    

"""
    
