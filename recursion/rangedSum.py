def rangedSum(nums: list, start: int, end: int) -> int:
    """
    Returns the sum of the values in the range [start, end]
    """
    sum = 0
    for i in range(start, end+1):
        if i < len(nums):
            sum += nums[i]
    return sum

def recRangedSum(nums: list, start: int, end: int) -> int:
    pass