#再帰処理　答え見ながら自分で考える。
target=8

def saikisyori(total,before,target,process):
    total+=before
    process  += " " + str(before)  
    
    
    if(total==target):
        print("end",process)
        return 0
    if(total>=target):
        print("八段以上",process)
        return 0
    if(before==1):
        saikisyori(total,1,target,process)
        saikisyori(total,2,target,process)
    if(before==2):
        saikisyori(total,1,target,process)
        
result="start"
#saikisyori(0,1,8,result)


#■課題1-3
#再帰処理で解く方法を実装せよ

num_of_method = 0
target_step  = 20  #目的の階段の段数

def kaidan(total_step, before_step, process):
   
   process  += " " + str(before_step)  
   total_step += before_step

   if total_step == target_step:
        global num_of_method
        num_of_method += 1
        print(process, "end")
        return 0
 
   if total_step >= target_step+1:
        print(process, "16dan damedayo")
        return 0
    
   if before_step == 1:
        kaidan(total_step, 1, process)
        kaidan(total_step, 2, process)
        
   if before_step == 2:
        kaidan(total_step, 1, process)

    
result ="start"
result2 ="start"

kaidan(0,1, result)
kaidan(0,2, result2)
print(num_of_method)



    
        
        
    