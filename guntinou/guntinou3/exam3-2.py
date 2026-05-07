#100個の整数をランダム生成（重複なし）で数列群(0,23,4,16,9…)を生成し、その数列群からある整数を線形探索するプログラムを作成し、
#ある整数を発見する平均試行回数（平均計算量）を調べよ（5000回ぐらい回してみる）

import random

def linear_search():
    random_suuretu = random.sample(range(100), k=100)#ランダムサンプルで並べられる。
    #print( len(random_suuretu), random_suuretu)
    random.seed()#完全なランダムにできる。
    target_number_of_linear_search = int( 100*random.random() )
    #print( target_number_of_linear_search) 

    for num in range(100):  
        #print(random_suuretu[num]) 
        if random_suuretu[num] == target_number_of_linear_search:
            #print(target_number_of_linear_search, "is found at",num)
            return num

    #print(target_number_of_linear_search,  "is not found")
    return 0

sikou_kaisuu = 5000
total = 0
for i in range(sikou_kaisuu):
    total += linear_search()

print(total/sikou_kaisuu)