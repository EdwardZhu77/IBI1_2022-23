# We want no more than 100 rabbits
# We could know the number of rabbit is in exponential growth
# Initialize the number of rabbits to 2
# Initialize the generation counter to 1
generation = 1   # Number of generation
number_of_rabbits = 2 # Number of rabitts
# Use a while loop to simulate rabbit breeding
while number_of_rabbits <= 100:
    # Next generation
	number_of_rabbits *= 2
    # Next generation
	generation += 1
   
# Print a message stating the generation at which the total number of rabbits exceeds 100
print ("At generation", generation ,"over 100 rabits have been born")
