'''
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
'''

def count_DNA_symbols(dna_string):

    count_A = count_C = count_G = count_T = 0

    for symbol in dna_string:
        if symbol == 'A':
            count_A += 1
        elif symbol == 'C':
            count_C += 1
        elif symbol == 'G':
            count_G += 1
        elif symbol == 'T':
            count_T += 1

    return count_A, count_C, count_G, count_T


DNA_string = "TGACACACACGACATTCCCTATGGTCCGCGTGCCAATCGGTTGTTAGCGCCGTATCCCGGCTCAAGAAGACCTTGGCTGGAATGGGCGTTTACCTTAATGTTATCTGATCTGGATTGTAAACGGCCTCACGGCAGGCCCCACCCGTGCGCCGCACTGCAGCGTATATAAGACGGCCGGCACGGAGGGAGTGTGCGCCACCAGAAAGGCGTCCGTACCCACTCACTACTGTCGGGACTCCGGCTTAGGCCAATCCATGATGTTTATTACAAGCGCGTCCGGCTTTCCACTTTGGCTCGCCCGGTAGCTGCAGCTGATTGCTGGGCAGTTGCGGGGGAGTGTAATATACTAGATACCGAGGTGATGCCCCTCGGAGGGCTATGAGCATTACCGGTAGATGCGCAGGGCTACGGGTGAGACTGTAGCAGCCATACAAGCGAGTCACGTGGCTAAATGTCCCGCCAATGCTACGTTCGTCCGAACTGGGACGATAGAACAGAGGCGGTAACGATAGGTACGTATACCACTAGTCCCAAGCACTGACACTTGCAGTTTCCTCTCCCGTTAGCATAGGACTGCGCTTACCCCCATCTTAGTCATATTCCGTTGTGGCGGCCCCCAACCTCCTACTACACGCGAGCAGTTTAAATTATCAGAGCGCGTCACGTGCTACACGCATAAAGCATCCAACAACTCCGATTAACGCGGGGCCTGGCGACTCGGTCCTTCATTTCCAGAGTCGGAAGAGCGACGCGGGGGCACCAATTATGCACCCTTCGAAAATTCGCCCTCCTTCATCATGTAGCCTCGACTCGGTAGGATTAAGATGACTTATCGTTTATCGTACGTCAGTTAAAGCTTCACGTTACGCCAAACGTTACGGTTCGAGAATTCAGTCACGAGTCTACCTAATGTCAATGTTGCTGTTTAAATAATTATGGCGGGACGGGTCGGGCTGCCTTCGTACCGATTTTT"

DNA_symbol_counts = count_DNA_symbols(DNA_string)

print(DNA_symbol_counts[0], DNA_symbol_counts[1], DNA_symbol_counts[2], DNA_symbol_counts[3])

#       A   C   G   T
#output 220 269 253 231


