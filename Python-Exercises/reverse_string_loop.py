phrase = str(input("saisir un string :"))
phrase_inv = []
for i in phrase : 
    phrase_inv.insert(0,i)
print(phrase , "-----",end=" ")
for j in phrase_inv : 
    print(j,end="")
