n_lignes = int(input("saisir le nombre de lignes :"))
for row in range(1,n_lignes+1):
    for col in range(1,2*n_lignes):
        if (row + col == n_lignes + 1) or (col-row == n_lignes -1) or (row == n_lignes):
            print("* ",end="")
        else : 
            print(end="  ")
    print()
