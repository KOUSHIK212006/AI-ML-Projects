# Smart User Authentication System
A console-based Python application built to practice secure user registration and login workflows using regex validation, dictionaries, and functional programming.

## Features
* **Register**: Create an account with unique credentials validated by strict regex rules and a dynamic password strength meter.
* **Login**: Authenticate secure profile access with a security lock mechanism after three consecutive failed attempts.
* **Change Password**: Safely update a password matching strength requirements within an active session.
* **View Profile**: Check session connectivity status and account metadata without exposing sensitive credentials.
* **Search User**: Query system databases for user accounts with built-in case-insensitive lookup functionality.

## Visual Examples
```text
===== AUTHENTICATION SYSTEM =====
1. Register
2. Login
3. Change Password
4. View Profile
5. Search User
6. Exit

Enter your choice (1-6): 1

--- Registration ---
Username: Koushik_123
Email: koushik@gmail.com
Password: Hello@123
Strength: Strong
User registered successfully!
```

## How to Run
1. Make sure you have Python installed on your system.
2. Save the script as `main.py`.
3. Open your terminal and run:
   ```bash
   python main.py
   ```
4. Navigate through the security options using the numerical menu inputs (1-6).
