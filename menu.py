"""
Функция guest_menu выводит меню роли
гость пользователю и предлагает ввести
опцию из меню
"""
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



"""
Функция user_menu выводит меню роли 
юзер пользователю и предлагает ввести 
опцию из меню. список опций другой
"""
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



"""
Функция admin_menu выводит меню роли 
админ пользователю и предлагает ввести 
опцию из меню. список опций расширен и доступ 
имеет только админ
"""
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