lower = int(input("enter the lower interval :"))
while lower<1 : 
    print("only positif number greater  than 1 !")
    lower = int(input("enter the lower interval :"))
upper = int(input("enter the upper interval :"))
while upper<1 : 
    print("only positif number greater  than 1 !")
    upper = int(input("enter the upper interval :"))
list_perfect = []
for n in range(lower,upper+1):
        sum = 0
        list_factors = []
        for i in range(1,n+1):
            if n%i == 0 :
                list_factors.append(i)
        if len(list_factors)!=0 :
            for i in list_factors :
                sum += i
            if sum == 2*n :
                list_perfect.append(n)
if len(list_perfect)!=0 :
     print("list des nombres parfait sont :",end="") 
     for i in list_perfect:
          print(i,end=" , ")    
else : 
     print("pas de nombres parfait dans l'interval [",lower,",",upper,"]")     



    

