from datetime import datetime, timedelta

# A dictionary to keep track of the body and its distance from earth in miles
# TODO: Add pluto
planets = { "the sun"     : 91.4e6,
            "mercury" : 48e6,
            "venus"   : 36e6,
            "earth"   : 0,
            "jupiter" : 365e6,
            "saturn"  : 746e6,
            "uranus"  : 1.6e9,
            "neptune" : 2.7e9}
vehicles =     {"ford f 150" : 120,
                "boeing 747" : 570,
                "apollo 11"  : 25000,
                "cruise ship": 27,
                "walking"    : 3,
                "bicycle"    : 16}
   


print("----------------------------------")
print("Hello welcome to my final project!")
print("----------------------------------")
name = input("To begin enter your name: ")
print("Hello", name, )
print()


while(1):
    print("please select a location to travel to!")
    print()
    for planet in planets:
        print(planet.upper())

    planet_selection = input().lower()

    if planet_selection not in planets:
        print("Selection Not valid, please enter a selection from the list")
        continue

    print()
    print("You chose: " , planet_selection.upper(), " This body is ", planets[planet_selection], "Miles away from Earth\n\n")

    print("Choose your mode of transportation")
    for v in vehicles:
        print(v.upper())

    vehicle_selection = input().lower()

    if vehicle_selection not in vehicles:
        print("Selection Not valid, please enter a selection from the list")
        continue

    print()
    print("You chose to go by" ,vehicle_selection.upper(), "travling with a avg speed of", vehicles[vehicle_selection], "MPH")
    print()

    hours = planets[planet_selection] / vehicles[vehicle_selection]

    d1 = datetime.today()
    d2 = d1 + timedelta(days = hours / 24.0)
    
    days = hours / 24.0

    years = days / 365

    leftover_days = days % 365    

    weeks = leftover_days / 7        

    new_leftover_days = leftover_days % 7  

    not_whole_days = days - int(days)   

    days = int(days)    

    decade = years / 10

    century = decade /10


    if century > 1: print("if you leave now it will take you", round(century, 2), "Centuries to get to", planet_selection, "your ETA is", d2)

    elif decade > 1: print("if you leave now it will take you", round(decade, 3), "decades to get to", planet_selection, "your ETA is", d2  )

    elif years > 1:
        print("if you leave now it will take you", round(years, 3), "years to get to", planet_selection, "your ETA is", d2 )

    else:
        print("You will make it to", planet_selection, "in", int(years), "years", int(weeks), "weeks", days, "days and", int(hours), "your ETA is", d2 )


    while(1):
        print()
        answer = input("Would you like to travle to anoter location?: ").lower()
        print ()
        if answer == "yes":
            
            break
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

