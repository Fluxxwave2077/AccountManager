from handlers import handle_guest_choice, handle_user_choice, handle_admin_choice
from menu import guest_menu, user_menu, admin_menu

def roles_pass(current_user):

    if current_user is None:
        choice = guest_menu()
        current_user = handle_guest_choice(choice, current_user)
    elif current_user["role"] == "user":
        choice = user_menu()
        current_user = handle_user_choice(choice, current_user)
    elif current_user["role"] == "admin":
        choice = admin_menu()
        current_user = handle_admin_choice(choice, current_user)
    else:
        print("Unknown role")

    return current_user

def main():
    current_user = None
    while True:
        current_user = roles_pass(current_user)

main()