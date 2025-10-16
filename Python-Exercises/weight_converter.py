weight = float(input("enter your weight :"))
type = str(input("kilograms or pounds ? (K or L) :"))
while type not in ["K","L","k","l","Kilograms","Pounds"]:
    print(type," is not valid !")
    type = str(input("kilograms or pounds ? (K or L) :"))
if type in ["K","k","Kilograms"]:
    w = round(weight * 2.20462,2)
    unit = "Lbs"
elif type in ["L","l","Pounds"] :
    w = round(weight / 2.20462)    
    unit = "Kgs"
print("Your weight is :",w," ",unit)


