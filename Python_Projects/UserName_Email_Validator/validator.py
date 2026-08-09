import re

username = input("Enter username: ")
email = input("Enter email: ")

# Username pattern
username_pattern = r"^[A-Za-z][A-Za-z0-9_]{4,14}$"

# Email pattern
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|in|org)$"

# Validate username
if re.fullmatch(username_pattern, username):
    print("Username: Valid")
else:
    print("Username: Invalid")

# Validate email
if re.fullmatch(email_pattern, email):
    print("Email: Valid")
else:
    print("Email: Invalid")
