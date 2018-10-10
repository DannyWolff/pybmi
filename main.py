def main_menu():

    choice ='0'
    while choice =='0':
        print("Main Choice: Choose Measurments")
        print("1 Metric")
        print("2 Imperial")
        print("3 Quit")

        choice = input ("Please make a choice: ")

        if choice == "1":
            print("Metric")
        elif choice == "2":
            print("Imperial")
        elif choice == "3":
            break
        else:
            print("Please enter 1 or 2.")
            main_menu()

def second_menu():
    pass

main_menu()
