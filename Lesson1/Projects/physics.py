# 12/20/2018
# Reviewing functions
# All the constants were provided.
# The goal is to create functions that calculates Celsius/Fahrenheit conversion,
# force, energy and work.

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# c is the constant for speed of light
c = 3*10**8

# Converts Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Converts Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

# Calculates force
def get_force(mass, acceleration):
  return mass * acceleration

# Calculates energy
def get_energy(mass):
  return mass * (c**2)

# Calculates work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

# Converting 100 degrees fahrenheit to celsius
f100_in_celsius = f_to_c(100)

# Converting 0 degrees celsius to fahrenheit
c0_in_fahrenheit = c_to_f(0)

# Calculating force outputted by train
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Calculating energy of bomb
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Calculating work done by train
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) +
      " Joules of work over " + str(train_distance) + " meters.")
