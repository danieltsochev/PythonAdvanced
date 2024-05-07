from unittest import TestCase, main
from project.restaurant import Restaurant

class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("The Best Restaurant", 10)

    def test_properties(self):
        self.assertEqual(self.restaurant.name, "The Best Restaurant")
        self.assertEqual(self.restaurant.capacity, 10)

    def test_wrong_name_value_error(self):
        expect = "Invalid name!"
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = " "
        self.assertEqual(expect, str(ve.exception))

    def test_wrong_capacity_value_error(self):
        expect = "Invalid capacity!"
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1
        self.assertEqual(expect, str(ve.exception))

    def test_test_add_waiter_when_no_space(self):
        expect = "No more places!"
        self.new_restaurant = Restaurant("London", 0)
        self.assertEqual(expect, self.new_restaurant.add_waiter("daniel"))




    def test_add_waiter(self):
        self.assertEqual(self.restaurant.add_waiter("Alice"), "The waiter Alice has been added.")
        self.assertEqual(len(self.restaurant.waiters), 1)

    def test_add_existing_waiter(self):
        self.restaurant.add_waiter("Bob")
        self.assertEqual(self.restaurant.add_waiter("Bob"), "The waiter Bob already exists!")
        self.assertEqual(len(self.restaurant.waiters), 1)

    def test_remove_waiter(self):
        self.restaurant.add_waiter("Charlie")
        self.assertEqual(self.restaurant.remove_waiter("Charlie"), "The waiter Charlie has been removed.")
        self.assertEqual(len(self.restaurant.waiters), 0)

    def test_remove_nonexistent_waiter(self):
        self.assertEqual(self.restaurant.remove_waiter("David"), "No waiter found with the name David.")

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("Eve")
        self.restaurant.add_waiter("Frank")
        self.restaurant.waiters[0]['total_earnings'] = 100
        self.restaurant.waiters[1]['total_earnings'] = 200
        self.assertEqual(self.restaurant.get_total_earnings(), 300)

    def test_get_waiters_with_earnings_range(self):
        self.restaurant.add_waiter("Grace")
        self.restaurant.add_waiter("Henry")
        self.restaurant.add_waiter("Isabella")
        self.restaurant.waiters[0]['total_earnings'] = 50
        self.restaurant.waiters[1]['total_earnings'] = 100
        self.restaurant.waiters[2]['total_earnings'] = 150
        waiters_in_range = self.restaurant.get_waiters(min_earnings=75, max_earnings=125)
        self.assertEqual(len(waiters_in_range), 1)
        self.assertEqual(waiters_in_range[0]['name'], "Henry")


if __name__ == "__main__":
    main()

