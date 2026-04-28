import random
#足し算するとちょうど60になる組み合わせを作成する。
#60までの素数のリストを作成する。
n=60
sosuu_list=[]
sum_list=[]

#素数の判定
for i in range(2,n+1):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if count==1:
        sosuu_list.append(i)

#print(sosuu_list)
#round=int(input("繰り返す回数を入力する"))
round=10
for i in range(round):
    sum_list.append([])
    while(sum(sum_list[i])<=60):
        n=random.randint(1,len(sosuu_list)-1)
        #print(n)
        sum_list[i].append(sosuu_list[n])
    print(sum_list)





    
    
