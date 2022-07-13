#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Version 2.0
print ('please input your DNA sequence: ')
input_sequence = list(input())
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
    print(f'your reverse complement is: {str(output)}')
else:
    print('You have entered unsupported charachters which will be skipped')
    input_sequence.reverse()
    for i in input_sequence:
        if i not in test_string:
            continue
        else:
            result.append(complementary_bases[i])
    output = ''.join(result)
    print(f'your reverse complement is: {str(output)}')
input()

