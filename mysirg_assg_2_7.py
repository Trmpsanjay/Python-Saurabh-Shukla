import math
a=float(input("Enter a,b and c"))
b=float(input())
c=float(input())

d=b*b-4*a*c
if d>=0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are ",r1,r2)
else:
    print("roots are imaginary")

