#100個のランダムな1-500の整数を小さい順にソートした数列を用意し、その数列に対し二分探索するプログラムを作成し、ある整数を発見する平均試行回数（平均計算量）を調べよ（5000回ぐらい回してみる）
#--小さな順にソートするのはライブラリを使っても良い
#--二分探索も外部サイトを参考にしてもよい。Webからソースコードを引用した場合はURLをコメントアウト
import random


def binary_search():
    yousosuu = 100
    max_seisuu = 500
    random_suuretu = random.sample(range(max_seisuu), k=yousosuu)#500までの整数から100個
    #l = range(500)
    #random_suuretu = random.sample(l, k=yousosuu)
    random.seed()
    target_number_of_binary_search = random_suuretu[ int( yousosuu*random.random() )] ##必ず見つかるパターン
    #target_number_of_binary_search =  int( random.random()*500 )#見つからないパターン
    random_suuretu.sort()#並び替える
    #print( len(random_suuretu), random_suuretu)
    
    #print( target_number_of_binary_search) 

    tansaku_kaisuu = 0
    left = 0 
    right = yousosuu
    while right >= left:
        tansaku_kaisuu += 1
        center = int( (left+right)/2 )
        if( center == yousosuu-1 ): #リストの終端の場合
            #print(target_number_of_binary_search,  "is not found list at last of right side ", tansaku_kaisuu) 
            return tansaku_kaisuu
        #print(center)
        
        if random_suuretu[center] == target_number_of_binary_search:
            #print(target_number_of_binary_search, "is found at",center)
            return tansaku_kaisuu
        
        if target_number_of_binary_search  >= random_suuretu[center]:
            left = center + 1
        else:
            right = center - 1
        #print(center)
       

    #print(target_number_of_binary_search,  "is not found", tansaku_kaisuu)
    return tansaku_kaisuu

sikou_kaisuu = 10
total = 0
for i in range(sikou_kaisuu):
    total += binary_search()

print(total/sikou_kaisuu)