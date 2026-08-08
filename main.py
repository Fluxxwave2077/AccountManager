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



current_user = None

"""
Функция handle_guest_choice вызывает 
определенную функцию при выборе опции иначе выдает ошибку
"""
def handle_guest_choice(choice):
    global current_user

    if choice == 1:
        register()
    elif choice == 2:
        current_user = login()
    elif choice == 0:
        exit_app()
    else:
        print("Invalid option")




def handle_user_choice(choice):
    global current_user

    if choice == 1:
        show_profile(current_user)
    elif choice == 2:
        change_password(current_user)
    elif choice == 0:
        log_out()
        current_user = None
    else:
        print("Invalid option")




def handle_admin_choice(choice):
    global current_user

    if choice == 1:
        show_users()
    elif choice == 2:
        find_user()
    elif choice == 3:
        block_user()
    elif choice == 4:
        unblock_user()
    elif choice == 5:
        change_user_role()
    elif choice == 6:
        show_profile(current_user)
    elif choice == 0:
        log_out()
        current_user = None


def roles_pass():

    if current_user is None:
        choice = guest_menu()
        handle_guest_choice(choice)
    elif current_user["role"] == "user":
        choice = user_menu()
        handle_user_choice(choice)
    elif current_user["role"] == "admin":
        choice = admin_menu()
        handle_admin_choice(choice)
    else:
        print("Unknown role")

def main():
    while True:
        roles_pass()