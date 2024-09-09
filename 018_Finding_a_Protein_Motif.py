'''
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
'''

import re
import requests

def fetch_fasta(uniprot_id):
    uniprot_id = uniprot_id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.ok:
        fasta_data = response.text.splitlines()[1:]
        return ''.join(fasta_data)
    return None

def find_nglycosylation_motif(protein_sequence):
    motif_pattern = r"(?=(N[^P][ST][^P]))"
    return [m.start() + 1 for m in re.finditer(motif_pattern, protein_sequence)]

def find_motif_in_proteins(uniprot_ids):
    results = {}
    for uniprot_id in uniprot_ids:
        protein_seq = fetch_fasta(uniprot_id)
        if protein_seq:
            locations = find_nglycosylation_motif(protein_seq)
            if locations:
                results[uniprot_id] = locations
    return results

uniprot_ids = ['A2Z669','B5ZC00','P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
results = find_motif_in_proteins(uniprot_ids)

for uniprot_id in uniprot_ids:
    if uniprot_id in results:
        print(f"{uniprot_id}\n{' '.join(map(str, results[uniprot_id]))}")
        
