# Importing module of the regular expression
import re

# Open input file containing DNA sequences
data = open("E:\study files (python)\IBI\IBI Practical\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
# Create output file for TGA stops genes
output = open("E:\study files (python)\IBI\IBI Practical\TGA_genes.fa", "w")  #"w" for writing mode

# Initialize an empty string to store the needed DNA sequence
sequence = ""

# We need a loop to scan through lines and split the part we don't want
for line in data:
 # The feature of being a new gene sequence is that the new gene sequence starts with ">"
 if line.startswith(">"):
  gene = re.split("\s", line, 1)[0]# The gene's name is the first phrase befor all the blanks, extract and get it 
  # The previous sequence ends with stop codon
  if re.search("TGA$", sequence):
   #write the sequence to the output file
   output.write(sequence)
  # Reset for the new gene
  sequence = ""
  # Reset the count of lines in the sequence to zero
  count = 0
 elif not line.startswith(">"): # The feature of being a new gene sequence is that the new gene sequence starts with ">"
        count += 1 # Go to the next line
        # Add the gene ID , if this is the first line
        if count == 1:
            sequence += gene + "\n"
        # Add the sequence data to the sequence string
        sequence += line

# Close the input and output files
data.close()
output.close()
#Most important things:
#The useless information just in one line!  And starts with ‘>’! 
#"cdna + ]" might be failed cause some information is in different format!