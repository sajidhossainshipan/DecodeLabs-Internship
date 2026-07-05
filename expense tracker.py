print("===== Expense Tracker =====")

total = 5050.0

while True:
    expense = float(input("Enter expense amount: "))
    total += expense

    choice = input("Do you want to add another expense? (yes/no): ").lower()

    if choice == "no":
        break

print("\n===== Expense Summary =====")
print(f"Total Spent: {total}")