from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
       self.player = TennisPlayer('Alex', 20, 50)

    def test_correct__init__(self):
        self.assertEqual('Alex', self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(50, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_when_wrong_value_error_less(self):
        expect = "Name should be more than 2 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'A'
        self.assertEqual(expect, str(ve.exception))

    def test_name_when_wrong_value_error_equal(self):
        expect = "Name should be more than 2 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'An'
        self.assertEqual(expect, str(ve.exception))

    def test_name_when_wrong_value_error_empty(self):
        expect = "Name should be more than 2 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.player.name = ''
        self.assertEqual(expect, str(ve.exception))

    def test_age_when_less_with_value_error(self):
        expect = "Players must be at least 18 years of age!"
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual(expect, str(ve.exception))

    def test_age_when_18_(self):
        expect = 18
        self.player.age = 18
        self.assertEqual(expect, self.player.age)

    def test_add_new_name_when_tournament_in_list(self):
        expect = "London has been already added to the list of wins!"
        self.player.wins.append('London')
        self.assertEqual(expect, self.player.add_new_win('London'))

    def test_add_new_name_when_tournament_not_in_list(self):
        expect = ['Paris']
        self.player.add_new_win('Paris')
        self.assertEqual(expect, self.player.wins)

    def test__lt__when_not_larger(self):
        self.second_p = TennisPlayer('Jason', 22, 30)
        expect = 'Alex is a better player than Jason'
        self.assertEqual(expect, self.player.__lt__(self.second_p))

    def test_lt_when_equal(self):
        self.second_p = TennisPlayer('Jason', 22, 50)
        expect = 'Alex is a better player than Jason'
        self.assertEqual(expect, self.player.__lt__(self.second_p))

    def test_lt_when_smaller(self):
        self.second_p = TennisPlayer('Jason', 22, 60)
        expect = 'Jason is a top seeded player and he/she is better than Alex'
        self.assertEqual(expect, self.player.__lt__(self.second_p))

    def test__str__(self):
        result = "Tennis Player: Alex\nAge: 20\nPoints: 50.0\nTournaments won: London, Paris"
        self.player.add_new_win('London')
        self.player.add_new_win('Paris')
        self.assertEqual(result, self.player.__str__())


if __name__ == '__main__':
    main()
