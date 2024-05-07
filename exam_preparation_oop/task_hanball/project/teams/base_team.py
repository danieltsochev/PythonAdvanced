from abc import ABC, abstractmethod


class BaseTeam(ABC):

    def __init__(self, name, country, advantage, budget):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value
        
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([eq.price for eq in self.equipment])
        try:
            avg_team_protection = sum([eq.protection for eq in self.equipment]) / len(self.equipment)
        except ZeroDivisionError:
            avg_team_protection = 0
        result = []
        result.append(f"Name: {self.name}")
        result.append(f"Country: {self.country}")
        result.append(f"Advantage: {self.advantage} points")
        result.append(f"Budget: {self.budget:.2f}EUR")
        result.append(f"Wins: {self.wins}")
        result.append(f"Total Equipment Price: {total_price_of_team_equipment:.2f}")
        result.append(f"Average Protection: {int(avg_team_protection)}")
        return "\n".join(result)
