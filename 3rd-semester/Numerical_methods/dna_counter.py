def count_dna(dna, nucleotide):
    counter = 0
    for ch in dna:
        if ch.lower() == nucleotide.lower():
            counter += 1
    return counter


dna = 'ATGCGGACCTAT'
print(f'DNA: {dna} has {count_dna(dna, "c")} cytosine(s).')
print(f'DNA: {dna} has {dna.count("C")} cytosine(s).')


def complementary_strand(dna):
    pairs = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    strand = ''
    for ch in dna:
        strand += pairs[ch]
    return strand


complementary = complementary_strand(dna)
print(f'dna {dna}, complementary strand {complementary}.')