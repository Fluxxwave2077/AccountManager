import bcrypt

from users import create_user, users


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
        print("User Logged In Successfully")
        return user
    else:
        print("Password Incorrect")
        return None
