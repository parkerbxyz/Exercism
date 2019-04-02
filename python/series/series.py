def slices(series, length):
    """Output all contiguous substrings of series that are length chars long"""
    if not length > 0:
        raise ValueError("Length must be greater than zero.")
    if len(series) < length:
        raise ValueError("Length cannot be less than the series length.")
    return [series[i:i + length] for i in range(len(series))
            if len(series[i:i + length]) == length]
