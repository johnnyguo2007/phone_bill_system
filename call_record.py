import dataclasses
from datetime import datetime
from dataclasses import dataclass
import csv


@dataclass
class CallRecord:
    date_time: datetime
    caller_number: int
    destination_number: int
    duration_seconds: int



    def __post_init__(self):
        """
        convert objects to appropriate datatypes
        :return: converted objects
        """
        if not isinstance(self.date_time, datetime):
            if isinstance(self.date_time, str):
                self.date_time = datetime.strptime(self.date_time, '%m/%d/%Y %H:%M')
                #print('hello')
        if not isinstance(self.duration_seconds, int):
            if isinstance(self.duration_seconds, str):
                self.duration_seconds = int(self.duration_seconds)
                #print('')


    def get_billing_year_month(self) -> int:
        """
        converts the month and year to appropriate format
        :return: formated month and year as an int
        """
        year: int = self.date_time.year
        month: int = self.date_time.month
        yyyymm = year * 100 + month
        return yyyymm

# def __init__(self, date_time: datetime, caller_number: int, destination_number: int, duration_seconds: int):
#     """
#     This is a class represent one phone call record.
#     :param date_time:
#     :param caller_number:
#     :param destination_number:
#     :param duration_seconds:
#     """


#     pass


class CallRecords:
    def __init__(self):
        self._data = []

    def get_call_records(self) -> list[CallRecord]:
        """
        get call records and store it into a list
        :return: list of records
        """
        return self._data

    def __repr__(self):
        str_records = ''
        for record in self._data:
            str_records += f"\n{str(record)}"
        return str_records

    def add_record(self, phone_record: CallRecord):
        """
        add a record to the internal collection (list)
        :param phone_record: one singular record
        :return:
        """
        self._data.append(phone_record)

    def total_duration(self, call_type, duration_seconds):
        """
        Compute total duration for all of the call in this object
        :param call_type: is international or local call
        :return:
        """
        pass

    def load_call_records_from_file(self, filename: str):
        """
        load data from records file to populate the internal collection
        :param filename: file path of plans file in string format
        :return:
        """
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                tp = tuple(row)
                obj_cr = CallRecord(*tp) #using wilecard to unpack the tuple
                self.add_record(obj_cr)
# import csv
#
# call_records = CallRecords()
# with open(r'C:\Users\patri\PycharmProjects\phone_bill_system\call_records.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         tp = tuple(row)
#         obj_cr = CallRecord(*tp) #using wilecard to unpack the tuple
#         call_records.add_record(obj_cr)
#
# print(call_records)

# load_file_to_call_records('/Users/johnnyguo/PycharmProjects/phone_bill_system/call_records.csv')

# c_dict = {
# 	"data_time": 'sadf',
# 	"caller_number": 3214,
# 	"destination_number": 32413,
# 	"duration_seconds": 230715015
# }
#
# cr = CallRecord(c_dict)
# print(cr)
