#Even/Odd and Positive/Negative Combined
#Even/Odd and Positive/Negative Combined
num=int(input("enter a number"))
if num>0:
  if num%2==0:
    print("positive and even ")
  else:
    print("positive and odd")
elif num<0:
  if num%2==0:
    print("even and negative")
  else: 
    print("odd and negative")
else: 
  print("not even or odd and not positive or negative ")
