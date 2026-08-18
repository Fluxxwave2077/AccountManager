import json

users = {
    "admin_1":{
        "username":"admin",
        "role":"admin",
        "password_hash":"",
        "blocked":False
    }
}


def load_users():
    with open("users.json", "r") as file:
        data = json.load(file)

    return data

users = load_users()

max_id = 0

for user_id in users:
    if user_id.startswith("user_"):
        user_number = int(user_id[5:])

        if user_number > max_id:
            max_id = user_number

next_user_id = max_id + 1


def create_user(username,password_hash):

    global next_user_id

    user_id = "user_" + str(next_user_id)
    users[user_id] = {
        "username": username,
        "password_hash": password_hash,
        "role": "user",
        "blocked": False
    }

    next_user_id += 1

    save_users()

    return user_id


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)