a=eval(input(" enter yaer :"))

if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Leap year")
        else:
            print("Not a leap Year")
    else:
        print(a," a leap Year")
else:
    print(a,"Not a Leap Year")
        
