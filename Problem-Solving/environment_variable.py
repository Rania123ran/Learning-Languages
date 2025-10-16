#how to access environment variable : 
import os 


fichiers = os.listdir("C:/Users/rania/Desktop/testing")  
chemin = os.path.abspath("test2.txt")
if os.path.exists("test2.txt"): 
    print("fichier existe ")
else : 
    print("fichier n'existe pas")
#os.mkdir("dossier")
#os.remove("fichier.txt")
os.system("dir")
print(fichiers)
print(chemin)
print(os.environ['PATH'])