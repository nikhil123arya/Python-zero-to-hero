# while loop 
def days_to_hours(days):
  return f"{days} days have {days * 24} hours"


def validate_and_execute():
  try:
      user_input_num = int(num_of_days)
      if user_input_num > 0:
        calculated_hours = days_to_hours(user_input_num)
        print(calculated_hours)
      elif user_input_num == 0:
        print("You entered a 0, please enter a valid postive integer")
      else:
        print("You entered a negative number. try again!")

  except ValueError:
    print("Your Input is not a valid Number, Don't try Blow up my program!")

user_input = ''
while user_input != "exit":
  user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
  for num_of_days in user_input.split(","):
   validate_and_execute()

# list 
# for loop : is used for iterating over a sequence like a list
