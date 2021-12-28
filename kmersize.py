dna = "ATGCGTATGCGTGTGTGTCAGTG"
k = 3

kmers = []
for g in range(len(dna) - k + 1):
    kmer = dna[g:g+k]
    kmers.append(kmer)

kmer_count = {}
for i in range(len(kmers)):
    if kmers[i] in kmer_count:
        kmer_count[kmers[i]] += 1
    else:
        kmer_count[kmers[i]] = 1

print(kmer_count)