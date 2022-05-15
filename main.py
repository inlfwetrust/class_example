class User:
    id = 1

    def __init__(self, name, age, sex, strength=10):
        self.name = name
        self.age = age
        self.sex = sex
        self.strength = strength
        self.id = User.id
        User.id += 1


user_bob = User('Bob', 32, 'male')
user_maria = User('Mari', 66, 'Female', 25)
user_jack = User('Jack', 23, 'Female', 1)


print(user_bob.id)
print(user_maria.id)
print(user_jack.id)

