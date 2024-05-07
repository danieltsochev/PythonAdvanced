from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:

    VALID_DELICACIES = {"Gingerbread": Gingerbread,  "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth,  "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy, name, price):
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy = next((d for d in self.delicacies if d.name == name), None)
        if delicacy is None:
            new_delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
            self.delicacies.append(new_delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
        else:
            raise Exception(f"{name} already exists!")

    def add_booth(self, type_booth, booth_number, capacity):
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth is None:
            new_booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
            self.booths.append(new_booth)
            return f"Added booth number {booth_number} in the pastry shop."
        else:
            raise Exception(f"Booth number {booth_number} already exists!")

    def reserve_booth(self, number_of_people):
        first_booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)
        if first_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        first_booth.reserve(number_of_people)
        return f"Booth {first_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        price_from_orders = sum([food.price for food in booth.delicacy_orders])
        total_price = price_from_orders + booth.price_for_reservation
        self.income += total_price
        booth.price_for_reservation = 0
        booth.delicacy_orders = []
        booth.is_reserved = False
        return f"Booth {booth_number}:\nBill: {total_price:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."