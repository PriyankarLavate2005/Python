#program to find common factor
def gcd(m,n):
  fn=[]
  ln=[]
  cn=[]
  for i in range(1,m+1):
      if m%i==0:
        fn.append(i)
      
  for j in range(1,n+1):
      if n%j==0:
        ln.append(j)
  for f1 in fn:
    for l1 in ln:
      if l1==f1:
        cn.append(l1)
  print("values factor of first is",fn)
  print("values factor of second is",ln)
  print("common factor is",cn)
gcd(12,16)