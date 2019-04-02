from functools import reduce


def largest_product(series, size):
    """The largest product for a contiguous substring of digits of length n"""
    if not size:
        return 1
    if not series.isdigit():
        raise ValueError("Series should only contain numbers.")
    if size < 0:
        raise ValueError("Size cannot be less than zero.")
    if len(series) < size:
        raise ValueError("Size cannot be less than the series length.")
    slices = [series[i:i + size] for i in range(len(series))
              if len(series[i:i + size]) == size]
    products = [reduce((lambda x, y: x * y), list(map(int, substr)))
                for substr in slices]
    return max(products)
