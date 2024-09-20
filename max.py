def max (x,y,z):
	maxim=x
	if y>maxim:
	  maxim=y
	if z>maxim:
	  maxim=z
	  return maxim    
    

print("------------------------------------")
x=int(input("Enter first integer\n"))
y=int(input("Enter second integer\n"))
z=int(input("Enter third  integer\n"))

print("The largest integer among the ones you entered is  number %d"% (max(x,y,z)))
