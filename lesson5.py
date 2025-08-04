class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated (private)

    def get_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

    def install_app(self, app_name):
        print(f"{app_name} installed on {self.model}")

class AndroidPhone(Smartphone):
    def install_app(self, app_name):
        print(f"Installing {app_name} from Google Play Store on {self.model} 📱")

class iPhone(Smartphone):
    def install_app(self, app_name):
        print(f"Installing {app_name} from App Store on {self.model} 🍎")

phone1 = AndroidPhone("Samsung", "Galaxy S22", 128)
phone2 = iPhone("Apple", "iPhone 14", 256)

print(phone1.get_info())
print(phone2.get_info())

phone1.install_app("WhatsApp")
phone2.install_app("Instagram")

class Vehicle:
    def move(self):
        print("The vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

