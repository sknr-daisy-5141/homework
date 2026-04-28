#1000までの素数を出力する。
n=1000
sosuu_list=[]

for i in range(2,n+1):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if count==1:
        #print(i)
        sosuu_list.append(i)
        
print(sosuu_list)


"""
#課題2-1
#1000までの素数を出力するプログラムを作成せよ
#エラトステネスの篩は後半の課題で出るので使わずに


#sosuu_hantei()関数、引数が素数である場合1を返す。引数が素数でない場合は０を返す。
def sosuu_hantei(candidated_number):
    for i in range(2, candidated_number):
        if candidated_number % i == 0 :
            #print("sosuuではない!!", candidated_number)
            return 0
    
    return 1
#max=合計の数の設定 process=途中経過をためておくバッファ　num_element=素数の要素数がこれ以上じゃないと認めない


p = 0
for p in range(2, 1000):
    if sosuu_hantei(p) == 1:
        print(p)

"""



    
    
