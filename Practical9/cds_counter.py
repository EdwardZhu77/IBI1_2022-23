# Importing module of the regular expression
import re

# Defining the given DNA sequence
seq = 'ATGCAATCGACTACGATCTGAGGGCCTAA' 

# Initialize a variable count the number of possible stop codons
Possible_Number = 0

# Define the start codon and stop codons
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

# Use loop to find the total number of possible coding sequences
for i in range(len(seq)):
 if seq[i:i+3] == start_codon:
  for stop_codon in stop_codons:  #In this code, stop_codons has been defined as a list containing 3 stop_codon 's'
    if stop_codon in seq[i+3:]:
      Possible_Number += 1 #Add 1 to the total number of possible coding sequences

#Print the whole outcome               
print("The total number of possible coding sequences is ", Possible_Number)
#It seems not necessary to use the regular expression :)