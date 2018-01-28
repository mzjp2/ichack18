from typing import List

Vector = List[float]

class Word:
    def __init__(self, text: str, vector: Vector) -> None:
        self.text = text
        self.vector = vector

def load_words(file_path: str) -> List[Word]:
    """Load and cleanup the data."""
    
    words = load_words_raw(file_path)
    print(f"Loaded {len(words)} words.")
    
    words = remove_stop_words(words)
    print(f"Removed stop words, {len(words)} remain.")
    
    words = remove_duplicates(words)
    print(f"Removed duplicates, {len(words)} remain.")
    
    return words

def vector_len(v: Vector) -> float:
    return math.sqrt(sum([x*x for x in v]))

def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2)
    return sum([x*y for (x,y) in zip(v1, v2)])

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot_product(v1, v2) / (vector_len(v1) * vector_len(v2))



if __name__ == '__main__':
	words = load_words('data/words.vec')