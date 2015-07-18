'''
Title: Rabbits and Recurrence Relations
ID: FIB

'''


def fibonacci(i,j):
    #Returns number of rabbits present after i generations with j pairs of litters
    rabbits = [0,1]
    for i in range(i-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + j*rabbits[i % 2]

    return rabbits[i % 2]


def main():
    # Read input
    with open('data/0004_FIB.txt') as input:
        i, j = map(int, input.read().strip().split())

    # Get number of rabbits
    number_of_rabbits = str(fibonacci(i,j))

    # Print and save the answer
    print (number_of_rabbits)
    with open('output/0004_FIB.txt', 'w') as output:
        output.write(number_of_rabbits)


if __name__ == '__main__':
    main()
