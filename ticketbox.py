print("welcome to jfp rollarcoaster")
height = int(input("what is your height ?"))
bill=0
if height>= 120:

    print("YOU CAN RIDE!")
    age = int(input("what is your age ?"))
    if age<12:
        bill=5
        print("you have to pay 5$")

    elif age<=18:
        bill=7
        print("you have to pay 7$")
    else:
        bill=12
        print("you have to pay 12$")
        print("don't jump from the rollarcoaster!!!")
    photo=input("do you want to take photo while in rollarcoaster? Y or N")
    if photo=="Y"or"y":
        bill +=3
        print(f"your final bill is {bill}")

else:
    print("YOU CAN'T RIDE.(sorry)")

