# A dictionary to keep track of the body and its distance from earth in miles
# TODO: Add pluto
planets = { "sun"     : 91.4e6,
            "mercury" : 48e6,
            "venus"   : 36e6,
            "earth"   : 0,
            "jupiter" : 365e6,
            "saturn"  : 746e6,
            "uranus"  : 1.6e9,
            "neptune" : 2.7e9}
vechles =     {"car" : 80,
             "plane" : 600,
          "spaceship": 1000}


print("----------------------------------")
print("Hello welcome to my final project!")
print("----------------------------------")
name = input("To begin enter your name: ")
print()
print("Hello", name, "please select a location to travel to!")
print()

while(1):
    for planet in planets:
        print(planet.upper())

    planet_selection = input().lower()

    if planet_selection not in planets:
        print("Selection Not valid, please enter a selection from the list")
        continue

    print("You chose: " , planet_selection.upper(), " This body is ", planets[planet_selection], "Miles away from Earth\n\n")

    print("Choose your mode of transportation")
    for v in vechles:
        print(v.upper())

    vechle_selection = input().lower()

    if vechle_selection not in vechles:
        print("Selection Not valid, please enter a selection from the list")
        continue

    print("You chose the" ,vechle_selection.upper(), "travling at", vechles[vechle_selection], "MPH")
    print()

    t = planets[planet_selection] / vechles[vechle_selection]

    days = t / 24.0

    years = days / 365

    if years > 1:
        print("It took you", round(years, 3), "years to get to", planet_selection, "using the", vechle_selection)
    else:
        print("It took you", round(days, 3), "days to get to", planet_selection, "using the", vechle_selection, "...")


    while(1):
        print()
        answer = input("Would you like to travle to anoter planet?: ").lower()
        if answer == "yes":
            break
        elif answer == "no":
            print()
            print("thank you for travaling with us")
            exit(1)
        else: 
            print("Please type 'Yes' or 'No'")
