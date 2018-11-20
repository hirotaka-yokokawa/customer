class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def display_profile(self):
        return f"{self.first_name} {self.family_name}, {self.age}"

    def entry_fee(self):
        if 20 > self.age:
            return 1000
        if 20 <= self.age < 65:  # Pychamが綺麗にしてくれた｡神
            return 1500
        if 65 <= self.age:
            return 1200

    def info_csv(self):
        return self.display_profile(), self.entry_fee()


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    print(ken.info_csv())

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    print(tom.info_csv())

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    print(ieyasu.info_csv())
