# Two goals
# Create a dictionary
# Drae a pie chart
myDict = {
    'Comedy': '73',
    'Action': '42',
    'Romance': '38',
    'F}antasy': '28',
    'Science-fiction': '22',
    'Horror': '19',
    'Crime': '18',
    'Documentary': '12',
    'History': '8',
    'War': '7'} # Create a dictionary
print('Comedy:', myDict['Comedy']) # the number of people who like comedy
import matplotlib.pyplot as plt # use pyplot
myDict = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}
labels = list(myDict.keys())
values = list(myDict.values()) # use the data from the dictionary
fig, ax = plt.subplots() # create figure
ax.pie(values, labels=labels, autopct='%1.1f%%') # pie chart create
ax.set_title('Favourite movie genres among Chinese university students') # create title
plt.show() # show the chart
