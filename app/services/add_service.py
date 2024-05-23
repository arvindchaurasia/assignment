from multiprocessing import Pool
from typing import List

def check_number(pair: List[int]) -> int:
    try:
        if not all(isinstance(x, int) for x in pair):
            raise ValueError("Each element must be integer.")
        return sum(pair)
    except Exception as e:
        print(str(e))

def addition(payload: List[List[int]]) -> List[int]:
    with Pool() as pool:
        try:
            result = pool.map(check_number, payload)
        except Exception as e:
            raise e
        return result

