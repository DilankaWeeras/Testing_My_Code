import csv


file_name = input("Name of CSV:\t")
with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',')

    with open("fix_csv.csv", 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for row in csv_reader:
            csv_writer.writerow(row)


