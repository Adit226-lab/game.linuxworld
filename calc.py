x=int(input("enter a number\n"))
y=int(input("enter a number\n"))
op=input("enter operator(+,-,/,*)")
if op=="+":
    print("sum is",x+y)
elif op=="*":
    print("multiplication is", x*y)
elif op=="-":
    print("substration is", x-y) 
else:
    print("divison is", x/y)  