from call_record import CallRecords
from calling_plan import CallingPlans
from customer import Customers
import util


class BillingEngine:
    def __init__(self, customer_file_path: str,
                 call_records_path: str,
                 plan_path: str):
        self.customer_file_path = customer_file_path
        self.call_records_path = call_records_path
        self.plan_path = plan_path

    def generate_one_bill(self, customer_name: str,
                          billing_year_month: int):
        """
        generate one bill for a given customer for a given month within the correct year
        :param customer_name: str
        :param billing_year_month: int
        :return: total bill
        """
        # 0. load all of the customers
        obj_customers = Customers()
        # 1. from customer name create a customer object
        obj_customers.load_customers_from_file(self.customer_file_path)
        obj_cust = obj_customers.get_customer(customer_name)
        # 2. from customer object we have a pricing plan we can use
        call_plan_name = obj_cust.get_calling_plan_name()
        obj_calling_plans = CallingPlans()
        obj_calling_plans.load_plans_from_file(self.plan_path)
        obj_call_plan = obj_calling_plans.get_plan(call_plan_name)
        # 3.0 load phone call record
        obj_call_records = CallRecords()
        obj_call_records.load_call_records_from_file(self.call_records_path)

        # 3. Go through each record in phone_records
        # 3.1 check if that record is within billing month
        # 3.2 and if the record belongs to the customer or not
        # 3.3 keep two totals of minutes. One local total and one international total.
        international_total_minutes: int = 0
        local_total_minutes: int = 0
        for record in obj_call_records.get_call_records():
            if record.get_billing_year_month() == billing_year_month \
                    and record.caller_number == obj_cust.caller_number:
                if util.is_international(record.destination_number):
                    international_total_minutes += record.duration_seconds / 60
                    print(record)
                    print(f'international_total_minutes: {international_total_minutes} ')
                else:
                    local_total_minutes += record.duration_seconds / 60
                    print(record)
                    print(f'local total minutes: {international_total_minutes}')

        # 4. imply calling_plan and subtract allowance for both local and internatinal and mutiply rates respectivly
        local_total_minutes -= obj_call_plan.get_local_allowance()
        local_total_minutes = max(0, local_total_minutes)
        international_total_minutes -= obj_call_plan.get_international_allowance()
        international_total_minutes = max(0, international_total_minutes)
        total_bill_cost = local_total_minutes * obj_call_plan.get_local_rate() \
                          + international_total_minutes * obj_call_plan.get_international_rate() \
                          + obj_call_plan.get_fixed_cost()

        # All functions above implemented
        # 5. generate bill
        print(f'Bill for {customer_name}\n'
              f'Date: {billing_year_month}\n '
              f'Total local minutes: {local_total_minutes}\n'
              f'Total international minutes: {international_total_minutes}\n'
              f'Your total bill is {total_bill_cost}')


# path_customer = 'C:\\Users\\patri\\PycharmProjects\\phone_bill_system\\Customers.csv'
# path_call_records = 'C:\\Users\\patri\\PycharmProjects\\phone_bill_system\\call_records.csv'
# path_plan = 'C:\\Users\\patri\\PycharmProjects\\phone_bill_system\\plans.csv'
path_customer_mac = '/Users/johnnyguo/PycharmProjects/phone_bill_system/Customers.csv'
path_call_records_mac = '/Users/johnnyguo/PycharmProjects/phone_bill_system/call_records.csv'
path_plan_mac = '/Users/johnnyguo/PycharmProjects/phone_bill_system/plans.csv'
#obj_billing_engine = BillingEngine(path_customer, path_call_records, path_plan)
obj_billing_engine = BillingEngine(path_customer_mac, path_call_records_mac, path_plan_mac)
cust_name = 'Novak'
yyyymm = 202105
obj_billing_engine.generate_one_bill(cust_name, yyyymm)
