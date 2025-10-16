# p
# p y 
# p y t 
# p y t h 
# p y t h o 
# p y t h o n 
l1 = ["p","y","t","h","o","n"]
n_lignes = int(input("nombres de lignes : "))
for row in range(n_lignes+1):
    index = 0 
    for col in range(row):
        print(l1[index],end=" ")
        index+=1
        if index == 6 : 
            index = 0 
    print(" ")
        

