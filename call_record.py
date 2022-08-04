import dataclasses
import datetime
from dataclasses import dataclass
import csv


@dataclass
class CallRecord:
	@dataclass
	class CallRecord:
		data_time: datetime
		caller_number: int
		destination_number: int
		duration_seconds: int

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
		pass

	def add_record(self, phone_record: CallRecord):
		pass

	def total_duration(self, call_type, duration_seconds):
		"""
        Compute total duration for all of the call in this object
        :param call_type: is international or local call
        :return:
        """
		pass


def load_file_to_call_records(filename: str):
	with open(filename) as f:
		reader = csv.reader(f)
		for row in reader:
			print(row[2])
			cr = CallRecord()
			print(cr)




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