from abc import ABC, abstractmethod


class BaseClient(ABC):
    VALID_TYPES = ["Regular", "VIP"]

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in BaseClient.VALID_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount):
        pass

    def apply_discount(self):

        if self.points >= 100:
            discount = 10
            self.points -= 100
        elif 50 <= self.points <= 99:
            discount = 5
            self.points -= 50
        else:
            discount = 0
        result = (discount, self.points)
        return result














