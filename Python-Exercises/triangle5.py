# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2
# 1
n_lignes = int(input("saisir nombre de lignes :"))
cnt  = 0 
for row in range(1,n_lignes+1):
    k = 1
    for col in range(n_lignes-cnt):
        print(k,end="")
        k+=1
    cnt+=1
    print(" ")
