print("Welcome to the tip calculator!.")
bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = tip / 100 * bill + bill
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
message = f"Each person should pay: ${final_amount}"

print(message)
