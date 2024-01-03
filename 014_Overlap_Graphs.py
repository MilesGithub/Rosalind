'''
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v.
For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
'''

from Bio import SeqIO

def generate_overlap_graph(fasta_records, k):
    adjacency_list = []

    for i, record_1 in enumerate(fasta_records):
        for j, record_2 in enumerate(fasta_records):
            if i != j and str(record_1.seq)[-k:] == str(record_2.seq)[:k]:
                adjacency_list.append((record_1.id, record_2.id))

    return adjacency_list

filename = "FASTA.txt"
fasta_records = list(SeqIO.parse(filename, "fasta"))
overlap_graph = generate_overlap_graph(fasta_records, k=3)

for edge in overlap_graph:
    print(f"{edge[0]} {edge[1]}")

