import csv
from typing import Dict


class CallingPlan:
    def __init__(self, plan_name: str ='Basic',
                 rate_domestic: float =0.01,
                 rate_inter: float =0.05,
                 allowance_domestic: int =1000,
                 allowance_inter: int =0,
                 fix_price: float =10
                 ):
        self.plan_name = plan_name
        self.rate_inter = float(rate_inter)
        self.rate_domestic = float(rate_domestic)
        self.allowance_inter = int(allowance_inter)
        self.fix_price = float(fix_price)
        self.allowance_domestic = int(allowance_domestic)


    def get_local_allowance(self) -> int:
        return self.allowance_domestic

    def get_international_allowance(self) -> int:
        return self.allowance_inter

    def get_fixed_cost(self) -> int:
        return self.fix_price

    def get_local_rate(self) -> float:
        return self.rate_domestic

    def get_international_rate(self) -> float:
        return self.rate_inter

    def __repr__(self):
        str_plan = f'{self.plan_name}\t{self.rate_domestic}\t{self.rate_inter}' \
                   f'\t{self.allowance_domestic}\t{self.allowance_inter}\t{self.fix_price}'
        return str_plan
class CallingPlans:
    def __init__(self):
        self._plan_dict : Dict[str: CallingPlan] = {}

    def add_plan(self, one_plan:CallingPlan):
        self._plan_dict[one_plan.plan_name] = one_plan

    def get_plan(self, plan_name: str) -> CallingPlan:
        one_plan: CallingPlan = self._plan_dict.get(plan_name)
        return one_plan

    def load_plans_from_file(self, file_path: str):
        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                tp = tuple(row)
                obj_pn = CallingPlan(*tp)
                self.add_plan(obj_pn)

    def __repr__(self):
        str_plans = ''
        for plan in self._plan_dict.values():
            # todo: need more complete repr
            str_plans += f'\n{repr(plan)}'
        return str_plans

def test_load_plans_from_file(file_path:str):
    obj_call_plans = CallingPlans()
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            tp = tuple(row)
            obj_pn = CallingPlan(*tp)
            obj_call_plans.add_plan(obj_pn)
        str_pns = repr(obj_call_plans)
        print(str_pns)

path = 'C:\\Users\\patri\\PycharmProjects\\phone_bill_system\\plans.csv'
test_load_plans_from_file(path)
