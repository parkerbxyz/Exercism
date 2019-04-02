def to_rna(dna_strand: str) -> str:
    """Return the RNA complement of a given DNA strand."""
    transcription = dna_strand.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(transcription)
