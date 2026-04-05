# ShadowFox Internship - Dictionary Task

# -------------------------------
# Task 1: List of friends and name lengths
# -------------------------------

friends = ["Anusha", "Rahul", "Sneha", "Kiran", "Meena"]

name_lengths = []

for name in friends:
    name_lengths.append((name, len(name)))

print("Friends and name lengths:")
print(name_lengths)


# -------------------------------
# Task 2: Expense Tracker
# -------------------------------

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expense:", your_total)
print("Partner total expense:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more money")
elif partner_total > your_total:
    print("Your partner spent more money")
else:
    print("Both spent the same amount")

# Find highest difference category
max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    
    if diff > max_diff:
        max_diff = diff
        max_category = category

print("Highest difference in category:", max
