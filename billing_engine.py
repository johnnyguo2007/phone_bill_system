from call_record import CallRecords
from calling_plan import CallingPlan
from customer import Customers, Customer
import util


class BillingEngine:
    def __init__(self, customer_file_path: str,
                 call_records_path: str,
                 duration_seconds, rate, is_international, ):
        self.customer_file_path = customer_file_path

    def generate_one_bill(self, customer_name: str,
                          phone_records: CallRecords,
                          billing_month: int):
        # 0. load all of the customers
        obj_customers = Customers()
        # 1. from customer name create a customer object
        obj_customers.load_customers_from_file(self.customer_file_path)
        obj_cust = obj_customers.get_customer(customer_name)
        # 2. from customer object we have a pricing plan we can use
        obj_call_plan = obj_cust.get_calling_plan()
        # 3.0 load phone call record
        obj_call_records = CallRecords()
        obj_call_records.load_call_records_from_file()
        # All functions above implemented

        # 3. Go through each record in phone_records
        # 3.1 check if that record is within billing month
        # 3.2 and if the record belongs to the customer or not
        # 3.3 keep two totals of minutes. One local total and one international total.
        international_total_minutes = 0
        local_total_minutes = 0
        for record in obj_call_records.get_call_records():
            if record.get_billing_month() == billing_month \
                    and record.caller_number == obj_cust.caller_number:
                if util.is_international(record):
                    international_total_minutes += record.duration_seconds / 60
                else:
                    local_total_minutes += record.duration_seconds / 60

        # 4. imply calling_plan and subtract allowance for both local and internatinal and mutiply rates respectivly
        local_total_minutes -= obj_call_plan.get_local_allowance()
        local_total_minutes = max(0, local_total_minutes)
        international_total_minutes -= obj_call_plan.get_international_allowance()
        international_total_minutes = max(0, international_total_minutes)
        total_bill_cost = local_total_minutes * obj_call_plan.get_local_rate() \
                          + international_total_minutes * obj_call_plan.get_international_rate() \
                          + obj_call_plan.get_fixed_cost()

        # 5. generate bill

