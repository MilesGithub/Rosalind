'''
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

'''

import itertools

def generate_permutations(n):

    elements = list(range(1, n + 1))

    permutations = list(itertools.permutations(elements))

    total_permutations = len(permutations)
    
    return total_permutations, permutations




n = 6
total_permutations, permutations = generate_permutations(n)

print(total_permutations)
for p in permutations:
    print(' '.join(map(str, p)))

    
    
