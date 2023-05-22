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
labels = list(myDict.keys())
values = list(myDict.values()) # use the data from the dictionary
# Create the pie chart and display it
plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()


# Ask the user for a movie genre
msg = input("Movie genre: ")
# print the number of students for which this genre is their favourite from the dictionary
dictionary[msg]
