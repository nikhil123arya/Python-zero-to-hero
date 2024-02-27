# input()
# => To ask the user for an input.
# => Buit-in function provided by python language itself
# => input is sting type value

user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
user_input_number = int(user_input)


# function return a value

def days_to_hours(day):
  return f"{day} days have {day * 24} hours"

result = days_to_hours(user_input_number);
print(result)

