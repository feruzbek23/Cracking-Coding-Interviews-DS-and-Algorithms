def missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(missing_number([100000,
						99999,
						100001,
						100002]))