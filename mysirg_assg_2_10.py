hindi=eval(input("enter hindi marks"))

english=eval(input("enter english marks"))

math=eval(input("enter math marks"))

bio=eval(input("enter bio marks"))

drawing=eval(input("enter drawing marks"))

total=hindi+english+math+bio+drawing

print("Total Marks : ",total)

if total>300:
    print("Pass")
else:
    print("Fail")
