email = list(input("Enter you email : "))
if "@" not in email : 
    print("il s'agit pas d'une adresse mail")
else : 
    print("your username is : ","".join(email[:email.index("@")])," and your domain name is : ","".join(email[email.index("@")+1:])) 