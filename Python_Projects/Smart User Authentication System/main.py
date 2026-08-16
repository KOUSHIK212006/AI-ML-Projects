import re

failed_attempts_tracker = {}
current_session = {"logged_in_user": None}


def validate_username(username: str) -> bool:
    pattern = r"^[A-Za-z]\w{4,14}$"
    return bool(re.match(pattern, username))


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def calculate_password_strength(password: str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1
    return score


def validate_password(password: str) -> bool:
    strength_score = calculate_password_strength(password)
    return strength_score == 5


def register_user(users: list) -> None:
    print("\n--- Registration ---")
    username = input("Username: ")
    
    for user in users:
        if user["username"].lower() == username.lower():
            print("Username already exists!")
            return

    if not validate_username(username):
        print("Invalid Username!")
        return

    email = input("Email: ")
    if not validate_email(email):
        print("Invalid Email format!")
        return

    password = input("Password: ")
    score = calculate_password_strength(password)
    
    if score <= 2:
        print("Strength: Weak")
    elif score <= 4:
        print("Strength: Medium")
    else:
        print("Strength: Strong")

    if not validate_password(password):
        print("Password too weak!")
        return

    new_user = {
        "username": username,
        "email": email,
        "password": password
    }
    users.append(new_user)
    print("User registered successfully!")


def login_user(users: list) -> None:
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if failed_attempts_tracker.get(username, 0) >= 3:
        print("Account temporarily locked. Maximum login attempts exceeded!")
        return

    target_user = None
    for user in users:
        if user["username"] == username:
            target_user = user
            break

    if target_user and target_user["password"] == password:
        current_session["logged_in_user"] = target_user
        failed_attempts_tracker[username] = 0
        print("Login successful! Welcome,", target_user["username"])
    else:
        current_failed = failed_attempts_tracker.get(username, 0) + 1
        failed_attempts_tracker[username] = current_failed
        
        remaining = 3 - current_failed
        if remaining > 0:
            print("Incorrect credentials.")
            print("Attempts remaining:", remaining)
        else:
            print("Incorrect credentials. Account temporarily locked.")


def change_password() -> None:
    user = current_session["logged_in_user"]
    if not user:
        print("Please log in first!")
        return

    print("\n--- Change Password ---")
    current_pass = input("Enter current password: ")
    
    if current_pass != user["password"]:
        print("Incorrect current password!")
        return

    new_pass = input("Enter new password: ")
    confirm_pass = input("Confirm new password: ")

    if new_pass != confirm_pass:
        print("Mismatch! New password and confirmation do not match.")
        return

    if not validate_password(new_pass):
        print("New password too weak!")
        return

    user["password"] = new_pass
    print("Password successfully updated!")


def view_profile() -> None:
    user = current_session["logged_in_user"]
    if not user:
        print("Action Denied. Please log in first!")
        return

    print("\n===== PROFILE =====")
    print("Username :", user["username"])
    print("Email    :", user["email"])
    print("Status   : Logged In")


def search_user(users: list) -> None:
    print("\n--- Search User ---")
    query = input("Enter target username to lookup: ").strip().lower()
    
    found = False
    for user in users:
        if user["username"].lower() == query:
            print("\nUser profile match verified!")
            print("Username :", user["username"])
            print("Email    :", user["email"])
            found = True
            break
            
    if not found:
        print("User not found.")


def main() -> None:
    users_database = []

    while True:
        print("\n===== AUTHENTICATION SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. View Profile")
        print("5. Search User")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            register_user(users_database)
        elif choice == "2":
            login_user(users_database)
        elif choice == "3":
            change_password()
        elif choice == "4":
            view_profile()
        elif choice == "5":
            search_user(users_database)
        elif choice == "6":
            current_session["logged_in_user"] = None
            print("\nExiting....")
            break
        else:
            print("Invalid menu choice. Please select fr6om options 1-6.")


main()
