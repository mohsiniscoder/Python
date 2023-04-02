import random
print("-----------------------------------")
print("Welcome to super password provider")
print("-----------------------------------")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h,', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','R','S','T', 'U','X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['@','_','%','&','#','<','>','(','|',')']
length_of_password =input("Enter the length of your password?=")
num_of_alphabets = int(input("Enter the number of alphabets you want to use for your password:"))
num_of_numbers = int(input("Enter the number of numbers you want to use for your password:"))
number_of_special_characters = int(input("Enter the number of characters you want to use for your password:"))
random_alphabets = ''
random_numbers =''
random_characters = ''
while num_of_alphabets > 0:
    idx = random.randint(0,len(alphabets)-1)
    random_alphabets += alphabets[idx]
    num_of_alphabets -=1
while num_of_numbers > 0:
    idx = random.randint(0,len(numbers)-1)
    random_numbers += numbers[idx]
    num_of_numbers -=1
while number_of_special_characters > 0:
    idx = random.randint(0,len(special_characters)-1)
    random_characters += special_characters[idx]
    number_of_special_characters -=1
password_simple = random_alphabets+random_numbers+random_characters
password = ''
length_of_password = int(length_of_password)
while length_of_password > 0:  
    idx = random.randint(0,len(password_simple)-1)
    password+=password_simple[idx]
    length_of_password -= 1
print(f"Your Password is {password} ")