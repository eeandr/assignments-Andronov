from __future__ import print_function, division

# fasta reader


def fasta_reader(fp):
    with open(fp) as seq:
        name = ''
        sequence = ''
        for line in seq:
            if line.startswith('>'):
                name = line.strip()
            sequence = "".join(seq).strip('\n')
    res = (name, sequence)
    print(res)
fasta_reader('/users/Evgeny_Andronov/Documents/ECOL_K12.fasta')
