from datetime import datetime, timedelta

# A dictionary to keep track of the body and its distance from earth in miles
# TODO: Add pluto
planets = { "the sun" : 9.296e7,
            "mercury" : 9.2026e7,
            "venus"   : 2.03573e8,
            "jupiter" : 4.83835e8,
            "saturn"  : 8.87542e8,
            "uranus"  : 1.78382e9,
            "neptune" : 2.794902e9,
            "mars"    : 1.41386e8}

vehicles =     {"ford f 150" : 60,
                "boeing 747" : 570,
                "apollo 11"  : 25000,
                "cruise ship": 27,
                "walking"    : 3,
                "bicycle"    : 16,
                "unicycle"   : 11,
                "running"    : 6,
                "submarine"  : 23,
                "riding on a house fly" : 5}
               

def select_location():
    print("please select a location to travel to!")
    print()
    for planet in planets:
        print(planet.upper())
    print()

    planet_selection = input("Type your selection: ").lower()

    if planet_selection not in planets:
        print()
        print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
        print("➡ Selection Not valid, please enter a selection from the list⬅")
        print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
        print()
        planet_selection = select_location()

    num = planets[planet_selection]

    print()
    print("You chose:", planet_selection.upper(), "This bodhgy is", (f"{num:,}"), "Miles from Earth\n\n")
    return planet_selection




def select_vehicle():
    print("Choose your mode of transportation")
    for v in vehicles:
        print(v.upper())
    print()

    vehicle_selection = input("Type your selection: ").lower()


    if vehicle_selection not in vehicles:
        print()
        print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
        print("➡ Selection Not valid, please enter a selection from the list⬅")
        print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
        print()
        vehicle_selection = select_vehicle()

    mode_num = vehicles[vehicle_selection]
        
    print()
    print("You chose to go to", planet_selection.upper(), "by" ,vehicle_selection.upper(), "travling with a avg speed of", (f"{mode_num:,}"), "MPH")
    print()
    return vehicle_selection


def start_new_location():
    while(1):
        print()
        answer = input("Would you like to run a new calculation?: ").lower()
        print ()
        if answer == "yes":
            return 1
        elif answer == "no":
            print()
            print("------------------------------------")
            print(" Thank you for travaling with us!!")
            print("------------------------------------")
            print()
            print()
            print()
            exit(1)
        else: 
            print("Please type 'Yes' or 'No'")
    

def calculate():
    pass

print("----------------------------------")
print("Hello welcome to my final project!")
print("----------------------------------")
name = input("To begin enter your name: ")
print("Hello", name, )
print()

do_we_restart = 0
while(1):

    if not do_we_restart:
        planet_selection = select_location()

        vehicle_selection = select_vehicle()

    hours = planets[planet_selection] / vehicles[vehicle_selection]

    y = hours / 8760

    today = datetime.today()

    today_year = today.year
        
    days = hours / 24.0

    hours = hours % 24.0

    years = days / 365

    days = days % 365    

    weeks = days / 7        

    days = int(days % 7) 

    century = years / 100

    arriaval_year = int(today_year + y)
    

    if century > 1: 
        print("You will make it to", planet_selection, "in", int(century), "centuries", int(years % 100), "years", int(weeks), "weeks", int(days), "days and", int(hours), "hours, year of arrival is: ", arriaval_year )
        print()

    elif years > 1:
        print("You will make it to", planet_selection, "in", int(years), "years", int(weeks), "weeks", int(days), "days and", int(hours), "hours, year of arrival: ", arriaval_year )
        print()

    else:
        print("You will make it to", planet_selection, "in", int(weeks), "weeks", int(days), "days and", int(hours), "hours, year of arrival: ", arriaval_year)
        print()
    
    while(1):
        answer = input("Would you like to select another vehicle?: ").lower()
        print()

        if answer == "yes":
            vehicle_selection = select_vehicle()
            do_we_restart = 1
            break

        elif answer == "no":
            do_we_restart = 0
            break
        else:
            print("Please type 'Yes' or 'No'")
            print()

            

    if do_we_restart:
        continue
    else:
        start_new_location()
