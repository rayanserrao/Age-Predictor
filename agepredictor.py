age=input('Enter your age or year of birth')
age1=int(age)
present_age=age1
if age1>2020:
    print('Your not born yet')
    exit()

elif len(age)<=3:

    ageyear=100-age1
    year=2020+ageyear
    if age1>100:
        print("You are the oldest person alive")
    else:
        ageyear=100-age1
        year=2020+ageyear
        
        print(f"You will become 100 years old after {ageyear} years in {year}")

elif len(age)>3:
    ageyear1=2020-age1
    present_age=ageyear1
    ageyear=100-ageyear1
    year=2020+ageyear
    if ageyear1>100:
        print("You are the oldest person alive")
    else:


        ageyear=100-ageyear1
        year=2020+ageyear
        
        print(f"You will become 100 years old after {ageyear} years in {year}")

print("you wish to continue or quit, press c for continue and q for quit")
user_choice=input()
while(user_choice=='c' or user_choice=='q'):
    if user_choice=='q':
        exit()
    else:
        print('Enter a future year in which you want to see your age')
        user_input_year=int(input())
        ageyear1=user_input_year-2020
        ageyear2=present_age+ageyear1
        print(f"You will become {ageyear2} years old in {user_input_year}")
        break


