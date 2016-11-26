#!/usr/bin/env python
import sys


def are_unique(nums):
    return len(nums) == len(set(nums))

data = []

for line in sys.stdin:
    if line.strip() != "":
        data.append(line.strip())

N, K = map(int, data[0].split())
assert 1 <= N <= 15
assert K < N
assert K == len(data) - 1

# for i in range(1, K+1):
#     line = data[i].split()
#     form = line[0]
#     pos = int(line[1])
#     num_nums = int(line[2])
#     nums = map(int, line[3:])
#     assert form in 'ab'
#     assert 1 <= pos <= N
#     assert len(nums) == num_nums
#     assert pos not in set(nums)
#     assert are_unique(nums)

valid_chars = 'ABCDEFGHIJKLMNOPQ'[0:N]
for i in range(1, K+1):
    line = data[i]
    char = line[0]
    form = line[1]
    assert char in valid_chars

    if form == '@':
        # exempel: C@01,05,12
        nums_commas = line[2:]
        every_third_char = nums_commas[2:-1:3]
        assert set(every_third_char) in (set(), set(','))
        nums = map(int, nums_commas.split(','))
        assert are_unique(nums)
        for x in nums:
            assert 0 < x <= N
    else:
        # exempel: B:DEF
        assert form == ':'
        chars = line[2:]
        assert are_unique(chars)
        for c in chars:
            assert c in valid_chars

sys.exit(42)