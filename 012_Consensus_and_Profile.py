'''
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''

from Bio import SeqIO
import numpy as np

def create_profile_matrix(dna_strings):

    length = len(dna_strings[0])
    if any(len(seq) != length for seq in dna_strings):
        raise ValueError("All DNA strings must have the same length.")

    profile_matrix = np.zeros((4, length), dtype=int)

    for dna_string in dna_strings:
        for i, nucleotide in enumerate(dna_string):
            if nucleotide == 'A':
                profile_matrix[0, i] += 1
            elif nucleotide == 'C':
                profile_matrix[1, i] += 1
            elif nucleotide == 'G':
                profile_matrix[2, i] += 1
            elif nucleotide == 'T':
                profile_matrix[3, i] += 1

    return profile_matrix

def consensus_string(profile_matrix):
    # Get the index of the maximum value for each column
    max_indices = np.argmax(profile_matrix, axis=0)
    # Map indices to nucleotides
    consensus = ''.join(['ACGT'[index] for index in max_indices])

    return consensus

filename = "fasta.txt"
records = list(SeqIO.parse(filename, "fasta"))
dna_strings = [str(record.seq) for record in records]
profile_matrix = create_profile_matrix(dna_strings)
consensus = consensus_string(profile_matrix)

print(consensus)
for symbol, counts in zip("ACGT", profile_matrix):
    print(f"{symbol}: {' '.join(map(str, counts))}")


