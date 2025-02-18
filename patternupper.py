num=int(input("enter number of rows"))
for i in range(num,0,-1):
    for i in range(0,num-i):
        print("*",end=" ")
    for j in range(0,i+1):
        print(end=" ")
    print()