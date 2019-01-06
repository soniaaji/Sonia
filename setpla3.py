N=int(input("Enter number: "))
rev=0
while(N>0):
    dig=N%10
    rev=rev*10+dig
    N=N//10
print("Reverse of the number:",rev)
