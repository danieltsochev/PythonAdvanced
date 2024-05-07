from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name):
        super().__init__(name, capacity=30)

    def details(self):
        result = [f'{self.name} Main Service:']
        robots = []
        if self.robots:
            for r in self.robots:
                robots.append(r.name)
        if robots:
            result.append(f'Robots: {" ".join(robots)}')
        else:
            result.append('Robots: none')
        return '\n'.join(result)




