def main_menu():

    choice ='0'
    while choice =='0':
        print("Main Choice: Choose Measurments")
        print("1 Metric")
        print("2 Imperial")
        print("3 Quit")

        choice = input ("\nPlease make a choice: ")

        if choice == "1":
            print("Metric\n")
            calc_bmi_metric()
        elif choice == "2":
            print("Imperial\n")
            calc_bmi_imperial()
        elif choice == "3":
            break
        else:
            print("Please enter 1 or 2.")
            main_menu()

def calc_bmi_metric():
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))

    bmi_metric = weight/((height**2)/(100**2))
    
    print("{:0.2f}".format(bmi_metric))

def calc_bmi_imperial():
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))

    bmi_imperial = (weight/((height**2)))*703
    
    print("{:0.2f}".format(bmi_imperial))

main_menu()
