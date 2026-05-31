import hashlib

class LoginSystem:
    def __init__(self):
        self.users = {}

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            print("Error: Username already exists.")
            return False
        self.users[username] = self._hash_password(password)
        print("Registration successful!")
        return True

    def login(self, username, password):
        hashed = self._hash_password(password)
        if self.users.get(username) == hashed:
            print(f"Success: Welcome to the Student Management System, {username}!")
            return True
        print("Error: Invalid username or password.")
        return False

if __name__ == "__main__":
    system = LoginSystem()
    
    while True:
        print("\n--- SMS Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            user = input("Enter new username: ")
            pwd = input("Enter new password: ")
            system.register(user, pwd)
        elif choice == '2':
            user = input("Enter username: ")
            pwd = input("Enter password: ")
            system.login(user, pwd)
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")