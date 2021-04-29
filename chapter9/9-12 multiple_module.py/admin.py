from user import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, age, birthday):
        super().__init__(first_name, last_name, age, birthday)
        self.privileges = Privileges()