import random
#足し算するとちょうど60になる組み合わせを作成する。
#60までの素数のリストを作成する。
n=60
sosuu_list=[]
sum_list=[]
sixty_list=[]

#素数の判定
for i in range(2,n+1):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if count==1:
        sosuu_list.append(i)

#print(sosuu_list)
round=int(input("繰り返す回数を入力する"))
count_d=0
#round=10000
#足し算してちょうど60になるような組み合わせを探す。
for i in range(round):
    #繰り返すたびにリストを増やす。
    sum_list.append([])
    
    while(sum(sum_list[i])<60):#リスト内が60以下なら繰り返す。
        n=random.randint(1,len(sosuu_list)-1)#素数リストからランダムで何番目かを選ぶ。
        #print(n)
        sum_list[i].append(sosuu_list[n])
        if(sum(sum_list[i])==60):#60の時、リストに追加する。
            #print(sum_list[i])
            sixty_list.append(sum_list[i])
            break

print(sixty_list)
print(str("組み合わせの数は")+str(len(sixty_list)))



"""
#課題2-2
#足し算するとちょうど 60 になるような素数の組合せを出力するプログラムを作成せよ（最低50万回試行）
#例： 41 17 2

import random
#sys.setrecursionlimit(200000000) #Linuxでは動くらしい
#sosuu_hantei()関数、引数が素数である場合1を返す。引数が素数でない場合は０を返す。
def sosuu_hantei(candidated_number):
    for i in range(2, candidated_number):
        if candidated_number % i == 0 :
            #print("sosuu!!", candidated_number)
            return 0
    
    return 1
#max=合計の数の設定 process=途中経過をためておくバッファ　num_element=素数の要素数がこれ以上じゃないと認めない
def plus_until_max(max,process, num_element=0):
    total = 0
    #process = ""
    element = 0
    sosuu_count = 0
    for i in range(max):
        
        while i >= 0:
            element = int( (max-2)*random.random() ) + 2 ## 0と１を除く →2から59をランダムで生成する。
            if sosuu_hantei(element) == 1:　→素数判定を行う。　　自分で考えたほうの素数のリストを作ってからそこからランダムで選ぶ方が良い。
                sosuu_count += 1
                break
        
        process  += " " + str(element)  ##人間表示用
        total += element ##打ち切り用の変数に出てきた素数を足す
        
        if total > max: ##計算打ち切り処理
            return 0

        if total == max:
            #print(process)
            global tmp_data
            tmp_data = process
            return 1
        



#for i in range(8000):
#    element = int(100*random.random())+1
#    if sosuu_hantei(element) == 1:
#        print(element)

result_set = set()
result_list = list()
tmp_data = ""
sikou_kaisuu = 500000
target_number = 300
sosuu_no_kazu = 10

for p in range( sikou_kaisuu ):
    tmp_data = ""
    if plus_until_max(target_number, tmp_data, sosuu_no_kazu) == 1: 
       result_set.add(tmp_data)
       result = tmp_data in result_list ##すでに、result_listの中に組み合わせがある場合は足さない。
       if result == False:
            result_list.append(tmp_data)

##ソートし直し
result_list.sort(key=lambda x: len(x))
print(result_list)

for index, value in enumerate(result_list):
    print(index, value)
#for item in result_set:
#    print(item)

    
    
"""




    
    
