import regex as re

def count_kmers(sequence, k):
    """
    Count the frequency of each valid k-mer of length k in the given DNA sequence.
    Only A, C, G, T are considered valid characters.
    """
    #check for empty string
    if not sequence:
        print("Please enter a DNA sequence!")
        
    #set A,T,C and G as only permissible bases in the sequence.
    sequence_cleaned = re.sub("[^atcg]","",sequence,flags = re.IGNORECASE)

    # set k-mer substring length
    start = 0
    kmer_length = k

    #set sequence to upper case 
    sequence = sequence_cleaned.upper()

    #create an empty dictionary 
    kmers = {}

    # iterate over the sequence. 
    # read k-mer length at a time.
    # append the k-mer to the dictionary as long as the substring length matches the k-mer length 
    # once the substring length is less than the k-mer length, stop reading the sequence. 
    while sequence:
        kmer_substring = sequence[start:kmer_length]
        start = start + 1
        kmer_length = kmer_length + 1
        if len(kmer_substring) == k:
            if kmer_substring in kmers:
                kmers[kmer_substring] +=1
            else:
                kmers[kmer_substring] = 1
        else:
            return kmers
        


#use-case example
sequence = "ATCGNATCGAATSC!G" #enter the sequence here
k = 4 #change this
print(count_kmers(sequence, k))

"""
Expected Output:
{
    'ATCG': 3,
    'TCGA': 2,
    'CGAT': 1,
    'GATC': 1,
    'CGAA': 1,
    'GAAT': 1,
    'AATC': 1
}
"""
