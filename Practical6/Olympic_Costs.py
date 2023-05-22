# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the number of data points
N = 8

# Olympic Games and corresponding cost
olympic_games = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
costs = [1, 8, 15, 7, 5, 14, 43, 40]
data = list(zip(olympic_games, costs))

# Sort the data based on cost
sorted_data = sorted(data, key=lambda x: x[1])

# Extract sorted games and costs from sorted data
sorted_olympic_games = [game for game, cost in sorted_data]
sorted_costs = [cost for game, cost in sorted_data]

# Set up the plot
ind = np.arange(N)
width = 0.35
pl = plt.bar(ind, sorted_costs, width)

# Set the title and axis labels for the plot
plt.ylabel('Costs (in $ billions)')
plt.title('Olympic Costs')
plt.xticks(ind, sorted_olympic_games, rotation=45)

# Set the length and scale of the vertical axis
plt.yticks(np.arange(0, 51, 10))

# Display the plot
plt.show()

# Print the costs
print(sorted_costs)
