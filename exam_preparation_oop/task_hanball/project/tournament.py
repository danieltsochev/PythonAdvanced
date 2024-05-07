from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for character in value:
            if not character.isalnum():
                raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        new_eq = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(new_eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        eq = next(eq for eq in reversed(self.equipment) if eq.__class__.__name__ == equipment_type)
        team = next(t for t in self.teams if t.name == team_name)
        if eq.price > team.budget:
            raise Exception("Budget is not enough!")
        self.equipment.remove(eq)
        team.equipment.append(eq)
        team.budget -= eq.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        count = 0
        eq_for_discount = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        for eq in eq_for_discount:
            eq.increase_price()
            count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1, team_name2):
        team1 = next(t for t in self.teams if t.name == team_name1)
        team2 = next(t for t in self.teams if t.name == team_name2)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        t_1_points = sum([eq.protection for eq in team1.equipment]) + team1.advantage
        t_2_points = sum([eq.protection for eq in team2.equipment]) + team2.advantage
        if t_1_points > t_2_points:
            winner = team1
            team1.win()
        elif t_2_points > t_1_points:
            winner = team2
            team2.win()
        else:
            return "No winner in this game."
        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_info = sorted(self.teams, key=lambda x: -x.wins)
        result = []
        result.append(f"Tournament: {self.name}")
        result.append(f"Number of Teams: {len(self.teams)}")
        result.append(f"Teams:")
        for team in sorted_info:
            result.append(team.get_statistics())
        return "\n".join(result)




