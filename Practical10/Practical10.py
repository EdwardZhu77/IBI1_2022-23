#Task 1: Mortgage affordability calculator
def Mortgage_affordability_calculator(annual_salary,value_of_the_house):
    annual_salary = int(annual_salary)
    value_of_the_house = int(value_of_the_house)
    if annual_salary*5 < value_of_the_house:
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

#Task 2: Triathlon times database
class Triathlon_time:
    def __init__(self, name, location, swim_time, cycle_time, run_time):
        self.name = name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_record(self):  
        print(f'{self.name} {self.location} {self.swim_time} {self.cycle_time} {self.run_time} {self.total_time}')  
        
    def __str__(self):
        return (f'{self.name}, {self.location}. Swim time: {self.swim_time}, Cycle time: {self.cycle_time}, Run time: {self.run_time}, Total time: {self.total_time}')  

record1 = Triathlon_time("Freddie_Mercury", "London", 30, 40, 35)
print(record1)

record2 = Triathlon_time(name=input("the name of athlete: "),  
                         location=input("the location: "),  
                         swim_time=int(input("Enter swim time: ")),
                         cycle_time=int(input("Enter cycle time: ")),  
                         run_time=int(input("Enter run time:")))
print(record2)
#Task 3: Protein-coding capability calculator
def coding_sequence(dna):

    dna = dna.upper()
    try: 
        start_idx = dna.index('ATG')
        stop_idx = dna.index('TGA')
    except ValueError:
        return 0, 'invalid DNA sequence'

    coding_region = stop_idx - start_idx + 3 
    total_length = len(dna)
    coding_percentage = (coding_region / total_length) * 100  

    if coding_percentage > 50:
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 10:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'  

example = coding_sequence('atgCTgCtGcTcccTcTcaccattTGAccTGaGtAAcTtat') 
print(example)

dna_seq = input("Enter the DNA sequence to check: ") 
example2 = coding_sequence(dna_seq)
print(example2)


