import pandas as pd
pd.options.display.max_rows = 20
import os.path
import os
clear = lambda: os.system('cls')
data = pd.DataFrame()
import time

def print_menu():       ## Your menu design here
    print();print(30 * "-" , "MENU" , 30 * "-")
    print("1 - Load database from file")
    print("2 - Save database to file")
    print("3 - Edit database")
    print("4 - Show database contents")
    print("5 - Exit")
    print(67 * "-"); print()

def print_data():
    print()
    print(data)
    print()

def print_sub_menu():
    print("1 - Remove record from database")
    print("2 - Edit record in database")
    print("3 - Add new record to database")
    print("4 - Exit submenu"); print()

def print_record(id):
    print("Choose number corresponding to column to edit it: ")
    print(data.loc[[id]])
    cols = list(data.columns.values)
    for i, name in enumerate(cols):
        print(i, name)
    print(str(len(list(data.columns.values)))+" Exit record-edit submenu")

def print_save_menu():
    print("Saving file - choose option")
    print("1 - semicolon format")
    print("2 - tab format")
    print("3 - exit save submenu")




def save_database():
    loop_save = True
    while loop_save:

        print_save_menu()

        try:
            choice = int(input("Enter your choice [1-3]: "))
        except ValueError:
            choice = -1

        clear()

        if choice==1:
            fname=input("Enter filename: ")
            data.to_csv(fname, sep=';', index=False)
            print("Saved.")


        elif choice ==2:
            fname=input("Enter filename: ")
            data.to_csv(fname, sep='\t', index=False)
            print("Saved.")

        elif choice ==3:
            loop_save = False
            clear()
            print("Exit")

        else:
            print("Wrong option chosen!")
            time.sleep(2)

def load_database():
    print("Loading the database")
    while True:
        fname = input("Enter the file name: ")
        if os.path.isfile(fname):
            break
        else:
            print("File does not exist!")
            time.sleep(2)

    data = pd.read_csv(fname, delimiter=';')
    if data.shape[1] ==1:
        data = pd.read_csv(fname, delimiter='\t')

    return data

def edit_record(id):
    loop_edit_record = True
    col_list = list(data.columns.values)
    while loop_edit_record:
        print_record(id)
        try:
            choice = int(input("Enter your choice [0-{}]: ".format(len(col_list) + 1)))
        except ValueError:
            choice = -1
        clear()

        if choice == len(col_list):
            print("Going back to submenu edit.")
            loop_edit_record = False

        elif choice < len(col_list) and choice >= 0:
            added = True
            while added:
                data.loc[id,col_list[choice]] = input("Enter the data to place in cell: ")
                if data.loc[id,col_list[0]] != '':
                    added=False
            print("Person added")


        else:
            print("Incorrect column index!")
            time.sleep(2)


def edit_menu():
    loop_edit = True
    while loop_edit:
        print_data()
        print_sub_menu()
        print()

        try:
            choice = int(input("Enter your choice [1-4]: "))
        except ValueError:
            choice = -1

        if choice == 1:
            try:
                id = input("Enter the index of record to be deleted: ")
                id = int(id)
                data.drop(int(id), inplace=True)
                print("Deleted.")
            except ValueError or KeyError:
                print("Not a number or out of range!")
                time.sleep(2)

        elif choice == 2:
            try:
                id = input("Enter the index of record to be edited: ")
                id = int(id)
                if len(data.index)-1 >= id:
                    edit_record(id)
                else:
                    print("Index out of range!")
                    time.sleep(2)

            except ValueError or KeyError:
                print("Not a number!")
                time.sleep(2)

        elif choice == 3:
            print("Adding new record.")
            new_id = data.shape[0]
            data.loc[new_id] = \
                [input(list(data.columns.values+": ")[n]) for n in range(len(list(data.columns.values)))]
            if False in [data.loc[new_id][x] != '' for x in range(len(list(data.columns.values)))]:
                print("Empty value in record! Record not added!")
                time.sleep(2)
                data.drop(int(new_id), inplace=True)



        elif choice == 4:
            print("Going to main menu.")
            loop_edit = False  # This will make the while loop to end as not value of loop is set to False
        else:
            print("Wrong input!")
            time.sleep(2)
        clear()

loop = True
while loop:
    print_menu()
    try:
        choice = int(input("Enter your choice [1-5]: "))
    except ValueError:
        choice = -1
    clear()


    # DB Load
    if choice == 1:
        data = load_database()

    # DB Save
    elif choice == 2:
        if(data.empty):
            print("No data to save!")
            time.sleep(2)
        else:
            save_database()

    # DB Edit
    elif choice == 3:
        print("Editing the database.")
        edit_menu()

    # DB Show
    elif choice == 4:
        print("Showing database contents:")
        print_data()

    # DB exit
    elif choice == 5:
        print("Exit\nBye!")
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        print("Wrong input!")
        time.sleep(2)