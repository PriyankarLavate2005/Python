n=input("enter some string:")
length=len(n)
for row in range(0,length):
    for col in range(0,row+1):
        print(n[col],end="")
    print()