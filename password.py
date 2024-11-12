import random
import string
n=int(input("Enter length:"))
print("Complexity levels available")
print(" 1: lowercase+uppercase \n 2: Letters and digits.\n 3: Letters, digits, and special characters.")
c=int(input("Enter complexity level:"))
if c == 1:
    characters = string.ascii_letters  
elif c == 2:
    characters = string.ascii_letters + string.digits  
elif c == 3:
    characters = string.ascii_letters + string.digits + string.punctuation  
else:
    print("Invalid complexity level. Please choose between 1 and 3.")
    characters = ""
password = ""
if characters!="":
    for i in range(0,n,+1):
        index = int(random.random() * len(characters))
        password += characters[index]  
    print("Generated Password:", password)

