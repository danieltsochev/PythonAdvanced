from abc import ABC, abstractmethod


class BaseDiver(ABC):

    def __init__(self, name, oxygen_level):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Diver name cannot be null or empty!')
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError('Cannot create diver with negative oxygen level!')
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish):
        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            self.competition_points += round(fish.points, 1)
            self.catch.append(fish)
        else:
            self.oxygen_level = 0

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f'{self.__class__.__name__}: [Name: {self.name},' \
               f' Oxygen level left: {self.oxygen_level},' \
               f' Fish caught: {len(self.catch)}, ' \
               f'Points earned: {self.competition_points:.1f}]'


