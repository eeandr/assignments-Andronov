#! /usr/bin/env python

from __future__ import print_function, division


def reconstruct_protein_alignment(seq_aln):
    letter_counter = 0  #  nucleotide counter
    gap_counter = 0     #  gap counter
    aseq_res = []       #  amino alignment
    aseq = ''           #  amino seq
    codon = ''          #  particular codon
    for seq in seq_aln:
        for sign in seq:
            if sign == '-':
                gap_counter += 1   #  counts 3 gaps and resets
            else:
                letter_counter += 1  # counts 3 nucleotide and resets
                codon += sign
            if gap_counter == 3:
                aseq += '-'
                gap_counter = 0
            elif letter_counter == 3:  #  making amino seq
                aseq += code_dict[codon]
                letter_counter = 0
                codon = ''
        aseq_res.append(aseq)
        aseq = ''
    print(aseq_res)


