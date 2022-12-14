from calling_plan import CallingPlan
import csv
from typing import List, Dict, TypedDict


class Customer:
	def __init__(self, name,
				 caller_number,
				 calling_plan_name: str):
		self.name = name
		self.caller_number = caller_number
		self.calling_plan_name = calling_plan_name

	def get_calling_plan_name(self) -> str:
		"""
		call plan getter
		:return: calling plan
		"""

		return self.calling_plan_name

	def __repr__(self):
		str_customer = f'{self.name}\t{self.caller_number}\t{self.calling_plan_name}'
		return str_customer


#
#
# class CustomerDict(TypedDict):
#     name: str
#     customer: Customer


class Customers:
	def __init__(self):
		self._customer_dict: Dict[str, Customer] = {}

	def add_customer(self, one_customer: Customer):
		"""
        add a customer object to the internal collection
        :param one_customer: customer object
        :return:
        """
		self._customer_dict[one_customer.name] = one_customer

	def get_customer(self, customer_name: str) -> Customer:
		'''
		gets a customer object from the customers object. Search by name.
		:param customer_name: name is just one string, first and last name
		are one string.
		:return: Customer object
		'''
		one_customer: Customer = self._customer_dict.get(customer_name)
		return one_customer

	def load_customers_from_file(self, file_path: str):
		"""
		load data from customers file to populate the internal collection
		:param file_path: file path of customers file in string format
		:return:
		"""
		with open(file_path) as f:
			reader = csv.reader(f)
			for row in reader:
				# todo: create a function that skips lines starting with #
				tp = tuple(row)
				obj_cm = Customer(*tp)
				self.add_customer(obj_cm)

	def __repr__(self):
		str_customers = ''
		for customer in self._customer_dict.values():
			str_customers += f'\n{repr(customer)}'
		return str_customers

# def test_load_customers_from_file(file_path: str):
#     obj_customers = Customers()
#     with open(file_path) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             tp = tuple(row)
#             obj_cm = Customer(*tp)
#             obj_customers.add_customer(obj_cm)
#     str_custs = repr(obj_customers)
#     print(str_custs)
#
#
# # path = '/Users/johnnyguo/PycharmProjects/phone_bill_system/Customers.csv'
# path = 'C:\\Users\\patri\\PycharmProjects\\phone_bill_system\\Customers.csv'
# test_load_customers_from_file(path)
