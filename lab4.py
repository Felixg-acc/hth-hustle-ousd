#1
checking = "yes"
while checking == "yes":
    print("What is your age: ")
    user_input = input()
    if user_input.isdigit() == False:
        print("number only")
    elif int(user_input) >= 18:
        print("Yes you can vote")
    else:
        print("You cannot vote")
    print("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2



#2
numbers = [3, -521521, 0, 358071, -10, 16]

for number in numbers:
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")




#3
blocks = ["gravel", "dirt", "stone", "coal", "diamond"]

for block in blocks:
    if block == "diamond":
        print("jackpot!")
    else:
        print(block)