print("welcome to love calculator!")
name1=input("what is your name?")
name2= input("what is your name?")
combined_string = name1+name2
lower_case_string = combined_string.lower()
t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")
true = t+r+u+e
l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")
s = lower_case_string.count("s")
loves=l+o+v+e+s
love_score=int(str(true)+str(loves))
if (love_score <10) or (love_score>90):
    print(f"your love score is {love_score}, you go together like coke and mentos!")
elif (love_score>=40) and (love_score<=50):
    print(f"your score is {love_score}, you are allright together")
elif love_score >50 or love_score >=70:
    print(f"your love score is {love_score},thats a great number to be together")
else:
    print(f"your score is {love_score},find another")

