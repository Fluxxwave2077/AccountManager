def guest_menu():
    while True:
        print("""
=== GUEST MENU ===
1. Register
2. Login
0. Exit
""")
        try:
            return int(input("Select an option: "))
        except ValueError:
            print("Invalid option")


def user_menu():
    while True:
        print("""
=== USER MENU ===
1. Show profile
2. Change password
0. Log out
""")
        try:
            return int(input("Select an option: "))
        except ValueError:
            print("Invalid option")


def admin_menu():
    while True:
        print("""
=== ADMIN MENU ===
1. Show all users
2. Find user
3. Block user
4. Unblock user
5. Change user role
6. Show profile
0. Logout
""")
        try:
            return int(input("Select an option: "))
        except ValueError:
            print("Invalid option")