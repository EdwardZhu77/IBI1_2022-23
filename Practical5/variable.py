# Store the longitude of Edinburgh as a
a = -3.19
# Store the longitude of Los Angeles as b
b = -118.24
# Store the longitude of Haining as c
c = 116.39
d = abs(a-b) # Calculate the longitude distance  as the difference between a and b. Store this value in a variable called d, abs for absolute value.
e = abs(c-a) # Calculate the longitude distance  as the difference between and a c. Store this value in a variable called e, abs for absolute value.
if d < e: print("e is greater than d and Rob travel further to Los Angeles")
else: print("d is greater than e and Rob travel further to Haining")
# Create variable X to store Boolean variables True
X = True
# Create variable Y to store Boolean variables False
Y = False
# Creat W to encode the Boolean variables “X an Y"
W = X and Y
# Creat Z to encode the Boolean variables “X or Y"
Z = X or Y

# Print the value of W and Z separately
print("The value of W is " , W) # Value of W
print("The value of Z is " , Z) # Value of Z
