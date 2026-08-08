
def login():
    username = input("Enter your Username: ")
    user = users.get(username)

    if user is None:
        print("User not found")
        return None

    password = input("Enter your Password: ")

    if password == user["password_hash"]:
        print("Login Successful")
        return user
    else:
        print("Wrong Password")
        return None
