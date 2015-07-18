'''
Title: Transcribing DNA into RNA 
ID: RNA

'''

def dna_to_rna(dna):
    #Translates DNA sequence to RNA sequence
    return dna.replace('T', 'U')


def main():

    #Read input
    with open('data/0002_RNA.txt') as input:
        dna = input.read().strip()

    # Translate DNA to RNA
    rna = dna_to_rna(dna)

    # Print and save the answer.
    print (rna)
    with open('output/0002_RNA.txt', 'w') as output:
        output.write(rna)

if __name__ == '__main__':
    main()
