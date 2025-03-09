import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
list = [letters,symbols,numbers]
print(list)
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy level
# password = ""
# for char in range(0,nr_letters):
#     password += random.choice_1(letters)
# for char2 in range(0,nr_symbols):
#     password += random.choice_1(symbols)
# for char3 in range(0,nr_numbers):
#     password += random.choice_1(numbers)
# print(password)
password_list = []
for char in range(0,nr_letters):
    password_list += random.choice(letters)
for char2 in range(0,nr_symbols):
    password_list += random.choice(symbols)
for char3 in range(0,nr_numbers):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = "".join(password_list)
print(password) 