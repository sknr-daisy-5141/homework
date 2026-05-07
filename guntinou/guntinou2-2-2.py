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
            print(sum_list[i])
            break

#print(sum_list)





    
    
