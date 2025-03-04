n=int(input("enter Number of rows"))
for i in range(0,n+1):
    for j in range(0,n+1):
        if i==j:
            print("*",end="")
        else:
            print(end="")
    print()
    