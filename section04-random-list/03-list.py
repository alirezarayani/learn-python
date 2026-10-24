#List is the way of organizing and storing data
fruits = ["kiwi fruits","oranges"]
state_of_iran = ['Yazd',"Tehran"]

print(state_of_iran[0])

state_of_iran[0] = "kerman"
print(state_of_iran[0])

print(state_of_iran[-1])

print(f"state of Iran: {state_of_iran}")

state_of_iran.append("Mashahad")

print(f"state of Iran: {state_of_iran}")


state_of_iran.extend(["Sari"])

print(f"state of Iran: {state_of_iran}")


print(state_of_iran.pop())