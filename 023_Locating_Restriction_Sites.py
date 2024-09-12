'''
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

'''

def parse_fasta(fasta_string):
    lines = fasta_string.strip().split('\n')
    return ''.join(lines[1:])
  
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_restriction_site(dna):
    results = []
    length = len(dna)
    
    # Loop through all possible positions and lengths between 4 and 12
    for start in range(length):
        for restriction_site_length in range(4, 13):
            if start + restriction_site_length <= length:
                substring = dna[start:start + restriction_site_length]
                if substring == reverse_complement(substring):
                    results.append((start + 1, restriction_site_length))
    
    return results


fasta_input = """
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

dna_string = parse_fasta(fasta_input)

restriction_sites = find_restriction_site(dna_string)

for pos, length in restriction_sites:
    print(pos, length)

