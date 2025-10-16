lower = int(input("enter the lower interval :"))
while lower<1 : 
    print("only positif number greater  than 1 !")
    lower = int(input("enter the lower interval :"))
upper = int(input("enter the upper interval :"))
list1_num = []
while lower<1 : 
    print("only positif number greater  than 1 !")
    upper = int(input("enter the upper interval :"))
for num in range(lower,upper+1):
    cnt = 0
    for div in range(2,num):
        if num % div == 0 :
            cnt += 1
            break
        else : 
            continue
    if cnt == 0 :
        list1_num.append(num) 
if len(list1_num)== 0 :
    print("there is no prime number in [",lower,",",upper,"]")
else : 
    print("Prime Numbers :")
    for i in list1_num : 
        print(i,end=" , ")
    

            
        
         
