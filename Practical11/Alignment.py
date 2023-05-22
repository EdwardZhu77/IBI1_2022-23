#open file in my own computer
import os
os.chdir("E:\study files (python)\IBI\IBI Practical")

# Open and read the BLOSUM62 matrix file 
BLOSUM62 = open("BLOSUM62.txt")  # In this way, we can not directly use the .xlsx file

# Read the matrix file line by line and store in a list, 
# removing newline characters 
BLOSUM62_matrix = BLOSUM62.readlines()[6:]
BLOSUM62_matrix = [line.rstrip() for line in BLOSUM62_matrix]

# Initialize the dictionary
blosum62 = {}

# Populate the dictionary with keys as amino acid pairs and values
# as the corresponding score from the BLOSUM62 matrix
# Extract the amino acid keys and matrix values from the list
# Keys are the first row, values are the remaining rows
for i in range(1, len(BLOSUM62_matrix)):
    BLOSUM62_matrix[i] = BLOSUM62_matrix[i].split()[1:]
keys = BLOSUM62_matrix[0].replace(" ","")
values = BLOSUM62_matrix[1:]

# Construct the dictionary
for i in range(0, len(keys)):
    for j in range(0, len(keys)):
        blosum62[(keys[i], keys[j])] = int(values[i][j])
# Open the FASTA files containing ACE2 sequences for human, mouse and cat
human = open("ACE2_human.fa")  
mouse = open("ACE2_mouse.fa")
cat = open("ACE2_cat.fa")

# Read the sequences from the FASTA files 
cat_seq = cat.readlines()
mouse_seq = mouse.readlines()
human_seq = human.readlines()

# Define a function to perform global alignment between two sequences 
def global_align(seq1, seq2):  
    #Perform global alignment between two sequences seq1 and seq2.
    
    # Extract sequence names and sequences from the FASTA format 
    Seq1_name = seq1[0]
    Seq1 = seq1[1].rstrip()
    Seq2_name = seq2[0]
    Seq2 = seq2[1].rstrip()

    # Initialize score and count of identical positions to 0 
    score = 0
    same = 0
    
    # Compare the two sequences by zipping them together
    compair = list(zip(Seq1, Seq2))  
    
    for pair in compair:
        if pair[0]==pair[1]:
            same += 1
        score += blosum62[pair]
    per = same/len(Seq1)*100
 
    # Print the alignment results
    print("Seq: ")
    print(Seq1_name+Seq2_name, end = "")
    print("Alignment Matrix: BLOSUM62")
    print("Alignment Score:", score)
    print("Identical Percentage:", per)
    print()
    
    # Return the alignment score
    return score

# Perform global alignment for all three pairs of sequences 
hc_score = global_align(cat_seq, human_seq)
hm_score = global_align(human_seq, mouse_seq)
cm_score = global_align(cat_seq, mouse_seq)
cat.close()
mouse.close()
human.close()