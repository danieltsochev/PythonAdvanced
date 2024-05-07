from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar('bmw', 'cope', 1000, 100.0)

    def test_correct__init__(self):
        self.assertEqual('bmw', self.car.model)
        self.assertEqual('cope', self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(100.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_wrong_price_set_value_error(self):
        expect = 'Price should be greater than 1.0!'
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual(expect, str(ve.exception))

        expect = 'Price should be greater than 1.0!'
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.8
        self.assertEqual(expect, str(ve.exception))

    def test_wrong_mileage_value_error(self):
        expect = 'Please, second-hand cars only! Mileage must be greater than 100!'
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual(expect, str(ve.exception))

        expect = 'Please, second-hand cars only! Mileage must be greater than 100!'
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 90
        self.assertEqual(expect, str(ve.exception))

    def test_set_promotional_price_when_raise_value_error(self):
        expect = 'You are supposed to decrease the price!'
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100.0)
        self.assertEqual(expect, str(ve.exception))

        expect = 'You are supposed to decrease the price!'
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(150.0)
        self.assertEqual(expect, str(ve.exception))

    def test_set_promotional_price_when_correct(self):
        self.car_test = SecondHandCar('wvv', 'cope', 1000, 200.0)
        exp_message = 'The promotional price has been successfully set.'
        result = self.car_test.set_promotional_price(150.0)
        self.assertEqual(exp_message, result)

        self.assertEqual(150.0, self.car_test.price)

    def test_need_repair_when_raise_value_error(self):
        expect = 'Repair is impossible!'
        result = self.car.need_repair(90.0, 'engine')
        self.assertEqual(expect, result)

    def test_test_need_repair_when_correct(self):
        exp_message = 'Price has been increased due to repair charges.'
        exp_price = 120.0
        exp_list = ['tyres']
        self.assertEqual(exp_message, self.car.need_repair(20.0, 'tyres'))
        self.assertEqual(exp_list, self.car.repairs)
        self.assertEqual(exp_price, self.car.price)

    def test__gt__when_car_type_not_same(self):
        self.first_car = SecondHandCar('first', 'typeX', 1000, 100.0)
        self.second_car = SecondHandCar('first', 'typeY', 1000, 100.0)
        expect = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expect, self.first_car.__gt__(self.second_car))

    def test__gt__when_car_type_are_same(self):
        self.first_car = SecondHandCar('first', 'typeX', 1000, 100.0)
        self.second_car = SecondHandCar('first', 'typeX', 1000, 130.0)
        expect = False
        self.assertEqual(expect, self.first_car.__gt__(self.second_car))

    def test_correct__str__(self):
        self.car.need_repair(20.0, 'tyres')
        self.assertEqual("Model bmw | Type cope | Milage 1000km\nCurrent price: 120.00 | Number of Repairs: 1", str(self.car))

if __name__ == '__main__':
    main()
