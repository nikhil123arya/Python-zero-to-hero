# function
# => A function is defined using def keyword.
# => Block of code which only runs when it is called.
# => Calling a function = to execute the function.

# Parameters
# => information can be passed into function as parameters 


cal_to_unit = 24
unit = "hours"

def days_to_units():
  print(f"20 days are {20 * cal_to_unit} {unit}")
  print('All good!')
  print('All this is inside a funtion.')
  
  
def days_to_units_1(no_of_days):
  print(f"{no_of_days} days are {no_of_days * cal_to_unit} {unit}")
  print('All good!')


def days_to_units_2(no_of_days, custom_message):
  print(f"{no_of_days} days are {no_of_days * cal_to_unit} {unit}")
  print(custom_message)


# days_to_units()

# days_to_units_1(10)
# days_to_units_1(35)
# days_to_units_1(50)
# days_to_units_1(120)

days_to_units_2(33, 'Awesome')
days_to_units_2(12, "looks good")