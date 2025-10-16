type = str(input("is this temperator in Celisius or Fahrenheit (C/F)  :"))
if type not in ["C","c","F","f"]:
    print(type," is an invalid unit of measurement ")
    type = str(input("is this temperator in Celisius or Fahrenheit (C/F)  :"))
num = int(input("Enter the temperature :"))
if type in ["F","f"]:
    F  = round((num -32) / 1.8,2)
    print("The temperator in Fahrenheit is : ",F,"°F")
elif type in ["C","c"]:
    C = round(num * 1.8 +32 ,2)
    print("The temperator in Celisius is : ",C,"°C")


