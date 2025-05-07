print("welcome to pizza deliveries")
size = input("what size you want to order? S,M,L")
add_pepperoni = input("do you want pepperoni?Y or N")
extra_cheese= input("do you want extra cheese?Y or N")
bill=0
if size=="S":
    bill+=15
    print("your pizza price is 15$")
elif size == "M":
       bill +=20
       print("your pizza price is 20$")
else:
    bill+=25

if add_pepperoni=="Y":
    if size =="S":
        bill +=2
    else:
        bill +=3

if extra_cheese =="Y":
 bill +=1

print(f"your total bill : {bill}")