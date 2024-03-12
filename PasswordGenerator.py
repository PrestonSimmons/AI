#Programmer: Preston Simmons
#Date: 3.12.2024
#Program: Password Generator
#Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os

def generate_salt():
    # Generate a random salt
    return os.urandom(16)

def hash_password(password, salt):
    # Hash the password with the salt using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode() + salt).hexdigest()
    return hashed_password

def main():
    # Accept password input from the user
    password = input("Enter your password: ")

    # Generate a random salt
    salt = generate_salt()

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
