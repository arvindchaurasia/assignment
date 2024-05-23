from multiprocessing import Pool
from typing import List

def check_number(pair: List[int]) -> int:
    if not all(isinstance(x, int) for x in pair):
        raise ValueError("each element must be integer.")
    return sum(pair)

def addition(payload: List[List[int]]) -> List[int]:
    with Pool() as pool:
        try:
            result = pool.map(check_number, payload)
        except Exception as e:
            raise e
        return result

