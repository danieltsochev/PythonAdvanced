from project.sports_car import SportsCar
from project.car import Car

sc = SportsCar()
c = Car()
print(c.__class__.__bases__[0].__name__)