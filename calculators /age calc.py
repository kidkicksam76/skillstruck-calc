
big_age = int(input("what the oldest persons age in years"))
small_age = int(input("what the youngest persons age in years"))
age_gap = big_age - small_age

if age_gap <= 3:
    print("you have a normal age gap")
if age_gap < 3:
    print("your below the average age gap")
else:
    print("your above the average age gap")

