# We want no mor than 100 rabbits
# We could know the number of rabbit is in exponential growth
n = 1   # number of generation
m = 2**n   # C
while m < 100:
    n = n + 1 # next generation
    m = 2**n # number of generation
print(n-1)   # number of generation
