#Task 2: Triathlon times database
class Triathlon_time:
    def __init__(self, name, location, swim_time, cycle_time, run_time): # Define the function to work with the data
        self.name = name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_record(self):  # Define the function to work with the data
        print(f'{self.name} {self.location} {self.swim_time} {self.cycle_time} {self.run_time} {self.total_time}')  
        
    def __str__(self):  # Define the function to work with the data
        return (f'{self.name}, {self.location}. Swim time: {self.swim_time}, Cycle time: {self.cycle_time}, Run time: {self.run_time}, Total time: {self.total_time}')  

record1 = Triathlon_time("Freddie_Mercury", "London", 30, 40, 35) # Random name :)
print(record1)

record2 = Triathlon_time(name=input("the name of athlete: "),   # Input part for the user
                         location=input("the location: "),  
                         swim_time=int(input("Enter swim time: ")),
                         cycle_time=int(input("Enter cycle time: ")),  
                         run_time=int(input("Enter run time:")))
print(record2)