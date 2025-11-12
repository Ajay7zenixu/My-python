x=int(input("enter number : "))
a,b = 0,1
for i in range(x):
  print(a,end=" ")
  a,b=b,a+b
