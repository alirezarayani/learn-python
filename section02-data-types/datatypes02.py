num_char = len(input("What is your name? "))
# print("your name has " +  num_char + " characters.") can only concatenate str (not "int") to str

print(type(num_char))

new_num_char = str(num_char)

print("your name has " + new_num_char + " characters.")
