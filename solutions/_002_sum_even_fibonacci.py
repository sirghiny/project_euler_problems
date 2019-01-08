"""Sum even numbers in a Fibonacci series."""


def fibonacci(start1, start2, stop):
    """Compute fibonacci series between limits."""
    series = [start1, start2]
    while series[-1] < stop:
        series.append(series[-1] + series[-2])
    if series[-1] >= stop:
        del series[-1]
    return series


def sum_even_numbers(start1, start2, stop):
    """Sum all even numbers in the series."""
    series = fibonacci(start1, start2, stop)
    return sum([i for i in series if not i % 2])


print(sum_even_numbers(1, 2, 4000000))
