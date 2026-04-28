#課題１　
import random 
#print(random.randrange(1,3,1))
data_1=0
data_2=0
total=0
list=[]

while(total!=8):
        data_1=random.randrange(1,3,1)
        total+=data_1
        #print(total)
        list.append(data_1)
        if(data_1==2 and data_2==2):
            print("2が連続 終了")
            break
        elif(total==8):
            print("合計が8 終了")
            break
        data_2=data_1
        
       
print(list)

"""
答えのコード
#■課題1-1
#ランダムで１か２を出力する関数をつくり、積算して８になるまで計算させ続けるプログラムを作れ。ただし、２が二回連続でると停止するものとする。
import random


max = 17 #目標段数

num = 0
while num < 10000:

        total = 0
        pre_element = 0
        element = 0
        process=""
        for i in range(max):
        
                element = int( 2*random.random() ) + 1 ## 1 or 2を生成                           →→→→→こいつの動作確認する。
           
        
                process  += " " + str(element)   ##途中経過を文字列として足して記録
                total += element                 ##階段を1段か2段のぼる
                if pre_element == 2 and element==2:
                        #print("２が二回連続出たので停止", process, "登った段数", total )
                        break
        
                pre_element = element #2段連続判定のために保存
        
   
        
                if total > max:    ##計算打ち切り処理 15段目が終了だとしても14+2の場合を弾く。失敗ということで0を返す
                        #print(process, "9段目にいってしまったので、これは無効")
                        break

                if total == max:   ##目的の段数に到達。成功したことを伝える１と途中経過がはいったprocessを返す
                        print(process, num,"回目でいけたはず")
                        break

                num += 1
"""
