import csv

counties_csv = r'MontanaCounties.csv'
row = {}
keys = []
values = []

# opens, reads, and stores the .csv file in a dictionary
with open(counties_csv, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        for key, value in record.items():
            keys.append(key)
            values.append(value)

# this function skips to every third value in the list
# to put in all the license plate prefixes
def every_lpp():
    lst = []
    for i in range(2, len(values), 3):
        lst.append(values[i])
    return lst

# this function checks to make sure that all the license plate prefixes are
# where they are supposed to be when each dictionary value is created
def check_all(lst):
    for key, value in zip(keys, values):
        row[key] = value
        print(row)
        if len(row) == 3:
            for i in lst:
                if i == row['License Plate Prefix'] and len(row) == 3:
                    print("This is the county:", row['County'])
                    print("This is the County seat:", row['County Seat'])
                    print("This is the string of the dictionary:", row['License Plate Prefix'])
                    print("This is the string in the list:", i, "\n")
                    row.clear()
                    lst.pop(lst.index(i))
                    break
                elif len(row) == 3 and i != row['License Plate Prefix']:
                    return False

# this runs the application and lets people input the license plate manually
def lpp_lookup():
    while True:
        llp_input = input("Please enter a Licence Plate Prefix: ")
        for key, value in zip(keys, values):
            row[key] = value
            if len(row) != 3:
                continue
            elif len(row) == 3 and llp_input == row['License Plate Prefix']:
                print("The county is:", row['County'])
                print("The county seat is:", row['County Seat'], "\n")
                row.clear()
                break
        if llp_input not in values:
            print("That License Plate Prefix is not valid. Please try again")


if __name__ == '__main__':
    lpp_lookup()
