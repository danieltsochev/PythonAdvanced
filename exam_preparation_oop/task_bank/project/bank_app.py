from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:

    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."
        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        client = [c for c in self.clients if c.client_id == client_id][0]
        if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or (
            loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"
        ):
            loan= [l for l in self.loans if l.__class__.__name__  == loan_type][0]
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise Exception("No such client!")
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        number_of_changed_loans = 0
        if self.loans:
            for l in self.loans:
                if l.__class__.__name__ == loan_type:
                    l.increase_interest_rate()
                    number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate):
        changed_client_rates_number = 0
        clients_with_less_than_min_rate = [c for c in self.clients if c.interest < min_rate]
        if clients_with_less_than_min_rate:
            for c in clients_with_less_than_min_rate:
                c.increase_clients_interest()
                changed_client_rates_number += 1
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([l.amount for c in self.clients for l in c.loans])
        not_granted_sum = sum([l.amount for l in self.loans])
        try:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0
        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {total_clients_income:.2f}\n"
        result += f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result
