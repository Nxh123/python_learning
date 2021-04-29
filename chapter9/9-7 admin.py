class User:
    def __init__(self, first_name, last_name, age, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday

    def describe_user(self):
        print(f'First Name:\t{self.first_name.title()}')
        print(f'Last Name:\t{self.last_name.title()}')
        print(f'Age:\t\t{self.age}')
        print(f'Birthday:\t{self.birthday}')

    def greet_user(self):
        print(
            f'Good morning,{self.first_name.title()} {self.last_name.title()}')


class Admin(User):
    def __init__(self, first_name, last_name, age, birthday):
        super().__init__(first_name, last_name, age, birthday)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


admin = Admin('xinhan', 'niu', 21, 'May 2nd')
admin.show_privileges()