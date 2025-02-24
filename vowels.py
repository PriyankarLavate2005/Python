sentence=input("enter the String ")
list1=["a","e","i","o","u"]
count=0
for i in sentence:
    if i in list1:
        count=count+1
print(count)