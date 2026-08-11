from auth import register, login, change_password
from options import log_out, exit_app, show_profile, show_users, find_user, set_block_status

"""
Функция handle_guest_choice вызывает 
определенную функцию при выборе опции иначе выдает ошибку
"""
def handle_guest_choice(choice, current_user):

    if choice == 1:
        register()
    elif choice == 2:
        return login()
    elif choice == 0:
        exit_app()
    else:
        print("Invalid option")

    return current_user


def handle_user_choice(choice, current_user):

    if choice == 1:
        show_profile(current_user)
    elif choice == 2:
        change_password(current_user)
    elif choice == 0:
        current_user = log_out()
    else:
        print("Invalid option")

    return current_user


def handle_admin_choice(choice, current_user):

    if choice == 1:
        show_users()
    elif choice == 2:
        find_user()
    elif choice == 3:
        show_profile(current_user)
    elif choice == 0:
        log_out()

    return current_user
