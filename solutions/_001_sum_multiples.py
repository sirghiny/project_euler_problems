"""Find the sum of all the multiples of 3 or 5 below 1000."""


def sum_multiples(start, stop, *digits):
    """Find sum of multiples of specific digits between limits."""
    initial = [[i for i in range(start, stop) if not i % j] for j in digits]
    multiples = set([i for sub_list in initial for i in sub_list])
    return sum(multiples)


print(sum_multiples(0, 1000, 3, 5))
