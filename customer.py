from calling_plan import CallingPlan
import csv


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
		self._customer_dict: {str: Customer} = dict()

	def add_customer(self, one_customer: Customer):
		self._customer_dict[one_customer.name] = one_customer

	def get_customer(self, customer_name: str) -> Customer:
		one_customer: Customer = self._customer_dict.get(customer_name)
		return one_customer

	def load_customers_from_file(self, file_path: str):
		with open(file_path) as f:
			reader = csv.reader(f)
			for row in reader:
				tp = tuple(row)
				obj_cm = Customer(*tp)
				self.add_customer(obj_cm)

	def __repr__(self):
		str_customers = ''
		for customer in self._customer_dict:
			str_customers += f'\n{str(customer)}'
		return str_customers


def test_load_customers_from_file(file_path: str):
	obj_customers = Customers()
	with open(file_path) as f:
		reader = csv.reader(f)
		for row in reader:
			tp = tuple(row)
			obj_cm = Customer(*tp)
			obj_customers.add_customer(obj_cm)
	str_custs = repr(obj_customers)
	print(str_custs)


path = '/Users/johnnyguo/PycharmProjects/phone_bill_system/Customers.csv'
test_load_customers_from_file(path)
