# Lets make a password generator

import  random
print("Radhe radhe!")
print("Passwordarator at  your service!")
print("Numerical-1")
print("Alphabatical-2")
print("Alphanumeric-3")
passy=int(input("What type of password you want?:"))

length=int(input("Enter thee length  of  the  password you  want:"))

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9','0']
aphnum=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             '0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','0']

x=""
if passy==1: 
    for i in range(0,length):
        x +=random.choice(num)
    print(x,end="")

elif passy==2:
    for i in range(0,length):
        x +=random.choice(alpha)
    print(x,end="")

elif passy==3:
    for i in range(0,length):
        x +=random.choice(aphnum)
    print(x,end="")

else:
    print("Ohooo! Invalid choice!")

with open ("passes.txt","a+") as f:
    f.seek(0)
    f.write(x)
    f.write("\n")