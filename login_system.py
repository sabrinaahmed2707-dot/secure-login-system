import hashlib

users = {}
attempts = 3

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed = hash_password(password)
    users[username] = hashed
    
    print("User registered successfully!\n")

def login():
    global attempts
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed = hash_password(password)
    
    if username in users and users[username] == hashed:
        print("Login successful!\n")
        attempts = 3
    else:
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
