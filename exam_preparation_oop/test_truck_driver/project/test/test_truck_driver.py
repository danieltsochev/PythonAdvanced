from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Alex', 10)

    def test_correct__init__(self):
        self.assertEqual('Alex', self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_when_raise_value_error(self):
        expect = 'Alex went bankrupt.'
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(expect, str(ve.exception))

    def test_add_cargo_offer_when_raise_value_error(self):
        expect = 'Cargo offer is already added.'
        self.driver.add_cargo_offer('cargoX', 20)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('cargoX', 16)
        self.assertEqual(expect, str(ex.exception))

    def test_add_cargo_offer_when_correct_works(self):
        expect_dict = {'cargoX': 20}
        expect_return = "Cargo for 20 to cargoX was added as an offer."
        result = self.driver.add_cargo_offer('cargoX', 20)
        self.assertEqual(expect_dict, self.driver.available_cargos)
        self.assertEqual(expect_return, result)



if __name__ == '__main__':
    main()
