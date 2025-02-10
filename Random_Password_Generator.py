import random
import string

def generate_pw():
    # store users choice of characters to include
    password_length = int(input("Enter password length: ").strip())
    include_special_characters = input("Include Special Characters: Y/N: ").lower().strip()
    include_upper_case = input("Include Upper Case: Y/N: ").lower().strip()
    include_digits = input("Include Digits: Y/N: ").lower().strip()
    
    # Password is requried to be greater than 4
    if password_length < 4:
        print('Password needs more than 4 characters')
        return
    # Ternary operator to store characters in variable if user input is yes otherwise store blank
    lower_case = string.ascii_lowercase
    special_characters = string.punctuation if include_special_characters == "y" else ""
    upper_case = string.ascii_uppercase if include_upper_case == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    
    # Concatenate the selected characters
    all_characters = lower_case + special_characters + upper_case + digits
    
    # Create a blank character list
    character_list = []
    
    # If statement checking if a character choice is included and choose 1 random char from the string and append in list.
    if include_special_characters == 'y':
        character_list.append(random.choice(special_characters))
    if include_upper_case == 'y':
        character_list.append(random.choice(upper_case))
    if include_digits == 'y':
        character_list.append(random.choice(digits))
    
    # Calculate the remaining characters to satisfy password lenght requirement
    remaining_length = password_length - len(character_list)
    
    # Convert character list to string
    password = character_list
    
    # loop through the remaining length and choose random characters from the selected character choices
    for x in range(remaining_length):
        character = random.choice(all_characters)
        # Append the mandatory characters and the remaining characters together
        password.append(character)
    
    # Shuffle the characters
    random.shuffle(password)
    # Join the list to a string
    string_pw = ''.join(password)
    # Print the final password
    print(string_pw)
    
generate_pw()
      
        
        





