#自分でやった奴はデータ消えた。　wordに一応残ってる。
#0-9の数字をランダムに出力し、それが小さい順に0,1,2,3,4,5,6,7となるまで終わらないプログラム
#を作り、その試行回数調べよ


import random
import sys

sys.setrecursionlimit(200000000)
target_number = 6

suuji_list = list()
owari = 0
sikou_kaisuu = 0

def check_list(slist):
    for i in range(target_number):
        if slist[i] != i:#iに当てはまらないとき0を返す。→当てはまるときowariに１が代入されてwhileから出る。
            return 0
    
    return 1



while  owari == 0:
    suuji_list.clear()
    for i in range(target_number):
        garagara = int( 10*random.random() )    #0-9の数字をtarget_number個生成しリストに保存
        suuji_list.append(garagara)
        
    sikou_kaisuu += 1
    print(suuji_list)
    owari = check_list(suuji_list)
    

print(suuji_list, sikou_kaisuu)

