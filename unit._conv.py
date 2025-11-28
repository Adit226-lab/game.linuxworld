print("Welcome to Unit Converter")

choice = input("What do you want to convert? (weight/time/distance): ").lower()

if choice == "weight":
    kg = float(input("Enter weight in kg: "))
    pounds = kg * 2.2
    print("The weight in pounds is:", pounds)

elif choice == "time":
    hours = int(input("Enter time in hours: "))
    minutes = hours * 60
    print("The conversion in minutes is:", minutes)

elif choice == "distance":
    metres = int(input("Enter distance in metres: "))
    cm = metres * 100
    print("The conversion in cm is:", cm)

else:
    print("Invalid choice!")
