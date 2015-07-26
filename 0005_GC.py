'''
Title: Computing GC Content
ID: GC

'''

from Bio import SeqIO
from Bio.SeqUtils import GC

def max_gc_content(records):

	GC_content = 0
	GC_id = ""
	for record in records:
		if GC_content < GC(record.seq):
			GC_content = GC(record.seq)
			GC_id = record.id

	ret_val = GC_id + "\n" + str(GC_content)
	return ret_val


def main():

        # Parse the input data.
        handle = open("data/0005_GC.txt", "rU")

        records = SeqIO.parse(handle, "fasta")
	
        highest_gc = max_gc_content(records)

		
        # Print and save the answer.
        print (highest_gc)
        with open('output/005_GC.txt', 'w') as output_data:
                output_data.write(highest_gc)

if __name__ == '__main__':
    main()
