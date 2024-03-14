#Programmer: Preston Simmons
#Date: 3.12.2024
#Program: Password Generator
#Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import getpass

# Prompt the user for a password without showing the input characters
password = getpass.getpass("Enter your password: ")

# You can then use the password variable however you need
print("Your password is:", password)
