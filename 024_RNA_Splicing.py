'''
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

'''

def parse_fasta(data):
    sequences = {}
    label = None
    for line in data.splitlines():
        if line.startswith(">"):
            label = line[1:]
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def dna_to_protein(data):

    sequences = parse_fasta(data)

    dna_seq = list(sequences.values())[0]

    introns = list(sequences.values())[1:]

    for intron in introns:
        dna_seq = dna_seq.replace(intron, "")
    
    rna_seq = dna_seq.replace("T", "U")

    codon_table = {
        'AUG': 'M', 'UGU': 'C', 'UGC': 'C', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UUU': 'F', 'UUC': 'F', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
        'GGG': 'G', 'CAU': 'H', 'CAC': 'H', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'UUA': 'L',
        'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AAA': 'K', 'AAG': 'K',
        'UUU': 'F', 'UUC': 'F', 'AAC': 'N', 'AAU': 'N', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
        'CCG': 'P', 'CAA': 'Q', 'CAG': 'Q', 'AGA': 'R', 'AGG': 'R', 'CGU': 'R', 'CGC': 'R',
        'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S',
        'UCG': 'S', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'UAU': 'Y', 'UAC': 'Y',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GAC': 'D', 'GAU': 'D', 'UGG': 'W',
        'UGA': 'Stop', 'UAA': 'Stop', 'UAG': 'Stop'
    }
    
    protein = []
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        if codon_table[codon] == "Stop":
            break
        protein.append(codon_table[codon])
    
    
    return "".join(protein)



data = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

protein_string = dna_to_protein(data)
print(protein_string)



