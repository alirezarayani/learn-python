from email import message

age = input("What is your current age?")
age_as_input = int(age)
years_remaining = 90 - age_as_input
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)