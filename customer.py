# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken.full_name()  # "Ken Tanaka" という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford").full_name()
# tom.full_name()  # "Tom Ford" という値を返す

class Customer:
    def __init__(self,first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def display_profile(self):
        print(f"{self.first_name} {self.family_nameR}")


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka")
    ken.display_profile()

    tom = Customer(first_name="Tom", family_name="Ford")
    tom.display_profile()
