op = str(input("Enter an operator (+ - * /) : "))
while( op not in ["+","-","*","/"]):
    op = str(input("Enter an operator  (+ - * /) : "))
num1 = float(input("Enter the 1st numbre : "))
num2 = float(input("Enter the 2nd numbre : "))
print("resultat : ",end="")
if op == "+" : 
    print(round(num1 + num2,2) )
elif op == "-" :
    print(round(num1 - num2,2))
elif op == "*" : 
    print(round(num2 * num1,2))
else : 
    if num2 == 0 :
        print("la division par 0 est imposible !")
    else : 
        print(round(num1/num2,2))




