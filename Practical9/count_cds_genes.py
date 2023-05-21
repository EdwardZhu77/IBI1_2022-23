# Importing module of the regular expression
import re

# Asks the user to input one of the three stop codons 
stop_codon = input("Enter one stop codon (TAA, TAG or TGA): ")

# Name the output file 
output = stop_codon + "_stop_genes.fa" #If the given stop codon is ‘TAA’ the output file should be ‘TAA_stop_genes.fa’

# Open the input file
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")  # It is "E:\study files (python)\IBI\IBI Practical\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa" in my computer
output = open(output, "w")

# Initialize an empty string to store the needed DNA sequence
sequence = "" 
count = 0

# We need a loop to scan through lines and split the part we don't want
for line in data:
# If it is a new gene, extract the gene name and reset the variable 
    if line.startswith(">"):
        gene = re.split("\s", line, 1)[0] 
        sequence = ""
        count = 0
# Otherwise, add the rows to the sequence and increment the count
    else:
        count += 1
        sequence += line  
        
# If the sequence ends with a stop codon, write it to the output file in FASTA format
    if re.search(stop_codon + "$", sequence):
        output.write(">"+gene+"_"+str(count)+"\n")
        output.write(sequence + "\n")

# Close the input and output files
data.close()
output.close()