import pandas as pd
pd.options.display.max_rows = 20
import os.path

data = pd.DataFrame()

def print_menu():       ## Your menu design here
    print();print(30 * "-" , "MENU" , 30 * "-")
    print("1 - Load database from file")
    print("2 - Save database to file")
    print("3 - Edit database")
    print("4 - Show database contents")
    print("5 - Exit")
    print(67 * "-")

def print_sub_menu():
    print("1 - Remove record from database")
    print("2 - Edit record in database")
    print("3 - Add new record to database")
    print("4 - Exit submenu")

def edit_menu():
    print_sub_menu()
    loop_edit = True
    while loop_edit:
        choice = int(input("Enter your choice [1-4]: "))

        if choice == 1:
            try:
                id = input("Enter the index of record to be deleted: ")
                id = int(id)
                data.drop(int(id), inplace=True)
                print("Deleted.")
            except ValueError and KeyError:
                print("Not a number or out of range!")


        elif choice == 2:
            None

        elif choice == 3:
            None

        elif choice == 4:
            print("Going to main menu.")
            loop_edit = False  # This will make the while loop to end as not value of loop is set to False
        else:
            print("Wrong input!")

loop = True
while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))

    # DB Load
    if choice == 1:
        print("Loading the database")
        while True:
            fname = input("Enter the file name: ")
            if os.path.isfile(fname) and fname.split('.')[-1]=='csv':
                break
            else:
                print("File does not exist or wrong format!")

        data = pd.read_csv(fname, delimiter=';')

    # DB Save
    elif choice == 2:
        fname = input("Saving the database.\nEnter the file name: ")
        if(data.empty):
            print("No data to save!")
        else:
            data.to_csv(fname+".csv", sep=';')

    # DB Edit
    elif choice == 3:
        print("Editing the database.")
        edit_menu()

    # DB Show
    elif choice == 4:
        print("Showing database contents:")
        print(data)

    # DB exit
    elif choice == 5:
        print("Exit\nBye!")
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        print("Wrong input!")