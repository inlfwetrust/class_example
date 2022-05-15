class User:
    def __init__(self, name, age, sex, strength=10):
        self.name = name
        self.age = age
        self.sex = sex
        self.strength = strength
        self.id = 0


user_bob = User('Bob', 32, 'male')
user_maria = User('Mari', 66, 'Female', 25)

print(user_bob.strength)
print(user_maria .id)

