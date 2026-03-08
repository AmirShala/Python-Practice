import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version
password = ""

for i in range(1,nr_letters + 1):
    password += random.choice(letters)

for i in range(1,nr_symbols + 1):
    password += random.choice(symbols)

for i in range(1,nr_numbers + 1):
    password += random.choice(numbers)

print(f"Easy Version password: {password}")


#Hard Version

# Converting our string to a list in order to be able to shuffle it
temp_list = list(password)
random.shuffle(temp_list)
# Converting the list back to a string
new_password = "".join(temp_list)
print(f"Hard Version password: {new_password}")