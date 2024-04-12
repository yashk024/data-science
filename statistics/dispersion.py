from typing import List
from central_tendencies import mean, quantile
from math import sqrt


def data_range(lst: List[float]) -> float:
    return max(lst) - min(lst)


def de_mean(lst: List[float]) -> List[float]:
    x_bar = mean(lst)
    return [x - x_bar for x in lst]


def variance(lst: List[float]) -> float:
    assert len(lst) >= 2, "variance requires atleast two elements"
    deviations = de_mean(lst)
    return sum(x**2 for x in deviations) / (len(deviations) - 1)


def standard_deviation(lst: List[float]) -> float:
    return sqrt(variance(lst))


def interquantile_range(lst: List[float]) -> float:
    # Returns the difference between the 75%-ile and the 25%-ile
    return quantile(lst, 0.75) - quantile(lst, 0.25)
