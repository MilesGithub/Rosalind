'''
For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.
Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.
Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.
As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.
Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

'''
    
def calculate_rna_possibilities(protein_string):
  
    codon_table = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,
        'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
        'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
        'E': 2, 'G': 4, 'STOP': 3
    }

    total_possibilities = 1
    modulo = 1000000

    for aa in protein_string:
        total_possibilities *= codon_table[aa]
        total_possibilities %= modulo

    # Account for the stop codon
    total_possibilities *= codon_table['STOP']
    total_possibilities %= modulo
    
    return total_possibilities


protein_string = 'MA'
result = calculate_rna_possibilities(protein_string)

print(result)


