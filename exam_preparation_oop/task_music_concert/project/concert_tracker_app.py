from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIAN_TYPES = {'Guitarist': Guitarist, 'Drummer': Drummer, 'Singer': Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')
        for m in self.musicians:
            if m.name == name:
                raise Exception(f'{name} is already a musician!')
        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name):
        for b in self.bands:
            if b.name == name:
                raise Exception(f'{name} band is already created!')
        new_band = Band(name)
        self.bands.append(new_band)
        return f'{name} was created.'

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for c in self.concerts:
            if c.place == place:
                raise Exception(f'{place} is already registered for {c.genre} concert!')
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name, band_name):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name, band_name):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        musician_in_band = next((m for m in band.members if m.name == musician_name), None)
        if musician_in_band is None:
            raise ValueError(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician_in_band)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        singer = True
        drummer = True
        guitarist = True
        band = [b for b in self.bands if b.name == band_name][0]
        for msc in band.members:
            if msc.__class__.__name__ == 'Singer':
                singer = False
            if msc.__class__.__name__ == 'Drummer':
                drummer = False
            if msc.__class__.__name__ == 'Guitarist':
                guitarist = False
        if singer or drummer or guitarist:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        concert = [c for c in self.concerts if c.place == concert_place][0]
        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."










