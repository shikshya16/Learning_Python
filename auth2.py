import getpass

#users = [{}, {}]
users = {
    "Shikshyapoudel16" : {
        "username" : "shikshyapoudel16",
        "password" : "password"
    },
    "cixya.poudel" : {
        "username" : "cixya.poudel",
        "password" : "123cixya"
    }
}

def signup(username, password):
    user = users.get(username)
    if user:
        print("Username already exists!")
        return
    users[username] = {
        "username" : username,
        "password" : password
    }
    print("User registered successfully!")

def login(username, password):
    user = users.get(username)
    if not user:
        print("User not registered! Please signup first.")
        return
    
    if user["password"] == password :
        print("login success!")
    else:
        print("Invalid password!")

if __name__ == '__main__':
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    #signup(username, password)
    login(username, password)