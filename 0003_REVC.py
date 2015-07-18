'''
Title: Complementing a Strand of DNA
ID: REVC

'''

def reverse_complement_dna(dna):
    #Returns the reverse complement of DNA strand
    translate = str.maketrans('ATCG', 'TAGC')
    return dna.translate(translate)[::-1]


def main():
    # Read the input data.
    with open('data/0003_REVC.txt') as input:
        dna = input.read().strip()

    # Get the reverse complement.
    reverse_complement = reverse_complement_dna(dna)

    # Print and save the answer.
    print (reverse_complement)
    with open('output/003_REVC.txt', 'w') as output:
        output.write(reverse_complement)

if __name__ == '__main__':
    main()
