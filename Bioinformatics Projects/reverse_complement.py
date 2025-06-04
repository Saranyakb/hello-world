# This is to find the reverse complement of a given sequence. 
import re
def reverse_complement(sequence):
    #set A,T,C and G as only permissible bases in the sequence.
    pattern = r'^[atcgATCG]+$'
    #check for empty string
    if not sequence:
        print("Please enter a DNA sequence!")
    #use regex to ensure A,T,C and G are the only upper or lower case letters in the sequence.
    if not re.match(pattern, sequence):
        print("Invalid characters found, please enter a different sequence!")
    #translate() is the most popular and efficient method to manipulate a string. set the conversion table to return the complement.
    rev_comp = sequence.maketrans('ATCG','TAGC')
    #apply the conversion table and return the reverse complement read from the opposite end
    return sequence.translate(rev_comp)[::-1]

# Sample use-case
sequence = "ATGC"
reverse = reverse_complement(sequence)
print("The reverse complement of this sequence is: \n",reverse)