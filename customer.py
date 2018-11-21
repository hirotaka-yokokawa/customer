class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def user_age(self):
        return f"{self.age}"

    def entry_fee(self):
        if 75 <= self.age:
            return 500
        if 3 >= self.age:
            return "free"
        if 20 > self.age:
            return 1000
        if 20 <= self.age < 65:  # Pychamが綺麗にしてくれた｡神
            return 1500
        if 65 <= self.age:
            return 1200


    def info_csv(self):
        print(self.full_name(), self.user_age(),self.entry_fee(), sep='|')


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.info_csv()

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    tom.info_csv()

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.info_csv()

    yokokawa = Customer(first_name="Hirotaka", family_name="Yokokawa", age=2)
    yokokawa.info_csv()

    sugano = Customer(first_name="Keita", family_name="Sugano", age=75)
    sugano.info_csv()

