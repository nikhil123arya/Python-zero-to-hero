# To validate user input we need to check it to avoid program execution failure
# Conditional statements can have two values: Ture or False
# Boolean Data Type: True/False

def days_to_hours(days):
  return f"{days} days have {days * 24} hours"


user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")

def validate_and_execute():
  if user_input.isdigit():
      user_input_num = int(user_input)
      if user_input_num > 0:
        calculated_hours = days_to_hours(user_input_num)
        print(calculated_hours)
      elif user_input_num == 0:
        print("You entered a 0, please enter a valid postive integer")
  else:
    print("Your Input is not a valid Number, Don't try Blow up my program!")


validate_and_execute()
  
# print(type("this should be of type string"))

# Nested if/else