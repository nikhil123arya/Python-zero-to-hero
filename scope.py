# Scope
# => A variable is only avaliable from inside the region it is created.
# => Global scope = variable avaliable from within any scope
# => Local scope = variable created inside function

units = 24

def test(no_of_days):
  print(no_of_days)
  

def scope_check(no_of_days):
  my_var = "variable inside function."
  print(units)
  print(no_of_days)
  print(my_var)


scope_check(23)
