def mendel(k, m, n):
    # Calculate the probability of obtaining an individual with a dominant allele

    # Probabilities for homozygous dominant individuals
    prob_dom_dom = (k * k - k) / ((k + m + n) * (k + m + n - 1))

    # Probabilities for heterozygous individuals
    prob_dom_het = 2 * (k * m) / ((k + m + n) * (k + m + n - 1))

    # Probabilities for homozygous recessive individuals
    prob_dom_rec = 2 * (k * n) / ((k + m + n) * (k + m + n - 1))

    # Probabilities for heterozygous individuals
    prob_het_het = 0.75 * (m * m - m) / ((k + m + n) * (k + m + n - 1))

    # Probabilities for heterozygous individuals
    prob_het_rec = 2 * (0.5 * m * n) / ((k + m + n) * (k + m + n - 1))

    # Total probability of having a dominant allele
    prob_dominant = prob_dom_dom + prob_dom_het + prob_dom_rec + prob_het_het + prob_het_rec

    return prob_dominant

k = 28  #homozygous dominant
m = 20  #heterozygous
n = 24  #homozygous recessive

result = mendel(k, m, n)
print(result)

