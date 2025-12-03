class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        print("меня зовут:", self.first_name)
        print("моя фамилия:", self.last_name)
        print("полное имя:", self.full_name)
