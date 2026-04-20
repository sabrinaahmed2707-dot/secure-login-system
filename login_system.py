import hashlib

users = {}
attempts = 3

import os

def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt, hashed

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
   salt, hashed = hash_password(password)
   users[username] = (salt, hashed)
    
    print("User registered successfully!\n")

def login():
    global attempts
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users:
        salt, stored_hash = users[username]
        new_hash = hashlib.sha256(salt + password.encode()).hexdigest()
        
        if new_hash == stored_hash:
            print("Login successful!\n")
            attempts = 3
            return
    
    attempts -= 1
    print(f"Invalid credentials! Attempts left: {attempts}\n")
    
    if attempts == 0:
        print("Too many failed attempts. Access temporarily blocked.\n")
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option\n")

main()
