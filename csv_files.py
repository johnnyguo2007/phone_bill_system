import csv

data = []
with open(r'/Users/johnnyguo/PycharmProjects/phone_bill_system/call_records.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        print(type(row))
        tp = tuple(row)
        data.append(tp)



print(data)


