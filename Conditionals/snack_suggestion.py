# A local cafe wants a program that suggests a snack.
# If a custumer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not abailable.
# Task: 
#  1. Take Snack input
# 2. If it's "cookies" or "samosa", confirm the order.
# 3. Else, show unavailability

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We'll serve you {snack}")
else: 
    print(f"Sorry, we work serve cookies or samosa with tea :(")