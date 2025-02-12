import getpass
#data store -> list of dictionary
users = [{
    'username' : 'poudelshikshya',
    'password' : 'password',
},
{
    'username' : 'cixyapoudel',
    'password' : 'cixya123'
}]

#function for signup
def signup(username, password):
    #loop through users to find the username
    for user in users:
        if user['username'] == username:
            print(f"User with username {username} already exists!")
            return
        
    users.append({
        'username' : username,
        'password' : password
    })
    print("User registration success!")

#function for login
def login(username, password):
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print("Login Successful!") 
            else:
                print("Invalid Password!")

            return
    print("Username not registered!")    

if __name__ == '__main__':

    # username = 'poudelshikshya'
    # password = 'password'
    
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    signup(username, password)
    login(username, password)

# username = 'abc1'
# password = 'password'
# login(username, password)