'''
Title: Counting DNA Nucleotides
ID: DNA

'''

from collections import Counter

def nucleotide_count_dna(dna):

    #Returns the count of each nucleotide in DNA sequence
    nucleotide_count = Counter(dna)
    return [nucleotide_count[nucleotide] for nucleotide in 'ACGT']

def main():

    #Read input
    with open('data/0001_DNA.txt') as input:
        dna = input.read().strip()

    #Get count of each nucleotide in DNA sequence
    nucleotide_count = map(str, nucleotide_count_dna(dna))

    #Print and save the answer.
    print (' '.join(nucleotide_count))
    with open('output/0001_DNA.txt', 'w') as output:
        output.write(' '.join(nucleotide_count))
		
if __name__ == '__main__':
    main()
