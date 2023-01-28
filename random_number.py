# This program shows how to generate a random number in a given range

import random

# We're going to generate 5 random numbers from 1 to 10
num = 5 

for i in range(1,num+1):
  # randrange parms:  start number, end number, step size.   
  # end number works like "range"....so it's not inclusive.
  # So this one does random numbers form 1 to 10.
  random_number = random.randrange(1, 11, 1)
  print("Number ", i, " is ", random_number) 
