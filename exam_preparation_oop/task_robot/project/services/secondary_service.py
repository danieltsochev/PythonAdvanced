from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name):
        super().__init__(name, capacity=15)

    def details(self):
        result = [f'{self.name} Secondary Service:']
        robots = []
        if self.robots:
            for r in self.robots:
                robots.append(r.name)
        if robots:
            result.append(f'Robots: {" ".join(robots)}')
        else:
            result.append('Robots: none')
        return '\n'.join(result)


