# ShadowFox Internship - For Loop Task

import random

# -------------------------------
# Task 1: Dice Simulation
# -------------------------------

rolls = []
count_6 = 0
count_1 = 0
two_sixes = 0

# Roll dice 20 times
for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1

# Check two consecutive 6s
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        two_sixes += 1

print("Rolls:", rolls)
print("Number of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Two consecutive 6s:", two_sixes)


# -------------------------------
# Task 2: Jumping Jacks Workout
# -------------------------------

total_jumps = 100
completed = 0

for i in range(1, total_jumps + 1, 10):
    completed += 10

    tired = input("\nAre you tired? (yes/y or no/n): ")

    if tired.lower() in ["yes", "y"]:
        skip = input("Do you want to skip remaining sets? (yes/y or no/n): ")

        if skip.lower() in ["yes", "y"]:
            print("You completed a total of", completed, "jumping jacks")
            break
    else:
        remaining = total_jumps - completed
        print("Remaining jumping jacks:", remaining)

    if completed >= total_jumps:
        print("Congratulations! You completed the workout")
