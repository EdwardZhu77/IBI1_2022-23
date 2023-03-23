data = "1 billion dollars, 8 billion dollars, 15 billion dollars, 7 billion dollars, 5 billion dollars, 14 billion dollars, 43 billion dollars, 40 billion dollars"
# plit the data string into a list of strings
# the cost for specific years.
cost_strings = data.split(", ")
# extract the cost for each year and store them in a new list
costs = []
for cost_string in cost_strings:
    # remove the "billion dollars"
    # part and convert the remaining string to a float.
    cost = float(cost_string.split(" ")[0])
    # Append the cost to the list.
    costs.append(cost)
print(costs)
