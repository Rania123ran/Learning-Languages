# 5 5 5 5 5
# 4 4 4 4 
# 3 3 3
# 2 2
# 1
n = n_lignes = int(input("saisir nombre de lignes :"))
for row in range(n_lignes):
    for col in range(n_lignes-row):
        print(n,end=" ")
    n-=1
    print("")
        