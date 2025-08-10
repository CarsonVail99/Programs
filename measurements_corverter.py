1 kilometer = 1000 meters
1 meter = 100 centimeters
1 centimenter = 10 millimeters

1 mile = 1760 yards
1 yard = 3 feet
1 foot = 12 inches


def from_measurement():
    try:
        choice = input("What would you like to convert from?\n1.Kilometers\n2.Meters\n3.Centimeters\n4.Millimeters\n5.Miles\n6.Yards\n7.Feet\n8.Inches\n ")
        if choice == "1":
            kilometers = float(input("Enter the value of kilometers:"))
            first_measurement = kilometers
            return first_measurement, choice
        elif choice == '2':
            meters = float(input("Enter the value of meters:"))
            first_measurement = meters
            return first_measurement, choice
        elif choice == '3':
            centimeters = float(input("Enter the value of centimeters:"))
            first_measurement = centimeters
            return first_measurement, choice
        elif choice == '4':
            millimeters = float(input('Enter the value of millimeters:'))
            first_measurement = millimeters
            return first_measurement, choice
        elif choice == '5':
            miles = float(input('Enter the value of miles:'))
            first_measurement = miles
            return first_measurement, choice
        elif choice == '6':
            yards = float(input('Enter the value of yards:'))
            first_measurement = yards
            return first_measurement, choice
        elif choice == '7':
            feet = float(input('Enter the value of feet:'))
            first_measurement = feet
            return first_measurement, choice
        elif choice == '8':
            inches = float(input('Enter the value of inches:'))
            first_measurement = inches
            return first_measurement, choice
    except ValueError as (e):
        print(e)


def to_measurement(first_measurement,choice):
    choice2 = int(input('What would you like to convert your measurement to?'
                        '\n1.Kilometers'
                        '\n2.Meters'
                        '\n3.Centimeters'
                        '\n4.Millimeters'
                        '\n5.Miles'
                        '\n6.Yards'
                        '\n7.Feet'
                        '\n8.Inches'
                        '\n'))
    if choice2 == 1:
        try:
            if choice == 1:
                print("Your measurement is already in kilometers.")
                return first_measurement
            elif choice == 2:
                kilometers = first_measurement / 1000
                print(f"Your measurement of {first_measurement} meters is {kilometers} kilometers.")
                return kilometers
            elif choice == 3:
                kilometers = first_measurement / 100000
                print(f"Your measurement of {first_measurement} centimeters is {kilometers} kilometers.")
                return kilometers
            elif choice == 4:
                kilometers = first_measurement / 1000000
                print(f"Your measurement of {first_measurement} millimeters is {kilometers} kilometers.")
                return kilometers
            elif choice == 5:
                kilometers = first_measurement / 1.609
                print(f"Your measurement of {first_measurement} miles is {kilometers} kilometers.")
                return kilometers
            elif choice == 6:
                kilometers = first_measurement / 1093.61
                print(f"Your measurement of {first_measurement} yards is {kilometers} kilometers.")
                return kilometers
            elif choice == 7:
                kilometers = first_measurement / 3280.84
                print(f"Your measurement of {first_measurement} feet is {kilometers} kilometers.")
            elif choice == 8:
                kilometers = first_measurement / 39370.0787
                print(f"Your measurement of {first_measurement} inches is {kilometers} kilometers.")
                return kilometers
        except ValueError as (e):
            print(e)
    elif choice2 == 2:
        try:
            if choice == 1:
                meters = first_measurement / 1000
                print(f'Your measurement of {first_measurement} kilometers is {meters} meters.')
                return meters
            elif choice == 2:
                print("Your measurement is already in meters.")
                return first_measurement
            elif choice == 3:
                meters = first_measurement * 100
                print(f'Your measurement of {first_measurement} centimeters is {meters} meters.')
                return meters
            elif choice == 4:
                meters = first_measurement * 1000
                print(f'Your measurement of {first_measurement} millimeters is {meters} meters.')
                return meters
            elif choice == 5:
                meters = first_measurement * 1609.34
                print(f'Your measurement of {first_measurement} miles is {meters} meters.')
                return meters
            elif choice == 6:
                meters = first_measurement * 1.094
                print(f'Your measurement of {first_measurement} yards is {meters} meters.')
                return meters
            elif choice == 7:
                meters = first_measurement * 3.28084
                print(f'Your measurement of {first_measurement} feet is {meters} meters.')
                return meters
            elif choice == 8:
                meters = first_measurement * 39.3700787
                print(f'Your measurement of {first_measurement} inches is {meters} meters.')
                return meters
        except ValueError as (e):
            print(e)
    elif choice2 == 3:
        try:
            if choice == 1:
                centimeters = first_measurement / 100000
                print(f'Your measurement of {first_measurement} kilometers is {centimeters} centimeters.')
                return centimeters
            elif choice == 2:
                centimeters = first_measurement / 100
                print(f'Your measurement of {first_measurement} meters is {centimeters} centimeters.')
                return centimeters
            elif choice == 3:
                print("Your measurement is already in centimeters.")
                return first_measurement
            elif choice == 4:
                centimeters = first_measurement / 10
                print(f'Your measurement of {first_measurement} millimeters is {centimeters} centimeters.')
            elif choice == 5:
                centimeters = first_measurement / 160934
                print(f'Your measurement of {first_measurement} miles is {centimeters} centimeters.')
            elif choice == 6:
                centimeters = first_measurement / 91.44
                print(f'Your measurement of {first_measurement} yards is {centimeters} centimeters.')
            elif choice == 7:
                centimeters = first_measurement / 30.48
                print(f'Your measurement of {first_measurement} feet is {centimeters} centimeters.')
            elif choice == 8:
                centimeters = first_measurement / 2.54
                print(f'Your measurement of {first_measurement} inches is {centimeters} centimeters.')
                return centimeters


