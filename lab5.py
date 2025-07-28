#1
def cat_greeting(word):
    print(f'Cat says {word}')
    print( 'Cat says nothing')
cat_greeting ("meeeow")


#2
def generate_superhero_power () :
    name = "hassan's"
    power = "time stop"
    print(f"{name}'s power is {power}")
generate_superhero_power ()


#3
def generate_superhero_power1():
    power = "flying"
    return power
print(generate_superhero_power1())


#4
def generate_superhero_power2(user_name, super_power):
    return f"{user_name}'s power is {super_power}"
(generate_superhero_power2("hassan", "super laughing"))


#5
def cat_greetings_loop():
    for _ in range(5):
        print("Meeeow")
cat_greetings_loop()


#6
def generate_multiple_powers(powers):
    for power in powers:
        print(power)
generate_multiple_powers(["super speed", "super strength", "integrity"])