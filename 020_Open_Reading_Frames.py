'''
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

'''

from Bio.Seq import Seq

def parse_fasta(fasta_string):
  lines = fasta_string.strip().split('\n')
  return ''.join(lines[1:])

def find_orfs_in_frame(dna_seq, codon_table):
  proteins = set()
  seq_length = len(dna_seq)

  for i in range(0, seq_length - 2, 3):
    codon = dna_seq[i:i+3]
    if codon == 'ATG':
      protein = []
      for j in range(i, seq_length - 2, 3):
        codon = dna_seq[j:j+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'STOP':
          proteins.add(''.join(protein))
          break
                
        protein.append(amino_acid)
  return proteins

def find_all_orfs(dna_seq, codon_table):

  proteins = set()

  for frame in range(3):
    proteins.update(find_orfs_in_frame(dna_seq[frame:], codon_table))
  
  reverse_complement_seq = str(Seq(dna_seq).reverse_complement())
  
  for frame in range(3):
    proteins.update(find_orfs_in_frame(reverse_complement_seq[frame:], codon_table))

  return proteins

codon_table = {
  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
  'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
  'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W',
}

fasta_string = """
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
"""

dna_seq = parse_fasta(fasta_string)

distinct_proteins = find_all_orfs(dna_seq, codon_table)

for protein in distinct_proteins:
  print(protein)

