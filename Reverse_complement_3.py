#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Version 3.0

def revcomp(dna_sequence):
    input_sequence = list(dna_sequence)
    complementary_bases = {'A':'T', 'a':'t', 'G':'C', 'g':'c', 'T':'A', 't':'a', 'C':'G', 'c':'g'}
    result = []

    #first perform input correctness test
    test_string = 'ATGCatgc'
    res = all (ele in test_string for ele in input_sequence)
    #if all nucleotides are correct
    if res == True:
        input_sequence.reverse()
        for i in input_sequence:
            result.append(complementary_bases[i])
        output = ''.join(result)
        return(f'your reverse complement is: {str(output)}')
    else:
        input_sequence.reverse()
        for i in input_sequence:
            if i not in test_string:
                continue
            else:
                result.append(complementary_bases[i])
        output = ''.join(result)
        return(f'your reverse complement is(unsupported characters were skipped): {str(output)}')
    input()
""""""
