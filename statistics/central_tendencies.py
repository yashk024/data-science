from typing import List
from collections import Counter


def mean(lst: List[float]) -> float:
    return sum(lst) / len(lst)


def median(lst: List[float]) -> float:
    n = len(lst)
    sorted_lst = sorted(lst)
    if n & 1 == 1:
        return sorted_lst[n // 2]
    return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(lst: List[float], p: float) -> float:
    # returns the p-th percentile value in lst
    p_index = int(p * len(lst))
    return sorted(lst)[p_index]


def mode(lst: List[float]) -> List[float]:
    counts = Counter(lst)
    max_count = max(counts.values())
    return [xi for xi, count in counts.items() if count == max_count]
