from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    VALID_WAITER = {"FullTimeWaiter": FullTimeWaiter,  "HalfTimeWaiter": HalfTimeWaiter}
    VALID_CLIENT = {"RegularClient": RegularClient,  "VIPClient": VIPClient}

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worked):
        if waiter_type not in self.VALID_WAITER:
            return f"{waiter_type} is not a recognized waiter type."
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter:
            return f"{waiter_name} is already on the staff."
        if waiter is None:
            new_waiter = self.VALID_WAITER[waiter_type](waiter_name, hours_worked)
            self.waiters.append(new_waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type, client_name):
        if client_type not in self.VALID_CLIENT:
            return f"{client_type} is not a recognized client type."
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            return f"{client_name} is already a client."
        if client is None:
            new_client = self.VALID_CLIENT[client_type](client_name)
            self.clients.append(new_client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter is None:
            return f"No waiter found with the name {waiter_name}."
        if waiter:
            return waiter.report_shift()

    def process_client_order(self, client_name, order_amount):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is None:
            return f"{client_name} is not a registered client."
        if client:
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        if client:
            return f"{client_name} received a {client.apply_discount()[0]}%" \
                   f" discount. Remaining points {client.points}" \

    def generate_report(self):
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)
        waiter_details = "\n".join(
            str(waiter) for waiter in sorted(self.waiters, key=lambda x: x.calculate_earnings(), reverse=True))
        return f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\nTotal Clients Unused Points:" \
               f" {total_client_points}\nTotal Clients Count: {clients_count}\n** Waiter Details **\n{waiter_details}"









