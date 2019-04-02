CODON_MAP = (
    (('AUG',), 'Methionine'),
    (('UUU', 'UUC'), 'Phenylalanine'),
    (('UUA', 'UUG'), 'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'), 'Serine'),
    (('UAU', 'UAC'), 'Tyrosine'),
    (('UGU', 'UGC'), 'Cysteine'),
    (('UGG',), 'Tryptophan'),
    (('UAA', 'UAG', 'UGA'), 'STOP'))

AMINO_ACIDS = {
    codon: amino_acid for codons, amino_acid in CODON_MAP for codon in codons}


def proteins(strand):
    protein_chain = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = AMINO_ACIDS.get(codon)
        if protein == 'STOP' or len(codon) < 3:
            break
        if protein is not None:
            protein_chain.append(protein)
    return protein_chain
