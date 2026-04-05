# Task 1: Format Function
def format_example(a, b):
    result = "First value is {} and second value is {}".format(a, b)
    return result

print(format_example(145, 'o'))


# Task 2: Pond Area and Water Calculation
pi = 3.14
r = 84

area = pi * r * r
print("Area of pond:", int(area))

water_per_sqm = 1.4
total_water = area * water_per_sqm
print("Total water in pond:", int(total_water))


# Task 3: Speed Calculation
distance = 490
time = 7 * 60  # convert minutes to seconds

speed = distance / time
print("Speed (m/s):", int(speed))

