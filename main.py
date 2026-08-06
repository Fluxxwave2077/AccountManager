"""
Функция guest_menu выводит меню роли
гость пользователю и предлагает ввести
опцию из меню
"""
def guest_menu ():
    print("""
=== GUEST MENU ===
1. Register
2. Login
0. Exit
""")
    return int(input("Select an option: "))


"""
Функция user_menu выводит меню роли 
юзер пользователю и предлагает ввести 
опцию из меню. список опций другой
"""
def user_menu ():
    print("""
=== USER MENU ===
1. Show profile
2. Change password
0. Logout
""")
    return int(input("Select an option: "))


"""
Функция admin_menu выводит меню роли 
админ пользователю и предлагает ввести 
опцию из меню. список опций расширен и доступ 
имеет только админ
"""
def admin_menu ():
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
    return int(input("Select an option: "))


"""
Функция handle_guest_choice вызывает 
определенную функцию при выборе опции иначе выдает ошибку
"""
def handle_guest_choice(choice):
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 0:
        exit()
    else:
        print("Invalid option")