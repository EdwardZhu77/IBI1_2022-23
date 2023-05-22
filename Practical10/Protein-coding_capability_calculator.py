#Task 3: Protein-coding capability calculator
def coding_sequence(dna):   # Define the function to work with the data

    dna = dna.upper() # Captialize the dna
    try: 
        start_idx = dna.index('ATG')
        stop_idx = dna.index('TGA')
    except ValueError:
        return 0, 'invalid DNA sequence'

    coding_region = stop_idx - start_idx + 3 # Restrict the region
    total_length = len(dna) # Make it as number
    coding_percentage = (coding_region / total_length) * 100  

    if coding_percentage > 50:
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 10:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'  

example = coding_sequence('atgCTgCtGcTcccTcTcaccattTGAccTGaGtAAcTtat') # Mixed upper and lower case letters
print(example)

dna_seq = input("Enter the DNA sequence to check: ") # Input by user
example2 = coding_sequence(dna_seq)
print(example2)