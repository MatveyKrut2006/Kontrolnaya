№8
class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating if 1 <= rating <= 100 else 1
        self.age = age

    def change_rating(self, value):
        new_rating = self.rating + value
        if new_rating < 1:
            value = 1 - self.rating
            self.rating = 1
        elif new_rating > 100:
            value = 100 - self.rating
            self.rating = 100
        else:
            self.rating = new_rating

        if value > 0:
            self.age -= abs(value) // 10
            if self.age < 18:
                self.age = 18
        elif value < 0:
            self.age += abs(value) // 10

    def __add__(self, string):
        self.rating += len(string)
        self.age -= len(string) // 10
        if self.age < 18:
            self.age = 18
        return self

    def __call__(self, num):
        return (num - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with rating {self.rating} looks {self.age} years old"
