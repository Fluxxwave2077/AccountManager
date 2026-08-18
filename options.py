from users import users, save_users

def exit_app():
    exit()


def log_out():
    print("Logged out")
    return None


def show_profile(current_user):
    print(f"=== PROFILE ===\nUsername: {current_user['username']},\nRole: {current_user['role']}")


def show_users():
    for user_id in users:
        print(
            f"{user_id}: {users[user_id]['username']} | "
            f"Role: {users[user_id]['role']} | " 
            f"Blocked: {users[user_id]['blocked']}"
        )


def find_user():
    username = input("Enter username to find user: ")
    for user_id in users:
        if users[user_id]['username'] == username:
            print(
            f"{user_id}: {users[user_id]['username']} | "
            f"Role: {users[user_id]['role']} | " 
            f"Blocked: {users[user_id]['blocked']}"
        )
            found = True
            user_actions(users[user_id])

    if not found:
        print("Username not found!!!")


def user_actions(user):
    print("""
1. Block/Unblock user
0. Back
""")

    choice = int(input("Select an option: "))

    if choice == 1:
        set_block_status(user)
    elif choice == 0:
        return
    else:
        print("Invalid option")


def set_block_status(user):
    if user['blocked']:
        user['blocked'] = False
        print("User has been unblocked")
    else:
        user['blocked'] = True
        print("User has been blocked")

    save_users()

