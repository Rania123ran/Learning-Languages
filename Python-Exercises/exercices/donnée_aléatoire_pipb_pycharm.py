from faker import Faker
fake = Faker("fr_FR")
for i in range(0,2):
    print("nom:",fake.first_name())
    print("prénom:",fake.last_name())
    print("ville:",fake.city())
    print("adresse:", fake.address())
    print("adresse mail:",fake.email())
    print("couleur :",fake.color_name())
    print("emploi :",fake.job())
    print("date de naissance:",fake.date_of_birth())
    print("-----")
