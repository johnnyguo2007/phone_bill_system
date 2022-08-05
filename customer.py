from calling_plan import CallingPlan


class Customer:
    def __init__(self, name,
                 caller_number,
                 calling_plan: CallingPlan):
        self.name = name
        self.caller_number = caller_number
        self.calling_plan = calling_plan

    def get_calling_plan(self) -> CallingPlan:
        pass


class Customers:
    def __init__(self):
        pass

    def add_customer(self, one_customer: Customer):
        pass

    def get_customer(self, customer_name: str) -> Customer:
        pass

    def load_customers_from_file(self, file_path: str):
        pass

    def __repr__(self):
        pass
