from typing import List

# type alias
Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be of the same length"
    return [vi + wi for vi, wi in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be of the same length"
    return [vi - wi for vi, wi in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    # checks that vectors is not empty
    assert vectors, "no vectors provided"
    # check the vectors are all same size
    vector_len = len(vectors[0])
    assert all(vector_len == len(v) for v in vectors), "vectors are of unequal lengths"

    return [sum(vector[i] for vector in vectors) for i in range(vector_len)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * vi for vi in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


# to compute the component-wise means of a list of (same-sized) vectors
def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be of the same length"
    return sum(vi * wi for vi, wi in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    return sum(vi**2 for vi in v)


assert sum_of_squares([1, 2, 3]) == 14


def magnitude(v: Vector) -> float:
    return sum(vi**2 for vi in v) ** 0.5


assert magnitude([3, 4]) == 5


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))
