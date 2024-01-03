'''
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''

from Bio import SeqIO

def longest_common_substring(dna_strings):
    reference_sequence = dna_strings[0]
    
    def is_common_substring(substring):
        return all(substring in seq for seq in dna_strings)

    longest_substring = ""

    for i in range(len(reference_sequence)):
        for j in range(i + len(longest_substring) + 1, len(reference_sequence) + 1):
            current_substring = reference_sequence[i:j]
          
            if is_common_substring(current_substring):
                longest_substring = current_substring

    return longest_substring


filename = "fasta.txt"
records = list(SeqIO.parse(filename, "fasta"))
dna_strings = [str(record.seq) for record in records]

result = longest_common_substring(dna_strings)
print(result)

