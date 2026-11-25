
n = int(input("Enter number of expenses: "))

total = 0
largest_expense = 0
largest_category = ""

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter amount in foreign currency: "))
    rate = float(input("Enter exchange rate: "))

    fee = amount * rate * 0.02
    converted = amount * rate + fee

    print("Converted amount in INR:", converted)

    total = total + converted

    if converted > largest_expense:
        largest_expense = converted
        largest_category = category

budget = float(input("\nEnter total budget in INR: "))

print("\n----- TRAVEL BUDGET SUMMARY -----")
print("Total expenses in INR:", total)
print("Largest expense category:", largest_category)
print("Largest expense amount:", largest_expense)

if total <= budget:
    print("Status: Within budget")
else:
    print("Status: Budget exceeded")
    print("Extra amount needed:", total - budget)

print("--------------------------------")
