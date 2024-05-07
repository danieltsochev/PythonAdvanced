from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch):
        used_oxy = round(time_to_catch * 0.3)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = 540

