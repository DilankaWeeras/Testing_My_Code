import csv

def open_csv():
    file_name = input("CSV name: ")
    try:
        f = open('TechCrunchcontinentalUSA.csv')
    except IOError:
        print("Could not open file!")
        return
    csv_f = csv.reader(f)
    return

def list_CSV():
    #if(csv_f.closed):
    #    return
    for row in csv_reader:
        print(row)
    return

def list_row():
    #if(f.closed):
    #    return
    print()
    return

def list_col():
    #if(f.closed):
    #    return
    col = input("Select col number: \t")
    for row in csv_f:
        print(row[col])
    return

def remove_space():
    #if(f.closed):
    #    return
    for row in csv_f:
        for col in row:
            col.replace(" ", "")
        print(row)
    return

def remove_space_col():
    #if(f.closed):
    #    return
    col = int(input("Select col number: \t"))
    for row in csv_f:
        row[col].replace(" ", "")
        print(row[col])
    return

def remove_le_space():
    #if(f.closed):
    #    return
    for row in csv_f:
        for col in row:
            col.strip()
        print(row)
    return

def remove_le_space_col():
    #if(f.closed):
    #    return
    col = int(input("Select col number: \t"))
    for row in csv_f:
        row[col].strip()
        print(row[col])
    return

with open('TechCrunchcontinentalUSA.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        col = 4
        for row in csv_reader:
            print(row[4])
            csv_writer.writerow(row)

        #RUNTIME MENU for modify
        def modify():
            modify_menu = ["Modify Menu \t----------\n"
            "(1)\tList CSV",
            "(2)\tList col in CSV",
            "(3)\tRemove ALL spaces in CSV",
            "(4)\tRemove ALL spaces leading and trailing spaces",
            "(5)\tRemove ALL spaces from a column",
            "(6)\tRemove leading and trailing spaces in col",
            "(q)\tQuit"
            ]
            
            while True:
                print("\n")
                for i in modify_menu:
                    print(i)
                user_in = input("Select:\t")
                if user_in == "1":
                    list_CSV()
                elif user_in == "2":
                    list_col()
                elif user_in == "3":
                    remove_space()
                elif user_in == "4":
                    remove_le_space()
                elif user_in == "5":
                    remove_space_col()
                elif user_in == "6":
                    remove_le_space_col()
                elif user_in.upper() == "Q":
                    break
                else:
                    print("Select a correct option\n")
            return

        main_menu = ["Menu:\t\t----------\n",
                    "(1)\tEnter a new CSV file",
                    "(2)\tModify CSV file",
                    "(q)\tQuit",
                    ]

        #RUNTIME BEGIN
        while True:
            for i in main_menu:
                print(i)
            user_in = input("Select:\t")
            if user_in == "1":
                open_csv()
            elif user_in == "2":
                modify()
            elif user_in.upper() == "Q":
                break
            else:
                print("Select a correct option\n")




