##Asking user what num they want to factor & num = input
print("What number do you want to factor?")
Num = int(input())
Factors = 0

##If input = 0 or 1 it can't be factored, else continue the program
if (Num == 0 or Num == 1):
    print(str(Num) + (" can't be factored you dumb dumb"))
else:
    print("Here are the factors of " + str(Num))

##Starting range @2 because I don't want one. If there is no remainder,x gets printed
for x in range(2,Num+1):
    if(Num%x == 0):
        print(x)
        Factors = Factors +1

##If the factor list only has one number it is prime
if (Factors == 1):
    print(str(Num) + " is a prime number")
