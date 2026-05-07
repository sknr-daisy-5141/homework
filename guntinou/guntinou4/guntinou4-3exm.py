import numpy as np
import random

current_row = 4 #頂点５から始める
foot_path = list()

def next_path():
    next_row = int(euler_circut_matrix.shape[1]*random.random() )
    
    global current_row
    global foot_path
    if euler_circut_matrix[current_row, next_row] == 1:
        euler_circut_matrix[current_row, next_row] = 0 #移動先の頂点へのパスを消す
        euler_circut_matrix[next_row, current_row] = 0 #移動した頂点から、移動前のパスも消す
        #print(next_row,euler_circut_matrix[next_row,:])
        foot_path.append(next_row+1)
        current_row = next_row
        #print("next vertex:", next_row+1, euler_circut_matrix[next_row,:])
        #print(current_row)
        print(foot_path)
        return 1
    
    
    return 0

euler_circut_matrix = np.array([ [0,1,0,0,0,1,0,0,0,0,0,0], [1,0,1,1,1,0,0,0,0,0,0,0], [0,1,0,0,0,0,1,0,0,0,0,0], [0,1,0,0,1,1,0,1,0,0,0,0], [0,1,0,1,0,0,1,1,1,0,0,0], [1,0,0,1,0,0,0,1,0,1,0,0], [0,0,1,0,1,0,0,0,1,0,0,1], [0,0,0,1,1,1,0,0,1,0,1,0], [0,0,0,0,1,0,1,1,0,0,1,0], [0,0,0,0,0,1,0,0,0,0,1,0], [0,0,0,0,0,0,0,1,1,1,0,1], [0,0,0,0,0,0,1,0,0,0,1,0] ])

foot_path.append(4+1)
#print(euler_circut_matrix) 

#start v5
print(euler_circut_matrix[4,:]) 

for i in range(100):
    next_path()
   
     #if next_path() == 1 :
        #print(euler_circut_matrix)

print("size=", len(foot_path), foot_path, )
#size=22じゃないとオイラー閉路ではない
if len(foot_path) != 22:
	print("Failed!! Please try again!!")
	print(euler_circut_matrix)

if len(foot_path) == 22:
	print("これはオイラー閉路だよ")
	print(euler_circut_matrix)
