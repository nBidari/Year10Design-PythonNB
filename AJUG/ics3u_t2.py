name = input("What's your name? ")
print("Nice to meet you " + name + "!")
year = input("What year were you born? ")
age = 2019 - int(year)
# print("You are " + str(age) + " years old, " + name + "!")
print(f"You are {str(age)} years old, {str(name)}!")

