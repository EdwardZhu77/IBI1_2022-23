# Importing some essenital libraries for working, visualizing and analysing the data
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Changing the working directory to the place of the data 
os.chdir("E:\study files (python)\IBI\IBI Practical")
'''Important point for task'''

#we use the pandas library to read the content of the .csv file into a dataframe object. and call our dataframe covid_data
covid_data = pd.read_csv("full_data.csv")
covid_data.head()
covid_data.info()
covid_data.describe()

#showing the second column from every 100th row from the first 1000 rows (inclusive)
covid_data.iloc[0:1001:100,1]  # exclude the line 1001

#Create a boolean value, True when the location is "Afghanistan", False otherwise and use this boolean value to find the desired row in the data box
location = covid_data["location"]  
Afghanistan_boolean = location == "Afghanistan"
Afghanistan_cases = covid_data[Afghanistan_boolean]["total_cases"]
#or Afghanistan_cases = covid_data.loc[Afghanistan_boolean, :] (?)

#Create a boolean value, True when the date is "2020-03-31", False otherwise and use this boolean value to find the desired row in the data box
date = covid_data["date"]  
March_31_2020_boolean = date == "2020-03-31"
March_31_2020_cases = covid_data.loc[March_31_2020_boolean, :]

#Create a boolean value, True when the location is "world", False otherwise and use this boolean value to find the desired row in the data box
country = covid_data["location"]  
World_boolean = country == "World"
World_cases = covid_data[World_boolean]  

#use numpy to compute the mean new cases and new deaths on this date (March_31_2020)
new_cases = March_31_2020_cases["new_cases"]
new_deaths = March_31_2020_cases["new_deaths"]
mean_cases = np.mean(new_cases)
print(mean_cases)
mean_deaths = np.mean(new_deaths)
print(mean_deaths)

#Plot the new cases and new deaths on 31 March as two separate box plots by using Matplotlib's boxplot() function
plt.boxplot(March_31_2020_cases.loc[:,"new_cases"])
plt.title("New cases of countries on 31 March 2020")
plt.show()
plt.boxplot(March_31_2020_cases.loc[:,"new_deaths"])
plt.title("New deaths of countries on 31 March 2020")
plt.show()
'''!!!still need to be checked!!!'''

#Plot the new cases and new deaths across the world over time as two separate box plots by using Matplotlib's boxplot() function
world_dates = World_cases.loc[:,"date"]  
world_new_cases = World_cases.loc[:,"new_cases"]
world_new_deaths = World_cases.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_cases, 'ro',markersize = '5')#red circle
plt.plot(world_dates, world_new_deaths, 'bo',markersize = '5')#blue circle
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title("The new cases and new deaths across the world over time")
plt.show()
'''!!!still need to be checked!!!'''

# Plot both new cases and total cases over time in China (Answer the question stated in file question.txt)
China_dates = covid_data.loc[:,"date"]  
China_new_cases = covid_data.loc[:,"new_cases"]
China_new_deaths = covid_data.loc[:,"new_deaths"]
plt.plot(China_dates, China_new_cases, 'ro',markersize = '5')#red circle
plt.plot(China_dates, China_new_deaths, 'bo',markersize = '5')#blue circle
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title("The new cases and new deaths in China over time")
plt.show()
