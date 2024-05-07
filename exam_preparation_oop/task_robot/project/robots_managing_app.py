from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in self.VALID_SERVICES:
            raise Exception('Invalid service type!')
        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception('Invalid robot type!')
        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name, service_name):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [c for c in self.services if c.name == service_name][0]
        if (robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'SecondaryService') or (
                robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'MainService'
        ):
            return 'Unsuitable service.'
        if service.capacity == len(service.robots):
            raise Exception('Not enough capacity for this robot!')
        self.robots.remove(robot)
        service.robots.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name, service_name):
        service = [c for c in self.services if c.name == service_name][0]
        try:
            r_needed = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception('No such robot in this service!')
        service.robots.remove(r_needed)
        self.robots.append(r_needed)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name):
        number_of_robots_fed = 0
        service = [c for c in self.services if c.name == service_name][0]
        if service.robots:
            for r in service.robots:
                r.eating()
                number_of_robots_fed += 1
        return f'Robots fed: {number_of_robots_fed}.'

    def service_price(self, service_name):
        service = [c for c in self.services if c.name == service_name][0]
        total_price = sum([r.price for r in service.robots])
        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self):
        services = [c for c in self.services]
        result = []
        if services:
            for s in services:
                result.append(f'{s.details()}')
        return '\n'.join(result)

