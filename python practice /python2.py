# Dictionary with people's names as keys and their heights as values
ride = {
    "Alice": 120,
    "Bob": 95,
    "Charlie": 105,
    "Diana": 85,
    "Eve": 110
}

# For loop to check each person's height
for x in ride:
    height = ride[x]
    if height >= 100:
        print("{x} is tall enough to ride.")
    else:
        print(f"{person} is too short to ride.")
