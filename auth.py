import bcrypt

from users import create_user, users, save_users


def register():
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    for user in users:
        if username == users[user]["username"]:
            print("Username Already Exists")
            return None

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
         bcrypt.gensalt()
    ).decode("utf-8")

    user_id = create_user(username,password_hash)
    print("User Created Successfully", user_id)
    return user_id


def login():
    username = input("Enter your Username: ")

    user = None

    for user_id in users:
        if username == users[user_id]["username"]:
            user = users[user_id]

    if user is None:
        print("User Not Found")
        return None

    password = input("Enter your Password: ")

    if bcrypt.checkpw(
        password.encode("utf-8"),
        user["password_hash"].encode("utf-8")
    ):
        if user["blocked"]:
            print("\n=== STATUS ===\nBlocked User")
            return None
        else:
            print("User Logged In Successfully")
            return user
    else:
        print("Password Incorrect")
        return None



def change_password(current_user):
    old_password = input("\nEnter your Old Password: ")
    if bcrypt.checkpw(
            old_password.encode("utf-8"),
            current_user["password_hash"].encode("utf-8")
    ):
        new_password = bcrypt.hashpw(
            input("New Password:").encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        current_user["password_hash"] = new_password
        save_users()
        print("Password Changed Successfully")
    else:
        print("Incorrect Old Password!!!")


