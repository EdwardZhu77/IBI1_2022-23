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

 import matplotlib.pyplot as plt # open pyblot
>>>
>>> data = [("Los Angeles 1984", 1),
...         ("Seoul 1988", 8),
...         ("Barcelona 1992", 15),
...         ("Atlanta 1996", 7),
...         ("Sydney 2000", 5),
...         ("Athens 2004", 14),
...         ("Beijing 2008", 43),
...         ("London 2012", 40)]
>>> data.sort(key=lambda x: x[1])
>>> x_labels = [x[0] for x in data]
>>> y_values = [x[1] for x in data] # similar to dictionary
>>>
>>> plt.bar(x_labels, y_values)
<BarContainer object of 8 artists>
>>> plt.xlabel("City") # x axi
Text(0.5, 0, 'City')
>>> plt.ylabel("Cost (billion dollars)") # y axi
Text(0, 0.5, 'Cost (billion dollars)')
>>> plt.title("Cost of Hosting the Summer Olympic Games")
Text(0.5, 1.0, 'Cost of Hosting the Summer Olympic Games')
>>> plt.show() # show the chart
