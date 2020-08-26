import csv


class Modify_CSV:
    def __init__(self, f_read, f_write):
        self.f_read = f_read
        self.f_write = f_write

        with open(f_read, 'r') as csv_r:
            self.csv_reader = csv.reader(csv_r, skipinitialspace=True, delimiter = ',')

        with open(f_write, 'w') as csv_w:
            self.csv_writer = csv.writer(csv_w)

    def list_CSV(self):
        for row in self.csv_reader:
            print(row)
        return

    # def list_row(self):
    #     pass

    # def list_col():
    #     #if(f.closed):
    #     #    return
    #     col = input("Select col number: \t")
    #     for row in csv_f:
    #         print(row[col])
    #     return

    # def remove_space():
    #     #if(f.closed):
    #     #    return
    #     for row in csv_f:
    #         for col in row:
    #             col.replace(" ", "")
    #         print(row)
    #     return

    # def remove_space_col():
    #     #if(f.closed):
    #     #    return
    #     col = int(input("Select col number: \t"))
    #     for row in csv_f:
    #         row[col].replace(" ", "")
    #         print(row[col])
    #     return

    # def remove_le_space():
    #     #if(f.closed):
    #     #    return
    #     for row in csv_f:
    #         for col in row:
    #             col.strip()
    #         print(row)
    #     return

    # def remove_le_space_col():
    #     #if(f.closed):
    #     #    return
    #     col = int(input("Select col number: \t"))
    #     for row in csv_f:
    #         row[col].strip()
    #         print(row[col])
    #     return

csv_1 = Modify_CSV("test.csv", "final.csv")
csv_1.list_CSV()