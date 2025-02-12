#OOP

class User:
    def __init__(self):
        print("Object Created")
user1 = User()
user2 = User()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
user1 = User('shikshya' , '1234')
user2 = User('cixya', '2345')
print(user1.username)
print(user1.password)



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
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def greet(self):
        print(f"Hello, {self.__username}")

    def get_username(self):
        print(self.__username)

    def login(self):
        user = users.get(self.__username)
        if not user:
            print("User not registered! Please signup first.")
            return
        
        if user["password"] == self.__password :
            print("login success!")
        else:
            print("Invalid password!")

    def signup(self):
        pass

user1 = User('shikshyapoudel16' , 'password')
user2 = User('cixya.poudel', '123cixya')

# user1.greet()
# user2.greet()  
#user1.login()
# print(user1.username)
# user1.username = "shikshya"
# print(user1.__username)
#print(user1.username)

user1.login()



#Single Inheritance

class Account:
    def __init__(self, accnum, blc):
        self.accnum = accnum
        self.blc = blc

    def get_acc_details(self):
        print(f"Account number = {self.accnum} and Balance = {self.blc}")

class FixedDepositAccount(Account):
    def __init__(self, accnum, blc, interest):
        super().__init__(accnum, blc)
        self.interest = interest

fd = FixedDepositAccount('1232123', 1000,10)
fd.get_acc_details()


