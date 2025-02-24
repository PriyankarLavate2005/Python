lower=int(input("enter starting number"))
higher=int(input("enter highest number"))
for i in range(lower,higher+1):
    for j in range(2,11):
        if i%j==0:
            print(i,"is not prime")
        else:
            print(i,"is prime")