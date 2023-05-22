#Task 1: Mortgage affordability calculator
def Mortgage_affordability_calculator(annual_salary,value_of_the_house): # Define the function 
    annual_salary = int(annual_salary) # It should be the number!
    value_of_the_house = int(value_of_the_house) # It should be the number!
    if annual_salary*5 < value_of_the_house: # The judgement part
     print("No")
    else:
     print("Yes")
     return
#From personal interest, I will show whether the mortgage affordability calculator is suitable for the situation in China (roughly estimation)
'''From the National Bureau of Statics in China, the average annual salary is 62448RMB, the housing space per capita is 41 m^2 and average house price is 10140RMB/m^2.
If we consider a family of three as a base unit, assuming two of the three have stable income jobs, then the average annual income of the family is 62448*2=124996RMB, 
their house area is 41*3=123m^2, then the total price of their house is 123*10140=1247220RMB.'''
annual_salary = 124996
value_of_the_house = 1247220
Mortgage_affordability_calculator(annual_salary,value_of_the_house)
#The answer is definite NO, Chinses people can not afford their house with their five years salary
#You can try what you want check in the following part
annual_salary = input("Enter the annual salary to check whether the purchaser can buy the house: ")
value_of_the_house = input("Enter the value of the house to check whether the purchaser can buy the house: ")
Mortgage_affordability_calculator(annual_salary,value_of_the_house)