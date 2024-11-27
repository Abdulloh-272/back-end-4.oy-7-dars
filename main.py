class MarsStudent:
    def __init__(self, id, password, coins):
        self.__id = id
        self.__password = password
        self.__coins = coins

    def get_id(self):
        return self.__id
    
    def get_password(self):
        return self.__password
    
    def get_coins(self):
        return self.__coins

    def set_id(self, id):
        self.__id = id
    
    def set_password(self, password):
        self.__password = password
    
    def set_coins(self, coins):
        self.__coins = coins

student = MarsStudent(12345, "mypassword", 100)

print(f"ID: {student.get_id()}")
print(f"Password: {student.get_password()}")
print(f"Coins: {student.get_coins()}")

student.set_id(67890)
student.set_password("newpassword")
student.set_coins(150)

print(f"Updated ID: {student.get_id()}")
print(f"Updated Password: {student.get_password()}")
print(f"Updated Coins: {student.get_coins()}")
