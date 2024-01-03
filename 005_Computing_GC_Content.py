'''
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

def read_fasta_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def fasta_to_dict(fasta_data):
    sequences = {}
    current_id = None
    current_sequence = []

    for line in fasta_data:
        if line.startswith(">"):
            if current_id is not None:
                sequences[current_id] = "".join(current_sequence)
            current_id = line.strip()
            current_sequence = []
        else:
            current_sequence.append(line.strip())

    if current_id is not None:
        sequences[current_id] = "".join(current_sequence)

    return sequences

def calculate_gc_content(dna_string):
    gc_count = sum(base in 'GC' for base in dna_string)
    total_bases = len(dna_string)
    gc_content = (gc_count / total_bases) * 100 if total_bases > 0 else 0
    return gc_content

def find_highest_gc_content(data):
    sequences = fasta_to_dict(data)
    highest_gc_id = None
    highest_gc_content = 0

    for seq_id, seq in sequences.items():
        gc_content = calculate_gc_content(seq)
        if gc_content > highest_gc_content:
            highest_gc_id = seq_id
            highest_gc_content = gc_content

    return highest_gc_id, highest_gc_content


filename = "fasta.txt"
fasta_data = read_fasta_from_file(filename)

result_id, result_content = find_highest_gc_content(fasta_data)

print(f"{result_id}\n{result_content:.6f}")
