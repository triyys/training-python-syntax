from typing import List
from collections.abc import Callable

# For massive test cases
def massive_input(ns: List, exercise: Callable) -> List:
    return [exercise(i) for i in ns]
