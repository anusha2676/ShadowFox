# ShadowFox Internship - If Condition Task

# -------------------------------
# Task 1: BMI Calculator
# -------------------------------

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# -------------------------------
# Task 2: City to Country
# -------------------------------

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found in the list")


# -------------------------------
# Task 3: Same Country Check
# -------------------------------

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

def get_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2:
    if country1 == country2:
        print("Both cities are in", country1)
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found in the list")
