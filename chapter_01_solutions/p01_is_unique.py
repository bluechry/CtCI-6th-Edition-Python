import time
import unittest
from collections import defaultdict


# Solution 1: Track Character Occurrences Using Array
def is_unique_1(s: str) -> bool:
    if len(s) > 128:
        return False

    occur = [False] * 128
    for c in s:
        if occur[ord(c)]:
            return False
        occur[ord(c)] = True
    return True


# Solution 2: Track Character Occurrences Using Bit Vector
def is_unique_2(s: str) -> bool:
    if len(s) > 128:
        return False

    occur = 0
    for c in s:
        mask = 1 << ord(c)
        if occur & mask:
            return False
        occur |= mask
    return True


# Solution 3: Hash Characters Using Dictionary
def is_unique_3(s: str) -> bool:
    occur = {}
    for c in s:
        if c in occur:
            return False
        occur[c] = True
    return True


# Solution 4: Remove Duplicate Characters Using Set
def is_unique_4(s: str) -> bool:
    occur = set()
    for c in s:
        if c in occur:
            return False
        occur.add(c)
    return True


# Solution 5: Sort Characters
def is_unique_5(s: str) -> bool:
    last = None
    for c in sorted(s):
        if c == last:
            return False
        last = c
    return True


# Solution 6: Pythonic Way
def is_unique_pythonic(s: str) -> bool:
    return len(set(s)) == len(s)


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_1,
        is_unique_2,
        is_unique_3,
        is_unique_4,
        is_unique_5,
        is_unique_pythonic
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
